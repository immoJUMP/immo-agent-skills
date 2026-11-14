"""Authenticate with a 60-second SIP REGISTER, then unregister this contact.

Credentials come exclusively from SIP_HOST, SIP_USERNAME, SIP_PASSWORD.
Output contains status lines only; never print raw SIP packets/digest headers.
"""
import hashlib
import os
import re
import secrets
import socket


def digest_response(username, realm, password, method, uri, nonce,
                    qop=None, nc='00000001', cnonce=''):
    def md5(value):
        return hashlib.md5(value.encode()).hexdigest()
    ha1 = md5(f'{username}:{realm}:{password}')
    ha2 = md5(f'{method}:{uri}')
    return md5(f'{ha1}:{nonce}:{nc}:{cnonce}:{qop}:{ha2}' if qop
               else f'{ha1}:{nonce}:{ha2}')


def build_register(host, username, local_ip, port, call_id, tag, seq,
                   expires=0, authorization=None):
    for field in (host, username, local_ip, call_id, tag, authorization or ''):
        if '\r' in field or '\n' in field:
            raise ValueError('SIP header injection rejected')
    headers = [
        f'REGISTER sip:{host} SIP/2.0',
        f'Via: SIP/2.0/TCP {local_ip}:{port};branch=z9hG4bK{secrets.token_hex(8)};rport',
        'Max-Forwards: 70',
        f'From: <sip:{username}@{host}>;tag={tag}',
        f'To: <sip:{username}@{host}>',
        f'Call-ID: {call_id}', f'CSeq: {seq} REGISTER',
        f'Contact: <sip:{username}@{local_ip}:{port};transport=tcp>',
        f'Expires: {expires}', 'User-Agent: Leo-registration-probe',
    ]
    if authorization:
        headers.append(f'Authorization: {authorization}')
    return '\r\n'.join(headers + ['Content-Length: 0', '', ''])


def probe(host, username, password, sip_port=5060):
    with socket.create_connection((host, sip_port), timeout=8) as conn:
        local_ip, port = conn.getsockname()
        call_id, tag = secrets.token_hex(16), secrets.token_hex(8)
        stream = conn.makefile('rb')

        def exchange(seq, authorization=None, expires=60):
            conn.sendall(build_register(host, username, local_ip, port, call_id,
                                       tag, seq, expires=expires,
                                       authorization=authorization).encode())
            while True:
                status = stream.readline().decode().strip()
                headers = {}
                while True:
                    line = stream.readline().decode().strip()
                    if not line:
                        break
                    name, _, value = line.partition(':')
                    headers[name.lower()] = value.strip()
                stream.read(int(headers.get('content-length', '0')))
                if not status.startswith('SIP/2.0 1'):
                    print(status, flush=True)
                    return status, headers

        status, headers = exchange(1)
        if not status.startswith('SIP/2.0 401'):
            raise SystemExit('Expected authentication challenge; no credential verdict')
        challenge = headers['www-authenticate']
        fields = dict((k, quoted or bare) for k, quoted, bare in
                      re.findall(r'(\w+)=(?:"([^"]*)"|([^,\s]+))', challenge))
        if fields.get('algorithm', 'MD5').upper() != 'MD5':
            raise SystemExit('Unsupported digest algorithm')
        qop = 'auth' if 'auth' in fields.get('qop', '').split(',') else None
        if fields.get('qop') and not qop:
            raise SystemExit('Unsupported digest qop')
        cnonce = secrets.token_hex(12)
        uri = f'sip:{host}'
        def authorization(nc):
            digest = digest_response(username, fields['realm'], password, 'REGISTER',
                                     uri, fields['nonce'], qop=qop, cnonce=cnonce, nc=nc)
            auth = (f'Digest username="{username}", realm="{fields["realm"]}", '
                    f'nonce="{fields["nonce"]}", uri="{uri}", response="{digest}", algorithm=MD5')
            if qop:
                auth += f', qop=auth, nc={nc}, cnonce="{cnonce}"'
            if 'opaque' in fields:
                auth += f', opaque="{fields["opaque"]}"'
            return auth
        status, _ = exchange(2, authorization('00000001'))
        if not status.startswith('SIP/2.0 200'):
            raise SystemExit('SIP authentication not accepted')
        print('SIP_AUTH_OK; no call placed')
        status, _ = exchange(3, authorization('00000002'), expires=0)
        if not status.startswith('SIP/2.0 200'):
            raise SystemExit('Unregistration not confirmed; temporary contact may remain')
        print('SIP_UNREGISTER_OK; expires=0')


def main():
    probe(*(os.environ[k] for k in ('SIP_HOST', 'SIP_USERNAME', 'SIP_PASSWORD')))


if __name__ == '__main__':
    main()
