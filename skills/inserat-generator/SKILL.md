---
description: "Erstellt professionelle, rechtskonforme Vermietungsinserate fuer ImmoScout24/Immowelt mit allen GEG-Pflichtangaben und AGG-konformen Formulierungen. Nutze diesen Skill wenn du eine leerstehende Wohnung inserieren oder einen Expose-Text erstellen willst."
---

# Inserat-Generator -- Vermietungsinserat erstellen

## Wann nutzen

- Professionelles Vermietungsinserat fuer leerstehende Wohnungen erstellen
- ImmoScout24- und Immowelt-kompatibles Format generieren
- Pflichtangaben nach GEG (Gebaeudeenergiegesetz) sicherstellen
- AGG-konforme Formulierungen garantieren (keine Diskriminierung)
- Mietpreisbremse-konforme Mietfestsetzung pruefen
- Expose-Text fuer Besichtigungsunterlagen erstellen

---

## Inputs

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `property_address` | String | Ja | Vollstaendige Adresse (Strasse, PLZ, Ort) |
| `unit_identifier` | String | Ja | Wohnungsbezeichnung (z.B. "3. OG links") |
| `area_sqm` | Number | Ja | Wohnflaeche in qm |
| `rooms` | Number | Ja | Zimmeranzahl (z.B. 2.5 fuer 2,5 Zimmer) |
| `cold_rent_eur` | Number | Ja | Nettokaltmiete in EUR |
| `utilities_prepayment_eur` | Number | Ja | Nebenkostenvorauszahlung in EUR |
| `heating_costs_eur` | Number | Nein | Heizkosten (separat oder in NK enthalten) |
| `deposit_eur` | Number | Nein | Kaution in EUR (max. 3 Monatskaltmieten) |
| `available_from` | String | Ja | Verfuegbar ab (Datum) |
| `energy_certificate` | Object | Ja | Energieausweis-Daten: Typ (Verbrauch/Bedarf), Kennwert (kWh/qm*a), Energietraeger, Baujahr, Energieeffizienzklasse |
| `construction_year` | Number | Ja | Baujahr des Gebaeudes |
| `floor` | String | Nein | Etage (z.B. "3. OG", "EG", "DG") |
| `features` | Array | Nein | Ausstattungsmerkmale (Balkon, Einbaukueche, Aufzug, Keller, etc.) |
| `condition` | String | Nein | Zustand (erstbezug, saniert, renoviert, gepflegt, unrenoviert) |
| `renovation_details` | Array | Nein | Durchgefuehrte Renovierungen/Modernisierungen (Massnahme, Jahr) |
| `parking` | Object | Nein | Stellplatz: Typ (Tiefgarage, Stellplatz, Garage), Kosten |
| `pet_policy` | String | Nein | Haustierregelung (erlaubt, Kleintiere erlaubt, nicht erlaubt, nach Absprache) |
| `photos` | Array | Nein | Verfuegbare Fotos (Beschreibung/Dateiname) |
| `mietpreisbremse_active` | Boolean | Nein | Gilt Mietpreisbremse im Gebiet? |
| `previous_rent_eur` | Number | Nein | Vormiete (relevant bei Mietpreisbremse) |
| `landlord_contact` | Object | Nein | Kontaktdaten fuer Anfragen |

---

## Auftrag

Du bist ein erfahrener Immobilienvermarkter, der professionelle, rechtskonforme Vermietungsinserate fuer den deutschen Wohnungsmarkt erstellt. Generiere ein Inserat, das alle gesetzlichen Pflichtangaben enthaelt (GEG/EnEV, AGG), auf den grossen Portalen (ImmoScout24, Immowelt) veroeffentlicht werden kann und die Wohnung sachlich und ansprechend praesentiert. Vermeide uebertriebene Superlative und jede Form von Diskriminierung.

---

## Strategie

1. **Pflichtangaben nach GEG pruefen** -- Folgende Energieausweis-Daten MUESSEN im Inserat stehen (§87 GEG, ehemals EnEV §16a):
   - Art des Energieausweises: Verbrauchsausweis oder Bedarfsausweis
   - Energiekennwert in kWh/(qm*a)
   - Wesentlicher Energietraeger (z.B. Gas, Fernwaerme, Oel, Waermepumpe)
   - Baujahr des Gebaeudes
   - Energieeffizienzklasse (A+ bis H)
   - Bussgeld bei Verstoss: bis zu 15.000 EUR (§108 GEG)

2. **Mietpreisbremse pruefen (§556d BGB)** -- Wenn Mietpreisbremse aktiv:
   - Zulaessige Miete: maximal ortsbuebliche Vergleichsmiete + 10%
   - Ausnahmen pruefen:
     - Vormiete war hoeher (§556e BGB): bisherige Hoehe darf beibehalten werden
     - Neubau/Erstvermietung (§556f BGB): Mietpreisbremse gilt nicht
     - Umfassende Modernisierung: Mietpreisbremse gilt nicht
   - Wenn Mietpreisbremse greift: vorvertragliche Auskunftspflicht beachten (§556g BGB)
   - Hinweis im Inserat nicht erforderlich, aber interne Pruefung dokumentieren

3. **Kaution pruefen** -- Maximal 3 Monatsnettokaltmieten (§551 BGB):
   - Berechnung: 3 x Nettokaltmiete (ohne Nebenkosten)
   - Ratenzahlung: Mieter darf in 3 Monatsraten zahlen (§551 Abs. 2 BGB)
   - Anlage auf Sparkonto mit ueblicher Verzinsung

4. **Wohnflaeche referenzieren** -- Angabe nach Wohnflaechenverordnung (WoFlV):
   - Vollflaechen: Raeume mit Deckenhoehe >= 2m
   - Teilflaechen: Raeume mit Deckenhoehe 1-2m (50% anrechenbar)
   - Balkone/Terrassen: 25% anrechenbar (maximal 50% bei besonderer Qualitaet)
   - Dachschraegen beachten
   - Hinweis: "Wohnflaeche ca. [X] qm" -- "ca." schuetzt bei Abweichungen bis 10%

5. **AGG-konforme Formulierung** -- Allgemeines Gleichbehandlungsgesetz beachten:
   - VERBOTEN: Formulierungen die nach Rasse, Geschlecht, Religion, Behinderung, Alter, sexueller Identitaet, ethnischer Herkunft diskriminieren
   - VERBOTEN: "nur fuer Deutsche", "keine Auslaender", "nur fuer Paare", "keine Kinder", "nur fuer Berufstaetige"
   - ERLAUBT: sachliche Anforderungen ("Nichtraucher-Wohnung", "ruhiges Wohnumfeld")
   - ERLAUBT: Bonitaetsanforderungen ("Einkommensnachweis erforderlich", "Schufa-Auskunft")
   - ERLAUBT: Haustierregelung (sachlicher Bezug zur Wohnung)

6. **Inserat-Titel erstellen** -- Praegnant, sachlich, informativ:
   - Schema: [Zimmer]-Zimmer-Wohnung | [qm] qm | [Top-Feature] | [Lage/Stadtteil]
   - Maximal 80 Zeichen (Portal-Vorgabe)
   - Keine Grossbuchstaben-Bloecke, keine uebertriebenen Ausrufezeichen

7. **Beschreibungstext erstellen** -- Strukturierter Expose-Text:
   - **Objektbeschreibung**: Sachliche Beschreibung der Wohnung (Raumaufteilung, Besonderheiten, Zustand)
   - **Ausstattung**: Auflistung aller relevanten Merkmale
   - **Lage**: Stadtteil, Infrastruktur, Verkehrsanbindung (OEPNV, Autobahn), Nahversorgung
   - **Sonstiges**: Verfuegbarkeit, Besichtigungstermine, Bewerbungsunterlagen
   - Ton: professionell, sachlich, einladend -- keine leeren Superlative
   - Renovierungen/Modernisierungen hervorheben (Wertargument fuer die Miete)

8. **Portal-Datenfelder befuellen** -- Strukturierte Daten fuer ImmoScout24/Immowelt:
   - Alle Pflichtfelder der Portale abdecken
   - Kategorisierung: Wohnungstyp, Etage, Heizungsart
   - Kosten aufschluesseln: Kaltmiete, Nebenkosten, Heizkosten, Gesamtmiete, Kaution
   - Ausstattungs-Tags fuer Filter-Sichtbarkeit

9. **Foto-Empfehlung** -- Falls Fotos vorhanden oder zu erstellen:
   - Empfohlene Reihenfolge: Aussen > Wohnzimmer > Kueche > Bad > Schlafzimmer > Balkon > Keller/Stellplatz
   - Mindestens 8-12 Fotos fuer gute Portal-Performance
   - Keine persoenlichen Gegenstaende von Vormietern sichtbar
   - Helle, natuerliche Beleuchtung

10. **Compliance-Check** -- Abschliessende Pruefung:
    - Alle GEG-Pflichtangaben vorhanden?
    - AGG-Konformitaet sichergestellt?
    - Kaution innerhalb des gesetzlichen Rahmens?
    - Mietpreisbremse (falls aktiv) eingehalten?
    - Keine irrefuehrenden Angaben (Wohnflaeche, Zustand)?

---

## Ausgabeformat

```json
{
  "report_type": "inserat_generator",
  "report_date": "2026-04-15",
  "property": "Musterstr. 12, 10115 Berlin",
  "unit": "3. OG links",
  "listing_title": "3-Zimmer-Wohnung | 72 qm | Balkon | Berlin-Mitte",
  "listing_description": {
    "object_description": "Helle 3-Zimmer-Wohnung im 3. Obergeschoss eines gepflegten Altbaus (Baujahr 1965) in Berlin-Mitte. Die Wohnung verfuegt ueber einen grosszuegigen Grundriss mit separater Kueche, Wohnzimmer mit Zugang zum Suedbalkon, zwei Schlafzimmer und ein modernisiertes Bad mit Dusche und Wanne.\n\nDie Wohnung wurde 2024 umfassend renoviert: neue Bodenbelaege (Echtholzparkett im Wohn- und Schlafbereich), modernes Badezimmer, neue Elektrik und Malerarbeiten in allen Raeumen.",
    "features_text": "- 3 Zimmer, ca. 72 qm Wohnflaeche\n- Suedbalkon\n- Echtholzparkett (2024 verlegt)\n- Modernes Bad mit Dusche und Wanne (2024 saniert)\n- Separate Kueche\n- Kellerabteil\n- Fahrradstellplatz im Hof\n- Aufzug im Haus\n- Gas-Zentralheizung",
    "location_text": "Zentrale Lage in Berlin-Mitte mit hervorragender Infrastruktur. U-Bahnhof Rosenthaler Platz (U8) in 3 Gehminuten. Supermrkt, Baeckerei und Apotheke im Erdgeschoss. Volkspark am Weinbergsweg in 5 Minuten erreichbar. Schulen und Kitas in der naeheren Umgebung.",
    "other_text": "Verfuegbar ab 01.07.2026.\n\nFuer eine Besichtigung bitten wir um Ihre Bewerbung mit folgenden Unterlagen:\n- Einkommensnachweis (letzte 3 Gehaltsabrechnungen)\n- Schufa-Bonitaetsauskunft\n- Kopie des Personalausweises\n- Mieterselbstauskunft\n- Mietschuldenfreiheitsbescheinigung des Vorvermieters"
  },
  "portal_data": {
    "property_type": "wohnung",
    "apartment_type": "etagenwohnung",
    "marketing_type": "miete",
    "area_sqm": 72.50,
    "rooms": 3,
    "bedrooms": 2,
    "bathrooms": 1,
    "floor": 3,
    "total_floors": 5,
    "construction_year": 1965,
    "condition": "renoviert",
    "last_renovation_year": 2024,
    "heating_type": "zentralheizung",
    "fuel_type": "gas",
    "available_from": "2026-07-01",
    "pets_allowed": "nach_absprache"
  },
  "costs": {
    "cold_rent_eur": 620.00,
    "cold_rent_sqm_eur": 8.55,
    "utilities_prepayment_eur": 180.00,
    "heating_costs_included": true,
    "warm_rent_eur": 800.00,
    "deposit_eur": 1860.00,
    "deposit_months": 3,
    "parking_eur": null,
    "commission": "provisionsfrei"
  },
  "energy_certificate": {
    "type": "verbrauchsausweis",
    "value_kwh_sqm_year": 128.5,
    "energy_class": "D",
    "primary_fuel": "Erdgas",
    "construction_year": 1965,
    "certificate_valid_until": "2032-06-15"
  },
  "mietpreisbremse_check": {
    "active": true,
    "vergleichsmiete_sqm_eur": 8.50,
    "max_rent_sqm_eur": 9.35,
    "requested_rent_sqm_eur": 8.55,
    "compliant": true,
    "exemption_applicable": false,
    "previous_rent_eur": null
  },
  "agg_compliance": {
    "checked": true,
    "issues": [],
    "compliant": true
  },
  "geg_compliance": {
    "all_fields_present": true,
    "issues": [],
    "compliant": true
  },
  "photo_recommendation": {
    "minimum_photos": 8,
    "recommended_photos": [
      "Aussenansicht Gebaeude",
      "Wohnzimmer (Richtung Balkon)",
      "Wohnzimmer (Richtung Kueche)",
      "Kueche",
      "Schlafzimmer 1",
      "Schlafzimmer 2",
      "Bad",
      "Balkon",
      "Flur/Eingangsbereich",
      "Kellerabteil"
    ]
  },
  "confidence_score": 0.92,
  "data_gaps": []
}
```

---

## Qualitaetspruefung

- [ ] Alle GEG-Pflichtangaben vorhanden (Energieausweis-Typ, Kennwert, Energietraeger, Baujahr, Effizienzklasse)
- [ ] AGG-Konformitaet: kein diskriminierender Inhalt
- [ ] Kaution <= 3 Monatsnettokaltmieten
- [ ] Mietpreisbremse (falls aktiv): Miete <= Vergleichsmiete + 10%
- [ ] Wohnflaeche mit "ca." angegeben
- [ ] Inserat-Titel <= 80 Zeichen
- [ ] Beschreibungstext sachlich und frei von leeren Superlativen
- [ ] Kosten korrekt aufgeschluesselt (Kaltmiete + NK = Warmmiete)
- [ ] Verfuegbarkeitsdatum angegeben
- [ ] Bewerbungsunterlagen-Liste enthaelt nur zulaessige Anforderungen
- [ ] Keine Angaben die Rechtsstreitigkeiten provozieren (z.B. uebertriebene Flaechenangaben)

---

## Warnsignale

| Signal | Bedeutung | Empfohlene Aktion |
|--------|-----------|-------------------|
| Kein Energieausweis vorhanden | GEG-Verstoss, Bussgeld bis 15.000 EUR | Energieausweis erstellen lassen BEVOR inseriert wird |
| Miete > Vergleichsmiete + 10% bei aktiver Mietpreisbremse | Rechtswidrig, Mieter kann ruegen | Miete reduzieren oder Ausnahmetatbestand pruefen |
| Kaution > 3 Monatsmieten | Verstoss gegen §551 BGB | Kaution auf 3 Nettokaltmieten begrenzen |
| "Nur fuer ..." im Text | AGG-Verstoss moeglich | Diskriminierende Formulierung entfernen |
| Wohnflaeche weicht > 10% ab | Mietminderungsanspruch des Mieters | Wohnflaeche nachmessen lassen |
| Energieeffizienzklasse F-H | Hohe Nebenkosten schrecken Mieter ab | Energetische Sanierung erwaegen, transparent kommunizieren |

---

## Bei fehlenden Daten

- Wenn kein Energieausweis vorliegt: WARNUNG ausgeben. Inserat NICHT ohne Energiedaten erstellen. Platzhalter "[ENERGIEAUSWEIS ERFORDERLICH]" einsetzen.
- Wenn Nebenkosten unbekannt: Durchschnittswert (2,50-3,50 EUR/qm) als Schaetzung angeben und als Schaetzung kennzeichnen.
- Wenn Mietpreisbremse-Status unklar: Als aktiv annehmen und Mietpreisbremse-Check durchfuehren.
- Wenn Zustand nicht angegeben: Neutralen Begriff "gepflegt" verwenden, Hinweis dass Zustand vor Ort zu pruefen ist.
- Wenn keine Fotos vorhanden: Dringend empfehlen. Inserate mit Fotos erhalten 4x mehr Anfragen.
- Alle Luecken im Feld `data_gaps` dokumentieren.

---

## Konfidenz-Bewertung

| Score | Bedeutung |
|-------|-----------|
| 0.9 - 1.0 | Alle Pflichtdaten vorhanden, Energieausweis vollstaendig, Mietpreisbremse geprueft |
| 0.7 - 0.9 | Pflichtdaten vorhanden, aber optionale Angaben fehlen (z.B. Details zur Lage) |
| 0.5 - 0.7 | Energieausweis unvollstaendig oder Wohnflaeche unsicher |
| < 0.5 | Wesentliche Pflichtdaten fehlen, Inserat nicht veroeffentlichungsfaehig |

Faktoren die den Score senken:
- Fehlender Energieausweis (-0.30 -- Inserat nicht zulaessig)
- Fehlende Wohnflaeche (-0.20)
- Mietpreisbremse-Status unklar (-0.10)
- Keine Fotos (-0.05)
- Fehlende Lagebeschreibung (-0.05)

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- GEG/EnEV, §556d BGB Mietpreisbremse, §551 BGB Kaution, AGG
- `knowledge/marktbenchmarks.md` -- Marktmieten nach Lage und Baujahr fuer Mietfestsetzung
- `skills/mieterhoehung/SKILL.md` -- Mietpreisbremse-Pruefung bei Neuvermietung
- `skills/vermieterbescheinigung/SKILL.md` -- Nach erfolgreicher Vermietung: Bescheinigung erstellen
- `skills/expose-parser/SKILL.md` -- Expose-Daten aus vorhandenen Unterlagen extrahieren
