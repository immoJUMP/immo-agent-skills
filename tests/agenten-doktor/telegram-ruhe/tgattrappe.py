#!/usr/bin/env python3
"""Telegram-Bot-API-Attrappe: beantwortet die Aufrufe von python-telegram-bot und schreibt jeden
Aufruf mit Methode und Daten nach /log/aufrufe.jsonl. Kein echter Telegram-Kontakt."""
import json
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

LOG = "/log/aufrufe.jsonl"
NR = [0]


def daten_lesen(h):
    n = int(h.headers.get("Content-Length") or 0)
    roh = h.rfile.read(n) if n else b""
    art = h.headers.get("Content-Type", "")
    try:
        if "json" in art:
            return json.loads(roh or b"{}")
        if "x-www-form-urlencoded" in art:
            return {k: v[0] for k, v in urllib.parse.parse_qs(roh.decode()).items()}
        if "multipart" in art:
            grenze = art.split("boundary=")[-1].encode()
            felder = {}
            for teil in roh.split(b"--" + grenze):
                if b"name=\"" in teil and b"\r\n\r\n" in teil:
                    kopf, wert = teil.split(b"\r\n\r\n", 1)
                    name = kopf.split(b"name=\"")[1].split(b"\"")[0].decode()
                    felder[name] = wert.rstrip(b"\r\n-").decode(errors="replace")
            return felder
    except Exception as e:  # noqa: BLE001
        return {"_fehler": str(e)}
    return {"_roh": roh[:500].decode(errors="replace")}


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def antwort(self, ergebnis):
        b = json.dumps({"ok": True, "result": ergebnis}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(b)))
        self.end_headers()
        self.wfile.write(b)

    def do_GET(self):
        self.do_POST()

    def do_POST(self):
        methode = self.path.rstrip("/").split("/")[-1].split("?")[0]
        d = daten_lesen(self)
        if methode != "getUpdates":
            with open(LOG, "a") as f:
                f.write(json.dumps({"zeit": time.strftime("%H:%M:%S"), "methode": methode, "daten": d}, ensure_ascii=False) + "\n")
        if methode == "getMe":
            return self.antwort({"id": 999, "is_bot": True, "first_name": "Testbot", "username": "test_bot",
                                 "can_join_groups": True, "can_read_all_group_messages": False,
                                 "supports_inline_queries": False})
        if methode == "getUpdates":
            time.sleep(min(float(d.get("timeout") or 1), 2))
            return self.antwort([])
        if methode in ("sendMessage", "editMessageText"):
            NR[0] += 1
            return self.antwort({"message_id": NR[0], "date": int(time.time()),
                                 "chat": {"id": int(d.get("chat_id") or 0), "type": "private"}, "text": d.get("text", "")})
        if methode == "getWebhookInfo":
            return self.antwort({"url": "", "has_custom_certificate": False, "pending_update_count": 0})
        if methode in ("getMyCommands", "getMyDescription", "getMyShortDescription", "getMyName"):
            return self.antwort([] if methode == "getMyCommands" else {})
        return self.antwort(True)


ThreadingHTTPServer(("0.0.0.0", 8081), H).serve_forever()
