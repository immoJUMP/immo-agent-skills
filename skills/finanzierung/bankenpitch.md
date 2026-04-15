# Bankenpitch -- Strukturierte Bankenpraesentation erstellen

Erstellt ein vollstaendiges, professionelles Praesentationsdokument fuer den Banktermin. Kombiniert die Ergebnisse aus Bankenkonzept und Cashflow-Modell zu einem ueberzeugenden Gesamtdokument, das den Firmenkundenberater in die Lage versetzt, die Finanzierung intern freizugeben.

> **Praxis-Insight:** Ein Investor hat mit einer strukturierten Bankenpraesentation zwei 1-Mio-Euro-Deals mit NULL Eigenkapital finanziert bekommen. Der Banker sagte: "Er hat sich wirklich Gedanken gemacht." Die Praesentation zeigte klar den Pfad: Ist-Mieten → organische Mieterhoehung → Modernisierung → tilgungsfrei Jahr 1 → Cashflow-positiv ab Jahr 2. Die Bank konnte das Konzept intern ohne Rueckfragen vorlegen.

---

## Wann diesen Skill nutzen

- Du hast das Bankenkonzept und Cashflow-Modell bereits erstellt und willst ein Praesentationsdokument fuer den Banktermin
- Du bereitest einen Ersttermin oder Zweitgespraech mit dem Firmenkundenberater vor
- Du willst dem Banker ein Dokument geben, das er intern (Marktfolge, Kreditausschuss) weiterreichen kann
- Du willst professionell auftreten und dich von anderen Finanzierungsanfragen abheben
- Du argumentierst eine 100%-Finanzierung oder ueberdurchschnittlichen Beleihungsauslauf

---

## Was du bereitstellen musst

### Pflichtangaben

```json
{
  "property": {
    "address": "Strasse, PLZ, Stadt",
    "type": "MFH | ZFH | ETW-Paket | Wohn-/Geschaeftshaus",
    "units": 8,
    "total_sqm": 520,
    "year_built": 1965,
    "condition": "teilsaniert | unsaniert | vollsaniert",
    "plot_size_sqm": 800,
    "parking_spaces": 4,
    "heating_type": "Gas-Zentralheizung",
    "energy_class": "E",
    "grundbuch_clean": true
  },
  "purchase": {
    "asking_price_eur": 850000,
    "offered_price_eur": 780000,
    "negotiation_basis": "Sanierungsstau + Leerstand als Verhandlungsargument",
    "buyer_commission_pct": 3.57,
    "grunderwerbsteuer_pct": 6.5,
    "notar_grundbuch_pct": 2.0
  },
  "financing_concept": {
    "source": "Ergebnis aus bankenkonzept.md Skill -- oder manuell eingeben",
    "total_investment_eur": 994146,
    "loan_amount_eur": 994146,
    "equity_eur": 0,
    "interest_rate_pct": 3.80,
    "repayment_rate_pct": 2.00,
    "fixed_rate_years": 10,
    "tilgungsfrei_months": 12,
    "sondertilgung_pct": 5
  },
  "cashflow_projection": {
    "source": "Ergebnis aus cashflow-modell.md Skill -- oder manuell eingeben",
    "cashflow_positive_month": 14,
    "dscr_year_1": 1.02,
    "dscr_year_3": 1.42,
    "cumulative_cashflow_5y": 42000
  }
}
```

### Optionale Angaben

```json
{
  "location_analysis": {
    "city_population": 85000,
    "population_trend": "wachsend | stabil | schrumpfend",
    "unemployment_rate_pct": 5.2,
    "major_employers": ["Universitaet", "Krankenhaus", "Industriepark"],
    "infrastructure": ["S-Bahn 5 Min", "Autobahn 10 Min", "Einkaufszentrum 500m"],
    "mikrolage": "Ruhige Wohnlage, gewachsene Nachbarschaft, Grundschule 300m",
    "bodenrichtwert_eur_sqm": 120,
    "mietspiegeldaten": "7,80 EUR/qm Durchschnitt, 9,50 EUR/qm Obergrenze"
  },
  "investor_profile": {
    "name": "Max Mustermann / Mustermann Immobilien GmbH",
    "experience_years": 5,
    "total_units_owned": 35,
    "total_portfolio_value_eur": 3500000,
    "annual_rental_income_eur": 280000,
    "existing_bank_relationships": ["Sparkasse", "Volksbank"],
    "track_record": [
      {
        "property": "Hauptstr. 10, Musterstadt",
        "purchased": "2021",
        "units": 6,
        "purchase_price_eur": 420000,
        "current_value_eur": 550000,
        "rent_increase_achieved_pct": 35
      }
    ],
    "profession": "Angestellt / Selbststaendig / GmbH-Geschaeftsfuehrer",
    "annual_income_eur": 85000,
    "schufa_score": "sehr gut"
  },
  "risk_mitigation": {
    "liquidity_reserve_eur": 30000,
    "additional_collateral": "Bestandsimmobilie als Zusatzsicherheit moeglich",
    "insurance": ["Gebaeudeversicherung", "Mietausfallversicherung"],
    "property_management": "Eigenverwaltung | professionelle Hausverwaltung"
  },
  "reference_properties": [
    {
      "address": "Beispielstr. 5, Musterstadt",
      "purchase_price_eur": 900000,
      "units": 7,
      "price_per_sqm": 1650,
      "rent_per_sqm": 8.20,
      "factor": 18.5,
      "note": "Vergleichbar, saniert, 2024 verkauft"
    }
  ],
  "photos_available": true,
  "documents_available": [
    "Grundbuchauszug",
    "Energieausweis",
    "Mietliste",
    "Teilungserklaerung",
    "Wirtschaftsplan"
  ]
}
```

---

## Auftrag

Erstelle ein vollstaendiges, bankenfertiges Praesentationsdokument, das:

1. **Auf einer Seite das Wesentliche zusammenfasst** (Executive Summary)
2. **Das Objekt professionell vorstellt** (Daten, Lage, Zustand)
3. **Den Finanzierungsplan nachvollziehbar darstellt** (Struktur, Cashflow, DSCR)
4. **Risiken proaktiv adressiert** (bevor die Bank fragt)
5. **Den Investor als kompetent und vertrauenswuerdig positioniert** (Track Record)
6. **Dem Firmenkundenberater ein Dokument gibt, das er intern weiterreichen kann** (Marktfolge/Kreditausschuss)

---

## Strategie

### Schritt 1: Executive Summary erstellen (1 Seite)

- Objektbezeichnung, Standort, Typ
- Kaufpreis und Gesamtinvestition
- Gewuenschte Finanzierungsstruktur (Darlehen, EK, Tilgung, Zinsbindung)
- Kernkennzahlen: Ist-Rendite, Soll-Rendite, DSCR, Cashflow-positiv ab Monat X
- Investitionsstrategie in 2-3 Saetzen: "Erwerb eines unterdurchschnittlich vermieteten MFH, Hebung des Mietpotenzials durch organische Mieterhoehung und selektive Modernisierung, Cashflow-positiv ab Monat 14."
- Eigenkapital-Rueckfluss oder Vermoegensaufbau-Prognose

### Schritt 2: Objektuebersicht strukturieren

- Adresse, Baujahr, Wohnflaeche, Grundstueck, Einheiten
- Technische Daten: Heizung, Energieausweis, Dach, Fenster
- Aktuelle Vermietungssituation: Mieteinnahmen, Leerstand, Mietvertragslaufzeiten
- Zustandsbewertung: Was ist gut, was muss gemacht werden
- Fotos einbinden (Aussen, Treppenhaus, Beispiel-WE) -- wenn verfuegbar

### Schritt 3: Standortanalyse praesentieren

- **Makrolage:** Stadt, Einwohner, Wirtschaftsstruktur, Arbeitslosenquote, Bevoelkerungsentwicklung
- **Mikrolage:** Strasse, Nachbarschaft, Infrastruktur, OEPNV, Schulen, Einkaufen
- **Mietmarkt:** Mietspiegel, Mietentwicklung, Nachfragesituation, Leerstandsquote
- **Bodenrichtwert:** Entwicklung, Vergleich mit Umgebung
- **Fazit Standort:** Warum ist dieser Standort fuer eine Wohnimmobilieninvestition geeignet?

### Schritt 4: Finanzierungskonzept einbetten

- Aus dem Bankenkonzept-Skill uebernehmen oder neu erstellen:
  - Gesamtinvestitionsaufstellung
  - Finanzierungsstruktur (Darlehen vs. EK)
  - Konditionen (Zins, Tilgung, Zinsbindung, Sondertilgung)
  - Massnahmenplan (Jahresschritte)
  - Kapitaldienstfaehigkeit (DSCR Ist und Soll)
  - Tilgungsszenarien

### Schritt 5: Cashflow-Projektion einbetten

- Aus dem Cashflow-Modell-Skill uebernehmen oder neu erstellen:
  - 5-Jahres-Projektion (Base Case)
  - Kernaussage: "Cashflow-positiv ab Monat X"
  - Best/Worst Case als Bandbreite
  - Sensitivitaetsanalyse (Zins, Leerstand)

### Schritt 6: Risikomitigierung darstellen

- Proaktiv die Fragen beantworten, die die Marktfolge stellen wird:
  - **"Was wenn Mieterhoehungen nicht durchsetzbar?"** → Konservatives Szenario zeigt: Auch mit 60% der geplanten Erhoehungen bleibt DSCR > 1,0
  - **"Was wenn Leerstand steigt?"** → Standortanalyse zeigt geringe Leerstandsquote, Liquiditaetsreserve vorhanden
  - **"Was wenn Zinsen steigen?"** → Stresstest: Cashflow bleibt bis +2% Zins positiv
  - **"Was wenn Sanierung teurer wird?"** → Puffer von 15-20% im Sanierungsbudget eingeplant
  - **"Wie ist die Bonitas des Investors?"** → Einkommen, Portfolio, Track Record
- Liquiditaetsreserve benennen
- Zusatzsicherheiten benennen (falls vorhanden)
- Versicherungsschutz darstellen

### Schritt 7: Investorenprofil praesentieren

- Persoenliche Daten / Firma
- Berufliche Situation und Einkommen
- Immobilienerfahrung und Track Record
- Bestandsportfolio (Anzahl Einheiten, Wert, Mieteinnahmen)
- Bestehende Bankbeziehungen
- Erfolgsgeschichten: "Objekt X gekauft fuer Y, Miete um Z% gesteigert, heute Wert W"

### Schritt 8: Referenzobjekte als Marktvalidierung

- 2-3 vergleichbare Objekte in der Region
- Kaufpreis/qm, Miete/qm, Faktor
- Zeigen: "Mein Kaufpreis liegt im oder unter dem Markt"
- Idealerweise eigene Portfolio-Objekte als Referenz ("So habe ich es schon gemacht")

### Schritt 9: Anhang strukturieren

- Detaillierte Berechnungen (aus Bankenkonzept und Cashflow-Modell)
- Mietliste / Mietaufstellung
- Grundbuchauszug-Zusammenfassung (keine Lasten, keine Vormerkungen)
- Energieausweis-Daten
- Fotos
- Bodenrichtwert-Auskunft
- Marktdaten (ImmoScout24, Mietspiegel, Vergleichsangebote)

---

## Ausgabeformat

```markdown
# Finanzierungsantrag: [Objektbezeichnung]
## [Adresse]
## Erstellt: [Datum] | Investor: [Name / Firma]

---

## 1. Executive Summary

**Investitionsuebersicht**

| Parameter | Wert |
|-----------|------|
| Objekt | MFH, 8 WE, 520 qm, BJ 1965 |
| Standort | [Stadt], [Bundesland] |
| Kaufpreis | 780.000 EUR |
| Gesamtinvestition | 994.146 EUR |
| Gewuenschtes Darlehen | 994.146 EUR (100%-Finanzierung inkl. NK + Sanierung) |
| Eigenkapital | 0 EUR |
| Zinsbindung | 10 Jahre |
| Tilgung | 2,0% (nach 12 Monaten tilgungsfrei) |
| Sondertilgung | 5% p.a. |

**Kernkennzahlen**

| Kennzahl | Ist | Soll (ab Jahr 3) |
|----------|-----|-------------------|
| Jahresnettokaltmiete | 38.400 EUR | 52.800 EUR |
| Bruttomietrendite | 4,9% | 6,8% |
| Kaufpreisfaktor | 20,3x | 14,8x |
| DSCR | 1,02 | 1,42 |
| Cashflow/Monat | +562 EUR (tilgungsfrei) | +1.095 EUR |

**Investitionsstrategie**

Erwerb eines unterdurchschnittlich vermieteten Mehrfamilienhauses in [Stadt] mit signifikantem Mietanpassungspotenzial. Die Ist-Miete liegt im Durchschnitt bei 5,85 EUR/qm -- der oertliche Mietspiegel weist 7,80 EUR/qm aus. Durch organische Mieterhoehung (Jahr 1), selektive Modernisierung (Jahr 2) und Neuvermietung bei Fluktuation wird die Miete auf durchschnittlich 8,50 EUR/qm angehoben. Der Kapitaldienst wird vollstaendig aus dem Objekt bedient. Die tilgungsfreie Anlaufphase ermoeglicht die Umsetzung der Massnahmen ohne zusaetzlichen Liquiditaetsbedarf.

---

## 2. Objektuebersicht

### 2.1 Eckdaten

| Parameter | Wert |
|-----------|------|
| Adresse | [Vollstaendige Adresse] |
| Objekttyp | Mehrfamilienhaus |
| Baujahr | 1965 |
| Wohneinheiten | 8 |
| Gewerbeeinheiten | 0 |
| Wohnflaeche | 520 qm |
| Grundstueck | 800 qm |
| Stellplaetze | 4 |
| Heizung | [Typ, Alter] |
| Energieausweis | [Klasse, kWh/qm/a] |
| Dach | [Zustand, letztes Jahr der Sanierung] |
| Fenster | [Zustand, Material, Baujahr] |
| Fassade | [Zustand] |

### 2.2 Aktuelle Vermietungssituation

| WE | Flaeche (qm) | Miete (EUR/qm) | Miete (EUR/Monat) | Mieter seit | Vertrag |
|----|---------------|----------------|-------------------|-------------|---------|
| 1 | 65 | 5,50 | 357,50 | 03/2015 | unbefristet |
| 2 | 70 | 6,00 | 420,00 | 07/2018 | unbefristet |
| ... | ... | ... | ... | ... | ... |
| 8 | 60 | -- | LEER | seit 06/2024 | -- |
| **Gesamt** | **520** | **Ø 5,85** | **3.200** | | |

**Leerstand:** 1 von 8 WE (12,5%) -- seit Juni 2024, sofort vermietbar nach Grundreinigung

### 2.3 Zustandsbewertung

| Bereich | Zustand | Handlungsbedarf | Geschaetzte Kosten |
|---------|---------|-----------------|-------------------|
| Dach | Gut (2015 erneuert) | Keiner | 0 EUR |
| Fassade | Befriedigend | Mittelfristig (5-8 Jahre) | 40.000 EUR |
| Fenster | Mangelhaft (Einfachverglasung) | Kurzfristig (Jahr 2) | 45.000 EUR |
| Heizung | Befriedigend (Gas, BJ 2005) | Mittelfristig | 25.000 EUR |
| Elektrik | Ausreichend | Bei Mieterwechsel | 3.000 EUR/WE |
| Baeder | Veraltet | Bei Mieterwechsel | 5.000 EUR/WE |
| Treppenhaus | Befriedigend | Optisch (geringer Aufwand) | 5.000 EUR |

### 2.4 Fotos

[Hinweis: Fotos als Anlage beifuegen -- Aussen, Treppenhaus, Beispiel-WE gut + schlecht]

---

## 3. Standortanalyse

### 3.1 Makrolage

| Parameter | Wert |
|-----------|------|
| Stadt | [Name] |
| Bundesland | [Name] |
| Einwohner | 85.000 |
| Bevoelkerungsentwicklung | [wachsend/stabil/schrumpfend] (+0,8% p.a.) |
| Arbeitslosenquote | 5,2% |
| Wirtschaftsstruktur | [Hauptarbeitgeber, Branchen] |
| Kaufkraftindex | [Wert, Vergleich Bundesdurchschnitt] |
| Hochschulstandort | [Ja/Nein, Anzahl Studierende] |

### 3.2 Mikrolage

| Parameter | Wert |
|-----------|------|
| Stadtteil | [Name] |
| Charakter | Ruhige Wohnlage, gewachsene Nachbarschaft |
| OEPNV | S-Bahn 5 Gehminuten, Bus direkt vor der Tuer |
| Autobahn | 10 Minuten |
| Einkaufen | Supermarkt 300m, Einkaufszentrum 500m |
| Schulen | Grundschule 300m, Gymnasium 1 km |
| Aerzte | Hausarzt 200m, Krankenhaus 3 km |
| Laermpegel | Ruhig (keine Hauptverkehrsstrasse, kein Gewerbe) |

### 3.3 Mietmarkt

| Parameter | Wert |
|-----------|------|
| Mietspiegel Durchschnitt | 7,80 EUR/qm |
| Mietspiegel Obergrenze | 9,50 EUR/qm |
| Neuvermietungsmiete (ImmoScout24) | 8,00 - 9,50 EUR/qm |
| Leerstandsquote (Stadt) | 2,8% |
| Mietentwicklung (5 Jahre) | +12% |
| Bodenrichtwert | 120 EUR/qm |
| Bodenrichtwert-Entwicklung (5 Jahre) | +25% |

### 3.4 Standort-Fazit

[Stadt] ist ein [Mittelzentrum/Oberzentrum] mit stabiler bis wachsender Bevoelkerung, diversifizierter Wirtschaftsstruktur und niedrigem Leerstand. Die Mikrolage bietet eine gute Wohnqualitaet mit kurzen Wegen zu Infrastruktur und OEPNV. Der Mietmarkt zeigt steigende Mieten bei geringem Leerstand -- ideale Bedingungen fuer eine nachhaltige Wohnimmobilieninvestition.

---

## 4. Finanzierungskonzept

### 4.1 Investitionsaufstellung

| Position | Betrag (EUR) |
|----------|-------------|
| Kaufpreis | 780.000 |
| Grunderwerbsteuer (6,5%) | 50.700 |
| Notar + Grundbuch (2,0%) | 15.600 |
| Maklerprovision (3,57%) | 27.846 |
| Sanierungsbudget | 120.000 |
| **Gesamtinvestition** | **994.146** |

### 4.2 Finanzierungsstruktur

| Parameter | Wert |
|-----------|------|
| Bankdarlehen | 994.146 EUR |
| Eigenkapital | 0 EUR |
| Beleihungsauslauf (auf Kaufpreis) | ca. 127% |
| Beleihungsauslauf (auf Ertragswert nach Massnahmen) | ca. 105% |
| Sollzins | 3,80% p.a. |
| Effektivzins | 3,92% p.a. |
| Zinsbindung | 10 Jahre |
| Anfaengliche Tilgung | 2,00% |
| Tilgungsfreie Anlaufphase | 12 Monate |
| Sondertilgung | bis 5% p.a. |
| Annuitaet (nach tilgungsfreier Phase) | 4.805 EUR/Monat |
| Rate in tilgungsfreier Phase | 3.148 EUR/Monat |

### 4.3 Massnahmenplan

| Phase | Zeitraum | Massnahme | Kosten (EUR) | Mehrmiete (EUR/Monat) |
|-------|----------|-----------|-------------|----------------------|
| **Phase 1** | Monat 1-3 | Leerstand beseitigen (Neuvermietung WE 8) | 2.000 | +510 |
| **Phase 2** | Monat 4-12 | Organische Mieterhoehung (§558 BGB) | 0 | +380 |
| **Phase 3** | Monat 13-18 | Fenstertausch + Heizungsoptimierung | 85.000 | +210 |
| **Phase 4** | Monat 19-24 | Badsanierung bei Mieterwechsel | 35.000 | +100 |
| **Phase 5** | Monat 25-36 | Stabilisierung, ggf. Sondertilgung | 0 | -- |

**Ergebnis:** Mieteinnahmen steigen von 3.200 EUR/Monat auf 4.400 EUR/Monat (+37,5%)

### 4.4 Kapitaldienstfaehigkeit (DSCR)

| Zeitpunkt | Nettomieteinnahmen (EUR/Jahr) | Annuitaet (EUR/Jahr) | DSCR | Bewertung |
|-----------|-------------------------------|----------------------|------|-----------|
| Jahr 1 (tilgungsfrei, nach Neuvermietung) | 38.520 | 37.776 | **1,02** | Ausreichend |
| Jahr 2 (Mieterhoehung umgesetzt) | 43.080 | 57.660 | **0,75** | Unter 1,0 -- durch tilgungsfreie Reserve gedeckt |
| Jahr 3 (Modernisierung abgeschlossen) | 45.600 | 57.660 | **1,42** | Komfortabel |
| Jahr 5 (stabilisiert) | 47.200 | 57.660 | **1,48** | Stark |

### 4.5 Stresstest

| Szenario | DSCR | Bewertung |
|----------|------|-----------|
| Base Case (Jahr 3) | 1,42 | Komfortabel |
| Zinsen +1% nach Zinsbindung | 1,25 | Tragbar |
| Zinsen +2% nach Zinsbindung | 1,08 | Knapp, aber positiv |
| Leerstand 10% | 1,22 | Tragbar |
| Kombination: +2% Zins + 10% Leerstand | 0,92 | Negativ -- Sondertilgung wirkt dem entgegen |

---

## 5. Cashflow-Projektion

### 5.1 Base Case (5 Jahre)

| Position | Jahr 1 | Jahr 2 | Jahr 3 | Jahr 4 | Jahr 5 |
|----------|--------|--------|--------|--------|--------|
| Mieteinnahmen (brutto) | 49.080 | 52.800 | 55.200 | 56.400 | 57.600 |
| - Leerstand/Mietausfall | -1.963 | -2.112 | -2.208 | -2.256 | -2.304 |
| - Bewirtschaftungskosten | -14.640 | -15.006 | -15.381 | -15.766 | -16.160 |
| **= Netto-Mieteinnahmen** | **32.477** | **35.682** | **37.611** | **38.378** | **39.136** |
| - Kapitaldienst | -37.776 | -57.660 | -57.660 | -57.660 | -57.660 |
| **= Cashflow vor Steuern** | **-5.299** | **-21.978** | **-20.049** | **-19.282** | **-18.524** |
| + Steuereffekt (AfA, Zinsabzug) | +23.146 | +22.044 | +21.123 | +20.381 | +19.618 |
| **= Cashflow nach Steuern** | **+17.847** | **+66** | **+1.074** | **+1.099** | **+1.094** |

**Kumulierter Cashflow nach Steuern (5 Jahre): ca. +21.180 EUR**

### 5.2 Szenario-Bandbreite

| Kennzahl | Best Case | Base Case | Worst Case |
|----------|-----------|-----------|------------|
| Kumulierter Cashflow (5 Jahre, nach Steuern) | +53.911 EUR | +21.180 EUR | -21.789 EUR |
| Cashflow-positiv ab (vor Steuern) | Monat 3 | Monat 14 | Monat 30 |
| DSCR Durchschnitt | 1,45 | 1,22 | 0,95 |

---

## 6. Risikomitigierung

| Risiko | Eintrittswahrscheinlichkeit | Auswirkung | Gegenmassnahme |
|--------|----------------------------|------------|----------------|
| Mieterhoehung nicht durchsetzbar | Niedrig | Mittel | Konservatives Szenario zeigt: Auch mit 60% der geplanten Erhoehungen bleibt DSCR > 1,0. Mietspiegel-Begruendung rechtlich abgesichert. |
| Leerstand steigt auf > 10% | Niedrig | Hoch | Leerstandsquote am Standort 2,8%. Neuvermietung in < 4 Wochen realistisch. Mietausfallversicherung moeglich. |
| Sanierungskosten ueberschreiten Budget | Mittel | Mittel | 15% Puffer im Budget eingeplant (120.000 EUR → effektiv 104.000 EUR geplante Kosten). Handwerkerangebote liegen vor. |
| Zinsanstieg nach Zinsbindung | Mittel | Hoch | 10 Jahre Zinsbindung sichern aktuelles Niveau. Sondertilgungen reduzieren Restschuld. Stresstest: +2% = DSCR 1,08 (tragbar). |
| Mieterwechsel erhoehen Kosten | Mittel | Niedrig | Fluktuation 10% p.a. eingeplant. Bei Auszug: Neuvermietung zu hoeherem Mietpreis = Chance. |
| Regulatorische Aenderungen (Mietpreisbremse, Heizungsgesetz) | Niedrig | Mittel | Konservative Kalkulation ohne Ausreizung der Mietgrenzen. Energetische Massnahmen im Sanierungsplan enthalten. |

### Liquiditaetsreserve

| Position | Betrag (EUR) |
|----------|-------------|
| Freie Liquiditaet | 30.000 EUR |
| Monatlicher Ueberschuss aus Bestandsportfolio | 8.500 EUR |
| Ungenutzter Kreditrahmen | [falls vorhanden] |
| **Verfuegbare Reserve** | **> 30.000 EUR** |

> Die Liquiditaetsreserve deckt ca. 8 Monatsraten (tilgungsfreie Phase) bzw. 6 Monatsraten (Vollannuitaet) ab.

### Zusatzsicherheiten

- [Bestandsimmobilie als nachrangige Grundschuld moeglich (Verkehrswert X EUR, Restschuld Y EUR, freier Beleihungsraum Z EUR)]
- [Weitere Sicherheiten falls vorhanden]

---

## 7. Investorenprofil

### 7.1 Persoenliche Daten

| Parameter | Wert |
|-----------|------|
| Name | [Name / Firma] |
| Beruf | [Beruf / Position] |
| Bruttoeinkommen p.a. | [Betrag] EUR |
| Familienstand | [Status] |
| SCHUFA | Sehr gut (Score > 97%) |

### 7.2 Immobilienportfolio

| Parameter | Wert |
|-----------|------|
| Erfahrung | [X] Jahre |
| Einheiten im Bestand | [X] WE |
| Portfoliowert (geschaetzt) | [X] EUR |
| Jahresmieteinnahmen (brutto) | [X] EUR |
| Bestehende Darlehen | [X] EUR |
| Monatlicher Netto-Cashflow (gesamt) | [X] EUR |
| Bestehende Bankbeziehungen | [Bank 1, Bank 2] |

### 7.3 Track Record

| Objekt | Erworben | Einheiten | Kaufpreis (EUR) | Aktueller Wert (EUR) | Mietsteigerung |
|--------|----------|-----------|-----------------|----------------------|----------------|
| Hauptstr. 10, Musterstadt | 2021 | 6 | 420.000 | 550.000 | +35% |
| Bahnhofstr. 22, Musterstadt | 2022 | 12 | 680.000 | 820.000 | +28% |
| Gartenweg 7, Musterstadt | 2023 | 4 | 290.000 | 340.000 | +22% |

> **Track Record zeigt:** Systematische Wertsteigerung durch Mieterhoehung und Modernisierung bei allen bisherigen Objekten. Erfahrung in der Umsetzung genau der Strategie, die hier geplant ist.

---

## 8. Referenzobjekte

| Objekt | Kaufpreis (EUR) | EUR/qm | Miete EUR/qm | Faktor | Anmerkung |
|--------|-----------------|--------|--------------|--------|-----------|
| Beispielstr. 5 | 900.000 | 1.650 | 8,20 | 18,5 | Vergleichbar, saniert, 2024 verkauft |
| Musterweg 12 | 720.000 | 1.440 | 7,00 | 17,1 | Gleiche Lage, unsaniert |
| Lindenallee 3 | 850.000 | 1.550 | 7,50 | 18,9 | Aehnliches BJ, teilsaniert |
| **Unser Objekt** | **780.000** | **1.500** | **5,85 → 8,50** | **20,3 → 14,8** | **Unterdurchschnittlich vermietet = Chance** |

**Fazit:** Das Objekt wird unter dem vergleichbaren Marktniveau erworben. Nach Umsetzung der Massnahmen liegt der wirtschaftliche Faktor mit 14,8x deutlich unter den Vergleichsobjekten -- ein starkes Value-Add-Profil.

---

## 9. Anhang

### Anlage 1: Detaillierte Mietliste
[Vollstaendige Mietaufstellung mit Vertragsdaten]

### Anlage 2: Tilgungsplan (10 Jahre)
[Aus Bankenkonzept-Skill]

### Anlage 3: Cashflow-Projektion (detailliert)
[Aus Cashflow-Modell-Skill, alle drei Szenarien]

### Anlage 4: Sensitivitaetsanalyse
[Zins- und Leerstandsmatrizen]

### Anlage 5: Grundbuchauszug
[Zusammenfassung: Keine Lasten, keine Vormerkungen Dritter]

### Anlage 6: Energieausweis
[Zusammenfassung der Kerndaten]

### Anlage 7: Fotos
[Aussen, Treppenhaus, Beispiel-Wohnungen, Keller, Dachboden]

### Anlage 8: Sanierungskostenaufstellung
[Detaillierte Aufstellung mit Handwerkerangeboten]

### Anlage 9: Marktdaten
[Mietspiegel, ImmoScout24-Vergleichsangebote, Bodenrichtwerte]

### Anlage 10: Selbstauskunft Investor
[Vermoegensuebersicht, Einkommensnachweise, SCHUFA]

---

**Checkliste: Dokument komplett?**

- [ ] Executive Summary auf 1 Seite
- [ ] Objektdaten vollstaendig
- [ ] Standortanalyse mit Makro + Mikrolage
- [ ] Finanzierungsstruktur klar dargestellt
- [ ] DSCR berechnet (Ist + Soll + Stresstest)
- [ ] Cashflow-Projektion mit Szenarien
- [ ] Risiken proaktiv adressiert
- [ ] Investorenprofil mit Track Record
- [ ] Referenzobjekte als Marktvalidierung
- [ ] Alle Anlagen vorbereitet
```

---

## Qualitaetspruefung

Pruefe das Dokument gegen diese Kriterien:

- [ ] **Executive Summary passt auf 1 Seite:** Alle Kernkennzahlen, keine Details
- [ ] **Bankenperspektive eingenommen:** Wuerde ein Firmenkundenberater dieses Dokument intern weiterreichen?
- [ ] **Zahlen konsistent:** Stimmen die Zahlen in Executive Summary, Finanzierungskonzept und Cashflow-Projektion ueberein?
- [ ] **Risiken proaktiv adressiert:** Werden die typischen Fragen der Marktfolge vorweggenommen?
- [ ] **Track Record ueberzeugend:** Zeigt der Investor, dass er die Strategie schon erfolgreich umgesetzt hat?
- [ ] **Referenzobjekte vorhanden:** Wird der Kaufpreis durch Marktvergleiche validiert?
- [ ] **Anhang vollstaendig:** Alle relevanten Dokumente aufgelistet und vorbereitet?
- [ ] **Sprache professionell:** Sachlich, praezise, keine Uebertreibungen, keine Anglizismen (ausser Fachbegriffe wie DSCR)
- [ ] **Massnahmenplan glaubwuerdig:** Sind die geplanten Schritte realistisch und zeitlich machbar?
- [ ] **Steuerliche Hinweise korrekt:** AfA-Satz, Zinsabzug, anschaffungsnahe Herstellungskosten beruecksichtigt?

---

## Warnsignale & Dealbreaker

| Warnsignal | Bewertung | Handlungsempfehlung |
|------------|-----------|---------------------|
| Kein Track Record und keine Berufserfahrung im Immobilienbereich | HOCH | Erfahrung anders belegen: Ausbildungen, Netzwerk, Co-Investor mit Erfahrung |
| DSCR < 1,0 auch nach Massnahmen im Base Case | KRITISCH | Deal ueberarbeiten oder andere Bank/anderes Produkt suchen |
| Keine Liquiditaetsreserve und kein laufendes Einkommen | KRITISCH | Bank wird ohne Sicherheitsnetz nicht finanzieren |
| Grundbuch belastet (Vormerkungen, Wegerechte, Altlasten) | HOCH | Klaeren vor Banktermin, ggf. im Kaufvertrag regeln |
| Energieausweis Klasse G/H ohne Sanierungsplan | MITTEL | Sanierungsplan mit konkreten Massnahmen und Kosten erstellen |
| Standort mit schrumpfender Bevoelkerung und hohem Leerstand | HOCH | Standortrisiko transparent kommunizieren, Mietniveau konservativ ansetzen |
| Praesentation enthaelt Widersprueche oder Rechenfehler | KRITISCH | Alle Zahlen gegenprufen, Konsistenz zwischen Abschnitten sicherstellen |
| Mietzins liegt ueber der ortsueblichen Vergleichsmiete | HOCH | Keine Mieten ueber Mietspiegel-Obergrenze planen, Glaubwuerdigkeit bewahren |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Fotos | Darauf hinweisen, dass Fotos nachgeliefert werden. Alternativ: Google Street View fuer Aussenansicht |
| Grundbuchauszug | Als "wird nachgereicht" markieren, aber keine Finanzierung ohne Grundbucheinsicht moeglich |
| Track Record (erster Deal) | Berufliche Qualifikation hervorheben, Netzwerk benennen (Hausverwaltung, Steuerberater, Handwerker), Weiterbildungen erwaehnen |
| Standortdaten | Statistisches Landesamt, kommunale Statistik, IHK-Daten verwenden |
| Referenzobjekte | ImmoScout24, Immowelt, lokale Makler fuer Vergleichspreise nutzen |
| Mietspiegel | Rathaus/Mieterverein anfragen, alternativ ImmoScout24-Mietpreisspiegel nutzen |
| Sanierungskosten | Markt-Benchmarks verwenden, transparent als "Schaetzung ohne Handwerkerangebot" kennzeichnen |
| Energieausweis | Darauf hinweisen, dass Verkaufer zur Vorlage verpflichtet ist (§16 EnEV / GEG) |

> **Tipp:** Lieber eine Luecke transparent benennen als mit unsicheren Daten die Glaubwuerdigkeit des gesamten Dokuments zu gefaehrden.

---

## Konfidenz-Bewertung

| Konfidenz | Kriterien |
|-----------|-----------|
| **HOCH** (90%+) | Alle Pflichtdaten vorhanden, Bankenkonzept und Cashflow-Modell bereits erstellt, Track Record vorhanden, Referenzobjekte recherchiert, Handwerkerangebote fuer Sanierung, Grundbuchauszug eingesehen, Mietspiegel vorliegend |
| **MITTEL** (70-89%) | Objektdaten und Finanzierung bekannt, aber Track Record duenn oder Referenzobjekte nicht recherchiert, Sanierungskosten geschaetzt, kein Grundbuchauszug vorliegend |
| **NIEDRIG** (< 70%) | Wesentliche Daten fehlen (z.B. keine Mietliste, kein Mietspiegel), kein Track Record, Finanzierungskonditionen nicht abgestimmt, Standortanalyse nicht durchgefuehrt |

---

## Verwandte Wissensdatenbanken

- `skills/finanzierung/bankenkonzept.md` -- Erstellt das zugrundeliegende Finanzierungskonzept (Schritt 4 und 5 der Praesentation)
- `skills/finanzierung/cashflow-modell.md` -- Erstellt die detaillierte Cashflow-Projektion (Schritt 5 der Praesentation)
- `skills/ankauf/marktanalyse.md` -- Erstellt die Standortanalyse (Schritt 3 der Praesentation)
- `skills/objektpruefung/unterlagen-analyst.md` -- Analysiert Objektunterlagen fuer die Zustandsbewertung
- `skills/objektpruefung/risiko-scanner.md` -- Identifiziert Risiken fuer die Risikomitigierung
- `knowledge/kalkulationsformeln.md` -- Renditekennzahlen, DSCR-Berechnung
- `knowledge/rechtsgrundlagen.md` -- BGB-Referenzen fuer Mieterhoehung und Modernisierungsumlage
- `knowledge/marktbenchmarks.md` -- Benchmarks fuer Sanierungskosten und Mietvergleiche
- `knowledge/risikobewertung.md` -- Risiko-Framework fuer systematische Risikoanalyse
