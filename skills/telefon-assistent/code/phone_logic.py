"""Phone policy and conversation handling, independent of network and model calls."""
from datetime import datetime, timedelta
import json
import hashlib
import re
from zoneinfo import ZoneInfo

ZONE = ZoneInfo('Europe/Berlin')
MODES = {
    'conversation': 'Besprich den genannten Anlass. Frage nur nach fehlenden Informationen.',
    'preparation': 'Bereite Chris auf den anstehenden Kundentermin vor: Ziel, bekannte Fakten, offene Fragen und mögliche Einwände. Keine Fakten zum Kunden erfinden.',
    'sales_training': 'Übe ein Verkaufsgespräch: übernimm den Interessenten mit realistischen Einwänden, stelle jeweils eine Frage und warte. Auf Wunsch beende die Rolle und gib konkretes Feedback zu Klarheit, Nutzen und nächstem Schritt.',
    'daily_review': 'Führe einen kurzen Tagesabschluss: Was wurde erreicht und entschieden, was bleibt offen, was ist morgen der wichtigste Schritt? Maximal drei Fragen, einzeln stellen.',
}


def redact(text):
    text = re.sub(r'\bsk-[A-Za-z0-9_-]{16,}', '[Zugangsdaten entfernt]', str(text))
    text = re.sub(r'(?i)(bearer\s+)[A-Za-z0-9_.-]{12,}', r'\1[entfernt]', text)
    text = re.sub(r'(?i)((?:password|passwort|api[_ -]?key|token)\s*[:=]\s*)[^\s,;]+', r'\1[entfernt]', text)
    return text


def call_policy(kind, now, daily_calls, proactive_calls, evidence='', daily_limit=10, proactive_limit=3):
    if kind not in ('requested', 'proactive', 'emergency', 'scheduled', 'info', 'decision'):
        raise ValueError('Invalid call kind')
    if kind in ('info', 'decision'):
        return 'message'
    if kind == 'emergency' and not evidence.strip():
        raise ValueError('Emergency requires verified evidence')
    if daily_calls >= daily_limit: return 'daily_limit'
    if kind != 'requested' and proactive_calls >= proactive_limit: return 'proactive_limit'
    if kind not in ('requested', 'emergency') and not 8 <= now.astimezone(ZONE).hour < 20:
        return 'quiet_hours'
    if kind == 'proactive' and not evidence.strip(): return 'unverified'
    return 'call'


def schedule_time(value, preparation=False):
    when = datetime.fromisoformat(value)
    if when.tzinfo is None: raise ValueError('Schedule requires explicit timezone')
    if preparation: when -= timedelta(minutes=15)
    return when.timestamp()


class Transcript:
    def __init__(self): self.turns = []
    def append(self, role, delta, start_ms=0, end_ms=0):
        if role not in ('user', 'assistant') or not isinstance(delta, str): return
        previous=next((t for t in reversed(self.turns) if t['role']==role),None)
        # Full-duplex transcripts interleave both speakers, even within one utterance.
        contiguous=previous is not None and 0<=start_ms-previous['end_ms']<(1800 if self.turns[-1] is previous else 600)
        if contiguous:
            previous['text']+=delta; previous['end_ms']=max(end_ms,previous['end_ms'])
        else:
            self.turns.append({'role':role,'text':delta,'start_ms':start_ms,'end_ms':end_ms})
        if len(self.turns) > 150: self.turns = self.turns[-150:]
    def last_user(self):
        return next((t['text'] for t in reversed(self.turns) if t['role'] == 'user'), '')
    def render(self, limit=18000):
        chosen=[]; size=0
        for t in reversed(self.turns):
            line=('Chris: ' if t['role']=='user' else 'Leo: ')+t['text']
            if size+len(line)>limit: break
            chosen.append(line); size+=len(line)
        return '\n'.join(reversed(chosen))


def normalized(text):
    return re.sub(r'[^a-zäöüß0-9 ]', '', text.lower().replace('’', '').replace("'", '')).strip()


def hangup_intent(text):
    # Match direct requests, not quotations, negations, reported speech or future plans.
    raw=str(text)
    if any(q in raw for q in ('"','„','“','«','»')): return False
    noun=r'(?:das|unser|dieses) (?:gespräch|telefonat)|(?:den|unseren|diesen) anruf'
    filler=r'(?:(?:bitte|jetzt|nun|gerne|gern|mal|einfach) )*'
    patterns=(
        rf'leg(?:e)? {filler}auf',
        rf'auflegen(?: bitte)?',
        rf'beende {filler}(?:{noun})(?: (?:bitte|jetzt|nun|gern|gerne))*',
        rf'ich (?:möchte|will|würde) {filler}(?:(?:{noun}) {filler})?(?:beenden|auflegen)',
        rf'(?:kannst|könntest|würdest) du {filler}(?:(?:{noun}) {filler})?(?:beenden|auflegen)',
        rf'(?:können|könnten|wollen) wir {filler}(?:{noun}) {filler}beenden',
        rf'lass uns {filler}(?:{noun}) {filler}beenden',
        r'(?:danke |vielen dank )?das (?:wars|war es)(?: für heute)?',
        r'(?:danke )?(?:tschüss|tschau|ciao|auf wiederhören)(?: leo)?',
    )
    for sentence in re.split(r'[.!?]+',raw):
        s=' '.join(normalized(sentence).split())
        s=re.sub(r'^(?:(?:okay|ok|gut|also|leo|danke|vielen dank|bitte) )+','',s)
        s=re.sub(r' (?:bitte|danke|leo)$','',s)
        if any(re.fullmatch(pattern,s) for pattern in patterns): return True
    return False


def voice_control(text):
    s=normalized(text)
    if s in ('stopp','stop','sei kurz still','bitte sei still','hör kurz auf zu sprechen'):
        return 'stop_speaking'
    if s in ('abbrechen','brich den auftrag ab','bitte brich den auftrag ab','brich die aufgabe ab','stoppe die aufgabe','alle aufträge abbrechen'):
        return 'cancel_tasks'
    if hangup_intent(text):
        return 'hangup'
    return None


def presence(text):
    s=normalized(text)
    if any(x in s for x in ('mailbox','signalton','hinterlassen sie','nicht erreichbar','anrufbeantworter','nachricht nach dem','sprechen sie nach')):
        return 'voicemail'
    if re.search(r'\b(hallo|ja|hier ist chris|ich höre dich|ich bin da|guten abend|guten morgen|servus|moin|hi leo)\b',s):
        return 'human'
    return None


def speech_chunks(text, limit=800, byte_limit=False):
    # UTF-8 bytes bound tokenizer size; Telegram uses the less restrictive character limit.
    size=lambda x: len(x.encode()) if byte_limit else len(x)
    words=str(text).split(); out=[]; current=''
    for word in words:
        if size(word)>limit:
            if current: out.append(current); current=''
            piece=''
            for char in word:
                if size(piece+char)>limit: out.append(piece); piece=''
                piece+=char
            if piece: out.append(piece)
            continue
        if current and size(current+' '+word)>limit:
            out.append(current); current=word
        else: current+=(' ' if current else '')+word
    if current: out.append(current)
    return out


def calendar_schedules(events, now, calendar_id='primary'):
    result=[]
    for event in events:
        start=event.get('start',{}).get('dateTime')
        if not start or event.get('status')=='cancelled' or event.get('transparency')=='transparent': continue
        if event.get('eventType','default') not in ('default',): continue
        if any(a.get('self') and a.get('responseStatus')=='declined' for a in event.get('attendees',[])): continue
        others=[a for a in event.get('attendees',[]) if not a.get('self') and a.get('responseStatus')!='declined']
        if not others and '[leo]' not in event.get('summary','').lower(): continue
        when=datetime.fromisoformat(start)
        if when.tzinfo is None or when.astimezone(ZONE).weekday()>=5: continue
        due=when.timestamp()-900
        if due<now-300: continue
        key='calendar:'+hashlib.sha256((calendar_id+':'+event['id']).encode()).hexdigest()[:32]
        payload={'reason':'Vorbereitung auf '+redact(event.get('summary','Termin'))[:300]+' um '+when.astimezone(ZONE).strftime('%H:%M')+' Uhr',
                 'kind':'scheduled','mode':'preparation','calendar_id':calendar_id,'calendar_event_id':event['id'],'calendar_start':start}
        result.append((key,due,payload))
    return result


def result_parts(raw):
    cleaned=raw.strip()
    if cleaned.startswith('```'): cleaned=re.sub(r'^```(?:json)?\s*|\s*```$', '', cleaned)
    try:
        value=json.loads(cleaned)
        if isinstance(value,dict) and isinstance(value.get('spoken'),str):
            spoken=value['spoken'].strip()
            detail=value.get('details',spoken)
            details=detail.strip() if isinstance(detail,str) else json.dumps(detail,ensure_ascii=False,indent=2)
            if spoken: return redact(spoken),redact(details or spoken)
    except (ValueError,TypeError): pass
    # No invented summary or mid-sentence cut. Long unstructured output goes to Telegram in full.
    details=redact(raw.strip())
    spoken=details if len(details)<1600 else 'Das Ergebnis ist ausführlicher. Ich schicke dir die vollständigen Details in unseren Telegram-Chat. Was möchtest du daraus besprechen?'
    return spoken,details
