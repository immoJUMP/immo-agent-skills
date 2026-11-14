import importlib
import json
from datetime import datetime, timezone
from pathlib import Path
import tempfile
import unittest
import uuid


def module(name):
    assert importlib.util.find_spec(name) is not None, f"Required workflow module missing: {name}"
    return importlib.import_module(name)


class PolicyTests(unittest.TestCase):
    def decide(self, **kw):
        m = module('phone_logic')
        now = datetime(2026, 9, 22, 21, tzinfo=timezone.utc)
        return m.call_policy(kw.pop('kind', 'proactive'), kw.pop('now', now),
                             kw.pop('daily_calls', 0), kw.pop('proactive_calls', 0), **kw)

    def test_quiet_hours_are_enforced_except_explicit_request_and_emergency(self):
        self.assertEqual(self.decide(), 'quiet_hours')
        self.assertEqual(self.decide(kind='requested'), 'call')
        self.assertEqual(self.decide(kind='emergency', evidence='Verified service outage'), 'call')
        with self.assertRaises(ValueError): self.decide(kind='emergency')

    def test_info_and_decision_are_messages_not_calls(self):
        self.assertEqual(self.decide(kind='info'), 'message')
        self.assertEqual(self.decide(kind='decision'), 'message')

    def test_daily_caps_apply_at_server_even_for_explicit_requests(self):
        self.assertEqual(self.decide(kind='requested', daily_calls=10), 'daily_limit')
        self.assertEqual(self.decide(now=datetime(2026,9,22,10,tzinfo=timezone.utc),
                                     proactive_calls=3, evidence='Deadline today'), 'proactive_limit')

    def test_preparation_deadlines_use_aware_times(self):
        m=module('phone_logic')
        self.assertEqual(m.schedule_time('2026-09-23T14:00:00+02:00', preparation=True),
                         datetime(2026,9,23,11,45,tzinfo=timezone.utc).timestamp())
        with self.assertRaises(ValueError): m.schedule_time('2026-09-23T14:00:00')


class ConversationTests(unittest.TestCase):
    def test_transcript_fragments_are_joined_without_invented_word_boundaries(self):
        m=module('phone_logic'); t=m.Transcript()
        t.append('user','Ruf mich we',0,400)
        t.append('user','gen Wolfgang an.',400,1100)
        self.assertEqual(t.last_user(), 'Ruf mich wegen Wolfgang an.')
        t.append('assistant','Gerne.',1200,1800)
        t.append('user','Danke, das war’s.',2300,3000)
        self.assertEqual(len(t.turns),3)
        self.assertEqual(m.voice_control(t.last_user()),'hangup')

    def test_full_duplex_interleaving_preserves_complete_user_sentence(self):
        m=module('phone_logic'); t=m.Transcript()
        t.append('user','Hallo Leo, ja, ich kann dich gut',8600,10800)
        t.append('assistant','Alles klar',10800,11000)
        t.append('user',' hören',11000,11200)
        t.append('assistant',', danke.',11000,12400)
        self.assertEqual(t.last_user(),'Hallo Leo, ja, ich kann dich gut hören')
        self.assertEqual(m.presence(t.last_user()),'human')
        t.append('user','Danke, das war es.',20000,21700)
        self.assertEqual(m.voice_control(t.last_user()),'hangup')

    def test_control_commands_do_not_confuse_silence_cancellation_and_negation(self):
        m=module('phone_logic')
        for s in ['Stopp','Sei kurz still']: self.assertEqual(m.voice_control(s),'stop_speaking')
        for s in ['Brich den Auftrag ab','Abbrechen']: self.assertEqual(m.voice_control(s),'cancel_tasks')
        for s in ['Bitte nicht auflegen','Er hat gesagt: danke das wars','Kannst du das Angebot abbrechen?']:
            self.assertIsNone(m.voice_control(s))

    def test_natural_end_of_call_requests_are_controls(self):
        m=module('phone_logic')
        for text in ['Okay, danke. Leg jetzt auf', 'Ich möchte das Gespräch beenden.', 'Ich will das Gespräch beenden.',
                     'Ich würde das Gespräch jetzt gerne beenden.', 'Leg bitte auf.',
                     'Leo, kannst du jetzt bitte auflegen?', 'Können wir das Gespräch jetzt beenden?',
                     'Okay, ich möchte jetzt unser Gespräch beenden. Danke!',
                     'Vielen Dank, das war es für heute.', 'Lass uns das Telefonat beenden.',
                     'Ich muss los. Bitte leg jetzt auf.', 'Bitte beende jetzt den Anruf.']:
            with self.subTest(text=text): self.assertEqual(m.voice_control(text),'hangup')

    def test_end_of_call_detection_rejects_negation_reports_and_future_conditions(self):
        m=module('phone_logic')
        for text in ['Ich möchte das Gespräch nicht beenden.', 'Bitte noch nicht auflegen.',
                     'Kannst du bitte nicht auflegen?', 'Er hat gesagt: Leg bitte auf.',
                     'Was bedeutet ich möchte das Gespräch beenden?',
                     'Wenn ich das sage, dann leg bitte auf.', 'Ich möchte das Gespräch morgen beenden.',
                     'Ich möchte den Auftrag beenden.', 'Kannst du das Telefonat zusammenfassen?',
                     'Leg bitte auf keinen Fall auf.', 'Zitiere: "Ich möchte das Gespräch beenden."']:
            with self.subTest(text=text): self.assertIsNone(m.voice_control(text))

    def test_voicemail_never_counts_as_human_confirmation(self):
        m=module('phone_logic')
        self.assertEqual(m.presence('Bitte sprechen Sie nach dem Signalton'), 'voicemail')
        self.assertEqual(m.presence('Ja, hier ist die Mailbox von Chris'), 'voicemail')
        self.assertEqual(m.presence('Ja, ich höre dich, hier ist Chris'), 'human')
        self.assertIsNone(m.presence('Unverständliches Rauschen'))

    def test_spoken_chunks_preserve_complete_result(self):
        m=module('phone_logic')
        text=('Das Angebot ist vorbereitet. Bitte prüfe noch den Termin. '*50).strip()
        parts=m.speech_chunks(text,limit=800)
        self.assertTrue(all(len(p)<=800 for p in parts))
        self.assertEqual(' '.join(parts),text)

    def test_readable_result_uses_explicit_spoken_summary(self):
        m=module('phone_logic')
        raw=json.dumps({'spoken':'Das Angebot liegt als Entwurf bereit.', 'details':'Alle Details.\n'*100})
        spoken,details=m.result_parts(raw)
        self.assertEqual(spoken,'Das Angebot liegt als Entwurf bereit.')
        self.assertIn('Alle Details.',details)

    def test_model_structured_details_do_not_leak_json_into_spoken_answer(self):
        m=module('phone_logic')
        spoken,details=m.result_parts(json.dumps({'spoken':'Der Entwurf ist bereit.','details':{'status':'verified','path':'/tmp/draft'}}))
        self.assertEqual(spoken,'Der Entwurf ist bereit.')
        self.assertIn('/tmp/draft',details)

    def test_transcript_redacts_credentials_before_cross_channel_delivery(self):
        m=module('phone_logic')
        self.assertNotIn('sk-proj-abcdef12345678901234567890',m.redact('Key sk-proj-abcdef12345678901234567890'))

    def test_unicode_append_chunks_fit_token_upper_bound(self):
        m=module('phone_logic'); text='Äpfel 🦁 東京 '*100
        chunks=m.speech_chunks(text,limit=400,byte_limit=True)
        self.assertTrue(all(len(c.encode())<=400 for c in chunks))
        self.assertEqual(' '.join(chunks),' '.join(text.split()))

    def test_calendar_skips_all_day_declined_cancelled_free_and_weekend(self):
        m=module('phone_logic')
        base={'id':'one','summary':'Kundentermin','start':{'dateTime':'2026-09-23T10:00:00+02:00'},'status':'confirmed','attendees':[{'self':True},{'email':'other@example.test'}]}
        now=datetime(2026,9,22,tzinfo=timezone.utc).timestamp()
        self.assertEqual(len(m.calendar_schedules([base],now)),1)
        for extra in [{'start':{'date':'2026-09-23'}},{'status':'cancelled'},{'transparency':'transparent'},
                      {'attendees':[{'self':True,'responseStatus':'declined'}]},
                      {'start':{'dateTime':'2026-09-26T10:00:00+02:00'}},{'eventType':'focusTime'},{'attendees':[]},{'attendees':[{'self':True}]}]:
            self.assertEqual(m.calendar_schedules([{**base,**extra}],now),[])
        self.assertEqual(len(m.calendar_schedules([{**base,'attendees':[],'summary':'[Leo] Besichtigung'}],now)),1)


class StateTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.path=Path(self.tmp.name)/'phone.sqlite3'
        self.store=module('phone_state').PhoneStore(self.path)
        self.cid=str(uuid.uuid4())
        self.store.prepare_call(self.cid,{'reason':'Angebot Wolfgang','session_id':'owner-session','mode':'conversation'})
    def tearDown(self): self.tmp.cleanup()

    def test_durable_job_deduplication_and_restart_recovery(self):
        a=self.store.enqueue(self.cid,'delegation-1','Bitte Entwurf erstellen')
        b=self.store.enqueue(self.cid,'delegation-1','Bitte Entwurf erstellen')
        self.assertEqual(a['id'],b['id'])
        self.store.claim()
        restarted=module('phone_state').PhoneStore(self.path)
        restarted.recover()
        self.assertEqual(restarted.job(a['id'])['state'],'interrupted')
        self.assertIsNone(restarted.claim()) # Never blindly rerun possibly completed external actions.

    def test_hangup_keeps_jobs_but_rejects_late_new_delegations(self):
        a=self.store.enqueue(self.cid,'delegation-1','Prepare draft')
        self.store.finish_call(self.cid,'ended',[{'role':'user','text':'Bitte Angebot vorbereiten'}])
        self.assertEqual(self.store.job(a['id'])['state'],'queued')
        with self.assertRaises(ValueError): self.store.enqueue(self.cid,'delegation-2','New work after hangup')

    def test_cancelled_running_job_cannot_publish_late_success(self):
        a=self.store.enqueue(self.cid,'one','Task')
        self.store.claim()
        self.store.cancel_call_jobs(self.cid)
        self.assertFalse(self.store.complete(a['id'],'Too late'))
        self.assertEqual(self.store.job(a['id'])['state'],'cancel_requested')

    def test_outbox_deduplicates_and_marks_uncertain_sends(self):
        self.store.notify('summary:'+self.cid,'session','summary')
        self.store.notify('summary:'+self.cid,'session','summary')
        n=self.store.claim_notification()
        self.assertIsNotNone(n)
        self.assertIsNone(self.store.claim_notification())
        self.store.recover()
        self.assertEqual(self.store.notifications()[0]['state'],'unknown')

    def test_summary_is_queued_only_once_after_finish(self):
        self.store.finish_call(self.cid,'ended',[])
        self.store.finish_call(self.cid,'ended',[])
        summaries=[j for j in self.store.jobs(self.cid) if j['kind']=='summary']
        self.assertEqual(len(summaries),1)

    def test_due_schedule_is_claimed_once_and_expired_calls_are_skipped(self):
        self.store.schedule('event-1',1000,{'reason':'Prep'})
        self.assertEqual(self.store.claim_schedule(1001)['event_id'],'event-1')
        self.assertIsNone(self.store.claim_schedule(1001))
        self.store.schedule('event-2',1000,{'reason':'Old'})
        self.assertIsNone(self.store.claim_schedule(2000))


if __name__=='__main__': unittest.main()
