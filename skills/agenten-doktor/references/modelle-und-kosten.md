# Modelle und Kosten

Alle Preise: **Stand prüfen am Tag der Einrichtung.** Zahlen mit „ca.“ sind Spannen
zur Orientierung, keine zugesagten Preise. Vor dem Ja des Nutzers prüfst du die aktuellen
Preise auf den Seiten der Anbieter und nennst sie.

## Modellzugänge im Vergleich

| Zugang | `MODELL_ANBIETER` | Bewertung |
|---|---|---|
| **ChatGPT-/Codex-Abo**, Anmeldung per Gerätecode | `codex` | **Standard.** In Hermes offiziell unterstützt, feste Monatskosten, kein Kostenrisiko. Kontingent je Abo, alle Agenten teilen es. Plus wird bei mehreren täglichen Routinen schnell knapp, Pro hat deutlich mehr |
| **OpenAI-API-Schlüssel** | `openai` | Sauber (Geschäftsbedingungen, Auftragsverarbeitung möglich). Abrechnung nach Verbrauch. **Pflicht: Ausgabelimit** im Projekt |
| **OpenRouter** | `openrouter` | Ein Schlüssel für viele Modelle, auch Claude. Guthaben vorab, Limit je Schlüssel. Zusätzlicher Vermittler, Datenweg und Anbieter-Routing prüfen |
| **Claude-API-Schlüssel** (Anthropic Console) | derzeit über `openrouter` | Sauber nach den Anthropic Commercial Terms, Ausgabelimit in der Console. Der Installer kennt noch keinen eigenen Anbieterwert für einen direkten Anthropic-Schlüssel. Bis dahin Claude-Modelle per API über OpenRouter |
| **Claude-Abo (Pro/Max) über Meridian** | `meridian` | **Nicht empfohlen.** Nur auf ausdrücklichen Wunsch nach schriftlicher Aufklärung (unten) |

Datenschutz: Mails und Mieterdaten gehen an den Modellanbieter. Verbrauchertarife
(ChatGPT Plus/Pro, Claude-Abo) sind dafür die schwächere Grundlage. Ein Tarif mit Vertrag
zur Auftragsverarbeitung (API oder Business-Tarif) ist sauberer. Beim ChatGPT-Abo mindestens
die Nutzung der Inhalte zum Training in den Einstellungen abschalten. Das ist keine
Rechtsberatung: mit der eigenen Datenschutzberatung klären.

## Aufklärung zu Meridian (wörtlich zeigen)

> Du möchtest dein Claude-Abo (Pro oder Max) für die Agenten nutzen. Bitte lies das vorher:
>
> 1. Die Verbraucherbedingungen von Anthropic erlauben es nicht, die Zugangsdaten eines
>    Pro- oder Max-Abos in fremden Programmen wie Hermes zu verwenden. Meridian reicht dein
>    Abo an Hermes weiter. Das ist ein Verstoß gegen diese Bedingungen.
> 2. Anthropic kann dein Konto deshalb sperren. Dann verlierst du womöglich auch deinen
>    eigenen Claude-Zugang, nicht nur die Agenten.
> 3. Alle Agenten teilen sich dein Abo-Kontingent, auch mit deiner eigenen Nutzung. Ist das
>    Wochenlimit erreicht, stehen alle Agenten still, bis es zurückgesetzt wird.
> 4. Ohne Sperrrisiko sind ein Claude-API-Schlüssel (Abrechnung nach Verbrauch, mit Limit)
>    oder die Anmeldung mit deinem ChatGPT-Abo.
>
> Wenn du es trotzdem willst, schreib: „Ich habe die Aufklärung zu Meridian gelesen und
> trage das Risiko.“

Erst nach genau dieser Bestätigung weiter. Bestätigung und Datum ins Logbuch.
Kein zweites Abo-Konto anlegen, um Limits zu umgehen.

## Kosten je Monat

### Server (Hetzner)

| Posten | ca. EUR je Monat | Hinweis |
|---|---|---|
| cx43 (8 vCPU, 16 GB RAM) | 15,99 | Typ und Preis in der Console prüfen |
| Primäre IPv4-Adresse | 0,50 | |
| Backups (20 Prozent des Serverpreises) | ca. 3,20 | ganze VM, mehrere Tagesstände |
| **Summe Server** | **ca. 19,70** | |
| Storage Box für externe Sicherung (optional) | ca. 3 bis 5 | kleinste Größe reicht meist |

Hetzner zeigt Preise je nach Kontoart netto oder brutto. In der Console nachsehen.

### Modell

| Zugang | ca. je Monat | Bemerkung |
|---|---|---|
| ChatGPT Plus | ca. 20 bis 25 EUR | festes Kontingent, für leichte Nutzung |
| ChatGPT Pro | ca. 200 bis 250 EUR | viel mehr Kontingent |
| API, gut gebaute Routinen (OpenAI, OpenRouter, Claude) | ca. 20 bis 100 EUR | hängt stark von Modell und Routinen ab |
| API, schlecht gebaute Routinen | mehrere hundert EUR möglich | daher Ausgabelimit Pflicht |
| Claude-Abo über Meridian | Pro ca. 20 EUR, Max ca. 100 bis 200 EUR | nicht empfohlen, siehe oben |

**Warum die Spanne so groß ist:** Eine Mieteingangskontrolle, die alle Umsätze und alle
Mieter in den Kontext lädt und bei jedem Werkzeugaufruf alles erneut mitschickt, kann
mehrere Millionen Tokens verbrauchen. Bei API-Preisen von ca. 1 bis 15 USD je Million Tokens
sind das ca. 3 bis 45 USD für einen einzigen Lauf, an jedem Werktag. Gut gebaut rechnet
MietJUMP den Abgleich selbst (`abgleich_ausfuehren`), und das Modell sieht nur die
Ausnahmen. Dann sind es eher Zehntausende Tokens je Lauf. Beim Abo zeigt sich dasselbe
Problem als ausgeschöpftes Kontingent statt als Rechnung.

Verbrauch prüfen: in der Nutzungsübersicht des Anbieters nach Tagen. Sprünge an Werktagen
gegen 9 Uhr deuten auf den Mieteingang.

### Voice (optional, Ausbaustufe)

| Posten | ca. Kosten | Hinweis |
|---|---|---|
| sipgate Rufnummer und Anschluss | ca. 0 bis 15 EUR je Monat | Tarif prüfen |
| sipgate Gesprächsminuten | ca. 2 bis 10 Cent je Minute | Mobilfunk teurer als Festnetz |
| ElevenLabs Gesprächsagent | Abo ca. 5 bis 100 USD je Monat, Minuten ca. 0,08 bis 0,15 USD | Modellkosten können dazukommen |
| OpenAI-Live als Ausweich | ca. 0,05 bis 0,30 USD je Minute | |
| **Beispiel:** 2 Anrufe am Tag à 5 Minuten | **ca. 40 bis 100 EUR je Monat** | |

Details: [voice.md](voice.md).

### Beispielrechnung Grundpaket

| Variante | ca. je Monat |
|---|---|
| Server plus ChatGPT Plus | ca. 40 bis 45 EUR |
| Server plus API mit gut gebauten Routinen | ca. 40 bis 120 EUR |
| Server plus ChatGPT Pro | ca. 220 bis 270 EUR |

## Ausgabelimit einrichten (Pflicht bei API)

Nach Ja des Nutzers in Chrome, Oberfläche kann abweichen, per Screenshot prüfen:

- **OpenAI:** eigenes Projekt `agenten`, dort Budget bzw. Limit und Benachrichtigung
  setzen, Schlüssel nur für dieses Projekt erzeugen.
- **OpenRouter:** wenig Guthaben aufladen, Limit je Schlüssel setzen.
- **Anthropic Console:** monatliches Ausgabelimit setzen.

Vorschlag für den Start: Limit ca. 50 EUR im Monat, nach vier Wochen anhand des echten
Verbrauchs anpassen.

## Modellwechsel

`MODELL_ANBIETER` und `MODELL` in `konfig.env` ändern, Zugang wie in
[aufbau.md](aufbau.md) Schritt 12 bis 14 einrichten, dann `doktor installieren`,
`doktor modell-test` und am nächsten Tag die Routinen prüfen (Fehlerbild „Routinen laufen
nach Modellwechsel nicht“ in [pflege.md](pflege.md)).
