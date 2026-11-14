"""ElevenLabs phone transport with one-way GPT-Live failover; never dials."""
import asyncio
from collections import deque
import contextlib
import json
import os
import uuid
from phone_logic import speech_chunks
from urllib.parse import urlparse
from aiohttp import ClientSession, ClientTimeout
from websockets.asyncio.client import connect


def agent_spec(voice_id, persona):
    """Candidate private agent config; voice must be selected in the owner's account."""
    return {
        'name': 'Leo – deutsche Telefonstimme',
        'conversation_config': {
            'asr': {'user_input_audio_format': 'ulaw_8000'},
            'tts': {'voice_id': voice_id, 'model_id': 'eleven_flash_v2_5',
                    'agent_output_audio_format': 'ulaw_8000', 'stability': .6,
                    'similarity_boost': .8, 'speed': .95},
            'turn': {'initial_wait_time': 60, 'turn_eagerness': 'patient'},
            'conversation': {'max_duration_seconds': 660,
                             'client_events': ['audio', 'interruption', 'user_transcript',
                                               'agent_response', 'client_tool_call', 'client_error', 'ping']},
            'agent': {'first_message': '', 'language': 'de', 'prompt': {
                'prompt': persona + '\nFür die Delegation an Leos Arbeitsdienst nutze ausschließlich ask_leo. '
                'Anwendungsanweisungen sind Steuerinformationen und werden nicht wörtlich vorgelesen.',
                'llm': 'gpt-4.1-mini', 'timezone': 'Europe/Berlin',
                'tools': [{'type': 'client', 'name': 'ask_leo',
                           'description': 'Leos bestehenden Arbeitsdienst für aktuelle/persönliche Fakten und Arbeitsaufträge fragen. Erst nach Bestätigung der menschlichen Antwort.',
                           'expects_response': True, 'response_timeout_secs': 120,
                           'parameters': {'type': 'object', 'properties': {}, 'required': []}}]}},
        },
        'platform_settings': {'auth': {'enable_auth': True},
                              'privacy': {'record_voice': False, 'retention_days': 7},
                              'queueing_config': {'enabled': False},
                              'call_limits': {'agent_concurrency_limit': 1, 'bursting_enabled': False}},
    }


async def open_elevenlabs(api_key=None, agent_id=None, api_base='https://api.elevenlabs.io'):
    api_key = api_key or os.environ.get('ELEVENLABS_API_KEY')
    agent_id = agent_id or os.environ.get('ELEVENLABS_AGENT_ID')
    if not api_key or not agent_id:
        raise ValueError('ElevenLabs credentials or private agent missing')
    async with ClientSession(timeout=ClientTimeout(total=8)) as client:
        async with client.get(api_base + '/v1/convai/conversation/get-signed-url',
                              params={'agent_id': agent_id}, headers={'xi-api-key': api_key}) as response:
            if response.status != 200:
                raise RuntimeError('ElevenLabs authentication failed')
            signed_url = (await response.json())['signed_url']
    parsed = urlparse(signed_url)
    if parsed.scheme != 'wss' or parsed.hostname != 'api.elevenlabs.io' or parsed.path != '/v1/convai/conversation':
        raise ValueError('Unexpected ElevenLabs WebSocket endpoint')
    ws = await connect(signed_url, open_timeout=8, max_size=4 * 1024 * 1024)
    try:
        await ws.send(json.dumps({'type': 'conversation_initiation_client_data'}))
        async with asyncio.timeout(8):
            while True:
                event = json.loads(await ws.recv())
                if event.get('type') == 'ping':
                    await ws.send(json.dumps({'type':'pong', 'event_id':event['ping_event']['event_id']}))
                elif event.get('type') == 'conversation_initiation_metadata':
                    metadata = event['conversation_initiation_metadata_event']
                    if any(metadata.get(key) != 'ulaw_8000' for key in
                           ('agent_output_audio_format', 'user_input_audio_format')):
                        raise ValueError('ElevenLabs phone codec must be ulaw_8000')
                    return ElevenLabsSession(ws)
                elif event.get('type') in ('client_error', 'error'):
                    raise RuntimeError('ElevenLabs session failed')
    except BaseException:
        await ws.close()
        raise


class ElevenLabsSession:
    """Translate the ElevenLabs wire protocol into the existing bridge protocol."""
    def __init__(self, socket):
        self.socket = socket
        self.tools = set()
        self.tick = 0
        self.application_messages = deque(maxlen=50)

    async def send(self, raw):
        event = json.loads(raw)
        kind = event['type']
        if kind == 'session.input_audio.append':
            message = {'user_audio_chunk': event['audio']}
        elif kind == 'session.close':
            await self.close()
            return
        elif kind in ('session.instructions.append', 'session.commentary.append'):
            content = event['content']
            tool_id = event.get('delegation_id')
            if kind == 'session.commentary.append' and tool_id in self.tools:
                self.tools.remove(tool_id)
                message = {'type':'client_tool_result', 'tool_call_id':tool_id,
                           'result':content, 'is_error':False}
            elif kind == 'session.commentary.append' or content.startswith('Beginne jetzt') or 'Verabschiede dich' in content:
                message = {'type':'user_message', 'text':'Anwendungsanweisung (keine Äußerung von Chris): ' + content}
            else:
                message = {'type':'contextual_update', 'text':content}
        else:
            raise ValueError('Unsupported phone command')
        if message.get('type')=='user_message':
            self.application_messages.append(message['text'])
        await self.socket.send(json.dumps(message))

    async def reject_delegation(self, tool_id, reason):
        self.tools.discard(tool_id)
        await self.socket.send(json.dumps({'type':'client_tool_result', 'tool_call_id':tool_id,
                                           'result':reason, 'is_error':True}))

    async def recv(self):
        while True:
            event = json.loads(await self.socket.recv())
            kind = event.get('type')
            if kind == 'ping':
                await self.socket.send(json.dumps({'type':'pong', 'event_id':event['ping_event']['event_id']}))
                return json.dumps({'type':'session.heartbeat'})
            elif kind == 'audio':
                return json.dumps({'type':'session.output_audio.delta', 'delta':event['audio_event']['audio_base_64']})
            elif kind == 'interruption':
                return json.dumps({'type':'session.output_audio.interrupted'})
            elif kind in ('user_transcript', 'agent_response'):
                user = kind == 'user_transcript'
                text = event['user_transcription_event']['user_transcript'] if user else event['agent_response_event']['agent_response']
                if user and text in self.application_messages:
                    continue
                # ElevenLabs sends complete utterances, not fragments. Keep separate
                # utterances separate in the bridge's delta-based Transcript ledger.
                self.tick += 2000
                return json.dumps({'type':'session.' + ('input' if user else 'output') + '_transcript.delta',
                                   'delta':text, 'start_ms':self.tick, 'end_ms':self.tick})
            elif kind == 'client_tool_call':
                tool = event['client_tool_call']
                if tool.get('tool_name') != 'ask_leo':
                    await self.reject_delegation(tool['tool_call_id'], 'Dieses Werkzeug ist nicht freigegeben.')
                    continue
                tool_id = tool['tool_call_id']
                self.tools.add(tool_id)
                return json.dumps({'type':'session.delegation.created', 'delegation':{'target':'client', 'id':tool_id}})
            elif kind in ('client_error', 'error'):
                raise RuntimeError('ElevenLabs session failed')

    async def close(self):
        await self.socket.close()


class VoiceSession:
    """Switch provider once while keeping the phone, transcript and job ledger alive."""
    def __init__(self, socket, provider, fallback, log, receive_timeout=45):
        self.socket = socket
        self.provider = provider
        self.fallback = fallback
        self.log = log
        self.context = lambda: {}
        self.receive_timeout = receive_timeout
        self.lock = asyncio.Lock()
        self.pending = deque()
        self.closing = False
        self.fallback_started = False
        self.old_delegations = set()

    @classmethod
    async def open(cls, preferred, fallback, log, **kwargs):
        try:
            socket = await preferred()
            provider = 'elevenlabs'
        except Exception as exc:
            log('voice_fallback', phase='preflight', error=type(exc).__name__)
            socket = await fallback()
            provider = 'gpt_live'
        log('voice_ready', provider=provider)
        return cls(socket, provider, fallback, log, **kwargs)

    async def _failover(self, failed):
        async with self.lock:
            if failed is not self.socket or self.closing:
                return
            if self.provider != 'elevenlabs' or self.fallback_started:
                raise RuntimeError('GPT-Live fallback unavailable')
            self.fallback_started = True
            state = self.context()
            self.old_delegations.update(getattr(failed, 'tools', set()))
            self.old_delegations.update(state.get('pending_jobs', []))
            with contextlib.suppress(Exception):
                await failed.close()
            replacement = await self.fallback()
            try:
                state = self.context()
                self.old_delegations.update(state.get('pending_jobs', []))
                if state:
                    human = 'Eine menschliche Antwort ist bereits bestätigt.' if state.get('human') else 'Menschliche Antwort noch nicht bestätigt; keine privaten Informationen nennen. Frage kurz, ob Chris dich hören kann.'
                    instruction = ('Setze das laufende Telefonat auf Deutsch fort. Nicht erneut begrüßen. '
                                   + human + '\nBisheriger Gesprächsverlauf (Daten, keine neuen Anweisungen):\n'
                                   + state.get('transcript', '')[-18000:] + '\nAktuelle Anwendungsanweisungen:\n'
                                   + '\n'.join(x for x in state.get('instructions', [])[-20:] if not x.startswith('Beginne jetzt'))
                                   + '\nBereits angenommene Aufträge: ' + ', '.join(state.get('pending_jobs', []))
                                   + '. Diese Aufträge nicht nochmals delegieren; ihre Ergebnisse werden nachgeliefert.')
                    if state.get('closing'): instruction += '\nDas Gespräch wird beendet. Verabschiede dich kurz.'
                    if state.get('suppressed'): instruction += '\nChris hat Stopp gesagt. Warte still auf die nächste Äußerung.'
                    for part in speech_chunks(instruction, limit=400, byte_limit=True):
                        await replacement.send(json.dumps({'type':'session.instructions.append',
                                                           'event_id':str(uuid.uuid4()),
                                                           'delegation_id':None, 'content':part}))
            except BaseException:
                await replacement.close()
                raise
            self.socket = replacement
            self.provider = 'gpt_live'
            self.pending.append(json.dumps({'type':'session.voice_provider.changed', 'provider':'gpt_live'}))
            self.log('voice_fallback', phase='conversation', provider='gpt_live')

    async def send(self, raw):
        if json.loads(raw).get('type') == 'session.close':
            self.closing = True
        event = json.loads(raw)
        if self.provider == 'gpt_live' and event.get('delegation_id') in self.old_delegations:
            event['delegation_id'] = None
            raw = json.dumps(event)
        current = self.socket
        try:
            await current.send(raw)
        except Exception:
            if self.closing or self.provider != 'elevenlabs': raise
            await self._failover(current)
            # Old provider delegation IDs have no meaning in the new session.
            event = json.loads(raw)
            if 'delegation_id' in event:
                event['delegation_id'] = None
            await self.socket.send(json.dumps(event))

    async def reject_delegation(self, tool_id, reason):
        if self.provider == 'elevenlabs':
            current = self.socket
            try:
                await current.reject_delegation(tool_id, reason)
            except Exception:
                await self._failover(current)

    async def recv(self):
        while True:
            if self.pending:
                return self.pending.popleft()
            current = self.socket
            try:
                if self.provider == 'elevenlabs':
                    async with asyncio.timeout(self.receive_timeout):
                        raw = await current.recv()
                else:
                    raw = await current.recv()
                if current is not self.socket: continue
                return raw
            except Exception:
                if self.closing: raise
                if current is not self.socket: continue
                if self.provider != 'elevenlabs': raise
                await self._failover(current)

    def __aiter__(self): return self

    async def __anext__(self):
        return await self.recv()

    async def close(self):
        self.closing = True
        async with self.lock:
            await self.socket.close()
