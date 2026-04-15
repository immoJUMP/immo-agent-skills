# Expose-Parser

> Eckdaten aus Makler-Exposes strukturiert extrahieren -- Kaufpreis, Flaechen, Mieteinnahmen, Zustand und Besonderheiten auf einen Blick, fertig fuer den Deal-Screener.

---

## Wann nutzen?

- Bei neuen Angeboten: Expose schnell auf die wesentlichen Kennzahlen reduzieren
- Bei Massenscreening: Mehrere Exposes gleichzeitig auswerten und vergleichen
- Vor der Besichtigung: Alle relevanten Daten strukturiert verfuegbar haben
- Fuer die Bierdeckel-Kalkulation: Daten direkt in den Deal-Screener uebergeben

---

## Inputs

Stelle folgende Informationen bereit:

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| `expose` | Ja | Expose-Dokument (PDF, Scan, Link, Freitext) |
| `ankaufskriterien` | Optional | Eigene Ankaufskriterien zum Sofort-Abgleich |
| `marktdaten` | Optional | Lokale Vergleichsdaten (Mietspiegel, Bodenrichtwerte, Angebotspreise) |

---

## Auftrag

Du bist ein erfahrener Immobilienanalyst mit Fokus auf deutsche Wohnimmobilien-Investments. Extrahiere aus dem uebergebenen Expose alle investitionsrelevanten Daten in ein strukturiertes Format. Berechne Standard-Kennzahlen. Identifiziere Besonderheiten, Risiken und fehlende Informationen. Die Ausgabe muss direkt als Input fuer den Deal-Screener verwendbar sein.

---

## Strategie

1. **Kerndaten extrahieren**
   - **Kaufpreis:** Angebotspreis in EUR
   - **Wohnflaeche:** Gesamtwohnflaeche in qm
   - **Nutzflaeche:** Gewerbeflaeche, Lagerflaeche in qm (falls vorhanden)
   - **Grundstuecksflaeche:** in qm
   - **Baujahr:** Urspruengliches Baujahr
   - **Anzahl Einheiten:** Wohnungen, Gewerbeeinheiten, Garagen/Stellplaetze
   - **Geschosse:** Anzahl Stockwerke
   - **Dachform:** Flachdach, Satteldach, Walmdach (relevant fuer Sanierungskosten)

2. **Mietdaten extrahieren**
   - **Ist-Miete (Jahresnettokaltmiete):** Aktuelle Mieteinnahmen p.a.
   - **Soll-Miete:** Mieteinnahmen bei Vollvermietung p.a. (falls angegeben)
   - **Miete pro qm:** Durchschnittliche Kaltmiete EUR/qm
   - **Leerstandsquote:** Aktueller Leerstand in Prozent
   - **Mietliste:** Falls im Expose enthalten, an mietlisten-parser weiterleiten

3. **Zustand und Ausstattung erfassen**
   - **Gesamtzustand:** Erstbezug, neuwertig, gepflegt, renovierungsbeduerftig, sanierungsbeduerftig
   - **Letzte Sanierung:** Jahr und Umfang (Dach, Fassade, Heizung, Fenster, Leitungen)
   - **Heizungstyp:** Gas-Zentralheizung, Oelheizung, Fernwaerme, Waermepumpe, Etagenheizung
   - **Energiekennwert:** kWh/(m2a)
   - **Energieeffizienzklasse:** A+ bis H
   - **Energieausweis-Typ:** Bedarfsausweis oder Verbrauchsausweis
   - **Fenster:** Material, Verglasung (Einfach, Doppel, Dreifach), Baujahr
   - **Dach:** Zustand, letzte Sanierung
   - **Fassade:** Daemmung vorhanden, WDVS, Klinker, Putz
   - **Leitungen:** Steigleitungen erneuert (Wasser, Abwasser, Elektro)
   - **Aufzug:** Vorhanden/nicht vorhanden, Baujahr

4. **Finanzielle Rahmendaten**
   - **Hausgeld:** Monatlich/jaehrlich (bei WEG)
   - **Instandhaltungsruecklage:** Hoehe (gesamt und pro Einheit/qm)
   - **Nicht umlagefaehige Kosten:** Verwaltung, Instandhaltung
   - **Grundsteuer:** Jaehrlicher Betrag (falls angegeben)
   - **Maklercourtage:** Prozent und Betrag
   - **Kaufnebenkosten-Schaetzung:** Grunderwerbsteuer (je Bundesland), Notar, Grundbuch

5. **Besonderheiten identifizieren**
   - **Erbbaurecht:** Erbbauzins, Restlaufzeit, Vertragskonditionen
   - **Denkmalschutz:** Eingetragenes Denkmal, Auflagen, steuerliche Vorteile (§7i EStG)
   - **Baulasten:** Oeffentlich-rechtliche Verpflichtungen
   - **Wohnungsbindung:** Sozialbindung, Mietobergrenze, Restlaufzeit
   - **Niesbrauch / Wohnrecht:** Bestehende Rechte Dritter
   - **Teilungserklaerung:** Auffaelligkeiten (z.B. eingeschraenktes Sondereigentum)
   - **Geplante Massnahmen:** Beschlossene Sonderumlagen, anstehende Sanierungen
   - **Altlasten:** Hinweise auf Bodenkontamination
   - **Mischnutzung:** Wohnen + Gewerbe, Aufteilung

6. **Standard-Kennzahlen berechnen**
   - **Kaufpreisfaktor:** Kaufpreis / Jahresnettokaltmiete (Ist)
   - **Bruttomietrendite:** Jahresnettokaltmiete / Kaufpreis x 100
   - **Kaufpreis pro qm:** Kaufpreis / Wohnflaeche
   - **Kaufpreis pro Einheit:** Kaufpreis / Anzahl Wohneinheiten
   - **Soll-Rendite:** Jahresnettokaltmiete (Soll) / Kaufpreis x 100
   - **Hausgeld-Ratio:** Hausgeld / Gesamtmiete (Anteil nicht umlagefaehig)

7. **Informationsluecken identifizieren**
   - Welche Daten fehlen im Expose?
   - Was muss vor einer Kaufentscheidung noch geklaert werden?
   - Welche Unterlagen muessen angefordert werden?

---

## Ausgabeformat

```json
{
  "expose_data": {
    "processing_date": "2025-11-15",
    "source": "Expose ABC Makler, Objekt-ID 12345",
    "confidence": 0.88,
    "core_data": {
      "asking_price": 580000.00,
      "address": {
        "street": "Musterstrasse 12",
        "zip": "40210",
        "city": "Duesseldorf",
        "district": "Stadtmitte",
        "state": "Nordrhein-Westfalen"
      },
      "total_living_area_sqm": 425.00,
      "total_commercial_area_sqm": 0.00,
      "total_usable_area_sqm": 425.00,
      "land_area_sqm": 310.00,
      "construction_year": 1965,
      "floors": 3,
      "roof_type": "satteldach",
      "units": {
        "residential": 6,
        "commercial": 0,
        "garages": 2,
        "parking_outdoor": 0,
        "total": 8
      }
    },
    "rental_data": {
      "actual_annual_net_cold_rent": 41040.00,
      "potential_annual_net_cold_rent": 46650.00,
      "average_rent_per_sqm": 8.05,
      "vacancy_rate_percent": 12.5,
      "vacant_units": 1,
      "rent_roll_available": true,
      "rent_roll_date": "2025-01-01"
    },
    "condition": {
      "overall_condition": "gepflegt",
      "last_renovation_year": 2015,
      "last_renovation_scope": "Dach, Fassadendaemmung WDVS",
      "heating_type": "gas_zentralheizung",
      "heating_year": 2010,
      "energy_certificate": {
        "type": "bedarfsausweis",
        "value_kwh": 142.0,
        "efficiency_class": "E",
        "valid_until": "2030-05-15"
      },
      "windows": {
        "material": "kunststoff",
        "glazing": "doppelverglasung",
        "year": 2005
      },
      "roof": {
        "condition": "gut",
        "last_renovation": 2015
      },
      "facade": {
        "insulation": true,
        "type": "wdvs",
        "year": 2015
      },
      "pipes": {
        "water_renewed": true,
        "water_year": 2008,
        "sewage_renewed": false,
        "electrical_renewed": true,
        "electrical_year": 2010
      },
      "elevator": false
    },
    "financial": {
      "hausgeld_monthly": null,
      "hausgeld_annual": null,
      "maintenance_reserve_total": null,
      "maintenance_reserve_per_sqm": null,
      "non_allocable_costs_annual": null,
      "property_tax_annual": 890.00,
      "broker_commission_percent": 3.57,
      "broker_commission_amount": 20706.00,
      "estimated_acquisition_costs": {
        "property_transfer_tax_rate": 0.065,
        "property_transfer_tax": 37700.00,
        "notary_fees": 8700.00,
        "land_registry_fees": 2900.00,
        "broker_commission": 20706.00,
        "total_acquisition_costs": 70006.00,
        "total_acquisition_costs_percent": 12.07
      }
    },
    "special_features": {
      "hereditary_building_right": {
        "applicable": false
      },
      "monument_protection": {
        "applicable": false
      },
      "building_encumbrances": {
        "mentioned": false,
        "details": null,
        "note": "Baulastenverzeichnis anfordern"
      },
      "social_housing_obligation": {
        "applicable": false
      },
      "usufruct_or_right_of_residence": {
        "applicable": false
      },
      "planned_measures": {
        "mentioned": false,
        "details": null
      },
      "contamination": {
        "mentioned": false,
        "note": "Altlastenkataster pruefen"
      },
      "mixed_use": false,
      "other_notes": []
    },
    "calculated_metrics": {
      "purchase_price_factor": 14.13,
      "gross_rental_yield_actual_percent": 7.08,
      "gross_rental_yield_potential_percent": 8.04,
      "price_per_sqm": 1364.71,
      "price_per_unit": 96666.67,
      "price_per_residential_unit": 96666.67
    },
    "missing_information": [
      {
        "item": "hausgeld",
        "importance": "hoch",
        "note": "Hausgeld/Wirtschaftsplan nicht im Expose enthalten -- anfordern"
      },
      {
        "item": "instandhaltungsruecklage",
        "importance": "hoch",
        "note": "Hoehe der Instandhaltungsruecklage unbekannt"
      },
      {
        "item": "teilungserklaerung",
        "importance": "hoch",
        "note": "Teilungserklaerung fuer Due Diligence erforderlich"
      },
      {
        "item": "grundbuchauszug",
        "importance": "hoch",
        "note": "Belastungen in Abt. II und III pruefen"
      },
      {
        "item": "abwasserleitungen",
        "importance": "mittel",
        "note": "Zustand der Abwasserleitungen nicht erwaehnt -- ggf. Kamerabefahrung"
      },
      {
        "item": "protokolle_eigentuemerversammlungen",
        "importance": "mittel",
        "note": "Letzte 3 Jahre anfordern fuer Beschlusscheck"
      }
    ],
    "deal_screener_ready": true,
    "deal_screener_input": {
      "purchase_price": 580000.00,
      "living_area_sqm": 425.00,
      "construction_year": 1965,
      "units_residential": 6,
      "annual_net_cold_rent_actual": 41040.00,
      "annual_net_cold_rent_potential": 46650.00,
      "vacancy_rate": 0.125,
      "condition": "gepflegt",
      "heating_type": "gas_zentralheizung",
      "energy_value_kwh": 142.0,
      "broker_commission_percent": 3.57,
      "property_transfer_tax_rate": 0.065,
      "property_tax_annual": 890.00,
      "state": "Nordrhein-Westfalen"
    }
  }
}
```

---

## Qualitaetspruefung

Vor der Ausgabe pruefen:

- [ ] Alle im Expose erkennbaren Daten sind extrahiert
- [ ] Kaufpreis und Flaechen sind korrekt uebernommen (keine Einheitenfehler)
- [ ] Kennzahlen sind rechnerisch korrekt (Rendite, Faktor, Preis/qm)
- [ ] Kaufnebenkosten-Schaetzung verwendet den korrekten GrESt-Satz fuer das Bundesland
- [ ] Besonderheiten sind vollstaendig erfasst (Erbbaurecht, Denkmal, Baulasten)
- [ ] Fehlende Informationen sind klar benannt mit Wichtigkeit
- [ ] Deal-Screener-Input ist vollstaendig und konsistent
- [ ] Bruttomietrendite basiert auf Ist-Miete (nicht Soll-Miete)

---

## Warnsignale

| Signal | Bedeutung | Aktion |
|--------|-----------|--------|
| Rendite > 10% | Entweder sehr guter Deal oder versteckte Probleme | Besonders kritisch pruefen |
| Rendite < 4% | In den meisten Maerkten nicht cashflow-positiv | Nur bei Wertsteigerungsstrategie |
| Baujahr vor 1950 ohne Sanierung | Erheblicher Sanierungsstau wahrscheinlich | Sanierungskosten einplanen |
| Energieklasse F-H | Hohe Heizkosten, GEG-Sanierungspflicht moeglich | Energetische Sanierung kalkulieren |
| Erbbaurecht | Erbbauzins reduziert Rendite, Vertragsende beachten | Erbbaurechtsvertrag anfordern |
| Denkmalschutz | Einschraenkungen bei Sanierung, aber steuerliche Vorteile | Denkmalschutzbescheid anfordern |
| Hohe Maklercourtage (> 5%) | Ueberdurchschnittliche Ankaufsnebenkosten | Verhandeln oder einkalkulieren |
| Leerstand > 15% | Vermietungsprobleme oder Sanierungsstau | Ursache klaeren vor Angebot |
| Expose ohne Mietliste | Wichtigste Kalkulationsgrundlage fehlt | Mietliste anfordern |
| Keine Angabe Hausgeld | Bei WEG: Kritische Kosteninformation fehlt | Wirtschaftsplan anfordern |
| Viele Sanierungen gleichzeitig noetig | Investitionsstau = hoher Kapitalbedarf | Sanierungsfahrplan erstellen |
| Expose-Fotos zeigen andere Realitaet als Text | Zustandsbeschreibung moeglicherweise geschoent | Besichtigung mit Checkliste |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Jahresnettokaltmiete | Aus Miete/qm x Flaeche x 12 schaetzen (wenn Miete/qm angegeben) |
| Baujahr | Aus Architekturstil und Fotos schaetzen, als "geschaetzt" markieren |
| Grundstuecksflaeche | Als "nicht angegeben" markieren, fuer Bewertung noetig |
| Hausgeld | Als "nicht angegeben" markieren, vor Angebot anfordern |
| Maklercourtage | Landesueblichen Satz ansetzen, als "Annahme" markieren |
| Energiekennwert | Als "nicht angegeben" markieren, Energieausweis anfordern |
| Sanierungshistorie | Als "nicht angegeben" markieren, vor Ort pruefen |
| Grunderwerbsteuer-Satz | Nach Bundesland automatisch ansetzen |

**Grunderwerbsteuersaetze nach Bundesland (Stand 2025):**

| Bundesland | Satz |
|------------|------|
| Baden-Wuerttemberg | 5,0% |
| Bayern | 3,5% |
| Berlin | 6,0% |
| Brandenburg | 6,5% |
| Bremen | 5,0% |
| Hamburg | 5,5% |
| Hessen | 6,0% |
| Mecklenburg-Vorpommern | 6,0% |
| Niedersachsen | 5,0% |
| Nordrhein-Westfalen | 6,5% |
| Rheinland-Pfalz | 5,0% |
| Saarland | 6,5% |
| Sachsen | 5,5% |
| Sachsen-Anhalt | 5,0% |
| Schleswig-Holstein | 6,5% |
| Thueringen | 5,0% |

---

## Konfidenz-Bewertung

| Stufe | Wert | Bedeutung |
|-------|------|-----------|
| Hoch | >= 0.90 | Professionelles Expose, alle Kerndaten klar angegeben |
| Mittel | 0.70 - 0.89 | Die meisten Daten vorhanden, einzelne Werte geschaetzt |
| Niedrig | 0.50 - 0.69 | Minimales Expose, viele Werte fehlen oder sind unklar |
| Unsicher | < 0.50 | Expose nicht auswertbar (zu wenig Informationen, unleserlich) |

---

## Verwandte Wissensdatenbanken

- `knowledge/kalkulationsformeln.md` -- Renditekennzahlen, Kaufpreisfaktoren
- `knowledge/marktbenchmarks.md` -- Vergleichswerte nach Lage und Baujahr
- `knowledge/risikobewertung.md` -- Risiko-Scoring-Framework
- `skills/ankauf/deal-screener.md` -- Naechster Schritt: Deal-Screening mit extrahierten Daten
- `skills/ankauf/bierdeckel-kalkulation.md` -- Schnellbewertung auf Basis der Expose-Daten
- `skills/dokumente/dokument-klassifizierer.md` -- Allgemeine Dokumentklassifizierung
- `skills/dokumente/mietlisten-parser.md` -- Mietliste aus Expose weiterverarbeiten
