#!/usr/bin/env python3
"""Postfach-Wache: der einzige Weg der Agenten zu Gmail.

Haelt den Google-Refresh-Token (kein Agent bekommt ihn) und reicht nur eine
Erlaubnisliste von Gmail-API-Aufrufen durch:

  lesen      GET  messages, messages/{id}, messages/{id}/attachments/{aid}, labels, drafts
  entwerfen  POST drafts                         (Entwurf anlegen, nie senden)
  ordnen     POST labels                         (nur eigene Labels mit erlaubtem Praefix)
             POST messages/{id}/modify           (nur addLabelIds mit eigenen Labels)

Alles andere (messages/send, drafts/send, trash, delete, batchModify, settings,
removeLabelIds, Systemlabels wie TRASH/SPAM/INBOX) wird mit 403 abgelehnt.
Jeder Aufruf landet im Protokoll (Agent, Methode, Pfad, Ergebnis), nie Inhalte.

Umgebung:
  GMAIL_CLIENT_ID, GMAIL_CLIENT_SECRET, GMAIL_REFRESH_TOKEN   Google-Anmeldung (nur hier)
  POSTFACH_ZUGAENGE   "vera:<schluessel>,kurt:<schluessel>"   je Agent ein Schluessel
  POSTFACH_LABEL_PRAEFIXE  Standard "Agenten/,Vera/"
  GMAIL_API_BASIS, GOOGLE_TOKEN_URL  nur fuer Tests
"""
from __future__ import annotations

import hmac
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

API = os.environ.get("GMAIL_API_BASIS", "https://gmail.googleapis.com/gmail/v1").rstrip("/")
TOKEN_URL = os.environ.get("GOOGLE_TOKEN_URL", "https://oauth2.googleapis.com/token")
PRAEFIXE = tuple(p.strip() for p in os.environ.get("POSTFACH_LABEL_PRAEFIXE", "Agenten/,Vera/").split(",") if p.strip())
MAX_KOERPER = 30 * 1024 * 1024
ID = r"[A-Za-z0-9_-]{1,200}"

ERLAUBT = [
    ("GET", re.compile(rf"^messages$")),
    ("GET", re.compile(rf"^messages/{ID}$")),
    ("GET", re.compile(rf"^messages/{ID}/attachments/{ID}$")),
    ("GET", re.compile(r"^labels$")),
    ("GET", re.compile(r"^drafts$")),
    ("GET", re.compile(rf"^drafts/{ID}$")),
    ("GET", re.compile(r"^profile$")),
    ("POST", re.compile(r"^drafts$")),
    ("POST", re.compile(r"^labels$")),
    ("POST", re.compile(rf"^messages/{ID}/modify$")),
]


def zugaenge() -> dict:
    z = {}
    for teil in os.environ.get("POSTFACH_ZUGAENGE", "").split(","):
        if ":" in teil:
            agent, schluessel = teil.split(":", 1)
            if len(schluessel) >= 24:
                z[agent.strip()] = schluessel.strip()
    return z


def protokoll(agent: str, methode: str, pfad: str, status: int, hinweis: str = "") -> None:
    zeit = time.strftime("%Y-%m-%d %H:%M:%S")
    print(json.dumps({"zeit": zeit, "agent": agent, "methode": methode, "pfad": pfad, "status": status,
                      "hinweis": hinweis}, ensure_ascii=False), flush=True)


class Google:
    def __init__(self):
        self._token = None
        self._ablauf = 0.0
        self._sperre = threading.Lock()
        self._labels: dict = {}
        self._labels_zeit = 0.0

    def token(self, erneuern=False) -> str:
        with self._sperre:
            if self._token and not erneuern and time.time() < self._ablauf - 60:
                return self._token
            daten = urllib.parse.urlencode({
                "client_id": os.environ["GMAIL_CLIENT_ID"], "client_secret": os.environ["GMAIL_CLIENT_SECRET"],
                "refresh_token": os.environ["GMAIL_REFRESH_TOKEN"], "grant_type": "refresh_token"}).encode()
            req = urllib.request.Request(TOKEN_URL, data=daten, method="POST",
                                         headers={"Content-Type": "application/x-www-form-urlencoded"})
            with urllib.request.urlopen(req, timeout=30) as r:
                antwort = json.loads(r.read())
            self._token = antwort["access_token"]
            self._ablauf = time.time() + int(antwort.get("expires_in", 3000))
            return self._token

    def aufruf(self, methode: str, pfad: str, query: str, koerper: bytes | None):
        url = f"{API}/users/me/{pfad}" + (f"?{query}" if query else "")
        for versuch in range(2):
            req = urllib.request.Request(url, data=koerper, method=methode, headers={
                "Authorization": f"Bearer {self.token(erneuern=versuch > 0)}", "Accept": "application/json",
                **({"Content-Type": "application/json"} if koerper is not None else {})})
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    return r.status, r.read()
            except urllib.error.HTTPError as e:
                if e.code == 401 and versuch == 0:
                    continue
                return e.code, e.read()
        return 502, b'{"error":{"message":"keine Antwort"}}'

    def eigene_labels(self) -> dict:
        """id -> name der Nutzer-Labels (Cache 60 s)."""
        if time.time() - self._labels_zeit > 60:
            s, roh = self.aufruf("GET", "labels", "", None)
            if s == 200:
                self._labels = {l["id"]: l.get("name", "") for l in json.loads(roh).get("labels", [])
                                if l.get("type") == "user"}
                self._labels_zeit = time.time()
        return self._labels


GOOGLE = Google()


def label_erlaubt(name: str) -> bool:
    return any(name.startswith(p) for p in PRAEFIXE)


class Wache(BaseHTTPRequestHandler):
    server_version = "postfach-wache"
    sys_version = ""

    def log_message(self, *args):  # eigenes Protokoll statt Standardausgabe
        pass

    def _antwort(self, status: int, koerper: bytes, agent="-", hinweis=""):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(koerper)))
        self.end_headers()
        self.wfile.write(koerper)
        teil = urllib.parse.urlsplit(self.path)
        protokoll(agent, self.command, teil.path, status, hinweis)

    def _ablehnen(self, status: int, text: str, agent="-"):
        self._antwort(status, json.dumps({"error": {"code": status, "message": text, "errors": [{"reason": "postfachWache"}]}},
                                         ensure_ascii=False).encode(), agent, text)

    def _agent(self) -> str | None:
        kopf = self.headers.get("Authorization", "")
        if not kopf.startswith("Bearer "):
            return None
        geschickt = kopf[7:].strip()
        for agent, schluessel in zugaenge().items():
            if hmac.compare_digest(geschickt, schluessel):
                return agent
        return None

    def _bearbeiten(self):
        if self.path == "/gesund":
            return self._antwort(200, b'{"status":"ok"}')
        agent = self._agent()
        if not agent:
            return self._ablehnen(401, "Unbekannter oder fehlender Zugangsschluessel.")
        teil = urllib.parse.urlsplit(self.path)
        praefix = "/gmail/v1/users/me/"
        if not teil.path.startswith(praefix):
            return self._ablehnen(404, "Unbekannter Pfad.", agent)
        pfad = teil.path[len(praefix):]
        if not any(m == self.command and r.match(pfad) for m, r in ERLAUBT):
            return self._ablehnen(403, f"Die Postfach-Wache erlaubt {self.command} {pfad} nicht. "
                                       "Agenten duerfen lesen, Entwuerfe anlegen und eigene Labels setzen, nie senden oder loeschen.", agent)
        laenge = int(self.headers.get("Content-Length") or 0)
        if laenge > MAX_KOERPER:
            return self._ablehnen(413, "Anfrage zu gross.", agent)
        koerper = self.rfile.read(laenge) if laenge else None
        if self.command == "POST":
            try:
                daten = json.loads(koerper or b"{}")
            except json.JSONDecodeError:
                return self._ablehnen(400, "Kein gueltiges JSON.", agent)
            if pfad == "labels":
                if not label_erlaubt(str(daten.get("name", ""))):
                    return self._ablehnen(403, f"Labels nur mit Praefix {', '.join(PRAEFIXE)}.", agent)
            elif pfad.endswith("/modify"):
                if set(daten) - {"addLabelIds"} or not isinstance(daten.get("addLabelIds"), list):
                    return self._ablehnen(403, "Nur addLabelIds ist erlaubt (nichts entfernen, nichts verschieben).", agent)
                eigene = GOOGLE.eigene_labels()
                for lid in daten["addLabelIds"]:
                    if lid not in eigene or not label_erlaubt(eigene[lid]):
                        return self._ablehnen(403, f"Label {lid} ist kein eigenes Agenten-Label.", agent)
            elif pfad == "drafts":
                if set(daten) - {"message"} or not isinstance(daten.get("message"), dict):
                    return self._ablehnen(403, "Nur ein Entwurf mit message ist erlaubt.", agent)
            koerper = json.dumps(daten).encode()
        try:
            status, roh = GOOGLE.aufruf(self.command, pfad, teil.query, koerper)
        except Exception as e:  # noqa: BLE001
            return self._ablehnen(502, f"Google nicht erreichbar oder Anmeldung ungueltig: {type(e).__name__}", agent)
        if pfad == "labels" and self.command == "POST":
            GOOGLE._labels_zeit = 0
        self._antwort(status, roh, agent)

    def do_GET(self):
        self._bearbeiten()

    def do_POST(self):
        self._bearbeiten()

    def do_PUT(self):
        self._ablehnen(405, "Methode nicht erlaubt.")

    do_DELETE = do_PATCH = do_PUT


def main():
    if not zugaenge():
        print("POSTFACH_ZUGAENGE fehlt oder Schluessel zu kurz.", file=sys.stderr)
    port = int(os.environ.get("POSTFACH_PORT", "8090"))
    srv = ThreadingHTTPServer(("0.0.0.0", port), Wache)
    print(json.dumps({"start": f"Postfach-Wache auf Port {port}", "label_praefixe": PRAEFIXE}), flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    main()
