# Portfolio-Ankauf mit immoJUMP als Backend

Referenz zu `immojump-cli`. Durchgespielt mit einem synthetischen Datenraum:
14 Haeuser, 912 Einheiten, 919 PDFs. Die Werte unter „Erwartung“ stammen aus
diesem Lauf.

---

## 0. Inventur, bevor geschrieben wird

```bash
find datenraum -type f -name '*.pdf' | wc -l                      # Dokumente gesamt
find datenraum -maxdepth 1 -mindepth 1 -type d | wc -l            # Haeuser (ein Ordner je Haus)
```

Halte fest, wie viele Haeuser es sind, wie viele Einheiten je Haus laut
Mieterliste, welche Dokumentarten vorliegen (Mietvertraege je Einheit,
Grundbuch, Teilungserklaerung, Energieausweis, Expose, Scans ohne Text) und wie
die Verkaeufer-Nummer aussieht (z. B. `RH-01-WE-001`).

**Stop-Regel:** Hat eine Einheit keine eindeutige Nummer, bilde vor dem Import
eine stabile Nummer aus Haus, Eingang, Geschoss und Lage, z. B.
`RH-01-A-EG-li`. Sie darf sich zwischen zwei Laeufen nie aendern.

---

## 1. Haeuser anlegen (wiederholbar)

```bash
immojump immobilien list --fields id,name,daten.extern_id      # was gibt es schon?
immojump immobilien create --type MFH \
  --set name='Mehrfamilienhaus Rosengasse 136-150, Koeln' \
  --set daten.adresse='Rosengasse 136-150, 50968 Koeln' \
  --set daten.extern_id=RH-01 \
  --set daten.kaufpreis=15220000 \
  --fields id
```

- Lege `daten.extern_id` an jedem Haus an. So findet der naechste Lauf das Haus
  wieder, ohne lokale Zuordnungsdatei.
- Typ `MFH` fuer reine Wohnhaeuser, `WGH` fuer Wohn- und Geschaeftshaeuser.
- Die neue Immobilie hat eine leere Start-„Einheit 1“. Der erste Import, der
  Einheiten anlegt, entfernt sie (`placeholder_removed: true`).

---

## 2. Mieterliste normalisieren

Die CLI erwartet die Feldnamen des Backends. Typische Spalten einer
Verkaeufer-Mieterliste:

| Mieterliste | Feld | Hinweis |
|---|---|---|
| Einheit-Nr., WE-Nr. | `extern_id` | Pflicht fuer wiederholbare Importe |
| Lage, Bezeichnung | `einheit` | z. B. „WE 001 EG links“ |
| Nutzung, Art | `type` | `wohnen`, `gewerbe`, `stellplatz`, `garage`, `sonstiges` |
| Wohnflaeche, qm | `livingspace` | Zahl in m²; Stellplatz/Garage 0 |
| Zimmer | `rooms` | 2.5 erlaubt |
| Ist-Kaltmiete, NKM | `ist_rent` | €/Monat; Leerstand 0 |
| Soll-/Marktmiete | `soll_rent` | ohne Angabe = `ist_rent` |
| Mietbeginn | `lease_start_date` | `YYYY-MM-DD` oder `DD.MM.YYYY` |
| letzte Mieterhoehung | `last_rent_increase_date` | dito |
| Bemerkung, Mieter | `note` | Mieternamen nur, wenn noetig (Datenschutz) |

Zuordnung der Nutzungsart:
- Wohnung, App., Maisonette -> `wohnen`
- Laden, Buero, Praxis, Gastro -> `gewerbe`
- TG-Platz, Stellplatz, Carport -> `stellplatz`
- Garage -> `garage`
- Lager, Keller, Antenne -> `sonstiges`

Regeln:
- **NDJSON:** eine Einheit je Zeile, Zahlen als JSON-Zahlen mit Punkt. Das
  Backend lehnt `"62,5"` ab, weil es nicht raten will, ob „1.250“ 1,25 oder
  1250 heisst.
- **CSV:** Kopfzeile = Feldnamen, deutsche Zahlen mit
  `--decimal-comma --delimiter ';'`.
- **Keine fremden Schluessel.** Unbekannte Felder (etwa `extern_id_objekt`)
  lehnt das Backend mit 400 ab. Entferne sie, bevor du die Datei je Haus
  aufteilst.
- **Leerstand:** `ist_rent` 0. Wenn bekannt, gehoert der Grund in `note`, z. B.
  „Leerstand - Sanierung erforderlich“.

Beispiel einer Zeile:

```json
{"extern_id":"RH-01-WE-001","einheit":"WE 001 EG links","type":"wohnen","livingspace":77.74,"rooms":3,"ist_rent":703.48,"soll_rent":856.19,"lease_start_date":"2012-05-10"}
```

---

## 3. Import mit Pruefpunkten

```bash
immojump units import "$ID" --file rh-01.ndjson --dry-run --fields created,updated,unchanged,placeholder_removed
immojump units import "$ID" --file rh-01.ndjson --fields created,updated,unchanged,batches
```

**Erwartung** beim ersten Lauf: `created` = Zeilen der Datei,
`placeholder_removed: true`. Beim zweiten Lauf mit derselben Datei:
`unchanged` = Zeilen, nichts angelegt. 912 Einheiten in 14 Haeusern dauerten
lokal unter einer Sekunde.

**Gegenpruefung je Haus** (Anzahl und Ist-Miete gegen die Quelle):

```bash
immojump units list "$ID" --all --fields ist_rent \
  | jq '{einheiten: length, ist_miete_monat: (map(.ist_rent // 0) | add * 100 | round / 100)}'
```

**Scheitert ein Stapel (Exit 11):**
- Die Fehlerzeile nennt `line`, `index` und die Meldung.
- Stapel davor sind gespeichert (`committed_batches`).
- Korrigiere die Datei und importiere sie **ganz** erneut. Gespeicherte Zeilen
  kommen als `unchanged` zurueck.

---

## 4. Datenraum hochladen

```bash
immojump documents upload datenraum/RH-01 --recursive --immobilie-id "$ID"
```

- Die CLI laedt in Stapeln von 10 Dateien bzw. 25 MB und berichtet je Datei
  (`uploaded`, `duplicates`, `failed`, `empty`).
- Exit 0 heisst: nichts ist gescheitert.
- Ein zweiter Lauf ist sicher: Schon Hochgeladenes erscheint unter
  `duplicates`.
- **Die Duplikat-Erkennung gilt fuer die ganze Organisation, nicht nur fuer
  das Haus.** Liegt dieselbe Datei schon an einem anderen Objekt, wird sie hier
  nicht angehaengt. Der Eintrag unter `duplicates` nennt das Objekt
  (`existingPropertyId`). Gehoert die Datei wirklich an beide Objekte (z. B.
  eine Teilungserklaerung fuer zwei Haeuser), lade sie mit `--allow-duplicate`
  erneut hoch.

**Erwartung:** 919 PDFs in 14 Haeusern dauerten lokal 32 s, der zweite Lauf
meldete nur noch Duplikate.

**Mietvertraege den Einheiten zuordnen.** Der Ordner-Upload haengt die
Vertraege nur an das Haus. Ein zweiter Upload mit `--unit-id` aendert daran
nichts, denn die Dateien sind dann Duplikate. Zugeordnet wird deshalb danach,
ueber die Dokument-ID. Enthaelt der Dateiname die Einheitennummer
(`Mietvertrag_RH-01-WE-001.pdf`), sieht das so aus:

```bash
immojump units list "$ID" --all --fields id,extern_id > units.json
immojump documents list --immobilie-id "$ID" --search Mietvertrag_ --all --fields id,dateiname > vertraege.json
jq -r --slurpfile u units.json '
  .[] | (.dateiname | sub("^Mietvertrag_"; "") | sub("\\.pdf$"; "")) as $nr
      | ($u[0][] | select(.extern_id == $nr) | .id) as $unit
      | "\(.id) \($unit)"' vertraege.json \
| while read -r dok unit; do immojump documents set-unit "$dok" --unit-id "$unit" --fields id >/dev/null || echo "FEHLER $dok"; done
```

**Erwartung:** 93 Vertraege in 1,8 s zugeordnet. Kontrolle:
`immojump documents list --immobilie-id "$ID" --unit-id <unit-id> --fields dateiname`.
Wer die Einheit schon vor dem Upload kennt, laedt einzelne Vertraege direkt
mit `--unit-id` hoch, aber nicht zusaetzlich im Ordner-Upload.

- **Die Duplikat-Erkennung gilt fuer die ganze Organisation, nicht nur fuer
  das Haus.** Liegt dieselbe Datei schon an einem anderen Objekt, wird sie hier
  nicht angehaengt. Der Eintrag unter `duplicates` nennt das Objekt
  (`existingPropertyId`). Gehoert die Datei wirklich an beide Objekte (z. B.
  eine Teilungserklaerung fuer zwei Haeuser), lade sie mit `--allow-duplicate`
  erneut hoch.

**Erwartung:** 919 PDFs in 14 Haeusern dauerten lokal 32 s, der zweite Lauf
meldete nur noch Duplikate.

**Mietvertrag an die Einheit haengen.** Enthaelt der Dateiname die
Einheitennummer:

```bash
for f in datenraum/RH-01/Mietvertraege/*.pdf; do
  nr=$(basename "$f" .pdf | sed 's/^Mietvertrag_//')          # RH-01-WE-001
  unit=$(immojump units list "$ID" --extern-id "$nr" --limit 1 --fields items.id | jq -r '.items[0].id // empty')
  [ -n "$unit" ] && immojump documents upload "$f" --immobilie-id "$ID" --unit-id "$unit" --category mietvertrag
done
```

Bei vielen Vertraegen laedst du die Einheiten einmal mit
`units list "$ID" --all --fields id,extern_id` und ordnest lokal zu, statt je
Datei die Liste abzufragen. Ein schon hochgeladenes Dokument ordnest du
nachtraeglich mit `documents set-unit <dok-id> --unit-id <unit-id>` zu.

---

## 5. Analysieren

```bash
immojump documents analyze-all --immobilie-id "$ID" --fields listed,queued
immojump documents list --immobilie-id "$ID" --analysis-status queued     --limit 1 --fields total
immojump documents list --immobilie-id "$ID" --analysis-status processing --limit 1 --fields total
immojump documents list --immobilie-id "$ID" --analysis-status failed     --all --fields id,dateiname,analysis_error
```

- **Kontingent:** Jede Analyse zaehlt auf das KI-Kontingent des Plans. Vor dem
  Start rechnest du die Zahl der Dokumente gegen das Kontingent und nennst sie
  dem Menschen.
- Scans ohne Textschicht brauchen OCR und dauern laenger.
- Bei Exit 7 laeuft `analyze-all` spaeter erneut. Bereits angestossene
  Dokumente werden uebersprungen.
- Die Analyse aendert keine Einheiten, die ein Mensch oder dein Import angelegt
  hat. Abweichungen (z. B. eine andere Miete im Mietvertrag) speichert sie als
  Vorschlag am Dokument.

---

## 6. Eigene Werte je Einheit

```bash
immojump fields list --model unit --fields definitions.id,definitions.name,definitions.type   # erst nachsehen
immojump fields create --model unit --name Marktmiete --type number          # nur wenn noch nicht da; Admin
immojump fields create --model unit --name Sanierungsbedarf --type text
# werte.ndjson: {"extern_id":"RH-01-WE-001","values":{"Marktmiete":13.5,"Sanierungsbedarf":"Bad, Fenster"}}
immojump units fields-set "$ID" --file werte.ndjson
immojump units fields-get "$ID" --fields extern_id,values
```

- Vorhandene Felder wiederverwenden: Ein Name ist je Organisation eindeutig,
  ein zweites `fields create` mit gleichem Namen endet mit Exit 9.
- Ein Feld je Kennzahl, mit fester Einheit im Namen, wenn noetig
  (z. B. „Marktmiete €/m²“).
- `null` leert einen Wert.
- Unbekannte Einheitennummern bricht die CLI ab, bevor etwas gesendet wird.

---

## 7. Auswerten ueber das Portfolio

Alle Rezepte lesen ueber `units list-org`. Das kostet einen Aufruf je 500
Einheiten. Gruppiert wird immer nach `immobilie_id`, denn zwei Haeuser koennen
gleich heissen. Der Name dient nur der Anzeige. Gerundet wird erst am Ende.

```bash
# Leerstand je Haus
immojump units list-org --vacant --all --fields immobilie_id,immobilie_name \
  | jq 'group_by(.immobilie_id) | map({haus: .[0].immobilie_name, id: .[0].immobilie_id, leer: length})'

# Ist-Miete p.a. (alle Einheiten inkl. Garagen und Stellplaetze), Wohn-/Gewerbeflaeche und €/m²
immojump units list-org --all --fields immobilie_id,immobilie_name,type,livingspace,ist_rent \
  | jq 'group_by(.immobilie_id)
        | map({haus: .[0].immobilie_name, id: .[0].immobilie_id,
               einheiten: length,
               miete_pa: (map(.ist_rent // 0) | add * 12),
               flaeche: (map(select(.type == "wohnen" or .type == "gewerbe") | .livingspace // 0) | add // 0),
               miete_flaeche_monat: (map(select(.type == "wohnen" or .type == "gewerbe") | .ist_rent // 0) | add // 0)})
        | map({haus, id, einheiten,
               ist_miete_pa: (.miete_pa * 100 | round / 100),
               flaeche_qm: (.flaeche | round),
               eur_qm: (if .flaeche > 0 then (.miete_flaeche_monat / .flaeche * 100 | round / 100) else null end)})'

# Mietsteigerungspotenzial: Soll minus Ist je Haus (p.a.)
immojump units list-org --all --fields immobilie_id,immobilie_name,ist_rent,soll_rent \
  | jq 'group_by(.immobilie_id) | map({haus: .[0].immobilie_name, id: .[0].immobilie_id,
        potenzial_pa: (map((.soll_rent // 0) - (.ist_rent // 0)) | add * 12 | round)})'
```

**Kaufpreisfaktor je Haus:**
1. Hole den Kaufpreis mit `immobilien get <id> --exclude units,dokumente --fields daten.kaufpreis`.
2. Teile ihn durch `ist_miete_pa` aus dem zweiten Rezept. Darin stecken alle
   Ist-Mieten, auch Garagen und Stellplaetze.

Fuer €/m² zaehlen nur Wohn- und Gewerbeflaechen, mit deren Miete.

Kennzahlen rechnet heute nur die Web-Oberflaeche. Per CLI rechnest du sie
selbst und schreibst Ergebnisse, die bleiben sollen, als benutzerdefinierte
Felder oder Notiz zurueck.

---

## 8. Haeufige Fehlerbilder

| Symptom | Ursache | Abhilfe |
|---|---|---|
| Exit 11, „Unbekannte Felder: …“ | Spalte mit falschem Namen, z. B. `wohnflaeche` | Feldnamen der Tabelle oben; die Meldung nennt den gemeinten Namen |
| Exit 11, „… ist keine Zahl“ | Dezimalkomma in NDJSON | Zahl mit Punkt oder CSV mit `--decimal-comma` |
| Exit 11, doppelte `extern_id` | dieselbe Nummer zweimal in der Datei | Nummernschema pruefen (Stop-Regel in Abschnitt 0) |
| Exit 9 / 409 | eine `extern_id` ist in diesem Haus schon vergeben | mit `units list --extern-id` nachsehen |
| Anzahl der Einheiten stimmt nicht | Datei je Haus falsch aufgeteilt | Gegenpruefung aus Abschnitt 3 |
| Exit 7 | Rate Limit | spaeter erneut starten; Importe und Lesen wiederholen sich selbst |
| Upload `failed` mit Zeitueberschreitung | sehr grosse Scans mit OCR | kleinere Stapel (`--batch-files 3`) |
| Plan-Fehler beim Anlegen eines Hauses | Planlimit aktiver Objekte erreicht | ein Haus = ein Objekt; sonst Plan pruefen |
