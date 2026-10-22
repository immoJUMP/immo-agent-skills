# Portfolio-Ankauf mit immoJUMP als Backend

Referenz zu `immojump-cli`. Durchgespielt mit einem synthetischen Datenraum:
14 Haeuser, 912 Einheiten, 919 PDFs. Die Werte unter „Erwartung“ stammen aus
diesem Lauf.

**Drei Muster gelten in jedem Block unten:**

1. `set -o pipefail` steht am Anfang. Ohne diese Zeile verschluckt `| jq` den
   Exit-Code der CLI. Ein gescheiterter Aufruf saehe dann aus wie
   „nichts gefunden“.
2. CLI-Ausgaben gehen erst in eine Datei, dann wird der Exit-Code geprueft,
   erst danach rechnet `jq`. Leere oder unvollstaendige Daten sind ein Fehler,
   kein Ergebnis.
3. Jeder schreibende Aufruf traegt `--allow read,write`. Die Shell jedes
   Aufrufs ist neu, ein frueheres `export IMMOJUMP_ALLOW` gilt dort nicht mehr.

---

## 0. Inventur und Freigabe, bevor geschrieben wird

```bash
find datenraum -type f ! -name '.*' | wc -l                       # alle Dateien, die der Upload senden wuerde
find datenraum -type f -iname '*.pdf' | wc -l                     # davon PDFs
find datenraum -maxdepth 1 -mindepth 1 -type d | wc -l            # Haeuser (ein Ordner je Haus)
```

Halte fest:
- wie viele Haeuser es sind,
- wie viele Einheiten je Haus laut Mieterliste,
- welche Dokumentarten vorliegen (Mietvertraege je Einheit, Grundbuch,
  Teilungserklaerung, Energieausweis, Expose, Scans ohne Text),
- wie die Verkaeufer-Nummer aussieht (z. B. `RH-01-WE-001`).

**Freigabe einholen.** Der Datenraum enthaelt personenbezogene Daten von
Mietern. Bevor du etwas hochlaedst, nenne dem Menschen Umfang und Ziel und
warte auf sein ausdrueckliches Go. Er bestaetigt dabei auch, dass NDA bzw.
Datenraum-Bedingungen das Hochladen in immoJUMP erlauben.

**Stop-Regel:** Hat eine Einheit keine eindeutige Nummer, bilde vor dem Import
eine stabile Nummer aus Haus, Eingang, Geschoss und Lage, z. B.
`RH-01-A-EG-li`. Sie darf sich zwischen zwei Laeufen nie aendern.

---

## 1. Haeuser anlegen (wiederholbar)

Vorher pruefen, ob das Haus schon existiert. Gesucht wird ueber die eigene
Nummer in `daten.extern_id`:

```bash
set -o pipefail
immojump immobilien list --fields id,name,daten.extern_id > haeuser.json || { echo "Liste nicht lesbar - NICHTS anlegen"; exit 1; }
treffer=$(jq '[.[] | select(.daten.extern_id == "RH-01")] | length' haeuser.json) || exit 1
if [ "$treffer" -gt 0 ]; then echo "RH-01 existiert schon - nicht neu anlegen"; exit 0; fi

immojump immobilien create --allow read,write --type MFH \
  --set name='Mehrfamilienhaus Rosengasse 136-150, Koeln' \
  --set daten.adresse='Rosengasse 136-150, 50968 Koeln' \
  --set daten.extern_id=RH-01 \
  --set daten.kaufpreis=15220000 \
  --fields id
```

- Lege `daten.extern_id` an jedem Haus an, mit einem gemeinsamen Praefix je
  Ankauf (hier `RH-`). Daran erkennt der naechste Lauf das Haus, und die
  Auswertung in Abschnitt 7 grenzt den Ankauf vom uebrigen Bestand ab.
- **Endet `create` mit Exit 8** (Zeitueberschreitung), kann das Haus trotzdem
  angelegt sein. Fuehre erst die Existenzpruefung erneut aus, dann ggf. `create`.
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
| Soll-/Marktmiete laut Verkaeufer | `soll_rent` | **unbekannt: `null` schicken**, siehe unten |
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
- **NDJSON:** genau ein JSON-Objekt je Zeile, Zahlen als JSON-Zahlen mit
  Punkt. Das Backend lehnt `"62,5"` ab, weil es nicht raten will, ob „1.250“
  1,25 oder 1250 heisst.
- **CSV:** Kopfzeile = Feldnamen, deutsche Zahlen mit
  `--decimal-comma --delimiter ';'`. Die CLI prueft streng und bricht mit
  Zeile und Spalte ab, statt zu raten.
- **Soll-Miete:** Fehlt sie beim **Anlegen**, setzt das Backend die Ist-Miete
  ein. Dann laesst sich spaeter nicht mehr erkennen, dass sie unbekannt war.
  Schicke deshalb `"soll_rent": null`, wenn der Verkaeufer keine nennt. Das
  geht nur in NDJSON/JSON, denn eine leere CSV-Zelle gilt als „nicht
  geschickt“. Bei einem **Update** aendert der Import nur mitgeschickte Felder.
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

Erst der Trockenlauf, dann der Vergleich mit der Datei, erst danach schreiben:

```bash
set -o pipefail
zeilen=$(jq -n '[inputs] | length' rh-01.ndjson) || { echo "rh-01.ndjson ist kein gueltiges NDJSON"; exit 1; }
immojump units import "$ID" --allow read,write --file rh-01.ndjson --dry-run > probe.json \
  || { echo "Trockenlauf gescheitert, nichts importiert"; exit 1; }
jq --argjson n "$zeilen" -e '(.created + .updated + .unchanged) == $n' probe.json >/dev/null \
  || { echo "Trockenlauf deckt nicht alle $zeilen Zeilen ab"; exit 1; }

immojump units import "$ID" --allow read,write --file rh-01.ndjson > import.json
rc=$?
jq '{created, updated, unchanged, placeholder_removed, batches, complete, ambiguous_retry}' import.json
if [ "$rc" -ne 0 ] || [ "$(jq -r '.complete' import.json)" != "true" ]; then echo "Import unvollstaendig (Exit $rc)"; exit 1; fi
```

**Erwartung:**
- Beim ersten Lauf: `created` = Zeilen der Datei, `placeholder_removed: true`.
- Beim zweiten Lauf mit derselben Datei: `unchanged` = Zeilen, nichts angelegt.
- 912 Einheiten in 14 Haeusern dauerten lokal unter einer Sekunde.

Steht `ambiguous_retry: true` im Ergebnis, wurde ein Stapel nach einem
Netzfehler wiederholt. Dann koennen die Zaehler ungenau sein, und die
Gegenpruefung unten entscheidet.

**Gegenpruefung je Haus** (Anzahl und Ist-Miete gegen die Quelle):

```bash
set -o pipefail
immojump units list "$ID" --all --fields ist_rent > ist.json || exit 1
jq '{einheiten: length, ist_miete_monat: ((map(.ist_rent // 0) | add // 0) * 100 | round / 100)}' ist.json
```

**Scheitert ein Stapel (Exit 11):**
- Die Fehlerzeile nennt `line`, `index` und die Meldung.
- Stapel davor sind gespeichert (`committed_batches`, und auf stdout eine
  Summe mit `complete: false`).
- Korrigiere die Datei und importiere sie **ganz** erneut. Gespeicherte Zeilen
  kommen als `unchanged` zurueck.

---

## 4. Datenraum hochladen

Nur nach dem Go aus Abschnitt 0.

```bash
set -o pipefail
immojump documents upload --allow read,write datenraum/RH-01 --recursive --immobilie-id "$ID" > upload.json
rc=$?
jq '{uploaded: (.uploaded | length), duplicates: (.duplicates | length), failed, empty}' upload.json
if [ "$rc" -ne 0 ]; then echo "Upload nicht vollstaendig (Exit $rc) - siehe failed/empty bzw. stderr"; exit "$rc"; fi
```

- Die CLI laedt in Stapeln von 10 Dateien bzw. 25 MB und berichtet je Datei
  (`uploaded`, `duplicates`, `failed`, `empty`).
- Exit 0 heisst: alles ist angekommen.
- Exit 1 heisst: Teile sind gescheitert oder leer. Lade nur die Dateien aus
  `failed` und `empty` erneut. Eintraege mit `may_exist: true` sind
  moeglicherweise schon gespeichert; ein erneuter Lauf ohne
  `--allow-duplicate` ist trotzdem sicher.
- Exit 4, 6 oder 7 heisst: Der Lauf wurde abgebrochen (Anmeldung, Recht,
  Rate Limit). Erst die Ursache klaeren.
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
set -o pipefail
immojump units list "$ID" --all --fields id,extern_id > units.json || exit 1
immojump documents list --immobilie-id "$ID" --search Mietvertrag --all --fields id,dateiname > dokumente.json || exit 1

# 1. Zuordnung planen, nichts schreiben. Jeder Vertrag braucht GENAU einen Treffer.
jq -c --slurpfile u units.json '
  .[] | select(.dateiname | test("^Mietvertrag_.*\\.pdf$"; "i"))
      | (.dateiname | sub("^Mietvertrag_"; ""; "i") | sub("\\.pdf$"; ""; "i")) as $nr
      | {dok: .id, datei: .dateiname, nr: $nr, units: [$u[0][] | select(.extern_id == $nr) | .id]}' \
  dokumente.json > plan.ndjson || exit 1
echo "Dokumente mit 'Mietvertrag' im Namen: $(jq length dokumente.json), im Plan: $(jq -n '[inputs] | length' plan.ndjson)"
jq -c 'select((.units | length) != 1)' plan.ndjson > ungeklaert.ndjson || exit 1
if [ -s ungeklaert.ndjson ]; then echo "Ohne eindeutige Einheit - erst klaeren, NICHTS geschrieben:"; cat ungeklaert.ndjson; exit 1; fi

# 2. Pilot mit drei Vertraegen; erst nach Pruefung der Rest (dieselbe Schleife ohne head -3).
jq -r '"\(.dok) \(.units[0])"' plan.ndjson | head -3 > lauf.txt
: > fehler.txt
while read -r dok unit; do
  immojump documents set-unit "$dok" --allow read,write --unit-id "$unit" --fields id >/dev/null
  rc=$?
  if [ "$rc" -eq 0 ]; then continue; fi
  case "$rc" in 3|4|6|7) echo "Abbruch: Exit $rc (Konfiguration, Anmeldung, Recht oder Rate Limit)"; exit "$rc";; esac
  echo "FEHLER $dok (Exit $rc)" >> fehler.txt
done < lauf.txt
if [ -s fehler.txt ]; then cat fehler.txt; exit 1; fi
```

Weichen Dateinamen ab (Leerzeichen, `Nachtrag_Mietvertrag_…`), fehlen sie im
Plan. Die Zeile „im Plan“ zeigt das. Melde dem Menschen die Differenz, statt
sie zu ignorieren. Kontrolle:
`immojump documents list --immobilie-id "$ID" --unit-id <unit-id> --fields dateiname`.
**Erwartung:** 93 Vertraege in 1,8 s zugeordnet.

Wer die Einheit schon vor dem Upload kennt, laedt einzelne Vertraege direkt
mit `--unit-id` hoch und nimmt sie **nicht** zusaetzlich in den Ordner-Upload.

---

## 5. Analysieren

**Jede Analyse verbraucht KI-Kontingent des Plans.**
- Der Profi-Plan hat 100 Analysen im Monat. 919 Dokumente waeren also rund
  neun Monate Kontingent.
- `analyze-all` ist ein schreibender Befehl, den eine `read,write`-Policy
  nicht sperrt.

Deshalb gilt:

1. Zaehle je Haus genau die Auswahl, die du analysieren willst, und zeige sie
   dem Menschen:
   ```bash
   set -o pipefail
   immojump documents list --immobilie-id "$ID" --analysis-status not_started --limit 1 --fields total
   ```
   Frisch hochgeladene Dokumente haben noch **keine Kategorie**; die vergibt
   erst die Analyse oder `--category` beim Upload. Ein Filter
   `--category mietvertrag` zaehlt deshalb vorher 0. Nutze ihn nur, wenn du
   beim Upload kategorisiert hast, dann aber beim Zaehlen UND beim Start.
2. **Warte auf eine ausdrueckliche Freigabe** fuer genau diese Auswahl (Haus,
   Anzahl) und nenne dabei den Kontingentverbrauch. Erst ein Pilot-Haus, dann
   der Rest, jeweils freigegeben.
3. Starten, mit **derselben** Auswahl, und kompakt auswerten. `failed` und
   `skipped` nicht wegfiltern:
   ```bash
   set -o pipefail
   immojump documents analyze-all --allow read,write --immobilie-id "$ID" > analyse.json
   rc=$?
   jq '{listed, queued: (.queued | length), skipped: (.skipped | length), failed}' analyse.json
   if [ "$rc" -ne 0 ]; then echo "Analyse-Start nicht vollstaendig (Exit $rc)"; fi
   immojump documents list --immobilie-id "$ID" --analysis-status processing --limit 1 --fields total
   immojump documents list --immobilie-id "$ID" --analysis-status failed     --all --fields id,dateiname,analysis_error
   ```

- Exit 7 heisst Rate Limit: Die uebrigen stehen unter `skipped`, spaeter
  erneut starten. Ein anderer Exit ungleich 0 (z. B. erschoepftes
  Kontingent): stoppen und den Menschen fragen.
- `failed` aus `analyze-all` sind Dokumente, deren Start scheiterte; sie stehen
  weiter auf `not_started`. `--analysis-status failed` sind gestartete
  Analysen, die spaeter scheiterten. Beides getrennt melden.
- Scans ohne Textschicht brauchen OCR und dauern laenger.
- Die Analyse aendert keine Einheiten, die ein Mensch oder dein Import angelegt
  hat (alle mit `extern_id`). Abweichungen, z. B. eine andere Miete im
  Mietvertrag, speichert sie als Vorschlag am Dokument.

---

## 6. Eigene Werte je Einheit

```bash
set -o pipefail
immojump fields list --model unit --fields definitions.id,definitions.name,definitions.type   # erst nachsehen
immojump fields create --allow read,write --model unit --name "Marktmiete EUR/qm" --type number   # nur wenn noch nicht da; Admin
immojump fields create --allow read,write --model unit --name Sanierungsbedarf --type text
# werte.ndjson: {"extern_id":"RH-01-WE-001","values":{"Marktmiete EUR/qm":13.5,"Sanierungsbedarf":"Bad, Fenster"}}
immojump units fields-set "$ID" --allow read,write --file werte.ndjson
immojump units fields-get "$ID" --fields extern_id,values
```

- Vorhandene Felder wiederverwenden: Ein Name ist je Organisation eindeutig,
  ein zweites `fields create` mit gleichem Namen endet mit Exit 9.
- Ein Feld je Kennzahl, die Masseinheit im Namen (EUR/qm, EUR/Monat).
- `null` leert einen Wert.
- Unbekannte Einheitennummern bricht die CLI ab, bevor etwas gesendet wird.

---

## 7. Auswerten ueber das Portfolio

Zuerst den Ankauf abgrenzen: In einer bestehenden Organisation liefert
`units list-org` auch den Altbestand. Die IDs der Ankaufshaeuser kommen ueber
das Praefix aus Abschnitt 1. Ohne vollstaendige Abgrenzung wird nicht
gerechnet:

```bash
set -o pipefail
immojump immobilien list --fields id,daten.extern_id > alle.json || exit 1
jq '[.[] | select((.daten.extern_id // "") | startswith("RH-")) | .id]' alle.json > ankauf_ids.json || exit 1
anzahl=$(jq length ankauf_ids.json) || exit 1
if [ "$anzahl" -ne 14 ]; then echo "Erwartet 14 Ankaufshaeuser, gefunden $anzahl - erst klaeren"; exit 1; fi
immojump units list-org --all --fields immobilie_id,immobilie_name,type,livingspace,ist_rent,soll_rent > org.json || exit 1
jq --slurpfile ids ankauf_ids.json 'map(select(.immobilie_id as $i | $ids[0] | index($i)))' org.json > einheiten.json || exit 1
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

# Theoretisches Mietpotenzial p.a.: Neuvermietung, Steigerung und Uebermiete getrennt, unbekannte Soll-Mieten gezaehlt
jq 'group_by(.immobilie_id)
    | map({haus: .[0].immobilie_name, id: .[0].immobilie_id,
           neuvermietung_pa: (map(select((.ist_rent // 0) == 0 and .soll_rent != null) | .soll_rent) | add // 0 | . * 12 | round),
           steigerung_vermietet_pa: (map(select((.ist_rent // 0) > 0 and .soll_rent != null and .soll_rent > .ist_rent)
                                       | .soll_rent - .ist_rent) | add // 0 | . * 12 | round),
           uebermiete_pa: (map(select((.ist_rent // 0) > 0 and .soll_rent != null and .soll_rent < .ist_rent)
                                       | .ist_rent - .soll_rent) | add // 0 | . * 12 | round),
           soll_unbekannt: (map(select(.soll_rent == null)) | length)})' einheiten.json
```

**Einordnung, bevor du Zahlen weitergibst:**
- „Ohne erfasste Ist-Miete“ ist noch kein Leerstand. Auch mietfreie
  Ueberlassung oder eine fehlende Angabe ergibt 0. Bestaetige Leerstand an der
  Mieterliste (`note`) oder beim Verkaeufer.
- EUR/qm rechnet nur vermietete Wohn- bzw. Gewerbeflaeche, getrennt. Leere
  Flaeche zaehlt nicht mit, sonst wirkt die Miete je m² zu niedrig.
- Das Mietpotenzial ist theoretisch:
  - Die Soll-Miete ist die Angabe des Verkaeufers und nicht gegen Mietspiegel,
    Kappungsgrenze oder Mietpreisbremse geprueft.
  - `uebermiete_pa` ist ein Risiko bei Neuvermietung, kein Potenzial.
  - Nenne `soll_unbekannt` immer mit. Die Zahl sagt nur etwas, wenn der Import
    unbekannte Soll-Mieten als `null` geschickt hat (Abschnitt 2).

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
| Exit 11, „… ist keine Zahl“ | Dezimalkomma als Text in NDJSON (`"62,5"`) oder unklare Zahl in CSV | Zahl mit Punkt; CSV mit `--decimal-comma` |
| Exit 2, „… genau ein JSON-…“ | ungueltiges NDJSON, z. B. `62,5` ohne Anfuehrungszeichen, zwei Objekte in einer Zeile oder zusaetzliche Schluessel neben `units` | Datei reparieren; `jq -n '[inputs] \| length' datei` prueft vorab |
| Exit 11, doppelte `extern_id` oder `id` | dieselbe Nummer zweimal in der Datei | Nummernschema pruefen (Stop-Regel in Abschnitt 0) |
| Exit 9 / 409 | eine `extern_id` ist in diesem Haus schon vergeben | mit `units list --extern-id` nachsehen |
| Exit 5 | Haus, Einheit oder Dokument nicht gefunden (oder keine Sicht darauf) | ID pruefen, nicht blind wiederholen |
| Anzahl der Einheiten stimmt nicht | Datei je Haus falsch aufgeteilt | Gegenpruefung aus Abschnitt 3 |
| Exit 7 | Rate Limit | spaeter erneut starten; Importe und Lesen wiederholen sich selbst |
| Exit 8 bei einem Schreibbefehl | Zeitueberschreitung, Ergebnis offen | erst nachsehen (Liste, Existenzpruefung), dann ggf. wiederholen |
| Upload `failed` mit „zu gross“ | Datei ueber `--max-file-mb` (250 MB) | Datei aufteilen oder komprimieren |
| Plan-Fehler beim Anlegen eines Hauses | Planlimit aktiver Objekte erreicht | ein Haus = ein Objekt; sonst Plan pruefen |
