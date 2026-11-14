import unittest
import importlib.util
import uuid


class VoiceTests(unittest.TestCase):
    def module(self, name):
        self.assertIsNotNone(importlib.util.find_spec(name), f'{name} is missing')
        return __import__(name)

    def test_only_configured_mobile_number_can_be_called(self):
        m = self.module('voice_protocol')
        self.assertEqual(m.validate_destination('015711111111', '015711111111'), '015711111111')
        for bad in ['112', '015711111112', '015711111111;Hangup()', '+4915711111111', '']:
            with self.assertRaises(ValueError):
                m.validate_destination(bad, '015711111111')

    def test_audiosocket_frame_roundtrip(self):
        m = self.module('voice_protocol')
        self.assertEqual(m.frame(0x10, b'\x01\x02'), b'\x10\x00\x02\x01\x02')
        self.assertEqual(m.frame(0, b''), b'\x00\x00\x00')

    def test_owner_dialplan_sets_identity_before_dialing(self):
        m = self.module('voice_protocol')
        self.assertTrue(hasattr(m, 'owner_dialplan'))
        plan = m.owner_dialplan('015711111111', '+492211234567', 'LEO AGENT')
        dial = plan.index('Dial(PJSIP/015711111111@fritz,30)')
        for setting in ['CALLERID(num)=+492211234567', 'CALLERID(name)=LEO AGENT',
                        'CALLERID(pres)=allowed_not_screened']:
            self.assertLess(plan.index(setting), dial)
        self.assertIn('[reject-incoming]\nexten => _.,1,Hangup()', plan)

    def test_owner_dialplan_rejects_injected_identity(self):
        m = self.module('voice_protocol')
        self.assertTrue(hasattr(m, 'owner_dialplan'))
        for number, name in [('+49123\n', 'LEO AGENT'), ('anonymous', 'LEO AGENT'),
                             ('+492211234567', '${SHELL(id)}'),
                             ('+492211234567', 'Leo\nsame => n,Hangup()')]:
            with self.assertRaises(ValueError):
                m.owner_dialplan('015711111111', number, name)
        with self.assertRaises(ValueError):
            m.owner_dialplan('112', '+492211234567', 'LEO AGENT')

    def test_separate_hermes_session_no_shell_interpolation(self):
        m = self.module('voice_protocol')
        call_id = str(uuid.uuid4())
        args = m.hermes_command(call_id)
        self.assertIn('leo-phone-' + call_id, args)
        self.assertIn('--query-file', args)
        self.assertIn('--create-if-missing', args)
        with self.assertRaises(ValueError):
            m.hermes_command('$(touch /tmp/owned)')

    def test_repeated_delegation_does_not_run_twice(self):
        m = self.module('voice_protocol')
        ledger = m.Delegations()
        self.assertTrue(ledger.claim('item_1'))
        self.assertFalse(ledger.claim('item_1'))
        self.assertTrue(ledger.claim('item_2'))

    def test_cooldown_blocks_repeated_calls(self):
        m = self.module('voice_protocol')
        gate = m.CallGate(cooldown=300)
        gate.reserve('one', 1000)
        with self.assertRaises(ValueError): gate.reserve('two', 1400)
        gate.release()
        with self.assertRaises(ValueError): gate.reserve('one', 1500)
        with self.assertRaises(ValueError): gate.reserve('two', 1100)
        gate.reserve('two', 1400)

    def test_audio_pacing_does_not_accumulate_processing_delay(self):
        m = self.module('voice_protocol')
        self.assertTrue(hasattr(m, 'next_audio_tick'))
        now = deadline = 0.0
        for _ in range(100):
            now += 0.003  # network/write processing per 20-ms frame
            deadline, delay = m.next_audio_tick(deadline, now)
            now += delay
        self.assertAlmostEqual(now, 2.0, places=6)


if __name__ == '__main__':
    unittest.main()
