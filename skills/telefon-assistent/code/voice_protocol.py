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
