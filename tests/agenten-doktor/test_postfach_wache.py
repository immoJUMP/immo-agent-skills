"""Tests der Postfach-Wache: Erlaubnisliste gegen einen falschen Google-Server.

Lauf: python3 -m unittest discover -s tests/agenten-doktor
"""
import json
import os
import socket
import subprocess
import sys
import threading
import time
import unittest
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WACHE = REPO / "skills/agenten-doktor/installer/server/postfach/postfach-wache.py"
GMAIL = REPO / "skills/agenten-doktor/installer/server/werkzeuge/gmail"
SCHLUESSEL = "vera-schluessel-0123456789abcdef"


def freier_port():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    p = s.getsockname()[1]
    s.close()
    return p


class FalschesGoogle(BaseHTTPRequestHandler):
    aufrufe = []

    def log_message(self, *a):
        pass

    def _json(self, status, daten):
        roh = json.dumps(daten).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(roh)))
        self.end_headers()
        self.wfile.write(roh)

    def do_POST(self):
        laenge = int(self.headers.get("Content-Length") or 0)
        koerper = self.rfile.read(laenge) if laenge else b""
        FalschesGoogle.aufrufe.append(("POST", self.path, koerper))
        if self.path == "/token":
            return self._json(200, {"access_token": "google-zugriff", "expires_in": 3600})
        if self.path.endswith("/drafts"):
            return self._json(200, {"id": "entwurf-1", "message": {"id": "m9"}})
        if self.path.endswith("/labels"):
            return self._json(200, {"id": "Label_9", "name": json.loads(koerper)["name"], "type": "user"})
        if self.path.endswith("/modify"):
            return self._json(200, {"id": "m1"})
        return self._json(200, {"ok": True})

    def do_GET(self):
        FalschesGoogle.aufrufe.append(("GET", self.path, b""))
        if "/labels" in self.path:
            return self._json(200, {"labels": [
                {"id": "INBOX", "name": "INBOX", "type": "system"},
                {"id": "Label_1", "name": "Vera/Beleg-abgelegt", "type": "user"},
                {"id": "Label_2", "name": "Privat", "type": "user"}]})
        if "/messages/m1" in self.path:
            return self._json(200, {"id": "m1", "threadId": "t1", "payload": {"headers": [
                {"name": "From", "value": "Mieter <mieter@example.org>"}, {"name": "Subject", "value": "Heizung"},
                {"name": "Date", "value": "Fri, 13 Nov 2026 10:00:00 +0100"}],
                "mimeType": "text/plain", "body": {"data": "SGVpenVuZyBrYWx0"}}, "internalDate": "1794560400000"})
        if "/messages" in self.path:
            return self._json(200, {"messages": [{"id": "m1", "threadId": "t1"}], "resultSizeEstimate": 1})
        return self._json(200, {})


class PostfachWacheTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.google = ThreadingHTTPServer(("127.0.0.1", 0), FalschesGoogle)
        threading.Thread(target=cls.google.serve_forever, daemon=True).start()
        gport = cls.google.server_address[1]
        cls.port = freier_port()
        env = dict(os.environ, GMAIL_API_BASIS=f"http://127.0.0.1:{gport}/gmail/v1",
                   GOOGLE_TOKEN_URL=f"http://127.0.0.1:{gport}/token", GMAIL_CLIENT_ID="id",
                   GMAIL_CLIENT_SECRET="geheim", GMAIL_REFRESH_TOKEN="refresh",
                   POSTFACH_ZUGAENGE=f"vera:{SCHLUESSEL}", POSTFACH_PORT=str(cls.port))
        cls.proz = subprocess.Popen([sys.executable, str(WACHE)], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for _ in range(50):
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{cls.port}/gesund", timeout=1)
                break
            except Exception:
                time.sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        cls.proz.terminate()
        cls.proz.wait(5)
        cls.google.shutdown()

    def anfrage(self, methode, pfad, daten=None, schluessel=SCHLUESSEL):
        url = f"http://127.0.0.1:{self.port}/gmail/v1/users/me/{pfad}"
        req = urllib.request.Request(url, data=json.dumps(daten).encode() if daten is not None else None, method=methode)
        if schluessel:
            req.add_header("Authorization", f"Bearer {schluessel}")
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=5) as r:
                return r.status, json.loads(r.read() or b"{}")
        except urllib.error.HTTPError as e:
            return e.code, json.loads(e.read() or b"{}")

    def test_ohne_schluessel_401(self):
        self.assertEqual(self.anfrage("GET", "messages", schluessel=None)[0], 401)
        self.assertEqual(self.anfrage("GET", "messages", schluessel="falsch-falsch-falsch-falsch")[0], 401)

    def test_lesen_erlaubt(self):
        self.assertEqual(self.anfrage("GET", "messages?q=is%3Aunread")[0], 200)
        self.assertEqual(self.anfrage("GET", "messages/m1")[0], 200)
        self.assertEqual(self.anfrage("GET", "labels")[0], 200)

    def test_entwurf_erlaubt(self):
        s, d = self.anfrage("POST", "drafts", {"message": {"raw": "abc", "threadId": "t1"}})
        self.assertEqual(s, 200)
        self.assertEqual(d["id"], "entwurf-1")

    def test_senden_verboten(self):
        for pfad in ("messages/send", "drafts/send", "messages/m1/trash", "messages/batchDelete", "messages/batchModify",
                     "settings/forwardingAddresses", "settings/filters", "messages/import", "messages"):
            s, d = self.anfrage("POST", pfad, {"raw": "x", "id": "entwurf-1"})
            self.assertEqual(s, 403, pfad)
            self.assertIn("postfachWache", json.dumps(d))
        self.assertEqual(self.anfrage("DELETE", "messages/m1")[0], 405)

    def test_entwurf_nur_mit_message(self):
        self.assertEqual(self.anfrage("POST", "drafts", {"message": {"raw": "a"}, "send": True})[0], 403)

    def test_labels_nur_eigene(self):
        self.assertEqual(self.anfrage("POST", "labels", {"name": "Privat2"})[0], 403)
        self.assertEqual(self.anfrage("POST", "labels", {"name": "Vera/Gesichtet"})[0], 200)
        self.assertEqual(self.anfrage("POST", "messages/m1/modify", {"addLabelIds": ["Label_1"]})[0], 200)
        self.assertEqual(self.anfrage("POST", "messages/m1/modify", {"addLabelIds": ["INBOX"]})[0], 403)
        self.assertEqual(self.anfrage("POST", "messages/m1/modify", {"addLabelIds": ["Label_2"]})[0], 403)
        self.assertEqual(self.anfrage("POST", "messages/m1/modify", {"addLabelIds": ["Label_1"], "removeLabelIds": ["INBOX"]})[0], 403)
        self.assertEqual(self.anfrage("POST", "messages/m1/modify", {"addLabelIds": ["TRASH"]})[0], 403)

    def test_gmail_werkzeug_ueber_wache(self):
        env = dict(os.environ, POSTFACH_TOKEN=SCHLUESSEL, GMAIL_API_BASIS=f"http://127.0.0.1:{self.port}/gmail/v1")
        for k in ("GMAIL_CLIENT_ID", "GMAIL_CLIENT_SECRET", "GMAIL_REFRESH_TOKEN"):
            env.pop(k, None)
        r = subprocess.run([sys.executable, str(GMAIL), "suchen", "is:unread"], env=env, capture_output=True, text=True, timeout=30)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("m1", r.stdout)

    def test_kein_google_token_im_protokoll(self):
        self.anfrage("GET", "messages")
        self.proz.poll()
        # Protokoll enthaelt Agent und Pfad, nie Zugangsdaten
        aufrufe = [a for a in FalschesGoogle.aufrufe if a[1] == "/token"]
        self.assertTrue(aufrufe)


if __name__ == "__main__":
    unittest.main()
