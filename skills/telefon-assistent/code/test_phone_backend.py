import json
from datetime import datetime
from unittest.mock import patch
import sys
from pathlib import Path
import tempfile
import threading
import time
import unittest
import uuid
import urllib.request
import urllib.error
from http.server import ThreadingHTTPServer
from backend import PhoneService, handler
from phone_state import PhoneStore


class Runtime:
    def __init__(self): self.sent=[]; self.recorded=[]; self.busy=False; self.fail_record=False
    def resolve_session(self,sid=None):
        if sid not in (None,'owner'): raise ValueError('Not owner chat')
        return 'owner'
    def context(self,sid): return [{'role':'user','text':'Wolfgang fragt nach dem Angebot.'}]
    def notification_session(self,sid): return self.resolve_session(sid)
    def session_busy(self,sid): return self.busy
    def send(self,text): self.sent.append(text); return str(len(self.sent))
    def record(self,sid,text,mid):
        if self.fail_record: raise RuntimeError('Concurrent turn')
        self.recorded.append((sid,text,mid))


class BackendTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.store=PhoneStore(Path(self.tmp.name)/'state.db')
        self.rt=Runtime(); self.prompts=[]
        def runner(job,prompt,readonly):
            self.prompts.append((prompt,readonly))
            return json.dumps({'spoken':'Der Entwurf ist bereit.','details':'Angebot als Entwurf vorbereitet; noch nicht versendet.'})
        self.service=PhoneService(self.store,self.rt,runner)
        self.cid=str(uuid.uuid4())
        self.service.prepare({'call_id':self.cid,'reason':'Angebot Wolfgang','session_id':'owner','mode':'sales_training'})
    def tearDown(self): self.tmp.cleanup()

    def test_original_chat_context_reaches_worker_and_summary_returns_to_same_chat(self):
        self.service.enqueue({'call_id':self.cid,'delegation_id':'one','conversation':'Chris: Bereite einen Entwurf vor.'})
        self.service.process(self.store.claim())
        self.assertIn('Wolfgang fragt nach dem Angebot.',self.prompts[0][0])
        self.store.finish_call(self.cid,'ended',[{'role':'user','text':'Entwurf vorbereiten'}])
        self.service.process(self.store.claim())
        self.service.deliver_once(); self.service.deliver_once()
        self.assertEqual(len(self.rt.sent),2)
        self.assertIn('Angebot als Entwurf vorbereitet; noch nicht versendet.',self.rt.sent[0])
        self.assertEqual(self.rt.recorded[0][0],'owner')
        self.assertTrue(self.prompts[-1][1]) # Summary uses read-only model route.

    def test_hangup_does_not_cancel_an_accepted_task(self):
        self.service.enqueue({'call_id':self.cid,'delegation_id':'one','conversation':'Bitte einen Entwurf vorbereiten'})
        self.store.finish_call(self.cid,'ended',[{'role':'user','text':'Bitte einen Entwurf vorbereiten'}])
        job=self.store.claim(); self.assertEqual(job['kind'],'turn')
        self.service.process(job)
        self.assertEqual(self.store.job(job['id'])['state'],'completed')

    def test_record_retry_never_sends_a_second_telegram_message(self):
        self.store.notify('once','owner','Summary'); self.rt.fail_record=True
        self.service.deliver_once()
        self.assertEqual(self.store.notifications()[0]['state'],'sent_unrecorded')
        self.rt.fail_record=False; self.service.deliver_once()
        self.assertEqual(len(self.rt.sent),1)
        self.assertEqual(len(self.rt.recorded),1)
        self.assertEqual(self.store.notifications()[0]['state'],'sent')

    def test_wrong_chat_context_is_rejected_before_creating_call(self):
        other=str(uuid.uuid4())
        with self.assertRaises(ValueError): self.service.prepare({'call_id':other,'reason':'Test','session_id':'other-person'})
        self.assertIsNone(self.store.call(other))

    def test_busy_chat_defers_delivery_without_losing_notice(self):
        self.store.notify('one','owner','Text'); self.rt.busy=True
        self.service.deliver_once(); self.assertEqual(self.rt.sent,[])
        self.rt.busy=False; self.service.deliver_once(); self.assertEqual(len(self.rt.sent),1)

    def test_voicemail_summary_contains_no_invented_conversation(self):
        self.store.finish_call(self.cid,'voicemail',[])
        self.service.process(self.store.claim()); self.service.deliver_once()
        self.assertIn('nicht sicher erreicht',self.rt.sent[0])
        self.assertEqual(self.prompts,[])

    def test_disabling_routines_cancels_pending_calls(self):
        self.service.configure_routines({'enabled':True,'daily_review_time':'18:00','calendar_preparation':True})
        self.store.reconcile_schedules('daily-review:',[('daily-review:2026-09-23',1000,{'reason':'Review'})])
        self.store.reconcile_schedules('calendar:',[('calendar:one',1100,{'reason':'Prep'})])
        self.service.configure_routines({'enabled':False,'calendar_preparation':False})
        self.assertTrue(all(x['state']=='cancelled' for x in self.store.schedules()))

    def test_rescheduled_calendar_event_replaces_pending_call_and_cancellation_removes_it(self):
        first=[('calendar:one',1000,{'reason':'Prep'})]
        self.store.reconcile_schedules('calendar:',first)
        self.store.reconcile_schedules('calendar:',[('calendar:one',2000,{'reason':'New time'})])
        self.assertIsNone(self.store.claim_schedule(1000))
        self.assertEqual(self.store.schedules()[0]['due'],2000)
        self.store.reconcile_schedules('calendar:',[])
        self.assertIsNone(self.store.claim_schedule(2000))

    def test_real_running_subprocess_is_terminated_after_cancel(self):
        job=self.service.enqueue({'call_id':self.cid,'delegation_id':'sleep','conversation':'test'})
        job=self.store.claim(); errors=[]
        def run():
            try: self.service.run_hermes(job,'test')
            except RuntimeError as e: errors.append(str(e))
        with patch('backend.hermes_command',return_value=[sys.executable,'-c','import sys,time;sys.stdin.read();time.sleep(30)']), patch('backend.WORKDIR',self.tmp.name):
            t=threading.Thread(target=run); t.start(); time.sleep(.4)
            self.store.cancel_call_jobs(self.cid); t.join(3)
            self.assertFalse(t.is_alive())
        self.assertEqual(self.store.job(job['id'])['state'],'cancelled')
        self.assertEqual(errors,['cancelled'])

    def test_http_auth_and_background_job_contract(self):
        server=ThreadingHTTPServer(('127.0.0.1',0),handler(self.service,'test-token'))
        thread=threading.Thread(target=server.serve_forever,daemon=True); thread.start()
        base='http://127.0.0.1:'+str(server.server_port)
        try:
            with self.assertRaises(urllib.error.HTTPError) as cm: urllib.request.urlopen(base+'/status')
            self.assertEqual(cm.exception.code,401); cm.exception.close()
            req=urllib.request.Request(base+'/jobs',data=json.dumps({'call_id':self.cid,'delegation_id':'new','conversation':'Erstelle einen Entwurf'}).encode(),headers={'Authorization':'Bearer test-token'})
            with urllib.request.urlopen(req) as response:
                self.assertEqual(response.status,202); job=json.load(response)
            self.assertEqual(job['state'],'queued')
            self.service.process(self.store.claim())
            req=urllib.request.Request(base+'/jobs/'+job['id'],headers={'Authorization':'Bearer test-token'})
            with urllib.request.urlopen(req) as response: result=json.load(response)
            self.assertEqual(result['state'],'completed')
            self.assertEqual(json.loads(result['result'])['spoken'],'Der Entwurf ist bereit.')
        finally: server.shutdown(); server.server_close(); thread.join()


if __name__=='__main__': unittest.main()
