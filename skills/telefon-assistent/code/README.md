# Telefon-Assistent (Vorbild: Leo)

Dein Agent ruft **nur dich** auf deinem Handy an, über deine FRITZ!Box, mit dem Kontext aus deinem
Chat. Im Gespräch nimmt er Aufträge an, arbeitet sie danach ab und schickt das Ergebnis schriftlich
in deinen Chat. Er kann Anrufe planen, etwa 15 Minuten vor einem Termin aus deinem Kalender.

Herkunft: der laufende Telefondienst von Christians Agent Leo (Stand 04.10.2026). Geändert wurden
nur persönliche Werte: Rufnummer, Chat-ID, Netzadressen, Registry. Namen in den Texten („Chris“,
„Leo“) sind noch fest im Code, siehe „Anpassen“.

## Bausteine

| Datei | Aufgabe |
|---|---|
| `bridge.py` | Telefon-Brücke: startet Asterisk, meldet es per PJSIP an der FRITZ!Box an, wählt nur die freigegebene Nummer, nimmt das Gespräch per AudioSocket entgegen, HTTP-Schnittstelle auf Port 8080 |
| `voice_provider.py` | Stimme über einen privaten ElevenLabs-Gesprächsagenten, bei Ausfall Wechsel auf das Echtzeit-Sprachmodell von OpenAI |
| `voice_protocol.py` | Wählplan, Prüfung der Zielnummer, Audio-Rahmen |
| `phone_logic.py` | Modi, Ruhezeiten, Mailbox-Erkennung, Steuerbefehle („Stopp“, „Danke, das war's“), Planung vor Terminen |
| `phone_state.py` | Aufträge, Anrufversuche und Zustellungen dauerhaft speichern |
| `backend.py` | Arbeitsdienst (Port 9120): lädt den Chat-Kontext, gibt Aufträge an den Agenten, meldet Ergebnisse in Telegram |
| `calendar_source.py` | liest den Google-Kalender für die Terminvorbereitung |
| `hold_music.py` | Wartemusik, während der Agent arbeitet |
| `call_owner.py` und `owner-phone-SKILL.md` | Skill für den Agenten: anrufen, prüfen, Status, auflegen, abbrechen, planen |
| `sip_probe.py` | Diagnose der SIP-Anmeldung, wählt nicht |
| `beispiel-kubernetes/` | So läuft es bei Leo, mit Platzhaltern statt echter Werte |
| `../references/architektur.md` | Ablauf, Stimme, Regeln und Grenzen im Detail |

## Voraussetzungen

- FRITZ!Box mit einem eingerichteten IP-Telefon (Telefonie, Telefoniegeräte, neues Gerät,
  LAN/WLAN-IP-Telefon) mit eigenem Benutzernamen und Passwort.
- Der Server mit der Brücke liegt im Netz der FRITZ!Box oder ist per VPN (WireGuard der FRITZ!Box)
  verbunden. Bei Leo läuft die Brücke direkt im Heimnetz.
- Asterisk mit PJSIP und AudioSocket, Python 3.12 (nicht 3.13, `audioop` fehlt dort),
  `aiohttp`, `websockets`. Ein fertiges Container-Image liegt nicht bei, dein Agent baut es.
- ElevenLabs-Konto mit Conversational AI, OpenAI-Schlüssel für den Ersatzweg, Telegram-Bot.

## Umgebungsvariablen

Brücke: `SIP_HOST`, `SIP_USERNAME`, `SIP_PASSWORD`, `SIP_MEDIA_ADDRESS` (Pflicht, IP des Servers im
FRITZ!Box-Netz), `SIP_CALLER_ID_NUMBER`, `SIP_CALLER_ID_NAME`, `CALL_ALLOWED_NUMBER` (deine
Handynummer, die einzige wählbare), `BRIDGE_TOKEN`, `VOICE_PROVIDER=elevenlabs`,
`ELEVENLABS_API_KEY`, `ELEVENLABS_AGENT_ID`, `OPENAI_API_KEY`, `LIVE_VOICE`, `LEO_BACKEND_URL`.

Arbeitsdienst: `BRIDGE_TOKEN`, `PHONE_URL`, `TELEGRAM_BOT_TOKEN`, `OWNER_TELEGRAM_CHAT_ID`,
`HERMES_HOME`. Alle Geheimnisse nur in der Geheimnis-Ablage deines Servers.

## Tests

```sh
python3.12 -m venv .venv && .venv/bin/pip install aiohttp websockets
.venv/bin/python -m unittest discover -s . -p 'test_*.py'
```

96 Tests, keine echten Anrufe und keine echten Telegram-Nachrichten. Freigabe nur mit null
übersprungenen Tests.

## Anpassen

- **Namen:** „Chris“ und „Leo“ stehen in `bridge.py` (Persona und Begrüßung), `backend.py`,
  `phone_logic.py`, `voice_provider.py`, `owner-phone-SKILL.md` und in Tests. Durch deinen Namen und den Namen
  deines Agenten ersetzen, Tests danach anpassen.
- **Agent:** `backend.py` (Klasse `HermesRuntime`) und `calendar_source.py` setzen einen
  Hermes-Agenten voraus (Sitzungen in `state.db`, Google-Workspace-Skill). Läuft dein Agent anders,
  ersetzt dein Agent genau diese zwei Stellen.
- **Chat:** Ergebnisse gehen an Telegram. Für Rocket.Chat die Zustellung in `backend.py` umstellen.
- **Adressen:** `call_owner.py` und `bridge.py` nennen die internen Adressen von Leos Cluster
  (`leo-voice-backend`, `leo-telephony`). An deinen Server anpassen.
