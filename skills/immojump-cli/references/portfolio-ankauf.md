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

Vorher pruefen, ob das Haus schon existiert. Gesucht wird ueber die eigene
Nummer in `daten.extern_id`:

```bash
immojump immobilien list --fields id,name,daten.extern_id \
  | jq -c '.[] | select(.daten.extern_id == "RH-01")'      # Treffer = schon da, NICHT neu anlegen

immojump immobilien create --type MFH \
  --set name='Mehrfamilienhaus Rosengasse 136-150, Koeln' \
  --set daten.adresse='Rosengasse 136-150, 50968 Koeln' \
  --set daten.extern_id=RH-01 \
  --set daten.kaufpreis=15220000 \
  --fields id
```

- Lege `daten.extern_id` an jedem Haus an, mit einem gemeinsamen Praefix je
  Ankauf (hier `RH-`). Daran erkennt der naechste Lauf das Haus, und die
  Auswertung in Abschnitt 7 grenzt den Ankauf vom uebrigen Bestand ab.
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
| Soll-/Marktmiete | `soll_rent` | beim ANLEGEN ohne Angabe = `ist_rent`; beim Update bleibt der alte Wert |
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
- **Update-Semantik:** Bei einer schon vorhandenen Einheit aendert der Import
  nur die mitgeschickten Felder. Wer nur `ist_rent` neu schickt, laesst
  `soll_rent` auf dem alten Wert.

Beispiel einer Zeile:

```json
{"extern_id":"RH-01-WE-001","einheit":"WE 001 EG links","type":"wohnen","livingspace":77.74,"rooms":3,"ist_rent":703.48,"soll_rent":856.19,"lease_start_date":"2012-05-10"}
```

---

## 3. Import mit Pruefpunkten

Erst der Trockenlauf, dann der Vergleich mit der Datei, erst danach schreiben:

```bash
zeilen=$(grep -c . rh-01.ndjson)
probe=$(immojump units import "$ID" --file rh-01.ndjson --dry-run) || { echo "Trockenlauf gescheitert, nichts importiert"; exit 1; }
echo "$probe" | jq --argjson n "$zeilen" -e '(.created + .updated + .unchanged) == $n' >/dev/null \
  || { echo "Trockenlauf deckt nicht alle $zeilen Zeilen ab"; exit 1; }
immojump units import "$ID" --file rh-01.ndjson --fields created,updated,unchanged,placeholder_removed,batches
```

**Erwartung** beim ersten Lauf: `created` = Zeilen der Datei,
`placeholder_removed: true`. Beim zweiten Lauf mit derselben Datei:
`unchanged` = Zeilen, nichts angelegt. 912 Einheiten in 14 Haeusern dauerten
lokal unter einer Sekunde.

**Gegenpruefung je Haus** (Anzahl und Ist-Miete gegen die Quelle):

```bash
immojump units list "$ID" --all --fields ist_rent \
  | jq '{einheiten: length, ist_miete_monat: ((map(.ist_rent // 0) | add // 0) * 100 | round / 100)}'
```

**Scheitert ein Stapel (Exit 11):**
- Die Fehlerzeile nennt `line`, `index` und die Meldung.
- Stapel davor sind gespeichert (`committed_batches`).
- Korrigiere die Datei und importiere sie **ganz** erneut. Gespeicherte Zeilen
  kommen als `unchanged` zurueck.

---

## 4. Datenraum hochladen

```bash
immojump documents upload datenraum/RH-01 --recursive --immobilie-id "$ID" \
  | jq '{uploaded: (.uploaded | length), duplicates: (.duplicates | length), failed, empty}'
```

- Die CLI laedt in Stapeln von 10 Dateien bzw. 25 MB und berichtet je Datei
  (`uploaded`, `duplicates`, `failed`, `empty`).
- Exit 0 heisst: alles ist angekommen. Exit 1 heisst: Teile sind gescheitert
  oder leer, der Bericht steht trotzdem auf stdout. Pruefe `failed` und `empty`
  und lade nur diese Dateien erneut.
- Ein zweiter Lauf ist sicher: Schon Hochgeladenes erscheint unter
  `duplicates`.
- **Die Duplikat-Erkennung gilt fuer die ganze Organisation, nicht nur fuer
  das Haus.** Liegt dieselbe Datei schon an einem anderen Objekt, wird sie hier
  nicht angehaengt. Der Eintrag unter `duplicates` nennt das Objekt
  (`existingPropertyId`). Gehoert die Datei wirklich an beide Objekte (z. B.
  eine Teilungserklaerung fuer zwei Haeuser), lade **genau diese Datei** mit
  `--allow-duplicate` erneut hoch. Nie einen ganzen Ordner mit
  `--allow-duplicate`.

**Erwartung:** 919 PDFs in 14 Haeusern dauerten lokal 32 s, der zweite Lauf
meldete nur noch Duplikate.

### Mietvertraege den Einheiten zuordnen

Der Ordner-Upload haengt die Vertraege nur an das Haus. Ein zweiter Upload mit
`--unit-id` aendert daran nichts, denn die Dateien sind dann Duplikate.
Zugeordnet wird deshalb **nach** dem Upload, ueber die Dokument-ID, mit
`documents set-unit`. Enthaelt der Dateiname die Einheitennummer
(`Mietvertrag_RH-01-WE-001.pdf`):

```bash
immojump units list "$ID" --all --fields id,extern_id > units.json
immojump documents list --immobilie-id "$ID" --search Mietvertrag --all --fields id,dateiname > dokumente.json

# 1. Zuordnung planen, nichts schreiben. Jeder Vertrag braucht GENAU einen Treffer.
jq -c --slurpfile u units.json '
  .[] | select(.dateiname | test("^Mietvertrag_.*\\.pdf$"; "i"))
      | (.dateiname | sub("^Mietvertrag_"; ""; "i") | sub("\\.pdf$"; ""; "i")) as $nr
      | {dok: .id, datei: .dateiname, nr: $nr, units: [$u[0][] | select(.extern_id == $nr) | .id]}' \
  dokumente.json > plan.ndjson
jq -c 'select((.units | length) != 1)' plan.ndjson     # muss leer sein, sonst: klaeren, NICHT schreiben

# 2. Pilot mit drei Vertraegen, dann pruefen; erst danach der Rest.
jq -r 'select((.units | length) == 1) | "\(.dok) \(.units[0])"' plan.ndjson | head -3 > pilot.txt
: > fehler.txt
while read -r dok unit; do
  immojump documents set-unit "$dok" --unit-id "$unit" --fields id >/dev/null
  rc=$?
  if [ "$rc" -eq 0 ]; then continue; fi
  if [ "$rc" -eq 6 ]; then echo "Keine Berechtigung - Abbruch"; exit 6; fi
  echo "FEHLER $dok (Exit $rc)" >> fehler.txt
done < pilot.txt
if [ -s fehler.txt ]; then cat fehler.txt; exit 1; fi
```

Fuer den Rest dieselbe Schleife ohne `head -3`. Am Ende muss `fehler.txt` leer
sein, sonst ist der Lauf gescheitert und du meldest die Liste. Kontrolle:
`immojump documents list --immobilie-id "$ID" --unit-id <unit-id> --fields dateiname`.
**Erwartung:** 93 Vertraege in 1,8 s zugeordnet.

Wer die Einheit schon vor dem Upload kennt, laedt einzelne Vertraege direkt
mit `--unit-id` hoch und nimmt sie **nicht** zusaetzlich in den Ordner-Upload.

---

## 5. Analysieren

**Jede Analyse verbraucht KI-Kontingent des Plans.** Der Profi-Plan hat 100
Analysen im Monat. `analyze-all` ist ein schreibender Befehl, den
`IMMOJUMP_ALLOW=read,write` nicht sperrt. Deshalb gilt:

1. Zaehle je Haus, was analysiert wuerde, und zeige es dem Menschen:
   ```bash
   immojump documents list --immobilie-id "$ID" --analysis-status not_started --limit 1 --fields total
   ```
2. **Warte auf eine ausdrueckliche Freigabe** fuer genau diese Auswahl
   (Haus, Dokumentart, Anzahl). Erst ein Pilot-Haus, dann der Rest, jeweils
   freigegeben.
3. Starten und kompakt auswerten. `failed` und `skipped` nicht wegfiltern:
   ```bash
   immojump documents analyze-all --immobilie-id "$ID" \
     | jq '{listed, queued: (.queued | length), skipped: (.skipped | length), failed}'
   immojump documents list --immobilie-id "$ID" --analysis-status queued     --limit 1 --fields total
   immojump documents list --immobilie-id "$ID" --analysis-status processing --limit 1 --fields total
   immojump documents list --immobilie-id "$ID" --analysis-status failed     --all --fields id,dateiname,analysis_error
   ```

- `failed` aus `analyze-all` sind Dokumente, deren Start scheiterte; sie stehen
  weiter auf `not_started`. `--analysis-status failed` sind gestartete
  Analysen, die spaeter scheiterten. Beides getrennt melden.
- Scans ohne Textschicht brauchen OCR und dauern laenger.
- Bei Exit 7 laeuft `analyze-all` spaeter erneut. Bereits angestossene
  Dokumente werden uebersprungen.
- Die Analyse aendert keine Einheiten, die ein Mensch oder dein Import angelegt
  hat (alle mit `extern_id`). Abweichungen, z. B. eine andere Miete im
  Mietvertrag, speichert sie als Vorschlag am Dokument.

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

Zuerst den Ankauf abgrenzen: In einer bestehenden Organisation liefert
`units list-org` auch den Altbestand. Die IDs der Ankaufshaeuser kommen ueber
das Praefix aus Abschnitt 1:

```bash
immojump immobilien list --fields id,daten.extern_id \
  | jq '[.[] | select((.daten.extern_id // "") | startswith("RH-")) | .id]' > ankauf_ids.json
immojump units list-org --all --fields immobilie_id,immobilie_name,type,livingspace,ist_rent,soll_rent \
  | jq --slurpfile ids ankauf_ids.json 'map(select(.immobilie_id as $i | $ids[0] | index($i)))' > einheiten.json
```

Alle Rezepte lesen `einheiten.json`. Gruppiert wird nach `immobilie_id`, denn
zwei Haeuser koennen gleich heissen; der Name dient nur der Anzeige. Gerundet
wird erst am Ende.

```bash
# Wohnungen und Gewerbe ohne erfasste Ist-Miete je Haus (Kandidaten fuer Leerstand)
jq 'map(select((.type == "wohnen" or .type == "gewerbe") and ((.ist_rent // 0) == 0)))
    | group_by(.immobilie_id)
    | map({haus: .[0].immobilie_name, id: .[0].immobilie_id, ohne_ist_miete: length,
           flaeche_qm: (map(.livingspace // 0) | add | round)})' einheiten.json

# Ist-Miete p.a. (alle Einheiten inkl. Garagen und Stellplaetze) und EUR/qm der VERMIETETEN Flaeche, getrennt nach Nutzung
jq 'group_by(.immobilie_id)
    | map(. as $h | {haus: $h[0].immobilie_name, id: $h[0].immobilie_id, einheiten: length,
          ist_miete_pa: (($h | map(.ist_rent // 0) | add) * 12 * 100 | round / 100),
          eur_qm: ([ "wohnen", "gewerbe" ] | map(. as $t
            | ($h | map(select(.type == $t and (.ist_rent // 0) > 0 and (.livingspace // 0) > 0))) as $v
            | {key: $t, value: (if ($v | length) > 0
                 then (($v | map(.ist_rent) | add) / ($v | map(.livingspace) | add) * 100 | round / 100)
                 else null end)}) | from_entries)})' einheiten.json

# Theoretisches Mietpotenzial p.a., zwei Zahlen, unbekannte Soll-Mieten gezaehlt statt als 0 gerechnet
jq 'group_by(.immobilie_id)
    | map({haus: .[0].immobilie_name, id: .[0].immobilie_id,
           neuvermietung_pa: (map(select((.ist_rent // 0) == 0 and .soll_rent != null) | .soll_rent) | add // 0 | . * 12 | round),
           anpassung_vermietet_pa: (map(select((.ist_rent // 0) > 0 and .soll_rent != null) | .soll_rent - .ist_rent) | add // 0 | . * 12 | round),
           soll_unbekannt: (map(select(.soll_rent == null)) | length)})' einheiten.json
```

**Einordnung, bevor du Zahlen weitergibst:**
- „Ohne erfasste Ist-Miete“ ist noch kein Leerstand. Auch mietfreie
  Ueberlassung oder eine fehlende Angabe ergibt 0. Bestaetige Leerstand an der
  Mieterliste (`note`) oder beim Verkaeufer.
- EUR/qm rechnet nur vermietete Wohn- bzw. Gewerbeflaeche, getrennt. Leere
  Flaeche zaehlt nicht mit, sonst wirkt die Miete je m² zu niedrig.
- Das Mietpotenzial ist theoretisch. Die Soll-Miete ist die Angabe des
  Verkaeufers und nicht gegen Mietspiegel, Kappungsgrenze oder
  Mietpreisbremse geprueft. Nenne `soll_unbekannt` immer mit.

**Kaufpreisfaktor je Haus:**
1. Hole den Kaufpreis mit `immobilien get <id> --exclude units,dokumente --fields daten.kaufpreis`.
2. Teile ihn durch die ungerundete Jahresmiete aller Einheiten
   (`ist_miete_pa` oben, auf Cent genau). Ist sie 0, gibt es keinen Faktor.
   Melde das, statt durch 0 zu teilen.

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
