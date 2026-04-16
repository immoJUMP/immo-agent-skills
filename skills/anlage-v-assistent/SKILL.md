---
description: "Erstellt vorausgefuellte Anlage V (Einkunft aus Vermietung und Verpachtung) fuer die Steuererklaerung. Ordnet Belege den Zeilen zu und prueft auf Vollstaendigkeit. Nutze diesen Skill wenn du deine jaehrliche Steuererklaerung vorbereitest oder mehrere Objekte hast und pro Objekt eine Anlage V brauchst."
---

# Anlage-V-Assistent

> Anlage V (Einkuenfte aus Vermietung und Verpachtung) Zeile fuer Zeile vorausfuellen -- damit der Steuerberater ein fertiges Dokument statt Rohdaten bekommt.

---

## Wann nutzen?

- Zur Vorbereitung der jaehrlichen Einkommensteuererklaerung
- Pro Objekt eine Anlage V erstellen
- Nach der DATEV-Vorbereitung als finaler Schritt
- Wenn geprueft werden soll, ob alle Belege einer Anlage-V-Zeile zugeordnet sind

---

## Inputs

Stelle folgende Informationen bereit:

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| `steuerjahr` | Ja | Veranlagungsjahr |
| `steuerpflichtiger` | Ja | Name, Steuernummer, Finanzamt |
| `objekt` | Ja | Adresse, Baujahr, Anschaffungsdatum, Gebaeudewert, Grundstueckswert |
| `einheiten` | Ja | Anzahl Wohnungen, Gewerbeeinheiten, Garagen |
| `mieteinnahmen` | Ja | Kaltmieten, NK-Vorauszahlungen, Umlagen pro Einheit und Monat |
| `werbungskosten_belege` | Ja | Klassifizierte Belege (Output aus beleg-sortierer.md oder datev-vorbereitung.md) |
| `darlehen` | Empfohlen | Zinsbescheinigungen mit Jahressumme Schuldzinsen |
| `leerstand` | Empfohlen | Leerstandszeiten pro Einheit mit Grund |
| `eigennutzung` | Empfohlen | Selbstgenutzte Einheiten oder Zeitraeume |
| `verbilligte_vermietung` | Optional | Einheiten mit Miete unter Marktniveau (z.B. an Angehoerige) |
| `verteilung_erhaltungsaufwand` | Optional | Gewuenschte Verteilung auf 2-5 Jahre (§82b EStDV) |

---

## Auftrag

Du bist ein erfahrener Steuerberater-Assistent mit Spezialisierung auf Einkuenfte aus Vermietung und Verpachtung. Erstelle eine vollstaendig vorausgefuellte Anlage V fuer jedes Objekt. Ordne alle Einnahmen und Werbungskosten den korrekten Zeilen zu. Erstelle zusaetzlich eine Belegliste, die jede Zeile mit den zugrunde liegenden Belegen verknuepft. Weise auf steuerliche Gestaltungsoptionen hin.

---

## Strategie

1. **Kopfdaten der Anlage V erfassen**
   - Zeile 1-3: Lage des Grundstuecks (Strasse, PLZ, Ort)
   - Zeile 4: Art der Nutzung (Eigentumswohnung, Mehrfamilienhaus, etc.)
   - Zeile 5: Eigentumsverhaeltnis (Alleineigentum, Miteigentum, Bruchteilsgemeinschaft)
   - Zeile 6-7: Anschaffungs-/Herstellungsdaten

2. **Mieteinnahmen berechnen (Zeile 9-16)**
   - **Zeile 9:** Mieteinnahmen (Kaltmiete) -- Summe aller Kaltmieten des Jahres
   - **Zeile 10:** Einnahmen aus Umlagen/Nebenkosten-Vorauszahlungen
   - **Zeile 11:** Erstattete Nebenkosten aus Vorjahresabrechnung (Mieter-Nachzahlungen)
   - **Zeile 12:** Vereinnahmte Gelder fuer Instandhaltungsruecklage (nur bei Vermietung ganzer Gebaeude)
   - **Zeile 13:** Oeffentliche Zuschuesse (z.B. KfW, BAFA, Wohngeld-Erstattung)
   - **Zeile 14:** Sonstige Einnahmen (Stellplatzmiete, Werbeflaechenmiete)
   - **Zeile 15-16:** Summe der Einnahmen
   - Leerstandsmonate: Keine Einnahmen, aber Werbungskosten weiterhin absetzbar (wenn Vermietungsabsicht besteht)

3. **Verbilligte Vermietung pruefen (§21 Abs.2 EStG)**
   - Verhaeltnis Miete zu ortsueblicher Vergleichsmiete berechnen
   - **>= 66% der ortsueblichen Miete:** Voller Werbungskostenabzug
   - **< 66% der ortsueblichen Miete:** Werbungskosten nur anteilig absetzbar (Aufteilung entgeltlich/unentgeltlich)
   - Ortsuebliche Vergleichsmiete: Mietspiegel oder Vergleichsmieten
   - Warmmiete als Vergleichsbasis (Kaltmiete + umlagefaehige NK)

4. **Werbungskosten zuordnen (Zeile 33-51)**

   **Zeile 33-34: Absetzung fuer Abnutzung (AfA)**
   - Bemessungsgrundlage: Gebaeudewert (Kaufpreis minus Grundstueck)
   - Baujahr ab 1925: 2% linear
   - Baujahr vor 1925: 2,5% linear
   - Fertigstellung ab 2023: 3% linear
   - Zeitanteilige AfA im Anschaffungsjahr (ab Monat der Anschaffung)
   - Denkmal-AfA (§7i EStG): Separat berechnen und ausweisen

   **Zeile 35-36: Sonder-AfA (§7b EStG)**
   - Neubau-Mietwohnungen mit Bauantrag ab 01.09.2018
   - 5% jaehrlich fuer 4 Jahre (zusaetzlich zur linearen AfA)
   - Baukostenobergrenze: 3.000 EUR/qm (bis 2022), 4.800 EUR/qm (ab 2023)
   - Bemessungsgrundlage max. 2.500 EUR/qm (bis 2022), 2.500 EUR/qm (ab 2023)

   **Zeile 37: Schuldzinsen**
   - Nur Zinsen, keine Tilgung
   - Nur fuer Darlehen, die dem Objekt zugeordnet sind
   - Bei gemischt genutztem Darlehen: Aufteilung erforderlich
   - Vorfaelligkeitsentschaedigungen: Als Schuldzinsen absetzbar (bei Umschuldung/Verkauf)

   **Zeile 38: Geldbeschaffungskosten**
   - Bearbeitungsgebuehren, Schaetzkosten, Bereitstellungszinsen
   - Grundschuldbestellungskosten (Notar + Grundbuch fuer Grundschuld)

   **Zeile 39-40: Erhaltungsaufwand**
   - Sofort absetzbar ODER Verteilung auf 2-5 Jahre (§82b EStDV)
   - Verteilung ist bei hohen Betraegen sinnvoll (Progressionsglaettung)
   - Betraege aus Vorjahren, die auf dieses Jahr verteilt wurden, separat ausweisen
   - Achtung: Nur Erhaltungsaufwand, keine Herstellungskosten (diese ueber AfA)

   **Zeile 41-42: Nicht umlagefaehige Nebenkosten**
   - Hausverwaltung, Kontogebuehren, Reparaturkosten
   - Nicht auf den Mieter umlegbare Betriebskosten

   **Zeile 46: Grundsteuer**
   - Grundsteuerbescheid des Steuerjahres
   - Wenn an Mieter umgelegt: Trotzdem hier eintragen (Einnahme in Zeile 10)

   **Zeile 47: Versicherungen**
   - Gebaeudeversicherung, Haus- und Grundbesitzerhaftpflicht
   - Rechtsschutzversicherung (nur Mietrechtsanteil)
   - Mietausfallversicherung, Elementarversicherung

   **Zeile 48: Verwaltungskosten**
   - WEG-Verwaltung, Mietverwaltung, Sondereigentumsverwaltung
   - Steuerberaterkosten (anteilig fuer Anlage V)
   - Kontogebuehren Mietkonto

   **Zeile 49-50: Sonstige Werbungskosten**
   - Fahrtkosten zum Objekt (0,30 EUR/km einfach)
   - Telefon-/Portokosten
   - Fachliteratur
   - Mitgliedsbeitraege (Haus & Grund, Vermieterverband)
   - Inseratskosten bei Neuvermietung
   - Raeuumungskosten
   - Gerichts-/Anwaltskosten (mietrechtliche Streitigkeiten)

   **Zeile 51: Summe der Werbungskosten**

5. **Verteilung Erhaltungsaufwand pruefen (§82b EStDV)**
   - Nur bei Gebaeuden, die nicht zum Betriebsvermoegen gehoeren
   - Gleichmaessige Verteilung auf 2-5 Jahre moeglich
   - Wahlrecht wird durch Erklaerung ausgeubt und ist bindend
   - Bei Verkauf: Restbetrag im Verkaufsjahr sofort absetzbar
   - Empfehlung: Verteilung nutzen bei hohem Grenzsteuersatz oder Spitzensteuersatz

6. **Ergebnis berechnen**
   - Einnahmen minus Werbungskosten = Einkuenfte aus V+V
   - Bei Verlust: Pruefen ob Liebhaberei-Verdacht (Totalueberschussprognose)
   - Bei mehreren Objekten: Jedes Objekt einzeln, Zusammenfassung im Hauptvordruck

7. **Belegliste erstellen**
   - Jede Zeile der Anlage V mit zugehoerigen Belegen verknuepfen
   - Belegdateiname nach Namenskonvention
   - Summen pro Zeile muessen mit Belegen uebereinstimmen

---

## Ausgabeformat

```json
{
  "anlage_v": {
    "tax_year": 2025,
    "taxpayer": {
      "name": "Max Mustermann",
      "tax_id": "12/345/67890",
      "tax_office": "Finanzamt Duesseldorf-Mitte"
    },
    "property": {
      "property_id": "OBJ-001",
      "address": "Musterstrasse 12, 40210 Duesseldorf",
      "type": "mehrfamilienhaus",
      "ownership": "alleineigentum",
      "acquisition_date": "2022-06-15",
      "construction_year": 1965,
      "units_residential": 6,
      "units_commercial": 0,
      "units_garage": 2
    },
    "income": {
      "line_9_rental_income": 43200.00,
      "line_10_utility_prepayments": 14400.00,
      "line_11_utility_settlement_prior_year": 850.00,
      "line_12_maintenance_reserve": 0.00,
      "line_13_public_subsidies": 0.00,
      "line_14_other_income": 1200.00,
      "line_15_16_total_income": 59650.00,
      "income_details": {
        "rental_by_unit": [
          {
            "unit": "WE 1",
            "tenant": "Familie Schmidt",
            "cold_rent_monthly": 620.00,
            "months_rented": 12,
            "cold_rent_annual": 7440.00,
            "utility_prepayment_annual": 2400.00
          }
        ],
        "vacancy_periods": [
          {
            "unit": "WE 5",
            "from": "2025-03-01",
            "to": "2025-05-31",
            "reason": "renovierung_nach_mieterwechsel",
            "reletting_efforts": "Inserat bei ImmoScout24 ab 15.04.2025"
          }
        ]
      }
    },
    "reduced_rent_check": {
      "applicable": true,
      "units_affected": [
        {
          "unit": "WE 6",
          "tenant": "Schwester des Eigentuemers",
          "actual_rent_warm": 450.00,
          "market_rent_warm": 620.00,
          "ratio_percent": 72.6,
          "threshold_percent": 66.0,
          "result": "full_deduction",
          "note": "Miete >= 66% der ortsueblichen Miete, voller Werbungskostenabzug"
        }
      ]
    },
    "deductions": {
      "line_33_34_depreciation": {
        "amount": 6400.00,
        "calculation": {
          "building_value": 320000.00,
          "land_value": 80000.00,
          "depreciation_rate": 0.02,
          "depreciation_type": "linear",
          "legal_basis": "§7 Abs.4 Nr.2a EStG",
          "months_in_year": 12,
          "annual_depreciation": 6400.00
        }
      },
      "line_35_36_special_depreciation": {
        "amount": 0.00,
        "applicable": false,
        "note": "Baujahr 1965 -- §7b EStG nicht anwendbar"
      },
      "line_37_interest": {
        "amount": 4200.00,
        "loans": [
          {
            "loan_id": "DAR-001",
            "bank": "Sparkasse Duesseldorf",
            "interest_annual": 4200.00,
            "certificate_date": "2026-01-15",
            "document_ref": "2026-01-15_Zinsbescheinigung_4200EUR"
          }
        ]
      },
      "line_38_financing_costs": {
        "amount": 0.00
      },
      "line_39_40_maintenance": {
        "amount_current_year": 8500.00,
        "amount_from_prior_year_distribution": 3200.00,
        "total": 11700.00,
        "distribution_elections": [
          {
            "year_of_expense": 2024,
            "total_amount": 16000.00,
            "distribution_years": 5,
            "annual_amount": 3200.00,
            "remaining_years": 4,
            "description": "Heizungsanlage Wartung und Reparatur"
          }
        ],
        "current_year_items": [
          {
            "document_ref": "2025-03-15_Handwerkerrechnung_2450EUR",
            "description": "Sanitaer Mischbatterie WE3",
            "amount": 2450.00,
            "distribution": "sofort_absetzbar"
          }
        ]
      },
      "line_46_property_tax": {
        "amount": 890.00,
        "document_ref": "2025-01-15_Grundsteuerbescheid_890EUR"
      },
      "line_47_insurance": {
        "amount": 1920.00,
        "items": [
          {
            "type": "gebaeudeversicherung",
            "amount": 1450.00,
            "document_ref": "2025-01-01_Versicherung_1450EUR"
          },
          {
            "type": "haftpflicht",
            "amount": 320.00,
            "document_ref": "2025-01-01_Versicherung_320EUR"
          },
          {
            "type": "rechtsschutz_mietrecht",
            "amount": 150.00,
            "document_ref": "2025-02-01_Versicherung_150EUR"
          }
        ]
      },
      "line_48_administration": {
        "amount": 2450.00,
        "items": [
          {
            "type": "hausverwaltung",
            "amount": 2160.00,
            "description": "WEG-Verwaltung 12 x 180 EUR"
          },
          {
            "type": "kontogebuehren",
            "amount": 120.00
          },
          {
            "type": "steuerberater_anteil",
            "amount": 170.00,
            "note": "Anteiliger Steuerberatungskosten fuer Anlage V"
          }
        ]
      },
      "line_49_50_other": {
        "amount": 840.00,
        "items": [
          {
            "type": "fahrtkosten",
            "amount": 480.00,
            "calculation": "16 Fahrten x 50 km x 0,30 EUR x 2 (hin+rueck)"
          },
          {
            "type": "inseratskosten",
            "amount": 200.00
          },
          {
            "type": "mitgliedsbeitrag_haus_und_grund",
            "amount": 160.00
          }
        ]
      },
      "line_51_total_deductions": 28400.00
    },
    "result": {
      "total_income": 59650.00,
      "total_deductions": 28400.00,
      "taxable_income_from_rental": 31250.00,
      "profit_or_loss": "profit"
    },
    "document_checklist": [
      {
        "anlage_v_line": "33-34",
        "description": "AfA-Berechnung",
        "documents": ["AfA-Tabelle_OBJ-001"],
        "complete": true
      },
      {
        "anlage_v_line": "37",
        "description": "Schuldzinsen",
        "documents": ["2026-01-15_Zinsbescheinigung_4200EUR"],
        "complete": true
      },
      {
        "anlage_v_line": "39-40",
        "description": "Erhaltungsaufwand",
        "documents": [
          "2025-03-15_Handwerkerrechnung_2450EUR",
          "2025-05-20_Handwerkerrechnung_3100EUR",
          "2025-08-10_Handwerkerrechnung_2950EUR"
        ],
        "complete": true
      },
      {
        "anlage_v_line": "46",
        "description": "Grundsteuer",
        "documents": ["2025-01-15_Grundsteuerbescheid_890EUR"],
        "complete": true
      }
    ],
    "optimization_notes": [
      {
        "topic": "Verteilung Erhaltungsaufwand",
        "suggestion": "Groessere Erhaltungsaufwendungen koennen gemaess §82b EStDV auf 2-5 Jahre verteilt werden. Bei hohem Grenzsteuersatz kann Sofortabzug vorteilhafter sein.",
        "potential_impact": "Steuerersparnis durch Progressionsglaettung"
      },
      {
        "topic": "Verbilligte Vermietung WE 6",
        "suggestion": "Mietverhaeltnis mit 72,6% ueber der 66%-Grenze. Bei naechster Mieterhoehung darauf achten, dass die ortsuebliche Miete nicht schneller steigt als die vereinbarte Miete.",
        "potential_impact": "Risiko: Unterschreitung der 66%-Grenze = anteiliger Werbungskostenabzug"
      }
    ]
  }
}
```

---

## Qualitaetspruefung

Vor der Ausgabe pruefen:

- [ ] Jedes Objekt hat eine eigene Anlage V
- [ ] Alle Zeilen sind mit Belegen hinterlegt (Belegliste vollstaendig)
- [ ] Summe Einnahmen ist rechnerisch korrekt
- [ ] Summe Werbungskosten ist rechnerisch korrekt
- [ ] AfA ist korrekt berechnet (Baujahr, Satz, Bemessungsgrundlage)
- [ ] Schuldzinsen stimmen mit Zinsbescheinigung ueberein
- [ ] Verbilligte Vermietung ist geprueft (66%-Grenze)
- [ ] Leerstand ist dokumentiert (Vermietungsabsicht nachweisbar)
- [ ] Erhaltungsaufwand-Verteilung ist konsistent mit Vorjahren
- [ ] Keine Ueberschneidung: Herstellungskosten sind nicht als Erhaltungsaufwand gebucht
- [ ] Einkuenfte-Berechnung: Einnahmen minus Werbungskosten korrekt

---

## Warnsignale

| Signal | Bedeutung | Aktion |
|--------|-----------|--------|
| Dauerhafte Verluste | Liebhaberei-Verdacht durch Finanzamt | Totalueberschussprognose erstellen |
| Leerstand > 6 Monate | Finanzamt koennte Vermietungsabsicht anzweifeln | Vermietungsbemuehungen dokumentieren |
| Verbilligte Miete < 66% | Nur anteiliger Werbungskostenabzug | Miete erhoehen oder Aufteilung vornehmen |
| Hoher Erhaltungsaufwand bei Neuerwerb | 15%-Grenze anschaffungsnahe HK | Pruefung durch Steuerberater |
| AfA auf Grundstueck | Grundstueck ist nicht abschreibbar | Grundstuecksanteil herausrechnen |
| Eigennutzung nicht angegeben | Fehlerhafte Steuererlaerung | Eigengenutzte Zeiten korrekt erfassen |
| Fehlende Zinsbescheinigung | Schuldzinsen nicht belegbar | Bank kontaktieren |
| NK-Abrechnung fehlt | Einnahmen moeglicherweise unvollstaendig | Hausverwaltung kontaktieren |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Mietspiegel fuer 66%-Pruefung | Auf Basis vergleichbarer Mieten im Objekt schaetzen, als Schaetzwert kennzeichnen |
| Zinsbescheinigung | Zeile 37 leer lassen, Hinweis "Zinsbescheinigung ausstehend" |
| Grundsteuerbescheid | Vorjahreswert uebernehmen, als "vorlaeufig" markieren |
| NK-Abrechnung Vorjahr | Zeile 11 leer lassen, Hinweis an Hausverwaltung |
| Fahrtenbuch | Geschaetzte Fahrten mit Anlass dokumentieren, konservativ ansetzen |
| Gebaeude-/Grundstuecksaufteilung | BMF-Arbeitshilfe oder Bodenrichtwert-Methode vorschlagen |

---

## Konfidenz-Bewertung

| Stufe | Wert | Bedeutung |
|-------|------|-----------|
| Hoch | >= 0.90 | Alle Belege vorhanden, Zuordnung eindeutig, Berechnung geprueft |
| Mittel | 0.70 - 0.89 | Einzelne Belege fehlen, Zuordnung ueberwiegend klar |
| Niedrig | 0.50 - 0.69 | Wesentliche Belege fehlen, mehrere Schaetzwerte |
| Unsicher | < 0.50 | Anlage V nicht belastbar erstellbar, Steuerberater muss pruefen |

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- EStG, EStDV, Mietrecht
- `knowledge/kalkulationsformeln.md` -- AfA-Berechnung, Renditeformeln
- `skills/beleg-sortierer/SKILL.md` -- Vorheriger Schritt: Belege klassifizieren
- `skills/datev-vorbereitung/SKILL.md` -- Vorheriger Schritt: Buchungssaetze erstellen
- `skills/mieterhoehung/SKILL.md` -- Mietspiegel und ortsuebliche Miete
