#!/usr/bin/env python3
"""google-anmeldung: Gmail-Zugang für die Agenten einrichten (Mac-Seite des Doktors).

OAuth-Desktop-Ablauf mit Loopback auf 127.0.0.1 und PKCE. Das Refresh-Token geht
direkt per stdin an `security -i` in den Schlüsselbund, nie in argv, Ausgabe oder Datei.
Nur Python-Standardbibliothek (3.11+).
"""

import argparse
import base64
import hashlib
import json
import os
import re
import secrets
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

AUTH_URL = os.environ.get("GOOGLE_AUTH_URL", "https://accounts.google.com/o/oauth2/v2/auth")
TOKEN_URL = os.environ.get("GOOGLE_TOKEN_URL", "https://oauth2.googleapis.com/token")
API_BASIS = os.environ.get("GMAIL_API_BASIS", "https://gmail.googleapis.com/gmail/v1").rstrip("/")
SCOPES = (
    # gmail.modify deckt Lesen, Entwuerfe und Labels ab. Senden, Loeschen und alles
    # andere verhindert die Postfach-Wache auf dem Server (Erlaubnisliste), nicht der Scope.
    "https://www.googleapis.com/auth/gmail.modify",
)
KC_DIENST = "agenten-doktor"
WARTEZEIT = 300
ZEITLIMIT = 30

HINWEIS_PRODUKTION = (
    "Wichtig: Die OAuth-App muss in der Google Cloud Console unter "
    "\"Google Auth Platform > Zielgruppe\" auf \"In Produktion\" stehen. "
    "Im Status \"Testen\" laufen Refresh-Tokens nach 7 Tagen ab und die Agenten verlieren den Zugang."
)

HILFE = f"""\
google-anmeldung: Gmail-Zugang für die Agenten einrichten (läuft auf dem Mac des Doktors).

Aufruf:
  google-anmeldung.py [client_secret_XXX.json] [--projekt NAME] [--kein-browser]

Ablauf:
  1. Client-ID und Client-Secret kommen aus der heruntergeladenen JSON-Datei eines
     OAuth-Clients vom Typ Desktop-App. Sie werden dabei im Schlüsselbund abgelegt
     (Dienst {KC_DIENST}, Konto <projekt>/gmail-client-id und <projekt>/gmail-client-secret).
     Ohne Datei werden sie von dort gelesen.
  2. Der Standardbrowser öffnet die Google-Anmeldung. Melde dich mit dem Postfach an,
     das die Agenten lesen sollen, und setze alle Haken.
  3. Das Refresh-Token landet nur im Schlüsselbund (Konto <projekt>/gmail-refresh-token),
     nie in der Ausgabe. Ein Testaufruf zeigt danach die verbundene Adresse.
  Danach auf den Server: doktor-lokal.sh geheimnis-senden <root@host> gmail-refresh-token
  GMAIL_REFRESH_TOKEN, ebenso gmail-client-id und gmail-client-secret.

Berechtigung: gmail.modify (die Postfach-Wache auf dem Server laesst nur Lesen, Entwuerfe und eigene Labels durch).
{HINWEIS_PRODUKTION}

Projekt: --projekt oder Umgebung DOKTOR_PROJEKT (Standard: agenten).
Exit-Codes: 0 verbunden, 1 Fehler, 2 falscher Aufruf.
"""


class Fehler(Exception):
    pass


class Aufruffehler(Exception):
    pass


_UEBERSETZUNG = {
    "unrecognized arguments: %s": "unbekannte Angaben: %s",
    "expected one argument": "erwartet einen Wert",
    "argument %(argument_name)s: %(message)s": "%(argument_name)s: %(message)s",
}
argparse._ = lambda s: _UEBERSETZUNG.get(s, s)


class _Parser(argparse.ArgumentParser):
    def error(self, message):
        raise Aufruffehler(message)


# ---------- Schlüsselbund ----------

def _konto(projekt, name):
    return f"{projekt}/{name}"


def kc_lesen(projekt, name):
    r = subprocess.run(
        ["security", "find-generic-password", "-s", KC_DIENST, "-a", _konto(projekt, name), "-w"],
        capture_output=True, text=True)
    wert = r.stdout.strip() if r.returncode == 0 else ""
    return wert or None


def kc_schreiben(projekt, name, wert):
    """Schreibt über `security -i` (Befehl per stdin), damit der Wert nie in argv steht."""
    if not wert or re.search(r"[\s\"'\\]", wert):
        raise Fehler(f"Wert für {name} ist leer oder enthält Leer- oder Sonderzeichen. Nicht gespeichert.")
    zeile = f"add-generic-password -U -s {KC_DIENST} -a {_konto(projekt, name)} -w {wert}\n"
    r = subprocess.run(["security", "-i"], input=zeile, capture_output=True, text=True)
    if r.returncode != 0 or kc_lesen(projekt, name) != wert:
        raise Fehler(f"{name} ließ sich nicht im Schlüsselbund speichern "
                     f"(Dienst {KC_DIENST}, Konto {_konto(projekt, name)}).")


# ---------- OAuth ----------

def client_laden(datei, projekt):
    if datei:
        try:
            with open(datei, encoding="utf-8") as f:
                daten = json.load(f)
        except OSError as e:
            raise Fehler(f"{datei} nicht lesbar ({e.strerror}).")
        except ValueError:
            raise Fehler(f"{datei} ist keine gültige JSON-Datei.")
        if not isinstance(daten, dict):
            raise Fehler(f"{datei} enthält keinen OAuth-Client.")
        if "web" in daten and "installed" not in daten:
            raise Fehler("Diese Datei gehört zu einem OAuth-Client vom Typ Webanwendung. Lege in der "
                         "Google Cloud Console einen Client vom Typ Desktop-App an und lade dessen JSON herunter.")
        client = daten.get("installed")
        if not isinstance(client, dict):
            raise Fehler(f"{datei} enthält keinen OAuth-Client vom Typ Desktop-App (Schlüssel installed fehlt).")
        cid, geheim = client.get("client_id"), client.get("client_secret")
        if not cid or not geheim:
            raise Fehler(f"In {datei} fehlen client_id oder client_secret.")
        kc_schreiben(projekt, "gmail-client-id", cid)
        kc_schreiben(projekt, "gmail-client-secret", geheim)
        print(f"Client-ID und Client-Secret im Schlüsselbund gespeichert (Konto {projekt}/gmail-client-...).")
        return cid, geheim
    cid, geheim = kc_lesen(projekt, "gmail-client-id"), kc_lesen(projekt, "gmail-client-secret")
    if not cid or not geheim:
        raise Fehler(f"Client-ID oder Client-Secret fehlt im Schlüsselbund (Projekt {projekt}). "
                     "Gib die heruntergeladene client_secret_XXX.json als Argument an.")
    return cid, geheim


def pkce():
    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode("ascii")).digest())
    return verifier, challenge.decode("ascii").rstrip("=")


class _Rueckruf(BaseHTTPRequestHandler):
    timeout = 10  # leere Vorab-Verbindungen des Browsers blockieren sonst die Schleife

    def do_GET(self):
        url = urllib.parse.urlsplit(self.path)
        werte = {k: v[0] for k, v in urllib.parse.parse_qs(url.query).items()}
        if url.path != "/" or not ({"code", "error"} & set(werte)):
            self.send_response(404)
            self.end_headers()
            return
        if self.server.ergebnis is None:
            self.server.ergebnis = werte
        ok = "code" in werte and werte.get("state") == self.server.state
        text = ("Anmeldung erhalten. Du kannst dieses Fenster schließen und zum Terminal zurückkehren."
                if ok else "Anmeldung nicht abgeschlossen. Details stehen im Terminal.")
        inhalt = (f"<!doctype html><meta charset=utf-8><title>Agenten-Doktor</title>"
                  f"<p style='font:16px sans-serif;margin:3em'>{text}</p>").encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(inhalt)))
        self.end_headers()
        self.wfile.write(inhalt)

    def log_message(self, *args):
        pass


def _post_form(url, felder):
    anfrage = urllib.request.Request(url, data=urllib.parse.urlencode(felder).encode(), method="POST",
                                     headers={"Content-Type": "application/x-www-form-urlencoded"})
    try:
        with urllib.request.urlopen(anfrage, timeout=ZEITLIMIT) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        try:
            info = json.loads(e.read() or b"{}")
        except ValueError:
            info = {}
        code = info.get("error", f"HTTP {e.code}")
        beschreibung = info.get("error_description") or ""
        raise Fehler(f"Google lehnt den Tausch des Anmeldecodes ab ({code}"
                     + (f": {beschreibung}" if beschreibung else "") + ").")
    except urllib.error.URLError as e:
        raise Fehler(f"Keine Verbindung zu Google ({e.reason}).")


def profil_adresse(access_token):
    anfrage = urllib.request.Request(f"{API_BASIS}/users/me/profile",
                                     headers={"Authorization": "Bearer " + access_token})
    try:
        with urllib.request.urlopen(anfrage, timeout=ZEITLIMIT) as r:
            return json.loads(r.read() or b"{}").get("emailAddress") or "unbekannt"
    except urllib.error.HTTPError as e:
        raise Fehler(f"Testaufruf an Gmail fehlgeschlagen (HTTP {e.code}). "
                     "Ist die Gmail API im Google-Cloud-Projekt aktiviert?")
    except urllib.error.URLError as e:
        raise Fehler(f"Testaufruf an Gmail fehlgeschlagen ({e.reason}).")


def anmelden(datei, projekt, browser=True):
    if not shutil.which("security"):
        raise Fehler("Der Befehl security fehlt. Dieser Helfer läuft nur auf dem Mac (Schlüsselbund).")
    cid, geheim = client_laden(datei, projekt)
    verifier, challenge = pkce()
    state = secrets.token_urlsafe(24)

    server = HTTPServer(("127.0.0.1", 0), _Rueckruf)
    server.state, server.ergebnis, server.timeout = state, None, 1
    redirect = f"http://127.0.0.1:{server.server_address[1]}/"
    url = AUTH_URL + "?" + urllib.parse.urlencode({
        "client_id": cid,
        "redirect_uri": redirect,
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent",
        "code_challenge": challenge,
        "code_challenge_method": "S256",
        "state": state,
    })
    print("Anmeldeseite (öffnet sich im Standardbrowser, sonst Adresse selbst öffnen):")
    print(url)
    print(flush=True)
    if browser:
        try:
            subprocess.run(["open", url], check=True, timeout=15, capture_output=True)
        except (OSError, subprocess.SubprocessError):
            print("Browser ließ sich nicht öffnen. Öffne die Adresse oben selbst.", flush=True)
    print(f"Warte bis zu {WARTEZEIT // 60} Minuten auf die Anmeldung ...", flush=True)
    ende = time.monotonic() + WARTEZEIT
    try:
        while server.ergebnis is None and time.monotonic() < ende:
            server.handle_request()
    finally:
        server.server_close()
    ergebnis = server.ergebnis
    if ergebnis is None:
        raise Fehler("Keine Anmeldung innerhalb der Wartezeit. Bitte erneut starten.")
    if ergebnis.get("state") != state:
        raise Fehler("Sicherheitsprüfung fehlgeschlagen (state passt nicht). Bitte erneut starten.")
    if "error" in ergebnis:
        raise Fehler(f"Anmeldung abgebrochen oder abgelehnt ({ergebnis['error']}).")

    antwort = _post_form(TOKEN_URL, {
        "code": ergebnis["code"],
        "client_id": cid,
        "client_secret": geheim,
        "redirect_uri": redirect,
        "grant_type": "authorization_code",
        "code_verifier": verifier,
    })
    refresh, access = antwort.get("refresh_token"), antwort.get("access_token")
    if not refresh or not access:
        raise Fehler("Google hat kein Refresh-Token geliefert. Entferne den Zugriff der App unter "
                     "myaccount.google.com/permissions und starte erneut.")
    erteilt = set((antwort.get("scope") or "").split())
    fehlend = [s.rsplit("/", 1)[-1] for s in SCOPES if s not in erteilt]
    if erteilt and fehlend:
        raise Fehler(f"Nicht alle Berechtigungen erteilt, es fehlt: {', '.join(fehlend)}. "
                     "Bitte erneut starten und alle Haken setzen. Nichts gespeichert.")
    kc_schreiben(projekt, "gmail-refresh-token", refresh)
    print(f"Refresh-Token im Schlüsselbund gespeichert (Dienst {KC_DIENST}, Konto {projekt}/gmail-refresh-token).")
    print(f"Verbunden mit: {profil_adresse(access)}")
    print()
    print(HINWEIS_PRODUKTION)
    return 0


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if any(x in ("-h", "--help", "--hilfe") for x in argv):
        sys.stdout.write(HILFE)
        return 0
    p = _Parser(add_help=False, allow_abbrev=False)
    p.add_argument("datei", nargs="?")
    p.add_argument("--projekt", default=os.environ.get("DOKTOR_PROJEKT", "agenten"))
    p.add_argument("--kein-browser", action="store_true")
    try:
        a = p.parse_args(argv)
        if not re.match(r"^[A-Za-z0-9._-]+$", a.projekt):
            raise Aufruffehler(f"ungültiger Projektname {a.projekt!r}")
        return anmelden(a.datei, a.projekt, browser=not a.kein_browser)
    except Aufruffehler as e:
        print(f"Falscher Aufruf: {e}. Hilfe: google-anmeldung.py -h", file=sys.stderr)
        return 2
    except Fehler as e:
        print(f"Fehler: {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("Abgebrochen.", file=sys.stderr)
        return 130


if __name__ == "__main__":
    sys.exit(main())
