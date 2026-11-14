"""Exercise the actual audio conversation loop without OpenAI, SIP or a real call."""
import asyncio
import importlib.util
import json
import os
import time
import unittest
import uuid
from unittest.mock import AsyncMock, patch

# Runtime image supplies audioop (Python 3.12), aiohttp and websockets.
AVAILABLE=all(importlib.util.find_spec(n) for n in ('audioop','aiohttp','websockets'))


class WS:
    def __init__(self): self.events=asyncio.Queue(); self.sent=[]
    async def send(self,raw): self.sent.append(json.loads(raw))
    def __aiter__(self): return self
    async def __anext__(self): return json.dumps(await self.events.get())
    async def text(self,text,start=0):
        await self.events.put({'type':'session.input_transcript.delta','delta':text,'start_ms':start,'end_ms':start+500})


class Writer:
    def __init__(self): self.frames=[]
    def write(self,data): self.frames.append((time.monotonic(),data))
    async def drain(self): pass


@unittest.skipUnless(AVAILABLE,'Run this integration suite in the deployed Python 3.12 runtime image')
class BridgeTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        os.environ.setdefault('BRIDGE_TOKEN','test'); os.environ.setdefault('CALL_ALLOWED_NUMBER','015711111111')
        import bridge
        self.b=bridge; self.cid=str(uuid.uuid4()); self.ws=WS()
        self.b.STATUS[self.cid]={'mode':'conversation'}
        self.backend=AsyncMock()
        self.patches=[patch.object(bridge,'backend_request',self.backend),patch.object(bridge,'persist',lambda:None)]
        for p in self.patches: p.start()
    async def asyncTearDown(self):
        for p in self.patches: p.stop()
        self.b.STATUS.pop(self.cid,None)
    async def run_conversation(self,producer,timeout=6):
        self.writer=Writer()
        task=asyncio.create_task(producer())
        try:
            await asyncio.wait_for(self.b.conversation(self.cid,self.ws,asyncio.StreamReader(),self.writer,'Vertrauliches Angebot'),timeout)
        finally:
            task.cancel(); await asyncio.gather(task,return_exceptions=True)
    async def test_voicemail_closes_without_disclosing_reason_or_starting_work(self):
        async def events():
            await asyncio.sleep(.05); await self.ws.text('Bitte sprechen Sie nach dem Signalton.')
        await self.run_conversation(events)
        self.assertEqual(self.b.STATUS[self.cid]['report']['state'],'voicemail')
        self.assertNotIn('Vertrauliches Angebot',json.dumps(self.ws.sent))
        self.backend.assert_not_called()
    async def test_spoken_goodbye_ends_real_conversation_loop(self):
        async def events():
            await asyncio.sleep(.05); await self.ws.text('Ja, ich höre dich.')
            await asyncio.sleep(1.1); await self.ws.text('Danke, das war’s.',start=3000)
        await self.run_conversation(events)
        self.assertIn('human_confirmed_at',self.b.STATUS[self.cid])
        self.assertIn('Vertrauliches Angebot',json.dumps(self.ws.sent))
        self.assertEqual(self.b.STATUS[self.cid]['report']['state'],'ended')
        self.assertIn('Verabschiede',json.dumps(self.ws.sent))
    async def test_natural_hangup_request_terminates_and_does_not_delegate(self):
        async def events():
            await self.ws.text('Ja, ich höre dich.')
            await asyncio.sleep(1.1)
            await self.ws.text('Okay, danke. Leg jetzt auf',start=4000)
            await self.ws.events.put({'type':'session.delegation.created','delegation':{'id':'end-request','target':'client'}})
        await self.run_conversation(events)
        self.assertEqual(self.b.STATUS[self.cid]['report']['state'],'ended')
        self.assertEqual(self.b.STATUS[self.cid]['end_reason'],'user_hangup')
        self.backend.assert_not_called()

    async def test_waiting_job_produces_music_and_result_clears_waiting(self):
        accepted=[None]; completed=[None]
        async def backend(path,data=None):
            if path=='/jobs': accepted[0]=time.monotonic(); return {'id':'research'}
            if time.monotonic()-accepted[0]<4: return {'state':'running'}
            completed[0]=time.monotonic()
            return {'state':'completed','result':json.dumps({'spoken':'Das Ergebnis ist da.'})}
        self.backend.side_effect=backend
        async def events():
            await self.ws.text('Ja, ich höre dich.')
            await asyncio.sleep(1.1)
            await self.ws.text('Was steht morgen in meinem Kalender?',start=3000)
            await self.ws.events.put({'type':'session.delegation.created','delegation':{'id':'research','target':'client'}})
            await asyncio.sleep(6.5)
            await self.ws.text('Leg jetzt auf.',start=12000)
        await self.run_conversation(events,timeout=12)
        self.assertGreater(self.b.STATUS[self.cid].get('music_frames',0),0)
        self.assertEqual(self.b.STATUS[self.cid]['backend_answers'],1)
        self.assertTrue(self.writer.frames)
        self.assertLessEqual(self.writer.frames[-1][0],completed[0])
        self.assertEqual(self.b.STATUS[self.cid]['end_reason'],'user_hangup')

    async def test_provider_interruption_discards_queued_speech(self):
        import base64
        async def events():
            await asyncio.sleep(.05)
            await self.ws.events.put({'type':'session.output_audio.delta',
                                      'delta':base64.b64encode(b'\x7f'*8000).decode()})
            await self.ws.events.put({'type':'session.output_audio.interrupted'})
            await asyncio.sleep(.1)
            await self.ws.text('Dies ist die Mailbox.')
        await self.run_conversation(events)
        self.assertEqual(self.writer.frames, [])

    async def test_provider_takeover_discards_old_provider_audio(self):
        import base64
        async def events():
            await asyncio.sleep(.05)
            await self.ws.events.put({'type':'session.output_audio.delta',
                                      'delta':base64.b64encode(b'\x7f'*8000).decode()})
            await self.ws.events.put({'type':'session.voice_provider.changed','provider':'gpt_live'})
            await asyncio.sleep(.1)
            await self.ws.text('Dies ist die Mailbox.')
        await self.run_conversation(events)
        self.assertEqual(self.writer.frames, [])
        self.assertEqual(self.b.STATUS[self.cid]['voice_provider'], 'gpt_live')

    async def test_elevenlabs_preflight_is_preferred_to_native_voice(self):
        self.assertTrue(hasattr(self.b, 'open_voice'), 'open_voice is missing')
        primary = AsyncMock(return_value=self.ws)
        native = AsyncMock()
        with patch.dict(os.environ, {'VOICE_PROVIDER':'elevenlabs'}), \
             patch.object(self.b, 'open_elevenlabs', primary), \
             patch.object(self.b, 'open_live', native):
            session = await self.b.open_voice()
        self.assertEqual(session.provider, 'elevenlabs')
        native.assert_not_awaited()

    async def test_unconfirmed_delegation_cannot_start_an_action(self):
        async def events():
            await self.ws.events.put({'type':'session.delegation.created','delegation':{'id':'one','target':'client'}})
            await asyncio.sleep(1.1); await self.ws.text('Dies ist die Mailbox.')
        await self.run_conversation(events)
        self.backend.assert_not_called()

    async def test_normal_provider_audio_burst_does_not_hang_up_after_human_answer(self):
        import base64
        async def events():
            await self.ws.text("Ja, ich höre dich.")
            await asyncio.sleep(1.1)
            # Provider sends twelve seconds of speech faster than real time.
            await self.ws.events.put({"type":"session.output_audio.delta",
                                      "delta":base64.b64encode(b"\x7f" * (8000 * 12)).decode()})
            await asyncio.sleep(.3)
            await self.ws.events.put({"type":"session.output_audio.interrupted"})
            await self.ws.text("Danke, das war’s.", start=4000)
        await self.run_conversation(events)
        self.assertEqual(self.b.STATUS[self.cid]["end_reason"], "user_hangup")
        self.assertGreater(self.b.STATUS[self.cid]["output_frames"], 0)
        self.assertIn("human_confirmed_at", self.b.STATUS[self.cid])

    async def test_abnormally_large_audio_burst_remains_bounded_and_has_specific_reason(self):
        import base64
        async def events():
            await self.ws.events.put({"type":"session.output_audio.delta",
                                      "delta":base64.b64encode(b"\x7f" * (8000 * 61)).decode()})
        await self.run_conversation_failure(events)
        self.assertEqual(self.b.STATUS[self.cid]["end_reason"], "audio_queue_limit")

    async def run_conversation_failure(self, producer):
        with self.assertRaisesRegex(RuntimeError, "Audio queue exceeds bounded answer buffer"):
            await self.run_conversation(producer)


if __name__=='__main__': unittest.main()
