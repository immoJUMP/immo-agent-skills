import unittest

import voice_protocol as m

# Stand von Leo vor der Anbieterwahl (bridge.py, 04.10.2026): FRITZ!Box über TCP.
LEO_FRITZBOX = '''[transport-tcp]
type=transport
protocol=tcp
bind=0.0.0.0:15062
local_net=10.42.0.0/16
local_net=127.0.0.0/8
external_media_address=192.0.2.10
external_signaling_address=192.0.2.10
external_signaling_port=15062

[fritz-auth]
type=auth
auth_type=userpass
username=leo
password=geheim

[fritz-registration]
type=registration
transport=transport-tcp
outbound_auth=fritz-auth
server_uri=sip:fritz.box;transport=tcp
client_uri=sip:leo@fritz.box
contact_user=leo
retry_interval=60
expiration=300

[fritz-aor]
type=aor
contact=sip:fritz.box:5060;transport=tcp
qualify_frequency=60

[fritz]
type=endpoint
transport=transport-tcp
context=reject-incoming
disallow=all
allow=alaw,ulaw
outbound_auth=fritz-auth
aors=fritz-aor
from_user=leo
from_domain=fritz.box
send_pai=yes
direct_media=no
rtp_symmetric=yes
force_rport=yes
rewrite_contact=yes

[fritz-identify]
type=identify
endpoint=fritz
match=fritz.box
'''


class SipAnbieterTests(unittest.TestCase):
    def test_fritzbox_unchanged_from_leo(self):
        self.assertEqual(m.pjsip_config('fritzbox', 'fritz.box', 'leo', 'geheim', '192.0.2.10'), LEO_FRITZBOX)

    def test_default_provider_is_fritzbox(self):
        self.assertEqual(m.pjsip_config('', 'fritz.box', 'leo', 'geheim', '192.0.2.10'), LEO_FRITZBOX)

    def test_sipgate_registers_over_udp_with_outbound_proxy(self):
        c = m.pjsip_config('sipgate', '', '1234567e0', 'geheim', '203.0.113.7')
        self.assertIn('[transport-udp]\ntype=transport\nprotocol=udp\n', c)
        self.assertIn('server_uri=sip:sipgate.de\n', c)
        self.assertIn('client_uri=sip:1234567e0@sipgate.de\n', c)
        self.assertIn('contact=sip:sipgate.de:5060\n', c)
        self.assertEqual(c.count('outbound_proxy=sip:sipgate.de\;lr\n'), 2)
        self.assertIn('external_media_address=203.0.113.7\n', c)
        self.assertIn('local_net=172.16.0.0/12\n', c)
        self.assertNotIn('transport=tcp', c)
        self.assertNotIn('10.42.0.0/16', c)
        self.assertIn('context=reject-incoming', c)

    def test_local_networks_can_be_overridden(self):
        c = m.pjsip_config('sipgate', '', '1234567e0', 'geheim', '203.0.113.7', m.lokale_netze('172.18.0.0/16, 127.0.0.0/8'))
        self.assertIn('local_net=172.18.0.0/16\nlocal_net=127.0.0.0/8\nexternal_media_address', c)
        self.assertNotIn('192.168.0.0/16', c)

    def test_rejects_unknown_provider_bad_networks_and_injection(self):
        with self.assertRaises(ValueError):
            m.pjsip_config('telekom', 'x', 'u', 'p', '203.0.113.7')
        for bad in ['10.0.0.0', '300.1.1.1/8', '10.0.0.0/33', '10.0.0.0/8\nfoo']:
            with self.assertRaises(ValueError):
                m.lokale_netze(bad)
        for user, password in [('u', 'p;x'), ('u\nallow=all', 'p'), ('', 'p')]:
            with self.assertRaises(ValueError):
                m.pjsip_config('sipgate', '', user, password, '203.0.113.7')

    def test_fritzbox_needs_a_host(self):
        with self.assertRaises(ValueError):
            m.pjsip_config('fritzbox', '', 'leo', 'geheim', '192.0.2.10')


if __name__ == '__main__':
    unittest.main()
