"""Durable call, task and delivery state. Never blindly retry external effects."""
from contextlib import contextmanager
import json
from pathlib import Path
import sqlite3
import time
import uuid


class PhoneStore:
    def __init__(self,path):
        self.path=Path(path); self.path.parent.mkdir(parents=True,exist_ok=True)
        with self.tx() as db:
            db.executescript('''
            CREATE TABLE IF NOT EXISTS calls(id TEXT PRIMARY KEY,payload TEXT NOT NULL,state TEXT NOT NULL DEFAULT 'prepared',transcript TEXT NOT NULL DEFAULT '[]',created REAL NOT NULL,ended REAL);
            CREATE TABLE IF NOT EXISTS jobs(id TEXT PRIMARY KEY,call_id TEXT NOT NULL,event_key TEXT NOT NULL,kind TEXT NOT NULL,prompt TEXT NOT NULL,state TEXT NOT NULL,result TEXT,created REAL NOT NULL,updated REAL NOT NULL,UNIQUE(call_id,event_key));
            CREATE TABLE IF NOT EXISTS outbox(id INTEGER PRIMARY KEY,event_key TEXT UNIQUE,session_id TEXT NOT NULL,text TEXT NOT NULL,state TEXT NOT NULL,created REAL NOT NULL,message_id TEXT,error TEXT);
            CREATE TABLE IF NOT EXISTS schedules(event_id TEXT PRIMARY KEY,due REAL NOT NULL,payload TEXT NOT NULL,state TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS settings(key TEXT PRIMARY KEY,value TEXT NOT NULL);
            ''')
        self.path.chmod(0o600)
    @contextmanager
    def tx(self):
        db=sqlite3.connect(self.path,timeout=15); db.row_factory=sqlite3.Row
        try:
            db.execute('PRAGMA journal_mode=WAL'); db.execute('BEGIN IMMEDIATE')
            yield db; db.commit()
        except BaseException: db.rollback(); raise
        finally: db.close()
    def recover(self):
        with self.tx() as db:
            db.execute("UPDATE jobs SET state='interrupted',updated=? WHERE state IN ('running','cancel_requested')",(time.time(),))
            db.execute("UPDATE outbox SET state='unknown',error='Process restarted during delivery; verify before retry' WHERE state='sending'")
            db.execute("UPDATE schedules SET state='unknown' WHERE state='dispatching'")
    @staticmethod
    def decode(row):
        if row is None: return None
        d=dict(row)
        for k in ('payload','transcript'):
            if k in d: d[k]=json.loads(d[k])
        return d
    def prepare_call(self,cid,payload):
        with self.tx() as db:
            db.execute("INSERT OR IGNORE INTO calls(id,payload,created) VALUES(?,?,?)",(cid,json.dumps(payload),time.time()))
            row=self.decode(db.execute('SELECT * FROM calls WHERE id=?',(cid,)).fetchone())
            if row['payload']!=payload: raise ValueError('Call id reused with different request')
            return row
    def call(self,cid):
        with self.tx() as db: return self.decode(db.execute('SELECT * FROM calls WHERE id=?',(cid,)).fetchone())
    def calls(self):
        with self.tx() as db: return [self.decode(r) for r in db.execute('SELECT * FROM calls ORDER BY created DESC LIMIT 100')]
    def update_call(self,cid,state):
        with self.tx() as db: db.execute('UPDATE calls SET state=? WHERE id=? AND ended IS NULL',(state,cid))
    def enqueue(self,cid,event_key,prompt,kind='turn'):
        with self.tx() as db:
            previous=db.execute('SELECT * FROM jobs WHERE call_id=? AND event_key=?',(cid,event_key)).fetchone()
            if previous: return dict(previous)
            call=db.execute('SELECT * FROM calls WHERE id=?',(cid,)).fetchone()
            if not call: raise ValueError('Unknown call')
            if call['ended'] is not None and kind!='summary': raise ValueError('Call already ended')
            now=time.time(); jid=str(uuid.uuid4())
            db.execute('INSERT INTO jobs VALUES(?,?,?,?,?,?,?,?,?)',(jid,cid,event_key,kind,prompt,'queued',None,now,now))
            return dict(db.execute('SELECT * FROM jobs WHERE id=?',(jid,)).fetchone())
    def finish_call(self,cid,state,transcript):
        with self.tx() as db:
            db.execute('UPDATE calls SET state=?,transcript=?,ended=COALESCE(ended,?) WHERE id=?',(state,json.dumps(transcript),time.time(),cid))
        return self.enqueue(cid,'summary','',kind='summary')
    def claim(self):
        with self.tx() as db:
            row=db.execute("SELECT * FROM jobs WHERE state='queued' ORDER BY created,id LIMIT 1").fetchone()
            if row is None: return None
            db.execute("UPDATE jobs SET state='running',updated=? WHERE id=?",(time.time(),row['id']))
            return dict(db.execute('SELECT * FROM jobs WHERE id=?',(row['id'],)).fetchone())
    def job(self,jid):
        with self.tx() as db:
            row=db.execute('SELECT * FROM jobs WHERE id=?',(jid,)).fetchone()
            return dict(row) if row else None
    def jobs(self,cid=None):
        with self.tx() as db:
            rows=db.execute('SELECT * FROM jobs '+('WHERE call_id=? ' if cid else '')+'ORDER BY created DESC LIMIT 100', (cid,) if cid else ())
            return [dict(r) for r in rows]
    def complete(self,jid,result,state='completed'):
        with self.tx() as db:
            return bool(db.execute("UPDATE jobs SET state=?,result=?,updated=? WHERE id=? AND state='running'",(state,result,time.time(),jid)).rowcount)
    def cancel_call_jobs(self,cid):
        with self.tx() as db:
            db.execute("UPDATE jobs SET state=CASE state WHEN 'queued' THEN 'cancelled' ELSE 'cancel_requested' END,updated=? WHERE call_id=? AND kind='turn' AND state IN ('queued','running')",(time.time(),cid))
            return [dict(r) for r in db.execute("SELECT * FROM jobs WHERE call_id=? AND state IN ('cancelled','cancel_requested')",(cid,))]
    def acknowledge_cancel(self,jid):
        with self.tx() as db: db.execute("UPDATE jobs SET state='cancelled',updated=? WHERE id=? AND state='cancel_requested'",(time.time(),jid))
    def notify(self,event_key,session_id,text):
        with self.tx() as db: db.execute("INSERT OR IGNORE INTO outbox(event_key,session_id,text,state,created) VALUES(?,?,?,'queued',?)",(event_key,session_id,text,time.time()))
    def claim_notification(self):
        with self.tx() as db:
            r=db.execute("SELECT * FROM outbox WHERE state='queued' ORDER BY id LIMIT 1").fetchone()
            if not r: return None
            db.execute("UPDATE outbox SET state='sending' WHERE id=?",(r['id'],)); return dict(r)
    def finish_notification(self,nid,state,message_id=None,error=None):
        with self.tx() as db: db.execute('UPDATE outbox SET state=?,message_id=?,error=? WHERE id=?',(state,message_id,error,nid))
    def notifications(self):
        with self.tx() as db: return [dict(r) for r in db.execute('SELECT * FROM outbox ORDER BY id DESC LIMIT 100')]
    def schedule(self,event_id,due,payload):
        with self.tx() as db:
            db.execute("INSERT OR IGNORE INTO schedules VALUES(?,?,?,'scheduled')",(event_id,due,json.dumps(payload)))
            row=self.decode(db.execute('SELECT * FROM schedules WHERE event_id=?',(event_id,)).fetchone())
            if row['due']!=due or row['payload']!=payload: raise ValueError('Schedule id reused with different request')
            return row
    def reconcile_schedules(self,prefix,items):
        """Replace only pending managed reminders; never repeat already dispatched effects."""
        desired={key:(due,payload) for key,due,payload in items}
        with self.tx() as db:
            for row in db.execute("SELECT event_id FROM schedules WHERE state='scheduled'"):
                key=row['event_id']
                if key.startswith(prefix) and key not in desired:
                    db.execute("UPDATE schedules SET state='cancelled' WHERE event_id=?",(key,))
            for key,(due,payload) in desired.items():
                if not key.startswith(prefix): raise ValueError('Invalid managed schedule prefix')
                db.execute("INSERT INTO schedules VALUES(?,?,?,'scheduled') ON CONFLICT(event_id) DO UPDATE SET due=excluded.due,payload=excluded.payload,state='scheduled' WHERE schedules.state IN ('scheduled','cancelled')",(key,due,json.dumps(payload)))

    def schedules(self):
        with self.tx() as db: return [self.decode(r) for r in db.execute('SELECT * FROM schedules ORDER BY due DESC LIMIT 100')]
    def claim_schedule(self,now):
        with self.tx() as db:
            db.execute("UPDATE schedules SET state='expired' WHERE state='scheduled' AND due<?",(now-300,))
            row=db.execute("SELECT * FROM schedules WHERE state='scheduled' AND due<=? ORDER BY due LIMIT 1",(now,)).fetchone()
            if not row: return None
            db.execute("UPDATE schedules SET state='dispatching' WHERE event_id=?",(row['event_id'],)); return self.decode(row)
    def finish_schedule(self,event_id,state):
        with self.tx() as db: db.execute('UPDATE schedules SET state=? WHERE event_id=?',(state,event_id))
    def cancel_schedule(self,event_id):
        with self.tx() as db: return bool(db.execute("UPDATE schedules SET state='cancelled' WHERE event_id=? AND state='scheduled'",(event_id,)).rowcount)
    def setting(self,key,default=None):
        with self.tx() as db:
            r=db.execute('SELECT value FROM settings WHERE key=?',(key,)).fetchone()
            return json.loads(r['value']) if r else default
    def set_setting(self,key,value):
        with self.tx() as db: db.execute('INSERT INTO settings VALUES(?,?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',(key,json.dumps(value)))
