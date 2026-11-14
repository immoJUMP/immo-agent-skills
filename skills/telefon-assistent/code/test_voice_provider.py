"""Phone-provider failover without external APIs or dialing."""
import asyncio
import importlib
import json
import unittest
from unittest.mock import AsyncMock


class Socket:
    def __init__(self):
        self.incoming = asyncio.Queue()
        self.sent = []
        self.closed = False
        self.fail_send = False
    async def recv(self):
        event = await self.incoming.get()
        if isinstance(event, Exception): raise event
        return json.dumps(event)
    async def send(self, raw):
        if self.fail_send: raise ConnectionError('credential must not appear in logs')
        self.sent.append(json.loads(raw))
    async def close(self):
        self.closed = True
        self.incoming.put_nowait(ConnectionError('closed'))


class ProviderTests(unittest.IsolatedAsyncioTestCase):
    def module(self):
        self.assertIsNotNone(importlib.util.find_spec('voice_provider'), 'voice_provider is missing')
        return importlib.import_module('voice_provider')
    def eleven(self):
        m = self.module()
        self.sock = Socket()
        return m.ElevenLabsSession(self.sock)
    async def test_phone_audio_is_forwarded_as_ulaw_without_resampling(self):
        session = self.eleven()
        await session.send(json.dumps({'type':'session.input_audio.append','audio':'AQID'}))
        self.assertEqual(self.sock.sent, [{'user_audio_chunk':'AQID'}])
    async def test_audio_and_interruption_are_mapped_to_bridge_events(self):
        session = self.eleven()
        self.sock.incoming.put_nowait({'type':'audio','audio_event':{'audio_base_64':'AQID'}})
        self.assertEqual(json.loads(await session.recv()), {'type':'session.output_audio.delta','delta':'AQID'})
        self.sock.incoming.put_nowait({'type':'interruption'})
        self.assertEqual(json.loads(await session.recv())['type'],'session.output_audio.interrupted')
    async def test_full_utterances_have_distinct_boundaries(self):
        session = self.eleven()
        for word in ('Hallo.', 'Danke.'):
            self.sock.incoming.put_nowait({'type':'user_transcript','user_transcription_event':{'user_transcript':word}})
        first, second = [json.loads(await session.recv()) for _ in range(2)]
        self.assertEqual(first['delta'],'Hallo.')
        self.assertGreaterEqual(second['start_ms']-first['end_ms'],1800)
    async def test_ping_is_answered_without_becoming_a_transcript(self):
        session = self.eleven()
        self.sock.incoming.put_nowait({'type':'ping','ping_event':{'event_id':42}})
        self.sock.incoming.put_nowait({'type':'audio','audio_event':{'audio_base_64':'AQID'}})
        self.assertEqual(json.loads(await session.recv())['type'], 'session.heartbeat')
        self.assertEqual(json.loads(await session.recv())['type'], 'session.output_audio.delta')
        self.assertEqual(self.sock.sent,[{'type':'pong','event_id':42}])
    async def test_only_leo_backend_tool_is_delegated(self):
        session = self.eleven()
        self.sock.incoming.put_nowait({'type':'client_tool_call','client_tool_call':{'tool_name':'ask_leo','tool_call_id':'one'}})
        event = json.loads(await session.recv())
        self.assertEqual(event['delegation'],{'target':'client','id':'one'})
        await session.send(json.dumps({'type':'session.commentary.append','delegation_id':'one','content':'Der Entwurf ist fertig.'}))
        self.assertEqual(self.sock.sent[-1],{'type':'client_tool_result','tool_call_id':'one','result':'Der Entwurf ist fertig.','is_error':False})
    async def test_unknown_tool_is_rejected_locally(self):
        session = self.eleven()
        self.sock.incoming.put_nowait({'type':'client_tool_call','client_tool_call':{'tool_name':'dial_anyone','tool_call_id':'bad'}})
        self.sock.incoming.put_nowait({'type':'audio','audio_event':{'audio_base_64':'AQID'}})
        await session.recv()
        self.assertTrue(self.sock.sent[0]['is_error'])
    async def test_application_context_does_not_masquerade_as_spoken_user_input(self):
        session = self.eleven()
        await session.send(json.dumps({'type':'session.instructions.append','content':'Eine menschliche Antwort ist bestätigt.'}))
        self.assertEqual(self.sock.sent[0]['type'],'contextual_update')
    async def test_application_command_echo_is_not_a_human_answer(self):
        session = self.eleven()
        await session.send(json.dumps({'type':'session.instructions.append','content':'Beginne jetzt mit Hallo Chris.'}))
        text = self.sock.sent[-1]['text']
        self.sock.incoming.put_nowait({'type':'user_transcript','user_transcription_event':{'user_transcript':text}})
        self.sock.incoming.put_nowait({'type':'audio','audio_event':{'audio_base_64':'AQID'}})
        self.assertEqual(json.loads(await session.recv())['type'], 'session.output_audio.delta')

    async def test_large_context_uses_bounded_session_wide_appends(self):
        router = await self.make_router()
        self.context['transcript'] = 'Chris: ' + 'Größe und Mieterlöse. '*250
        self.context['instructions'].append('Beginne jetzt mit Hallo Chris.')
        self.primary.incoming.put_nowait(ConnectionError('closed'))
        await router.recv()
        self.assertGreater(len(self.native.sent), 1)
        for event in self.native.sent:
            self.assertLessEqual(len(event['content'].encode()), 400)
            self.assertIsNone(event['delegation_id'])
            self.assertIn('event_id', event)
        text = ' '.join(event['content'] for event in self.native.sent)
        self.assertIn('Mieterlöse', text)
        self.assertNotIn('Beginne jetzt', text)
        await router.close()

    async def test_receive_stall_switches_to_fallback(self):
        m = self.module()
        primary, native = Socket(), Socket()
        fallback = AsyncMock(return_value=native)
        router = await m.VoiceSession.open(AsyncMock(return_value=primary),fallback,
                                          log=lambda *a,**kw:None,receive_timeout=.01)
        self.assertEqual(json.loads(await router.recv())['type'], 'session.voice_provider.changed')
        fallback.assert_awaited_once()
        await router.close()

    async def test_pending_native_result_drops_old_provider_tool_id(self):
        router = await self.make_router()
        self.primary.incoming.put_nowait(ConnectionError('closed'))
        await router.recv()
        await router.send(json.dumps({'type':'session.commentary.append','delegation_id':'one','content':'Fertig.'}))
        self.assertIn('delegation_id', self.native.sent[-1])
        self.assertIsNone(self.native.sent[-1]['delegation_id'])
        await router.close()

    async def test_backend_error_triggers_failover(self):
        session = self.eleven()
        self.sock.incoming.put_nowait({'type':'client_error','error_event':{'message':'sensitive'}})
        with self.assertRaisesRegex(RuntimeError,'ElevenLabs session failed'):
            await session.recv()
    async def make_router(self, primary=None, failure=None):
        m = self.module()
        self.native = Socket()
        self.fallback = AsyncMock(return_value=self.native)
        self.primary = primary or Socket()
        self.preferred = AsyncMock(return_value=self.primary, side_effect=failure)
        self.events = []
        router = await m.VoiceSession.open(self.preferred,self.fallback,log=lambda *a,**kw:self.events.append((a,kw)))
        self.context = {'transcript':'Chris: Ein Angebot vorbereiten.','human':True,'pending_jobs':['one'],'instructions':['Arbeitsauftrag angenommen.']}
        router.context = lambda:self.context
        return router
    async def test_primary_is_used_without_opening_gpt_live(self):
        router = await self.make_router()
        await router.send(json.dumps({'type':'session.input_audio.append','audio':'AQID'}))
        self.preferred.assert_awaited_once()
        self.fallback.assert_not_awaited()
        self.assertEqual(router.provider,'elevenlabs')
        await router.close()
    async def test_preflight_error_uses_gpt_live_without_dialing(self):
        router = await self.make_router(failure=TimeoutError())
        self.assertEqual(router.provider,'gpt_live')
        self.fallback.assert_awaited_once()
        await router.close()
    async def test_mid_call_disconnect_transfers_context_and_keeps_same_media(self):
        router = await self.make_router()
        self.primary.incoming.put_nowait(ConnectionError('private URL'))
        event = json.loads(await router.recv())
        self.assertEqual(event['type'],'session.voice_provider.changed')
        self.assertEqual(router.provider,'gpt_live')
        context = '\n'.join(event['content'] for event in self.native.sent)
        self.assertIn('Ein Angebot vorbereiten', context)
        self.assertIn('one', context)
        self.assertIn('bestätigt', context)
        self.native.incoming.put_nowait({'type':'session.output_audio.delta','delta':'AQID'})
        self.assertEqual(json.loads(await router.recv())['delta'],'AQID')
        self.assertTrue(self.primary.closed)
        self.assertNotIn('private URL',str(self.events))
        await router.close()
    async def test_native_delegation_ids_are_preserved_after_takeover(self):
        router = await self.make_router()
        self.primary.incoming.put_nowait(ConnectionError('closed'))
        await router.recv()
        await router.send(json.dumps({'type':'session.commentary.append','delegation_id':'native-two','content':'Fertig.'}))
        self.assertEqual(self.native.sent[-1]['delegation_id'],'native-two')
        await router.close()

    async def test_failed_mid_call_fallback_is_not_opened_twice(self):
        router = await self.make_router()
        self.fallback.side_effect = ConnectionError('native unavailable')
        self.primary.incoming.put_nowait(ConnectionError('closed'))
        with self.assertRaises(ConnectionError): await router.recv()
        with self.assertRaises(RuntimeError): await router.recv()
        self.fallback.assert_awaited_once()
        await router.close()

    async def test_send_failure_retries_current_input_on_fallback(self):
        router = await self.make_router()
        self.primary.fail_send = True
        await router.send(json.dumps({'type':'session.input_audio.append','audio':'AQID'}))
        self.assertEqual(self.native.sent[-1],{'type':'session.input_audio.append','audio':'AQID'})
        self.fallback.assert_awaited_once()
        await router.close()
    async def test_concurrent_failures_open_fallback_only_once(self):
        router = await self.make_router()
        self.primary.fail_send = True
        self.primary.incoming.put_nowait(ConnectionError('closed'))
        await asyncio.gather(router.recv(),router.send(json.dumps({'type':'session.input_audio.append','audio':'AQID'})))
        self.fallback.assert_awaited_once()
        await router.close()
    async def test_fallback_error_is_propagated_without_retry_loop(self):
        router = await self.make_router(failure=TimeoutError())
        self.native.incoming.put_nowait(ConnectionError('native closed'))
        with self.assertRaises(ConnectionError): await router.recv()
        self.fallback.assert_awaited_once()
        await router.close()
    async def test_normal_close_does_not_activate_fallback(self):
        router = await self.make_router()
        await router.send(json.dumps({'type':'session.close'}))
        await router.close()
        self.fallback.assert_not_awaited()
        self.assertTrue(self.primary.closed)
    async def test_agent_spec_uses_german_voice_and_only_owner_backend_tool(self):
        m = self.module()
        spec = m.agent_spec('german-male-voice','Persona')
        config = spec['conversation_config']
        self.assertEqual(config['agent']['language'],'de')
        self.assertEqual(config['agent']['first_message'],'')
        self.assertEqual(config['tts']['voice_id'],'german-male-voice')
        self.assertEqual(config['tts']['agent_output_audio_format'],'ulaw_8000')
        self.assertEqual(config['asr']['user_input_audio_format'],'ulaw_8000')
        self.assertTrue(spec['platform_settings']['auth']['enable_auth'])
        self.assertEqual([t['name'] for t in config['agent']['prompt']['tools']],['ask_leo'])


class HandshakeTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        from aiohttp import web
        self.m = importlib.import_module('voice_provider')
        self.requests = []
        self.http_status = 200
        self.signed_url = 'wss://api.elevenlabs.io/v1/convai/conversation?token=test-secret'
        async def signed(request):
            self.requests.append((request.headers.get('xi-api-key'), request.query.get('agent_id')))
            return web.json_response({'signed_url':self.signed_url}, status=self.http_status)
        app = web.Application()
        app.router.add_get('/v1/convai/conversation/get-signed-url', signed)
        self.runner = web.AppRunner(app)
        await self.runner.setup()
        site = web.TCPSite(self.runner,'127.0.0.1',0)
        await site.start()
        self.base = 'http://127.0.0.1:' + str(site._server.sockets[0].getsockname()[1])
    async def asyncTearDown(self):
        await self.runner.cleanup()
    async def test_signed_private_agent_validates_both_telephone_codecs(self):
        from unittest.mock import patch
        sock = Socket()
        sock.incoming.put_nowait({'type':'conversation_initiation_metadata','conversation_initiation_metadata_event':{
            'agent_output_audio_format':'ulaw_8000','user_input_audio_format':'ulaw_8000'}})
        with patch.object(self.m,'connect',AsyncMock(return_value=sock)):
            session = await self.m.open_elevenlabs('test-key','private-agent',api_base=self.base)
        self.assertEqual(self.requests,[('test-key','private-agent')])
        self.assertEqual(sock.sent[0],{'type':'conversation_initiation_client_data'})
        await session.close()
    async def test_wrong_codec_closes_connection_before_any_call(self):
        from unittest.mock import patch
        sock = Socket()
        sock.incoming.put_nowait({'type':'conversation_initiation_metadata','conversation_initiation_metadata_event':{
            'agent_output_audio_format':'pcm_16000','user_input_audio_format':'ulaw_8000'}})
        with patch.object(self.m,'connect',AsyncMock(return_value=sock)):
            with self.assertRaises(ValueError):
                await self.m.open_elevenlabs('test-key','private-agent',api_base=self.base)
        self.assertTrue(sock.closed)
    async def test_auth_rejection_never_opens_websocket(self):
        from unittest.mock import patch
        self.http_status = 401
        connector = AsyncMock()
        with patch.object(self.m,'connect',connector):
            with self.assertRaisesRegex(RuntimeError,'authentication failed'):
                await self.m.open_elevenlabs('test-key','private-agent',api_base=self.base)
        connector.assert_not_awaited()
    async def test_signed_url_to_foreign_host_is_rejected(self):
        from unittest.mock import patch
        self.signed_url = 'wss://attacker.example/steal?token=test-secret'
        connector = AsyncMock()
        with patch.object(self.m,'connect',connector):
            with self.assertRaisesRegex(ValueError,'Unexpected'):
                await self.m.open_elevenlabs('test-key','private-agent',api_base=self.base)
        connector.assert_not_awaited()

if __name__ == '__main__': unittest.main()
