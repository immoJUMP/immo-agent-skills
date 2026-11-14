"""Pure, shared phone boundary rules; no credentials or external effects."""
import re
import struct
import uuid


def validate_destination(number, allowed):
    if not re.fullmatch(r'0[1-9][0-9]{8,13}', number or '') or number != allowed:
        raise ValueError('Only the configured owner number is allowed')
    return number


def frame(kind, payload):
    return struct.pack('!BH', kind, len(payload)) + payload


def owner_dialplan(destination, caller_number, caller_name):
    destination = validate_destination(destination, destination)
    if not re.fullmatch(r'\+[1-9][0-9]{7,14}', caller_number or ''):
        raise ValueError('Caller number must be E.164')
    if not re.fullmatch(r'[A-Za-z0-9 -]{1,40}', caller_name or ''):
        raise ValueError('Invalid caller name')
    return f'''[reject-incoming]
exten => _.,1,Hangup()

[owner-call]
exten => owner,1,Set(CALLERID(num)={caller_number})
same => n,Set(CALLERID(name)={caller_name})
same => n,Set(CALLERID(pres)=allowed_not_screened)
same => n,Dial(PJSIP/{destination}@fritz,30)
same => n,Hangup()
'''


# SIP-Anbieter. "fritzbox" ist der Stand von Leo (Server im Heimnetz, TCP zur Box, Kubernetes-Pod-Netz).
# "sipgate" ist für einen Server mit öffentlicher IP in der Cloud: UDP zu sipgate.de, Docker-Netze als lokal.
SIP_ANBIETER = {
    'fritzbox': {'protokoll': 'tcp', 'host': None, 'proxy': None,
                 'lokale_netze': ('10.42.0.0/16', '127.0.0.0/8')},
    # Der Backslash schützt das Semikolon vor dem Kommentarzeichen in pjsip.conf
    'sipgate': {'protokoll': 'udp', 'host': 'sipgate.de', 'proxy': 'sip:sipgate.de\\;lr',
                'lokale_netze': ('10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16', '127.0.0.0/8')},
}
_NETZ = re.compile(r'(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])){3}/([0-9]|[12][0-9]|3[0-2])')


def sip_anbieter(name):
    name = (name or 'fritzbox').strip().lower()
    if name not in SIP_ANBIETER:
        raise ValueError('Unknown SIP provider')
    return name


def lokale_netze(text):
    """SIP_LOCAL_NETS: kommagetrennte IPv4-Netze, leer heißt Vorgabe des Anbieters."""
    netze = tuple(n.strip() for n in (text or '').split(',') if n.strip())
    for n in netze:
        if not _NETZ.fullmatch(n):
            raise ValueError('Invalid local network')
    return netze


def pjsip_config(anbieter, host, user, password, media, netze=()):
    """pjsip.conf für den Owner-Anruf. Nur ausgehend zur festen Nummer, eingehend wird abgewiesen."""
    a = SIP_ANBIETER[sip_anbieter(anbieter)]
    host = host or a['host']
    if not host:
        raise ValueError('SIP_HOST is required')
    for value in (host, user, password, media):
        if not value or '\n' in value or '\r' in value or ';' in value:
            raise ValueError('Invalid SIP configuration')
    netze = netze or a['lokale_netze']
    proto = a['protokoll']
    tp = f'transport-{proto}'
    lokal = ''.join(f'local_net={n}\n' for n in netze)
    if proto == 'tcp':
        server, kontakt = f'sip:{host};transport=tcp', f'sip:{host}:5060;transport=tcp'
    else:
        server, kontakt = f'sip:{host}', f'sip:{host}:5060'
    proxy = f"outbound_proxy={a['proxy']}\n" if a['proxy'] else ''
    return f'''[{tp}]
type=transport
protocol={proto}
bind=0.0.0.0:15062
{lokal}external_media_address={media}
external_signaling_address={media}
external_signaling_port=15062

[fritz-auth]
type=auth
auth_type=userpass
username={user}
password={password}

[fritz-registration]
type=registration
transport={tp}
outbound_auth=fritz-auth
server_uri={server}
client_uri=sip:{user}@{host}
contact_user={user}
{proxy}retry_interval=60
expiration=300

[fritz-aor]
type=aor
contact={kontakt}
qualify_frequency=60

[fritz]
type=endpoint
transport={tp}
context=reject-incoming
disallow=all
allow=alaw,ulaw
outbound_auth=fritz-auth
aors=fritz-aor
from_user={user}
from_domain={host}
{proxy}send_pai=yes
direct_media=no
rtp_symmetric=yes
force_rport=yes
rewrite_contact=yes

[fritz-identify]
type=identify
endpoint=fritz
match={host}
'''


def next_audio_tick(previous_deadline, now):
    deadline = previous_deadline + 0.02
    # Keep cadence independent of write/drain overhead; avoid a burst after a stall.
    if now - deadline > 0.2:
        deadline = now
    return deadline, max(0.0, deadline - now)


def hermes_command(call_id):
    call_id = str(uuid.UUID(call_id))
    return ['/opt/hermes/.venv/bin/hermes', 'chat', '--cli', '-Q', '--oneshot',
            '--query-file', '-', '--continue', 'leo-phone-' + call_id,
            '--create-if-missing', '--source', 'voice-live',
            '--run-budget', '120', '--max-turns', '12']


class Delegations:
    def __init__(self):
        self.seen = set()

    def claim(self, delegation_id):
        if not delegation_id or delegation_id in self.seen:
            return False
        self.seen.add(delegation_id)
        return True


class CallGate:
    def __init__(self, cooldown=300):
        self.cooldown = cooldown
        self.active = None
        self.last_time = None
        self.seen = set()

    def reserve(self, event_id, now):
        if self.active or event_id in self.seen:
            raise ValueError('Call already active or event already handled')
        if self.last_time is not None and now - self.last_time < self.cooldown:
            raise ValueError('Call cooldown active')
        self.active = event_id
        self.last_time = now
        self.seen.add(event_id)

    def release(self):
        self.active = None
