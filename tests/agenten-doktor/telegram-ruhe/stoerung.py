#!/usr/bin/env python3
"""Nachweis Teil 2: echter Doktor-Code (stoerung_melden, telegram_an_eigentuemer, http_json) gegen die
Telegram-Attrappe. Nur die Adresse api.telegram.org wird auf die Attrappe umgebogen, Zustand und
Konfiguration liegen in einem Wegwerf-Ordner."""
import importlib.machinery
import importlib.util
import json
import pathlib
import tempfile

lo = importlib.machinery.SourceFileLoader("d", "/root/tgtest/doktor-neu")
spec = importlib.util.spec_from_loader("d", lo)
d = importlib.util.module_from_spec(spec)
lo.exec_module(d)

tmp = pathlib.Path(tempfile.mkdtemp())
zustand = {}
d.zustand = lambda: json.loads(json.dumps(zustand))
d.zustand_speichern = lambda z: (zustand.clear(), zustand.update(z))
d.geheim = lambda: {"TELEGRAM_BOT_TOKEN": "123456:TESTTOKEN"}
d.konfig = lambda: {"EIGENTUEMER_TELEGRAM_ID": "4711", "DOMAIN": "test.example.de"}
logbuch = []
d.logbuch = lambda titel, zeilen, art=None: logbuch.append(titel)
echt = d.http_json
d.http_json = lambda m, u, *a, **kw: echt(m, u.replace("https://api.telegram.org", "http://127.0.0.1:8081"), *a, **kw)

defs = {"kurt": {"name": "Kurt"}, "vera": {"name": "Vera"}}
k = d.konfig()
R, G = d.ROT, d.GRUEN
stoerung = [(R, "agent-vera", "exited (1)"), (R, "agenten-mietjump-1", "exited (137)"), (G, "Festplatte", "61 % frei")]
for lauf in (1, 2, 3, 4):
    d.stoerung_melden(k, defs, stoerung)
    print(f"Reparaturlauf {lauf} (Vera und MietJUMP rot): Zustand gemeldet={zustand['stoerung']['gemeldet']}")
d.stoerung_melden(k, defs, [(G, "agent-vera", "Up"), (G, "agenten-mietjump-1", "Up")])
print("Reparaturlauf 5 (alles gruen): Zustand", zustand or "leer")
print("Logbuch:", logbuch)
