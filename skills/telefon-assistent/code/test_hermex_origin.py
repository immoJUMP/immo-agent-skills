"""Owner-phone origin tests: no calls, network access or Telegram delivery."""
import contextlib
import io
import json
import os
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch
import uuid

from backend import HermesRuntime, PhoneService
from phone_state import PhoneStore
import call_owner


class SessionDB:
    def __init__(self, home): self.home = home
    def get_session(self, sid):
        with sqlite3.connect(self.home / 'state.db') as con:
            con.row_factory = sqlite3.Row
            row = con.execute('SELECT * FROM sessions WHERE id=?', (sid,)).fetchone()
            return dict(row) if row else None
    def get_messages(self, sid, **kwargs):
        return [{'id': 42, 'role': 'user', 'content': 'Hermex-Kontext' if sid == 'abcdef123456' else 'Telegram-Kontext'}]


class HermexOriginTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.home = Path(self.tmp.name)
        self.sessions = self.home / 'webui/sessions'
        self.sessions.mkdir(parents=True)
        self.sid = 'abcdef123456'
        self.session_file = self.sessions / (self.sid + '.json')
        self.session_file.write_text(json.dumps({'session_id': self.sid, 'profile': 'default'}))
        with sqlite3.connect(self.home / 'state.db') as con:
            con.execute('CREATE TABLE sessions (id TEXT PRIMARY KEY, source TEXT, chat_id TEXT, chat_type TEXT, profile_name TEXT, ended_at REAL, started_at REAL)')
            con.executemany('INSERT INTO sessions VALUES (?,?,?,?,?,?,?)', [
                (self.sid, 'webui', None, None, 'default', None, 2),
                ('owner', 'telegram', '123', 'private', 'default', None, 1),
                ('foreign', 'telegram', '999', 'private', 'default', None, 3),
                ('group', 'telegram', '123', 'group', 'default', None, 4),
                ('desktop', 'api', None, None, 'default', None, 5),
            ])
        self.rt = HermesRuntime.__new__(HermesRuntime)
        self.rt.home = self.home
        self.rt.db = SessionDB(self.home)
        self.rt.owner = '123'
        self.rt.allow_hermex = True

    def test_known_default_hermex_session_is_accepted_with_explicit_opt_in(self):
        self.assertEqual(self.rt.resolve_session(self.sid), self.sid)

    def test_hermex_is_rejected_when_not_enabled(self):
        self.rt.allow_hermex = False
        with self.assertRaises(ValueError): self.rt.resolve_session(self.sid)

    def test_telegram_owner_rules_still_apply(self):
        self.assertEqual(self.rt.resolve_session('owner'), 'owner')
        self.assertEqual(self.rt.resolve_session(), 'owner')
        for sid in ('foreign', 'group', 'desktop', 'unknown', '../../state'):
            with self.subTest(sid=sid), self.assertRaises(ValueError): self.rt.resolve_session(sid)

    def test_session_must_exist_in_both_stores(self):
        self.session_file.unlink()
        with self.assertRaises(ValueError): self.rt.resolve_session(self.sid)

    def test_profile_identity_and_json_must_match(self):
        for data in ({'session_id': self.sid, 'profile': 'other'},
                     {'session_id': 'other', 'profile': 'default'},
                     {'session_id': self.sid}, [], None):
            self.session_file.write_text(json.dumps(data))
            with self.subTest(data=data), self.assertRaises(ValueError): self.rt.resolve_session(self.sid)
        self.session_file.write_text('{')
        with self.assertRaises(ValueError): self.rt.resolve_session(self.sid)

    def test_database_profile_must_match_even_if_json_claims_default(self):
        with sqlite3.connect(self.home / 'state.db') as con:
            con.execute('UPDATE sessions SET profile_name=? WHERE id=?', ('other', self.sid))
        with self.assertRaises(ValueError): self.rt.resolve_session(self.sid)

    def test_symlink_cannot_substitute_session_registration(self):
        target = self.home / 'outside.json'
        self.session_file.rename(target)
        self.session_file.symlink_to(target)
        with self.assertRaises(ValueError): self.rt.resolve_session(self.sid)

    def test_prepare_keeps_hermex_context_but_delivers_to_owner_telegram(self):
        store = PhoneStore(self.home / 'phone.sqlite3')
        service = PhoneService(store, self.rt)
        cid = str(uuid.uuid4())
        payload = service.prepare({'call_id': cid, 'reason': 'Übung', 'session_id': self.sid})
        self.assertEqual(payload['origin_session_id'], self.sid)
        self.assertEqual(payload['session_id'], 'owner')
        self.assertEqual(payload['context'][0]['text'], 'Hermex-Kontext')
        service.queue_notice(cid, 'Ergebnis', 'test')
        self.assertEqual(store.notifications()[0]['session_id'], 'owner')

    def test_no_telegram_delivery_context_means_no_call_prepared(self):
        with sqlite3.connect(self.home / 'state.db') as con:
            con.execute("DELETE FROM sessions WHERE id='owner'")
        store = PhoneStore(self.home / 'phone.sqlite3')
        cid = str(uuid.uuid4())
        with self.assertRaises(ValueError):
            PhoneService(store, self.rt).prepare({'call_id': cid, 'reason': 'Übung', 'session_id': self.sid})
        self.assertIsNone(store.call(cid))

    def test_client_check_only_resolves_current_session_and_never_calls(self):
        (self.home / 'telephony-client.json').write_text(json.dumps({'token': 'fake', 'url': 'http://unused'}))
        with patch.dict(os.environ, {'HERMES_HOME': str(self.home), 'HERMES_SESSION_ID': self.sid}), \
                patch('sys.argv', ['call_owner.py', '--check']), \
                patch.object(call_owner, 'request', return_value={'session_id': self.sid, 'request_id': '42'}) as request, \
                contextlib.redirect_stdout(io.StringIO()) as output:
            call_owner.main()
        self.assertEqual(request.call_count, 1)
        self.assertEqual(request.call_args.args[2:], ('/resolve', {'session_id': self.sid}))
        self.assertEqual(json.loads(output.getvalue())['session_id'], self.sid)


if __name__ == '__main__': unittest.main()
