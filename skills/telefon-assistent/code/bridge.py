"""Owner-only FRITZ!Box/Asterisk AudioSocket with ElevenLabs/GPT-Live voices."""
import asyncio
import audioop
import base64
import contextlib
import hmac
import hashlib
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import struct
import time
import uuid
from aiohttp import web, ClientSession, ClientTimeout
from websockets.asyncio.client import connect
from phone_logic import MODES, ZONE, Transcript, call_policy, presence, voice_control, speech_chunks, redact
from hold_music import HoldMusic
from voice_provider import VoiceSession, open_elevenlabs
from voice_protocol import CallGate, Delegations, frame, validate_destination, next_audio_tick, owner_dialplan, pjsip_config, lokale_netze

TOKEN = os.environ['BRIDGE_TOKEN']
ALLOWED = os.environ['CALL_ALLOWED_NUMBER']
LIVE_VOICE = os.environ.get('LIVE_VOICE', 'meridian')
BACKEND = os.environ.get('LEO_BACKEND_URL', 'http://leo-voice-backend:9120')
JOURNAL = Path('/state/calls.json')
GATE = CallGate()
STATUS = {}
PENDING = {}
TASKS = set()
AST = None
CODE_REVISION = "20261004-audio-burst-1"
# A provider may synthesize a complete answer much faster than real time.
# Sixty seconds of 8 kHz, 16-bit mono PCM is a bounded one-answer buffer.
MAX_AUDIO_QUEUE_BYTES = 8000 * 2 * 60

PERSONA = """Du bist Leo, der persönliche KI-Assistent von Chris, am Telefon.
Sprich durchgehend natürliches Standarddeutsch, ruhig und in kurzen Sätzen.
Sprich Zahlen, Daten und Uhrzeiten auf Deutsch. Wechsle die Sprache nur auf ausdrücklichen Wunsch. Du bist eine KI, kein Mensch.
Beginne nur mit einer kurzen Begrüßung und warte auf Chris. Solange die Anwendung
keine menschliche Antwort bestätigt, keine persönlichen Informationen oder Anlässe nennen.
Lasse Chris ausreden, höre beim Unterbrechen sofort zu. Stelle jeweils nur eine Frage.
Delegation policy:
Backend tools: Leos bestehendes Gedächtnis, Projektkontext und Arbeitswerkzeuge.
Delegate to the backend when: Chris fragt nach persönlichen/aktuellen Fakten,
will eine Entscheidung fundiert besprechen oder erteilt einen konkreten Arbeitsauftrag.
Do not delegate to the backend when: Begrüßung, Wiederholung eines bekannten Ergebnisses,
Smalltalk, Verabschiedung, Stopp oder Abbruch. Diese Steuerbefehle behandelt die Anwendung.
Sage bei Recherche einmal kurz, dass du nachsiehst. Erfinde keine Ergebnisse und
versprich keine ausgeführte Aktion, bevor das Backend deren Erfolg bestätigt.
Aufträge können nach dem Auflegen weiterlaufen; Ergebnisse kommen im Telegram-Chat.
„Stopp“ bedeutet aufhören zu sprechen. „Brich den Auftrag ab“ bedeutet Aufgabe abbrechen.
Bei „Danke, das war's“ kurz verabschieden; die Anwendung beendet die Verbindung.
Lies keine Markdown-Zeichen, langen URLs oder technischen IDs vor."""



def log(event, **fields):
    print(json.dumps({'time': time.time(), 'event': event, **fields}), flush=True)


def persist():
    JOURNAL.parent.mkdir(parents=True, exist_ok=True)
    tmp = JOURNAL.with_suffix('.tmp')
    tmp.write_text(json.dumps({'last_time': GATE.last_time, 'seen': list(GATE.seen)[-1000:],
                               'status': STATUS}))
    tmp.chmod(0o600)
    tmp.replace(JOURNAL)


def configure_asterisk():
    # SIP_PROVIDER: fritzbox (Vorgabe, wie Leo im Heimnetz) oder sipgate (Server mit öffentlicher IP).
    # SIP_MEDIA_ADDRESS: bei FRITZ!Box die IP des Servers im Heimnetz, bei sipgate die öffentliche IP.
    config = pjsip_config(os.environ.get('SIP_PROVIDER', 'fritzbox'), os.environ.get('SIP_HOST', ''),
                          os.environ['SIP_USERNAME'], os.environ['SIP_PASSWORD'],
                          os.environ['SIP_MEDIA_ADDRESS'], lokale_netze(os.environ.get('SIP_LOCAL_NETS', '')))
    configs = {
        'pjsip.conf': config,
        'rtp.conf': '[general]\nrtpstart=26000\nrtpend=26020\nstrictrtp=yes\n',
        'extensions.conf': owner_dialplan(ALLOWED, os.environ['SIP_CALLER_ID_NUMBER'],
                                         os.environ['SIP_CALLER_ID_NAME']),
        'http.conf': '[general]\nenabled=no\n',
        'manager.conf': '[general]\nenabled=no\n',
        'logger.conf': '[general]\n[logfiles]\nconsole => error,warning\n',
        'cdr.conf': '[general]\nenable=no\n',
        'cel.conf': '[general]\nenable=no\n',
        'modules.conf': '[modules]\nautoload=yes\nnoload=chan_sip.so\nnoload=chan_iax2.so\nnoload=res_hep.so\nnoload=res_hep_pjsip.so\nnoload=res_hep_rtcp.so\n',
    }
    for name, data in configs.items():
        p = Path('/etc/asterisk') / name
        p.write_text(data)
        p.chmod(0o600)


async def ast_command(command):
    p = await asyncio.create_subprocess_exec('/usr/sbin/asterisk', '-rx', command,
                                             stdout=asyncio.subprocess.PIPE,
                                             stderr=asyncio.subprocess.DEVNULL)
    out, _ = await asyncio.wait_for(p.communicate(), 8)
    return out.decode(errors='replace')


async def open_live():
    ws = await connect('wss://api.openai.com/v1/live/sessions',
                       additional_headers={'Authorization': 'Bearer ' + os.environ['OPENAI_API_KEY']},
                       open_timeout=15, max_size=4 * 1024 * 1024)
    try:
        await ws.send(json.dumps({'type': 'session.start', 'session': {
            'model': 'gpt-live-1', 'instructions': PERSONA,
            'audio': {'format': {'type': 'audio/pcmu', 'rate': 8000}, 'output': {'voice': LIVE_VOICE}},
            'delegation': {'type': 'client'}}}))
        async with asyncio.timeout(20):
            while True:
                event = json.loads(await ws.recv())
                if event['type'] == 'session.started':
                    log('live_ready', session_id=event['session']['id'], voice=LIVE_VOICE)
                    return ws
                if event['type'] == 'error':
                    log('live_rejected', code=event.get('error', {}).get('code'))
                    raise RuntimeError('Live session rejected')
    except BaseException:
        await ws.close()
        raise


async def open_voice():
    provider = os.environ.get('VOICE_PROVIDER', 'gpt_live')
    if provider == 'gpt_live':
        return await open_live()
    if provider != 'elevenlabs':
        raise ValueError('Unsupported voice provider')
    return await VoiceSession.open(open_elevenlabs, open_live, log=log)


async def audio_connection(reader, writer):
    done = None
    try:
        header = await asyncio.wait_for(reader.readexactly(3), 5)
        kind, size = struct.unpack('!BH', header)
        if kind != 1 or size != 16:
            return
        call_id = str(uuid.UUID(bytes=await reader.readexactly(16)))
        pending = PENDING.get(call_id)
        if not pending or pending[0].done():
            return
        future, done = pending
        future.set_result((reader, writer))
        await done.wait()
    except (asyncio.IncompleteReadError, TimeoutError):
        pass
    finally:
        writer.close()
        with contextlib.suppress(Exception):
            await writer.wait_closed()


async def backend_request(path, data=None, timeout=20):
    async with ClientSession(timeout=ClientTimeout(total=timeout)) as client:
        method=client.get if data is None else client.post
        kwargs={'headers':{'Authorization':'Bearer '+TOKEN}}
        if data is not None: kwargs['json']=data
        async with method(BACKEND+path,**kwargs) as response:
            result=await response.json()
            if response.status>=400: raise RuntimeError('Backend rejected '+path)
            return result


async def conversation(call_id, ws, reader, writer, reason):
    audio_queue=bytearray(); transcript=Transcript(); ledger=Delegations()
    backend_tasks=set(); waiting_jobs=set(); music=HoldMusic(); done=asyncio.Event()
    state={'human':False,'input_buffer':'','last_input':0.0,'closing_at':None,
           'suppress_output':False,'last_voice':0.0,'control_turn':None}
    counters={'input_frames':0,'output_frames':0,'delegations':0,'backend_answers':0,'music_frames':0}
    start=asyncio.get_running_loop().time()
    STATUS[call_id]['outcome']='unconfirmed'
    STATUS[call_id]['voice_provider']=getattr(ws,'provider','gpt_live')
    instructions=[]
    if isinstance(ws,VoiceSession):
        ws.context=lambda:{'transcript':transcript.render(),'human':state['human'],
                           'pending_jobs':sorted(waiting_jobs),'instructions':instructions,
                           'closing':state['closing_at'] is not None,'suppressed':state['suppress_output']}

    async def send(event): await ws.send(json.dumps(event))
    async def append(kind,text,delegation_id=None):
        if kind=='instructions':
            instructions.append(text); del instructions[:-20]
        for part in speech_chunks(text,limit=400,byte_limit=True):
            await send({'type':'session.'+kind+'.append','event_id':str(uuid.uuid4()),
                        'delegation_id':delegation_id,'content':part})

    async def reject_delegation(delegation_id):
        reject=getattr(ws,'reject_delegation',None)
        if reject is not None:
            await reject(delegation_id,'Kein neuer Auftrag: menschliche Antwort fehlt, Steuerbefehl oder Auftrag bereits angenommen.')

    async def delegate(delegation_id):
        await asyncio.sleep(.9)  # Transcript fragments can arrive shortly after delegation.
        if not state['human'] or state['closing_at'] is not None:
            await reject_delegation(delegation_id); return
        if voice_control(transcript.last_user()):
            await reject_delegation(delegation_id); return
        users=[t for t in transcript.turns if t['role']=='user']
        if not users:
            await reject_delegation(delegation_id); return
        latest=users[-1]
        fingerprint=hashlib.sha256(json.dumps(latest,sort_keys=True).encode()).hexdigest()
        if not ledger.claim('turn:'+fingerprint):
            await reject_delegation(delegation_id); return
        counters['delegations']+=1
        try:
            job=await backend_request('/jobs',{'call_id':call_id,'delegation_id':delegation_id,
                                               'conversation':transcript.render()})
            waiting_jobs.add(delegation_id)
            started=time.monotonic(); announced=False
            while not done.is_set():
                result=await backend_request('/jobs/'+job['id'])
                if result['state'] in ('completed','cancelled','cancel_requested','failed','interrupted'):
                    waiting_jobs.discard(delegation_id)
                if result['state']=='completed':
                    body=json.loads(result['result']); counters['backend_answers']+=1
                    await append('commentary',body['spoken'],delegation_id)
                    log('delegation_answered',call_id=call_id,job_id=job['id']); return
                if result['state'] in ('cancelled','cancel_requested'):
                    await append('commentary','Die Bearbeitung wurde gestoppt oder wird gerade beendet. Bereits ausgeführte externe Schritte werden dadurch nicht automatisch rückgängig gemacht.',delegation_id); return
                if result['state'] in ('failed','interrupted'):
                    await append('commentary','Die Aufgabe konnte nicht sicher abgeschlossen werden. Ich halte den offenen Status im Telegram-Chat fest.',delegation_id); return
                if time.monotonic()-started>6 and not announced:
                    await append('commentary','Ich prüfe das noch. Du kannst weiterreden; das Ergebnis bleibt auch nach dem Auflegen erhalten.',delegation_id); announced=True
                await asyncio.sleep(.7)
        except Exception as exc:
            waiting_jobs.discard(delegation_id)
            log('delegation_failed',call_id=call_id,error=type(exc).__name__)
            await append('commentary','Die Verbindung zu meinem Arbeitsdienst ist gerade gestört. Ich kann den Erfolg dieser Aufgabe noch nicht bestätigen.',delegation_id)

        finally:
            waiting_jobs.discard(delegation_id)

    async def phone_input():
        speech_frames=0
        while True:
            kind,size=struct.unpack('!BH',await reader.readexactly(3))
            if size>8192: raise ValueError('Oversized audio frame')
            payload=await reader.readexactly(size)
            if kind==0: return
            if kind==0x10:
                if len(payload)%2: raise ValueError('Invalid PCM frame')
                counters['input_frames']+=1
                if audioop.rms(payload,2)>650:
                    music.user_spoke(time.monotonic())
                    speech_frames+=1
                    if speech_frames==5: audio_queue.clear()
                else: speech_frames=0
                await send({'type':'session.input_audio.append','audio':base64.b64encode(audioop.lin2ulaw(payload,2)).decode()})
            elif kind==0xff: raise RuntimeError('AudioSocket error')

    async def live_output():
        async for raw in ws:
            event=json.loads(raw); kind=event.get('type')
            if kind=='session.output_audio.delta':
                if not state['suppress_output']:
                    audio_queue.extend(audioop.ulaw2lin(base64.b64decode(event['delta']),2))
                    state['last_voice']=time.monotonic()
                STATUS[call_id]['peak_audio_queue_bytes'] = max(
                    STATUS[call_id].get('peak_audio_queue_bytes', 0), len(audio_queue))
                if len(audio_queue)>MAX_AUDIO_QUEUE_BYTES:
                    STATUS[call_id]['end_reason'] = 'audio_queue_limit'
                    log('audio_queue_limit', call_id=call_id, queued_bytes=len(audio_queue))
                    raise RuntimeError('Audio queue exceeds bounded answer buffer')
            elif kind in ('session.output_audio.interrupted','session.voice_provider.changed'):
                audio_queue.clear()
                if kind=='session.voice_provider.changed':
                    STATUS[call_id]['voice_provider']=event['provider']
                    STATUS[call_id]['voice_fallback_at']=time.time(); persist()
            elif kind in ('session.input_transcript.delta','session.output_transcript.delta'):
                role='user' if kind.startswith('session.input') else 'assistant'
                delta=event.get('delta','')
                transcript.append(role,delta,event.get('start_ms',0),event.get('end_ms',0))
                if role=='user':
                    music.user_spoke(time.monotonic())
                    if state['suppress_output']: state['suppress_output']=False
                    state['input_buffer']+=delta; state['last_input']=time.monotonic()
            elif kind=='session.delegation.created':
                d=event.get('delegation',{})
                if d.get('target')=='client' and ledger.claim(d.get('id')):
                    task=asyncio.create_task(delegate(d['id'])); backend_tasks.add(task); task.add_done_callback(backend_tasks.discard)
            elif kind=='error':
                log('live_error',call_id=call_id,code=event.get('error',{}).get('code'))
                raise RuntimeError('Live error')
            elif kind=='session.closed': return

    async def controls():
        while not done.is_set():
            now=time.monotonic()
            if state['input_buffer'] and now-state['last_input']>.75:
                utterance=transcript.last_user(); state['input_buffer']=''
                detected=presence(utterance)
                if not state['human']:
                    if detected=='voicemail':
                        STATUS[call_id]['outcome']='voicemail'; audio_queue.clear(); done.set(); return
                    if detected=='human':
                        state['human']=True; STATUS[call_id]['outcome']='ended'
                        STATUS[call_id]['human_confirmed_at']=time.time(); persist()
                        mode=STATUS[call_id].get('mode','conversation')
                        await append('instructions','Eine menschliche Antwort ist bestätigt. '+MODES[mode])
                        await append('commentary','Anlass dieses Gesprächs: '+reason+'. Steige kurz und konkret ein; bei Unklarheit frage Chris.')
                if state['human']:
                    control=voice_control(utterance)
                    if control=='hangup' and state['closing_at'] is None:
                        state['closing_at']=now
                        STATUS[call_id].update(end_reason='user_hangup',hangup_detected_at=time.time())
                        log('hangup_detected',call_id=call_id)
                        await append('instructions','Chris beendet das Gespräch. Verabschiede dich jetzt in einem kurzen Satz. Keine neue Frage, keine Delegation.')
                    elif control=='stop_speaking':
                        audio_queue.clear(); state['suppress_output']=True
                        await append('instructions','Höre jetzt auf zu sprechen und warte still auf Chris. Dies ist kein Abbruch laufender Aufgaben.')
                    elif control=='cancel_tasks':
                        result=await backend_request('/cancel',{'call_id':call_id})
                        await append('commentary','Der Abbruch der laufenden Aufträge ist angefordert.' if result['jobs'] else 'Es gibt gerade keinen laufenden Auftrag zum Abbrechen.')
            if not state['human'] and now-start>18:
                STATUS[call_id]['outcome']='unconfirmed'; done.set(); return
            if state['closing_at'] is not None and (now-state['closing_at']>4 or (now-state['closing_at']>1.2 and not audio_queue and now-state['last_voice']>.4)):
                done.set(); return
            if now-start>590 and state['closing_at'] is None:
                await append('instructions','Die maximale Gesprächsdauer ist erreicht. Verabschiede dich kurz. Ergebnisse folgen in Telegram.')
                if state['closing_at'] is None: state['closing_at']=now
            await asyncio.sleep(.1)

    async def playback():
        loop=asyncio.get_running_loop(); deadline=loop.time()
        while True:
            had_audio=bool(audio_queue)
            chunk=bytes(audio_queue[:320]); del audio_queue[:320]
            pcm=music.render(chunk.ljust(320,b'\0'),waiting=bool(waiting_jobs),now=time.monotonic(),
                             muted=not state['human'] or state['suppress_output'] or state['closing_at'] is not None)
            if had_audio or music.audible:
                writer.write(frame(0x10,pcm)); await writer.drain()
                counters['output_frames']+=1
                if music.audible: counters['music_frames']+=1
            deadline,delay=next_audio_tick(deadline,loop.time()); await asyncio.sleep(delay)

    await append('instructions','Beginne jetzt sofort auf Deutsch mit: Hallo Chris, hier ist Leo, dein KI-Assistent. Kannst du mich hören? Danach warten und zuhören. Noch keinen Anlass nennen.')
    tasks=[asyncio.create_task(f()) for f in (phone_input,live_output,playback,controls)]
    tasks.append(asyncio.create_task(done.wait()))
    try:
        completed,_=await asyncio.wait(tasks,timeout=600,return_when=asyncio.FIRST_COMPLETED)
        for task in completed:
            if not task.cancelled() and task.exception() and not isinstance(task.exception(),asyncio.IncompleteReadError): raise task.exception()
    finally:
        done.set()
        for task in tasks+list(backend_tasks): task.cancel()
        await asyncio.gather(*tasks,*backend_tasks,return_exceptions=True)
        STATUS[call_id].update(counters)
        STATUS[call_id]['report']={'call_id':call_id,'state':STATUS[call_id].get('outcome','ended'),
                                 'transcript':transcript.turns}
        log('audio_metrics',call_id=call_id,**counters)


async def run_call(call_id, reason, ws):
    future = asyncio.get_running_loop().create_future()
    done = asyncio.Event()
    PENDING[call_id] = (future, done)
    try:
        # The only destination is the server-side allowlisted owner number.
        validate_destination(ALLOWED, ALLOWED)
        # Local dialplan sets identity before creating the outbound SIP channel.
        await ast_command(f'channel originate Local/owner@owner-call/n application AudioSocket {call_id},127.0.0.1:9019')
        STATUS[call_id]['dialed_at'] = time.time()
        STATUS[call_id]['state'] = 'dialing'
        persist()
        log('dialing', call_id=call_id)
        reader, writer = await asyncio.wait_for(future, 45)
        STATUS[call_id]['state'] = 'connected'
        STATUS[call_id]['connected_at'] = time.time()
        persist()
        log('connected', call_id=call_id)
        await conversation(call_id, ws, reader, writer, reason)
        STATUS[call_id]['state'] = STATUS[call_id].get('outcome', 'ended')
    except Exception as exc:
        STATUS[call_id]['state'] = 'failed'
        STATUS[call_id]['error'] = type(exc).__name__
        log('call_failed', call_id=call_id, error=type(exc).__name__)
    finally:
        done.set()
        PENDING.pop(call_id, None)
        with contextlib.suppress(Exception):
            STATUS[call_id]['hangup_requested_at']=time.time()
            await ast_command('channel request hangup all')
            log('hangup_requested',call_id=call_id,end_reason=STATUS[call_id].get('end_reason','connection_ended'))
        with contextlib.suppress(Exception):
            await ws.send(json.dumps({'type': 'session.close'}))
        await ws.close()
        STATUS[call_id]['ended_at'] = time.time()
        GATE.release()
        persist()
        STATUS[call_id].setdefault('report', {'call_id':call_id,'state':STATUS[call_id]['state'],'transcript':[]})
        STATUS[call_id]['report_status']='pending'
        persist()
        log('call_finished', call_id=call_id, state=STATUS[call_id]['state'])


def authorized(request):
    return hmac.compare_digest(request.headers.get('Authorization', ''), 'Bearer ' + TOKEN)


async def health(request):
    ready = AST is not None and AST.returncode is None
    return web.json_response({'ok': ready}, status=200 if ready else 503)


async def status(request):
    if not authorized(request): return web.json_response({'error':'unauthorized'},status=401)
    safe={cid:{k:v for k,v in row.items() if k not in ('report','context')} for cid,row in STATUS.items()}
    return web.json_response({'active':GATE.active,'calls':safe,'version':2,'code_revision':CODE_REVISION})


async def call(request):
    if not authorized(request): return web.json_response({'error':'unauthorized'},status=401)
    reserved=False
    try:
        data=await request.json(); validate_destination(data.get('number',ALLOWED),ALLOWED)
        cid=str(uuid.UUID(data['event_id'])); reason=data['reason']; kind=data.get('kind','requested')
        if not isinstance(reason,str) or not 1<=len(reason)<=1000: raise ValueError('Invalid reason')
        if cid in STATUS: raise ValueError('Event already handled; check status')
        mode=data.get('mode','conversation')
        if mode not in MODES: raise ValueError('Unknown mode')
        now=datetime.now(timezone.utc); today=now.astimezone(ZONE).date()
        attempts=[s for s in STATUS.values() if s.get('dialed_at') and datetime.fromtimestamp(s['dialed_at'],ZONE).date()==today]
        decision=call_policy(kind,now,len(attempts),sum(s.get('kind','requested')!='requested' for s in attempts),evidence=data.get('evidence',''))
        if decision=='call': GATE.reserve(cid,time.time()); reserved=True
    except (ValueError,KeyError,TypeError) as exc: return web.json_response({'error':str(exc)},status=409)
    STATUS[cid]={'state':'preflight','started_at':time.time(),'kind':kind,'mode':mode}; persist()
    try:
        await backend_request('/prepare',{**data,'call_id':cid})
        if decision!='call':
            labels={'message':'Information','quiet_hours':'Ruhezeit','daily_limit':'Tageslimit erreicht','proactive_limit':'Limit für selbstständige Anrufe erreicht','unverified':'Anlass noch nicht ausreichend belegt'}
            await backend_request('/notice',{'call_id':cid,'event_key':'policy:'+cid,
                'text':'Leo · '+labels[decision]+'\n\n'+redact(reason)+(('\nEntscheidung bis: '+str(data['deadline'])) if data.get('deadline') else '')})
            STATUS[cid]['state']='message_only'; STATUS[cid]['policy']=decision; persist()
            return web.json_response({'call_id':cid,'state':'message_only','policy':decision},status=202)
        if 'Registered' not in await ast_command('pjsip show registrations'): raise RuntimeError('SIP not registered')
        ws=await open_voice()
    except Exception as exc:
        if reserved: GATE.release()
        STATUS[cid].update(state='preflight_failed',error=type(exc).__name__,report_status='pending',report={'call_id':cid,'state':'preflight_failed','transcript':[]})
        persist(); return web.json_response({'error':'Preflight failed; no call placed','call_id':cid},status=503)
    task=asyncio.create_task(run_call(cid,reason,ws)); TASKS.add(task); task.add_done_callback(TASKS.discard)
    return web.json_response({'call_id':cid,'state':'starting'},status=202)


async def hangup(request):
    if not authorized(request): return web.json_response({'error':'unauthorized'},status=401)
    data=await request.json()
    if not GATE.active or data.get('call_id')!=GATE.active:
        return web.json_response({'error':'No matching active call'},status=409)
    await ast_command('channel request hangup all')
    return web.json_response({'state':'hangup_requested'})


async def reports_loop():
    while True:
        for cid,row in list(STATUS.items()):
            if row.get('report_status')=='pending':
                try:
                    await backend_request('/finish',row['report'])
                    row['report_status']='queued'; row.pop('report',None); persist()
                except Exception as exc: log('report_retry_pending',call_id=cid,error=type(exc).__name__)
        await asyncio.sleep(10)


async def main():
    global AST
    if JOURNAL.exists():
        saved = json.loads(JOURNAL.read_text())
        GATE.last_time = saved.get('last_time')
        GATE.seen = set(saved.get('seen', []))
        STATUS.update(saved.get('status', {}))
        for entry in STATUS.values():
            if entry.get('state') in ('dialing', 'connected', 'preflight'):
                entry['state'] = 'interrupted_by_restart'
                entry['report_status'] = 'pending'
    for cid,entry in STATUS.items():
        if entry.get('report_status')=='pending': entry.setdefault('report',{'call_id':cid,'state':entry['state'],'transcript':[]})
    configure_asterisk()
    ast_log = open('/tmp/asterisk.log', 'ab', buffering=0)
    AST = await asyncio.create_subprocess_exec('/usr/sbin/asterisk', '-f', '-g',
                                              stdout=ast_log, stderr=ast_log)
    server = await asyncio.start_server(audio_connection, '127.0.0.1', 9019)
    app = web.Application(client_max_size=4000)
    app.add_routes([web.get('/health', health), web.get('/status', status), web.post('/call', call), web.post('/hangup',hangup)])
    runner = web.AppRunner(app, access_log=None)
    await runner.setup()
    await web.TCPSite(runner, '0.0.0.0', 8080).start()
    reporter=asyncio.create_task(reports_loop())
    log('bridge_started',version=2)
    await AST.wait()
    reporter.cancel()
    server.close()
    await server.wait_closed()
    await runner.cleanup()
    raise RuntimeError('Asterisk exited')


if __name__ == '__main__':
    asyncio.run(main())
