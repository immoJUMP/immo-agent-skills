"""Protocol guardrails for the registration-only FRITZ!Box diagnostic."""
import unittest
import socket
import threading
import sip_probe
from sip_probe import digest_response, build_register


class DigestTests(unittest.TestCase):
    def test_rfc2617_known_digest(self):
        self.assertEqual(digest_response(
            'Mufasa', 'testrealm@host.com', 'Circle Of Life', 'GET', '/dir/index.html',
            'dcd98b7102dd2f0e8b11d0f600bfb0c093', qop='auth', nc='00000001',
            cnonce='0a4f113b'), '6629fae49393a05397450978507c4ef1')

    def test_register_only_and_expiry_zero(self):
        request = build_register('192.0.2.1', 'example', '192.0.2.2', 50000,
                                 'test-call', 'test-tag', 1, expires=0)
        self.assertTrue(request.startswith('REGISTER sip:192.0.2.1 SIP/2.0\r\n'))
        self.assertIn('\r\nExpires: 0\r\n', request)
        self.assertIn('transport=tcp', request)
        self.assertNotIn('INVITE', request)
        self.assertTrue(request.endswith('\r\n\r\n'))

    def test_header_injection_rejected(self):
        with self.assertRaises(ValueError):
            build_register('192.0.2.1', 'bad\r\nInjected: yes', '192.0.2.2',
                           50000, 'test', 'tag', 1)

    def test_digest_registration_is_followed_by_contact_cleanup(self):
        requests = []
        with socket.socket() as server:
            server.bind(('127.0.0.1', 0))
            server.listen(1)
            server.settimeout(3)
            def respond():
                with server.accept()[0] as conn:
                    conn.settimeout(3)
                    stream = conn.makefile('rb')
                    for status in [401, 200, 200]:
                        lines = []
                        while True:
                            line = stream.readline()
                            if not line or line == b'\r\n':
                                break
                            lines.append(line.decode())
                        requests.append(''.join(lines))
                        headers = ('WWW-Authenticate: Digest realm="test", nonce="nonce", qop="auth"\r\n'
                                   if status == 401 else '')
                        conn.sendall(f'SIP/2.0 {status} Test\r\n{headers}Content-Length: 0\r\n\r\n'.encode())
            thread = threading.Thread(target=respond)
            thread.start()
            sip_probe.probe('127.0.0.1', 'testuser', 'testpassword', server.getsockname()[1])
            thread.join(timeout=4)
        self.assertEqual(len(requests), 3)
        self.assertIn('Expires: 60\r\n', requests[0])
        self.assertIn('Authorization: Digest', requests[1])
        self.assertIn('nc=00000001', requests[1])
        self.assertIn('Expires: 0\r\n', requests[2])
        self.assertIn('nc=00000002', requests[2])
        self.assertNotIn('testpassword', ''.join(requests))


if __name__ == '__main__':
    unittest.main()
