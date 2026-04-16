---
description: "Generiert rechtskonforme Vermieterbescheinigungen nach Paragraph 19 BMG in 30 Sekunden statt 15 Minuten. Nutze diesen Skill wenn ein Mieter einzieht und die Bescheinigung fuers Einwohnermeldeamt braucht (Pflicht innerhalb 2 Wochen nach Einzug)."
---

# Vermieterbescheinigung -- Generator nach §19 BMG

## Wann nutzen

- Neuer Mieter zieht ein und benoetigt Vermieterbescheinigung fuer die Meldebehoerde
- Pflicht des Vermieters: innerhalb von 2 Wochen nach Einzug (§19 Abs. 3 BMG)
- Statt 15-20 Minuten manueller Arbeit: automatisch in 30 Sekunden generieren
- Serienproduktion bei mehreren gleichzeitigen Einzuegen

---

## Inputs

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `tenant_name` | String | Ja | Vollstaendiger Name des Mieters (Vor- und Nachname) |
| `tenant_date_of_birth` | String | Nein | Geburtsdatum des Mieters (fuer eindeutige Zuordnung) |
| `move_in_date` | String | Ja | Einzugsdatum |
| `move_out_date` | String | Nein | Auszugsdatum (nur bei Auszugsbestaetigung) |
| `property_address` | Object | Ja | Adresse der Wohnung: Strasse, Hausnummer, PLZ, Ort |
| `unit_identifier` | String | Nein | Wohnungsbezeichnung (z.B. "3. OG links", "WE 04") |
| `landlord_name` | String | Ja | Name des Vermieters (Person oder Gesellschaft) |
| `landlord_address` | Object | Nein | Anschrift des Vermieters: Strasse, Hausnummer, PLZ, Ort |
| `additional_tenants` | Array | Nein | Weitere einziehende Personen (Name, Geburtsdatum) |
| `confirmation_type` | String | Nein | Art: "einzug" (Default) oder "auszug" |
| `document_date` | String | Nein | Ausstellungsdatum (Default: aktuelles Datum) |

---

## Auftrag

Du bist ein erfahrener Immobilienverwalter, der Vermieterbescheinigungen nach §19 Bundesmeldegesetz (BMG) erstellt. Generiere eine vollstaendige, rechtskonforme Bescheinigung, die alle gesetzlich vorgeschriebenen Angaben enthaelt und direkt beim Einwohnermeldeamt vorgelegt werden kann. Die Bescheinigung muss druckfertig formatiert sein.

---

## Strategie

1. **Gesetzliche Pflichtangaben pruefen (§19 Abs. 4 BMG)** -- Folgende Angaben sind gesetzlich vorgeschrieben:
   - Name und Anschrift des Wohnungsgebers (Vermieter)
   - Art der Bestaetigung: Einzug oder Auszug
   - Einzugsdatum (bzw. Auszugsdatum)
   - Anschrift der Wohnung
   - Name der meldepflichtigen Person(en)

2. **Fristen pruefen** -- Gesetzliche Vorgaben:
   - Vermieter muss die Bescheinigung innerhalb von 2 Wochen nach Einzug ausstellen (§19 Abs. 3 BMG)
   - Mieter muss sich innerhalb von 2 Wochen nach Einzug beim Einwohnermeldeamt anmelden (§17 Abs. 1 BMG)
   - Bussgeld bei Versaeumnis: bis zu 1.000 EUR fuer den Vermieter (§54 Abs. 3 BMG)
   - Bussgeld bei Gefaelligkeitsbestaetigung (Scheinanmeldung): bis zu 50.000 EUR (§54 Abs. 3 BMG)

3. **Zusaetzliche Bewohner erfassen** -- Wenn mehrere Personen einziehen:
   - Jede Person einzeln mit Name auffuehren
   - Geburtsdatum wenn verfuegbar
   - Familienverhaeltnis ist NICHT erforderlich
   - Kinder unter 16 Jahren werden von den Eltern mitangemeldet

4. **Auszugsbestaetigung** -- Falls es sich um einen Auszug handelt:
   - Auszugsdatum angeben
   - Formulierung anpassen ("ist ausgezogen" statt "ist eingezogen")
   - Bestaetigung dass die Wohnung geraeumt wurde

5. **Dokument formatieren** -- Druckfertig und behoerdentauglich:
   - Klare Struktur mit allen Pflichtfeldern
   - Platz fuer Datum und Unterschrift des Vermieters
   - DIN A4-kompatibel
   - Offizielle, sachliche Sprache

6. **Validierung** -- Alle Eingaben auf Plausibilitaet pruefen:
   - Einzugsdatum nicht in ferner Zukunft (maximal 2 Wochen voraus)
   - Einzugsdatum nicht mehr als 2 Wochen in der Vergangenheit (sonst Fristversaeumnis)
   - Adresse vollstaendig (Strasse, Hausnummer, PLZ, Ort)
   - Name des Mieters vollstaendig (Vor- und Nachname)

---

## Ausgabeformat

```json
{
  "report_type": "vermieterbescheinigung",
  "report_date": "2026-04-15",
  "confirmation_type": "einzug",
  "deadline_check": {
    "move_in_date": "2026-04-01",
    "deadline_date": "2026-04-15",
    "within_deadline": true,
    "days_remaining": 0,
    "status": "fristgerecht"
  },
  "document": {
    "title": "Wohnungsgeberbestaetigung nach §19 Abs. 3 Bundesmeldegesetz (BMG)",
    "content": "WOHNUNGSGEBERBESTAETIGUNG\nnach §19 Abs. 3 Bundesmeldegesetz (BMG)\n\n---\n\n1. Name und Anschrift des Wohnungsgebers (Vermieters):\n\n   Max Mustermann\n   Vermieterstr. 1\n   10115 Berlin\n\n2. Hiermit wird der EINZUG folgender Person(en) bestaetigt:\n\n   Name: Erika Musterfrau\n   Geburtsdatum: 15.03.1990\n\n3. Einzugsdatum: 01.04.2026\n\n4. Anschrift der Wohnung:\n\n   Musterstr. 12\n   3. OG links (WE 04)\n   10115 Berlin\n\n5. Weitere in die Wohnung einziehende Personen:\n\n   - Thomas Musterfrau, geb. 22.07.1988\n\n---\n\nIch bestaetige die Richtigkeit der vorstehenden Angaben.\n\nHinweis: Wer als Wohnungsgeber eine Wohnungsgeberbestaetigung nicht, nicht richtig oder nicht rechtzeitig ausstellt, handelt ordnungswidrig (§54 Abs. 3 BMG). Die Ordnungswidrigkeit kann mit einer Geldbusse bis zu 1.000 EUR geahndet werden. Wer eine Wohnungsanschrift fuer eine Anmeldung zur Verfuegung stellt, obwohl ein tatsaechlicher Bezug der Wohnung weder stattgefunden hat noch beabsichtigt ist, handelt ordnungswidrig und kann mit einer Geldbusse bis zu 50.000 EUR belegt werden.\n\n\nOrt, Datum: Berlin, 15.04.2026\n\n\n___________________________________\nUnterschrift des Wohnungsgebers"
  },
  "document_structured": {
    "landlord": {
      "name": "Max Mustermann",
      "street": "Vermieterstr. 1",
      "zip": "10115",
      "city": "Berlin"
    },
    "confirmation_type": "einzug",
    "primary_tenant": {
      "name": "Erika Musterfrau",
      "date_of_birth": "1990-03-15"
    },
    "additional_tenants": [
      {
        "name": "Thomas Musterfrau",
        "date_of_birth": "1988-07-22"
      }
    ],
    "move_in_date": "2026-04-01",
    "move_out_date": null,
    "property": {
      "street": "Musterstr. 12",
      "unit": "3. OG links (WE 04)",
      "zip": "10115",
      "city": "Berlin"
    },
    "document_date": "2026-04-15",
    "signature_required": true
  },
  "warnings": [],
  "confidence_score": 0.98,
  "data_gaps": []
}
```

---

## Qualitaetspruefung

- [ ] Name des Wohnungsgebers (Vermieters) angegeben
- [ ] Anschrift des Wohnungsgebers angegeben
- [ ] Name der meldepflichtigen Person vollstaendig (Vor- und Nachname)
- [ ] Einzugsdatum (bzw. Auszugsdatum) angegeben
- [ ] Anschrift der Wohnung vollstaendig (Strasse, Hausnummer, PLZ, Ort)
- [ ] 2-Wochen-Frist nach Einzug eingehalten (oder Warnung ausgegeben)
- [ ] Weitere einziehende Personen aufgefuehrt (falls vorhanden)
- [ ] Hinweis auf Bussgeld-Regelung enthalten
- [ ] Platz fuer Datum und Unterschrift vorhanden
- [ ] Art der Bestaetigung korrekt (Einzug vs. Auszug)

---

## Warnsignale

| Signal | Bedeutung | Empfohlene Aktion |
|--------|-----------|-------------------|
| 2-Wochen-Frist abgelaufen | Ordnungswidrigkeit, Bussgeld bis 1.000 EUR | Sofort ausstellen, Fristversaeumnis ist bereits eingetreten |
| Einzugsdatum > 2 Wochen in der Zukunft | Ungewoehnlich, moeglicherweise Fehleingabe | Einzugsdatum verifizieren |
| Keine Wohnungsbezeichnung | Zuordnung bei MFH unklar | Etage und Lage ergaenzen |
| Vermieter = juristische Person | Vertretungsberechtigung erforderlich | Geschaeftsfuehrer/Prokurist als Unterzeichner benennen |
| Scheinanmeldung vermutet | Straftat, Bussgeld bis 50.000 EUR | Bescheinigung NICHT ausstellen, Vorgang pruefen |

---

## Bei fehlenden Daten

- Wenn Geburtsdatum des Mieters fehlt: Bescheinigung ohne Geburtsdatum erstellen (ist empfohlen, aber nicht gesetzlich vorgeschrieben als Pflichtangabe der Bescheinigung). Hinweis: Meldebehoerde wird Geburtsdatum vom Mieter direkt erfragen.
- Wenn Vermieteranschrift fehlt: Platzhalter "[Anschrift des Vermieters]" einsetzen, Hinweis dass die Angabe gesetzlich erforderlich ist.
- Wenn Wohnungsbezeichnung fehlt: Nur Strasse und Hausnummer verwenden, Empfehlung zur Ergaenzung geben.
- Wenn Ausstellungsdatum fehlt: Aktuelles Datum verwenden.
- Wenn unklar ob Einzug oder Auszug: "Einzug" als Standard annehmen, nachfragen.
- Alle Luecken im Feld `data_gaps` dokumentieren.

---

## Konfidenz-Bewertung

| Score | Bedeutung |
|-------|-----------|
| 0.9 - 1.0 | Alle Pflichtangaben vorhanden, Frist eingehalten, Dokument vollstaendig |
| 0.7 - 0.9 | Pflichtangaben vorhanden, aber optionale Felder fehlen (z.B. Geburtsdatum) |
| 0.5 - 0.7 | Einzelne Pflichtangaben fehlen (z.B. Vermieteranschrift) |
| < 0.5 | Wesentliche Pflichtangaben fehlen, Dokument nicht verwendbar |

Faktoren die den Score senken:
- Fehlende Vermieteranschrift (-0.20)
- Fehlender Mietername (-0.30 -- Dokument nicht erstellbar)
- Fehlendes Einzugsdatum (-0.30 -- Dokument nicht erstellbar)
- Fehlende Wohnungsadresse (-0.30 -- Dokument nicht erstellbar)
- Frist abgelaufen (-0.05 -- Dokument erstellen, aber warnen)
- Fehlende Wohnungsbezeichnung bei MFH (-0.05)

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- §19 BMG, §17 BMG, §54 BMG: Meldepflicht und Wohnungsgeberbestaetigung
- `knowledge/checklisten.md` -- Checkliste Mieterwechsel / Einzug
- `skills/inserat-generator/SKILL.md` -- Vermietungsprozess: nach Vertragsabschluss folgt Vermieterbescheinigung
- `skills/wochen-jourfixe/SKILL.md` -- Einzuege und Fristen im Wochen-Report tracken
