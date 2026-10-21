---
name: immojump-cli
description: "Steuert immoJUMP ueber die immojump-CLI als Backend fuer Agenten: Immobilien, Einheiten, Mieterlisten, Datenraum-Dokumente, KI-Analysen und eigene Analysewerte je Einheit -- auch bei Grossbestaenden mit hunderten Einheiten und tausend Dokumenten. Ersetzt lokale JSON-Zustandsdateien durch immoJUMP als einzige Quelle, laedt in Stapeln, ist wiederholbar und spart Kontext. Nutze diesen Skill wenn ein Agent Daten in immoJUMP schreiben oder daraus lesen soll, besonders bei Portfolio-Ankaeufen, Datenraeumen und Mieterlisten-Importen."
---

# immoJUMP-CLI -- immoJUMP als Backend fuer Agenten

> **Kategorie:** Werkzeug & Datenhaltung
> **Zielgruppe:** Investoren und Teams, die immoJUMP aus Claude Code, Codex oder eigenen Agenten steuern
> **Voraussetzung:** `immojump` installiert, API-Token und Organisation

Du arbeitest mit immoJUMP ueber die Kommandozeile `immojump`. immoJUMP ist die
**einzige Quelle der Wahrheit** fuer Objekte, Einheiten, Dokumente und deine
Analysewerte. Du haeltst keinen eigenen Zustand in lokalen JSON-Dateien: Was du
wissen musst, fragst du immoJUMP; was du herausfindest, schreibst du nach
immoJUMP zurueck.

---

## Wann diesen Skill nutzen

- Ein Portfolio-Ankauf mit vielen Haeusern und Einheiten soll in immoJUMP
  geladen und dort analysiert werden.
- Ein Datenraum (Mietvertraege, Grundbuch, Teilungserklaerung, Energieausweis,
  Exposes) soll hochgeladen, Einheiten zugeordnet und analysiert werden.
- Ein Agent soll eigene Ergebnisse je Einheit speichern, z. B. Marktmiete,
  Sanierungsbedarf oder eine Mieterhoehungsreserve.
- Ein bestehender Ablauf haelt seinen Stand in einer JSON-Datei, und die
  skaliert nicht mehr.

**Nicht der richtige Skill, wenn:** du nur fachlich bewerten willst, ohne Daten
in immoJUMP zu halten (dann `deal-screener`, `mietlisten-analyse`,
`unterlagen-analyst`), oder Pipelines und Prozesse bauen willst (dann
`prozess-designer`).

---

## Einrichtung (einmal)

```bash
curl -fsSL https://raw.githubusercontent.com/immoJUMP/immojump-cli/main/install.sh | sh
export IMMOJUMP_TOKEN=...            # immoJUMP: Einstellungen -> API-Zugang
export IMMOJUMP_ORGANISATION_ID=...  # aus der App-URL /o/<org-id>/
export IMMOJUMP_ALLOW=read,write     # nie loeschen, nie nach aussen freigeben
immojump auth status                 # prueft Token, Organisation und Rolle
```

Den Token nie in Dateien, Prompts oder Logs schreiben. Fuer reine Auswertungen
`--readonly` setzen.

---

## Die zehn Regeln

1. **Erst nachsehen, dann aufrufen.** Mit `immojump <ressource> --help`,
   `immojump schema <ressource> <befehl>` und `immojump docs` pruefst du die
   echten Flags. Parameter, die dort nicht stehen, gibt es nicht.
2. **Ein Haus = eine Immobilie** (`MFH`/`WGH`) mit Einheiten. Lege nie jede
   Wohnung als eigenes Objekt an: Der Profi-Plan erlaubt 200 aktive Objekte.
3. **Jede Einheit traegt die Nummer des Verkaeufers als `extern_id`**, z. B.
   `RH-01-WE-001`. Darueber ist jeder Import wiederholbar. Ohne `extern_id`
   verdoppelt ein zweiter Lauf die Einheiten.
4. **Stapel statt Schleifen.** Nutze `units import`, `units fields-set` und
   `documents upload <ordner> --recursive`, keine Schleife ueber 900 einzelne
   `units create`.
5. **Vor jedem Massen-Schreiben ein Trockenlauf.** Erst `--dry-run` und die
   Summe pruefen, dann ein Pilot mit einem Haus, dann der Rest.
6. **Kontext sparen.** Jede Liste bekommt `--fields`. Die Immobilie liest du
   mit `immobilien get <id> --exclude units,dokumente`. Fuer Fortschritt
   fragst du nur `--limit 1 --fields total`. OCR-Texte nie in Masse in den
   Kontext laden.
7. **Rechnen macht Code, nicht du.** Summen, Mittelwerte, Faktor und Rendite
   ueber hunderte Einheiten rechnest du mit `jq` oder einem Skript aus der
   CLI-Ausgabe. Nie im Kopf ueberschlagen.
8. **Auf Exit-Codes reagieren, nicht auf Meldungstexte.**
   - 7 (Rate Limit) und 8 (Server/Netz): spaeter erneut starten. Lesende
     Aufrufe und Importe wiederholen sich selbst.
   - 11 (ungueltige Eingabe): die Daten korrigieren.
   - 9 (Konflikt): erst nachsehen, nicht blind wiederholen.
   - 6 (keine Berechtigung oder Policy): stoppen und fragen.
9. **Schreiben nur mit Ziel.** Vor jedem schreibenden Lauf nennst du, welche
   Immobilie und wie viele Einheiten oder Dokumente betroffen sind. Loeschen
   (`destructive`) und Freigeben nach aussen (`external`) nur nach
   ausdruecklicher Freigabe des Menschen.
10. **Ergebnisse zurueckschreiben.** Eigene Analysewerte kommen in
    benutzerdefinierte Felder an der Einheit (`units fields-set`), Befunde zum
    Haus in eine Aktivitaet oder Notiz. Sonst wiederholt der naechste Agent
    deine Arbeit.

---

## Ablauf Portfolio-Ankauf (Kurzform)

Vollstaendig mit Pruefpunkten, Feldzuordnung und Auswertungsrezepten:
`references/portfolio-ankauf.md`. **Lies diese Datei, bevor du einen Datenraum
oder eine Mieterliste laedst.**

1. **Inventur des Datenraums.** Zaehle Haeuser, Einheiten je Haus und Dokumente
   je Art. Erst dann schreiben.
2. **Haeuser anlegen.** Vorher pruefen, ob sie schon existieren:
   `immobilien list --fields id,name,daten.extern_id`.
3. **Mieterliste normalisieren** (Spaltenzuordnung in der Referenz), dann
   `units import --dry-run`, danach der echte Import je Haus.
4. **Pruefen:** Die Zahl der Einheiten je Haus und die Summe der Ist-Miete
   stimmen mit der Quelle ueberein.
5. **Datenraum hochladen** je Haus, Mietvertraege mit `--unit-id` direkt an
   ihre Einheit.
6. **Analysieren:** `documents analyze-all` je Haus, den Fortschritt fragst du
   nur als Zahl ab.
7. **Auswerten** ueber das ganze Portfolio mit `units list-org --all --fields ...`.
   Eigene Werte schreibst du mit `units fields-set` zurueck.

---

## Antipatterns

| Statt | Besser |
|---|---|
| Zustand in `portfolio.json` mitfuehren | immoJUMP abfragen; `extern_id` ist der Schluessel |
| 900-mal `units create` | `units import` (Stapel zu 500) |
| `immobilien get` mit allen Einheiten und Dokumenten | `--exclude units,dokumente` |
| `documents list` ohne Filter | `--analysis-status`, `--unit-id`, `--limit 1 --fields total` |
| `api POST ...` fuer etwas, das ein Befehl kann | den Befehl nehmen: Er kennt Risk-Level und Stapel |
| Ein abgebrochener Import, dann neue Einheiten anlegen | dieselbe Datei erneut importieren; unveraenderte Zeilen schreiben nichts |
| Analysewerte in eine Notiz als Freitext | ein benutzerdefiniertes Feld je Kennzahl |

---

## Ausgabe an den Menschen

Nach jedem Lauf eine kurze Bilanz:
- was angelegt, geaendert und unveraendert ist, je Haus;
- was fehlschlug und warum, mit Datei und Zeile;
- was als Naechstes ansteht, z. B. „43 Dokumente warten auf Analyse“.

Keine Rohdaten-Dumps.
