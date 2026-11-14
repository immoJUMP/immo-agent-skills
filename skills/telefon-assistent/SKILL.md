---
name: telefon-assistent
description: "Übernimmt einen Telefon-Assistenten auf den eigenen Agenten-Server: Der Agent ruft ausschließlich den Inhaber über dessen FRITZ!Box auf dem Handy an, bringt den Kontext aus dem Chat mit, nimmt im Gespräch Aufträge an, schickt Ergebnisse danach in den Chat und ruft auf Wunsch 15 Minuten vor Terminen an. Stimme über ElevenLabs, Ersatz über das Echtzeit-Sprachmodell von OpenAI. Der Code läuft produktiv bei Christians Agent Leo. Verwenden bei „mein Agent soll mich anrufen“, „Telefon-Assistent einrichten“, „Anruf vor der Besichtigung“, „FRITZ!Box an den Agenten anbinden“. Nicht für Anrufe an Mieter, Makler oder andere Dritte."
---

# Telefon-Assistent

Ein fertiger Telefondienst für einen eigenen Agenten. Er ruft **nur den Inhaber** an, über dessen
FRITZ!Box, mit dem Kontext aus dem Chat. Im Gespräch nimmt er Aufträge an, der Agent arbeitet sie ab,
das Ergebnis kommt schriftlich in den Chat. Er kann Anrufe planen, etwa 15 Minuten vor einem Termin.

Der Code in `code/` ist der laufende Dienst von Christians Agent Leo (Stand 04.10.2026, 96 Tests),
bereinigt um persönliche Werte. Wie er funktioniert, steht in [code/README.md](code/README.md), Regeln
und Grenzen in [references/architektur.md](references/architektur.md).

## Ablauf

1. **Lesen:** `code/README.md`, `references/architektur.md` und `code/owner-phone-SKILL.md` vollständig.
2. **Bestand aufnehmen:** Wie laufen die Agenten des Nutzers (Hermes oder anders)? Welcher Chat
   (Telegram, Rocket.Chat)? Welcher Kalender? Liegt der Server im Netz der FRITZ!Box oder braucht er
   eine VPN-Verbindung dorthin (WireGuard der FRITZ!Box)?
3. **Plan vorlegen**, bevor etwas gebaut wird:
   - was unverändert übernommen wird,
   - was angepasst wird: Namen „Chris“ und „Leo“, Anbindung an den Agenten (`HermesRuntime` in
     `backend.py`, `calendar_source.py`), Zustellung in den Chat, interne Adressen,
   - welches Container-Image entsteht (Asterisk mit PJSIP und AudioSocket, Python 3.12),
   - was an der FRITZ!Box einzurichten ist (Telefonie, Telefoniegeräte, neues LAN/WLAN-IP-Telefon),
   - welche Zugangsdaten wohin gehören.
4. **Bauen erst nach dem Ja des Nutzers**, Schritt für Schritt in der Prüfreihenfolge aus
   `references/architektur.md`: Tests ohne übersprungene Fälle, SIP-Anmeldung ohne Wählen,
   Sprachsitzung ohne Anruf, Zugangstest ohne Anruf.
5. **Erster echter Anruf** nur, wenn der Nutzer ausdrücklich „Testanruf“ sagt.

## Grenzen, die bleiben

- Angerufen wird nur die Nummer des Inhabers. Nummer und Chat-Empfänger stehen fest auf dem Server.
- Tageslimits, Ruhezeiten (selbstständige Anrufe nur 8 bis 20 Uhr), kein erneutes Wählen nach
  Mailbox oder Nichtannahme, höchstens 10 Minuten Gespräch.
- Keine Aufzeichnung oder Transkription von Gesprächen mit anderen Personen.
- Zugangsdaten (SIP-Passwort, ElevenLabs- und OpenAI-Schlüssel, Bot-Token) nie im Chat abfragen, nie
  in Git, Logbuch oder Prompt. Der Nutzer trägt sie selbst in die Geheimnis-Ablage ein.
- Gesprächsaudio geht an ElevenLabs bzw. OpenAI: auf Verträge zur Auftragsverarbeitung hinweisen.

## Tests

```sh
cd skills/telefon-assistent/code
python3.12 -m venv .venv && .venv/bin/pip install aiohttp websockets
.venv/bin/python -m unittest discover -s . -p 'test_*.py'
```

Erwartet: 96 Tests, OK, keine übersprungenen. Python 3.13 fehlt `audioop`.
