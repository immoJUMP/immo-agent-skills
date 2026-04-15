# Bankenkonzept -- Finanzierungskonzept fuer die Bank erstellen

Erstellt ein vollstaendiges, bankenfertiges Finanzierungskonzept fuer den Ankauf einer Wohnimmobilie. Das Konzept zeigt der Bank nachvollziehbar: Ist-Zustand, geplante Wertschoepfung, Finanzierungsstruktur, Kapitaldienstfaehigkeit und Exit-Szenarien. Ziel ist eine Finanzierungszusage -- im Idealfall mit reduziertem oder ohne Eigenkapitaleinsatz.

> **Praxis-Insight:** Ein Investor hat mit exakt dieser Struktur zwei 1-Mio-Euro-Deals mit NULL Eigenkapital finanziert bekommen. Die Bank sagte: "Der hat sich wirklich Gedanken gemacht." Der Schluessel: Ist-Mieten → organischer Mietanstieg → Modernisierung → tilgungsfreies Jahr 1 → Cashflow-positiv ab Jahr 2.

---

## Wann diesen Skill nutzen

- Du hast ein konkretes Ankaufsobjekt und brauchst eine Bankfinanzierung
- Du willst der Bank zeigen, dass du einen durchdachten Plan hast
- Du bereitest ein Erstgespraech oder Zweitgespraech mit dem Firmenkundenberater vor
- Du willst eine 100%-Finanzierung oder 110%-Finanzierung (inkl. Nebenkosten) argumentieren
- Du musst die Kapitaldienstfaehigkeit nachweisen

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
    "condition": "teilsaniert | unsaniert | vollsaniert | Neubau",
    "plot_size_sqm": 800
  },
  "purchase": {
    "asking_price_eur": 850000,
    "offered_price_eur": 780000,
    "buyer_commission_pct": 3.57,
    "grunderwerbsteuer_pct": 6.5,
    "notar_grundbuch_pct": 2.0
  },
  "current_rents": {
    "cold_rent_monthly_eur": 3200,
    "vacancy_units": 1,
    "vacancy_since": "2024-06-01",
    "rent_roll_available": true
  },
  "planned_measures": {
    "organic_rent_increase": true,
    "modernization_planned": true,
    "modernization_budget_eur": 120000,
    "re_letting_target_rent_eur_sqm": 8.50
  },
  "financing_preferences": {
    "equity_available_eur": 0,
    "target_loan_to_value_pct": 100,
    "desired_fixed_rate_years": 10,
    "tilgungsfrei_months": 12,
    "sondertilgung_pct": 5
  }
}
```

### Optionale Angaben

```json
{
  "existing_portfolio": {
    "total_units": 35,
    "total_value_eur": 3500000,
    "annual_rental_income_eur": 280000,
    "existing_loans_eur": 2800000,
    "monthly_surplus_eur": 8500
  },
  "bank_valuation": {
    "beleihungswert_eur": null,
    "beleihungsauslauf_pct": null
  },
  "comparable_properties": [
    {
      "address": "Beispielstr. 5, gleiche Stadt",
      "purchase_price_eur": 900000,
      "units": 7,
      "price_per_sqm": 1650,
      "rent_per_sqm": 8.20,
      "factor": 18.5
    }
  ],
  "mietspiegel_data": {
    "average_rent_per_sqm": 7.80,
    "upper_range_per_sqm": 9.50,
    "applicable_category": "Baujahr 1960-1975, mittlere Lage, Standardausstattung"
  }
}
```

---

## Auftrag

Erstelle ein vollstaendiges Finanzierungskonzept, das der Bank zeigt:

1. **Warum dieses Objekt eine solide Investition ist** (Substanz + Potenzial)
2. **Wie der Kapitaldienst aus dem Objekt selbst bedient wird** (Kapitaldienstfaehigkeit)
3. **Dass du einen konkreten Massnahmenplan hast** (nicht nur "irgendwann Miete erhoehen")
4. **Welche Sicherheiten und Exit-Optionen bestehen** (Risikomitigierung fuer die Bank)

---

## Strategie

### Schritt 1: Ist-Situation analysieren

- Aktuelle Mieteinnahmen (Ist-Miete kalt) auflisten, pro Einheit wenn moeglich
- Leerstand identifizieren und bewerten (seit wann, warum, behebbar?)
- Ist-Miete vs. Mietspiegel vergleichen: Wie viel Potenzial steckt in den Bestandsmieten?
- Zustand des Objekts bewerten: Was muss gemacht werden, was ist Kuer?
- Aktuelle Bruttomietrendite und Kaufpreisfaktor berechnen

### Schritt 2: Soll-Situation definieren

- Zielmieten nach Massnahmen festlegen (realistisch, mietspiegelkonform)
- Neuvermietungsmieten fuer Leerstand und Fluktuation kalkulieren
- Modernisierungsumlage nach §559 BGB berechnen (max. 8% p.a. der Modernisierungskosten, Kappungsgrenze beachten)
- Ziel-Bruttomietrendite und Ziel-Kaufpreisfaktor nach Massnahmen berechnen

### Schritt 3: Massnahmenplan erstellen (Jahresschritte)

- **Jahr 1:** Organische Mieterhoehung (§558 BGB, Kappungsgrenze 15-20%), Leerstand beseitigen, tilgungsfreie Phase nutzen
- **Jahr 2:** Erste Modernisierungsmassnahmen (z.B. Fenster, Heizung, Fassade), Modernisierungsumlage ansetzen
- **Jahr 3:** Weitere Massnahmen, Neuvermietung bei Fluktuation zu Marktmiete
- **Jahr 4-5:** Stabilisierungsphase, Sondertilgungen wenn Cashflow positiv
- Fuer jeden Schritt: Kosten, erwartete Mehrmieteinnahmen, Zeitrahmen

### Schritt 4: Finanzierungsstruktur berechnen

- Gesamtinvestition: Kaufpreis + Grunderwerbsteuer + Notar/Grundbuch + Makler + Sanierungskosten
- Darlehensbetrag vs. Eigenkapitaleinsatz
- Beleihungswert schaetzen (konservativ: 80-90% des Kaufpreises)
- Beleihungsauslauf (BLA) berechnen: Darlehensbetrag / Beleihungswert
- Sollzins und Effektivzins einordnen (marktabhaengig)
- Annuitaet berechnen (Zins + Tilgung)

### Schritt 5: Tilgungsplan mit Szenarien erstellen

- **Szenario A:** Tilgungsfreie Phase (12-24 Monate) → dann 2% Tilgung
- **Szenario B:** Sofort 2% Tilgung, keine tilgungsfreie Phase
- **Szenario C:** 1% Tilgung + jaehrliche Sondertilgung aus Cashflow-Ueberschuss
- Fuer jedes Szenario: Restschuld nach Zinsbindung, Gesamtkosten, monatliche Rate

### Schritt 6: Kapitaldienstfaehigkeit (DSCR) berechnen

- DSCR = Nettomieteinnahmen (nach nicht umlagefaehigen Kosten) / Annuitaet
- Zielwert: DSCR >= 1,20 (Bank will min. 120% Deckung)
- DSCR fuer Ist-Zustand UND Soll-Zustand berechnen
- Stresstest: DSCR bei +2% Zinsanstieg nach Zinsbindungsende

### Schritt 7: Exit-Szenarien darstellen

- **Bestandshaltung:** Langfristiger Cashflow, Entschuldung ueber 25-30 Jahre
- **Verkauf nach Wertsteigerung:** Erwarteter Verkaufspreis nach Massnahmen (Faktor x Jahresmiete)
- **Aufteilung in ETW:** Abgeschlossenheitserklaerung → Einzelverkauf (hoehere qm-Preise)
- Fuer jedes Szenario: Eigenkapital-Rueckfluss berechnen

### Schritt 8: Eigenkapital-Rueckfluss berechnen

- Eingesetztes Eigenkapital (ggf. 0 bei 100%-Finanzierung)
- Jaehrlicher Cashflow nach Kapitaldienst
- Tilgung als Vermoegensaufbau beruecksichtigen
- Steuerliche Effekte (AfA, Zinsabzug) grob einordnen
- EK-Rueckfluss p.a. = (Cashflow + Tilgung + Steuerersparnis) / eingesetztes EK

### Schritt 9: Referenzobjekte als Vergleich

- Mind. 2-3 vergleichbare Objekte aus der gleichen Region
- Kaufpreis/qm, Miete/qm, Faktor vergleichen
- Zeigen: "Mein Objekt liegt im Markt" oder "Mein Objekt ist unterdurchschnittlich bewertet = Chance"

---

## Ausgabeformat

```markdown
# Finanzierungskonzept: [Objektbezeichnung]
## Erstellt am: [Datum]
## Investor: [Name / Firma]

---

### 1. Executive Summary

| Kennzahl | Wert |
|----------|------|
| Objekttyp | MFH, 8 WE, BJ 1965 |
| Kaufpreis | 780.000 EUR |
| Gesamtinvestition | 965.000 EUR |
| Ist-Miete (kalt, p.a.) | 38.400 EUR |
| Soll-Miete (kalt, p.a.) | 52.800 EUR |
| Ist-Faktor / Ist-Rendite | 20,3x / 4,9% |
| Soll-Faktor / Soll-Rendite | 14,8x / 6,8% |
| DSCR (Ist) | 1,05 |
| DSCR (Soll, ab Jahr 3) | 1,42 |
| Eigenkapitaleinsatz | 0 EUR |

---

### 2. Ist-Situation

#### 2.1 Mieteinnahmen aktuell

| WE | Flaeche (qm) | Ist-Miete (EUR/qm) | Ist-Miete (EUR/Monat) | Mietspiegel (EUR/qm) | Potenzial |
|----|---------------|---------------------|-----------------------|----------------------|-----------|
| 1  | 65            | 5,50                | 357,50                | 7,80                 | +42%      |
| 2  | 70            | 6,00                | 420,00                | 7,80                 | +30%      |
| ...| ...           | ...                 | ...                   | ...                  | ...       |

**Gesamtmiete Ist:** 3.200 EUR/Monat = 38.400 EUR/Jahr
**Leerstand:** 1 WE (seit 06/2024)
**Durchschnittsmiete:** 5,85 EUR/qm (Mietspiegel: 7,80 EUR/qm)

#### 2.2 Objektzustand

- Dach: [Zustand]
- Fenster: [Zustand]
- Heizung: [Typ, Alter]
- Fassade: [Zustand]
- Elektrik: [Zustand]
- Baeder/Kuechen: [Zustand]

---

### 3. Soll-Situation (Ziel nach 36 Monaten)

| WE | Flaeche (qm) | Ziel-Miete (EUR/qm) | Ziel-Miete (EUR/Monat) | Massnahme |
|----|---------------|----------------------|------------------------|-----------|
| 1  | 65            | 7,50                 | 487,50                 | Mieterhoehung §558 |
| 2  | 70            | 7,80                 | 546,00                 | Modernisierungsumlage |
| 8  | 60            | 8,50                 | 510,00                 | Neuvermietung |

**Gesamtmiete Soll:** 4.400 EUR/Monat = 52.800 EUR/Jahr

---

### 4. Massnahmenplan

| Zeitraum | Massnahme | Kosten (EUR) | Mehrmiete (EUR/Monat) | Rechtsgrundlage |
|----------|-----------|--------------|----------------------|-----------------|
| Monat 1-3 | Leerstand beseitigen (Neuvermietung) | 2.000 | +510 | Marktmiete |
| Monat 4-12 | Organische Mieterhoehung (Bestand) | 0 | +380 | §558 BGB |
| Monat 13-18 | Fenstertausch + Heizungsmodernisierung | 85.000 | +210 | §559 BGB |
| Monat 19-24 | Badsanierung bei Mieterwechsel | 35.000 | +100 | Neuvermietung |
| Monat 25-36 | Stabilisierung, Sondertilgung | 0 | -- | -- |

---

### 5. Finanzierungsstruktur

| Position | Betrag (EUR) |
|----------|-------------|
| Kaufpreis | 780.000 |
| Grunderwerbsteuer (6,5%) | 50.700 |
| Notar + Grundbuch (2,0%) | 15.600 |
| Maklerprovision (3,57%) | 27.846 |
| Sanierungsbudget | 120.000 |
| **Gesamtinvestition** | **994.146** |

| Finanzierung | Betrag (EUR) |
|--------------|-------------|
| Bankdarlehen | 994.146 |
| Eigenkapital | 0 |
| **Beleihungsauslauf** | **ca. 142%** |

**Anmerkung zum BLA:** Der Beleihungsauslauf bezieht sich auf den Kaufpreis. Nach Umsetzung der Massnahmen und Mietsteigerung sinkt der wirtschaftliche BLA auf Basis des gestiegenen Ertragswerts auf ca. 105%.

#### Konditionen (angenommen)

| Parameter | Wert |
|-----------|------|
| Sollzins | 3,80% |
| Effektivzins | 3,92% |
| Zinsbindung | 10 Jahre |
| Anfaengliche Tilgung | 2,00% |
| Tilgungsfreie Anlaufphase | 12 Monate |
| Sondertilgung p.a. | 5% |

---

### 6. Tilgungsplan & Szenarien

#### Szenario A: Tilgungsfrei Jahr 1, dann 2% Tilgung

| Jahr | Rate/Monat (EUR) | davon Zins | davon Tilgung | Restschuld (EUR) | Cashflow/Monat |
|------|-----------------|------------|---------------|-------------------|----------------|
| 1    | 3.148           | 3.148      | 0             | 994.146           | +562           |
| 2    | 4.805           | 3.148      | 1.657         | 974.268           | +105           |
| 3    | 4.805           | 3.085      | 1.720         | 953.620           | +495           |
| ...  | ...             | ...        | ...           | ...               | ...            |
| 10   | 4.805           | 2.650      | 2.155         | 812.340           | +1.095         |

#### Szenario B: Sofort 2% Tilgung
[Analog berechnet]

#### Szenario C: 1% Tilgung + Sondertilgung
[Analog berechnet]

---

### 7. Kapitaldienstfaehigkeit (DSCR)

| Zeitpunkt | Nettomieteinnahmen (EUR/Jahr) | Annuitaet (EUR/Jahr) | DSCR |
|-----------|-------------------------------|----------------------|------|
| Ist (Jahr 1, tilgungsfrei) | 38.400 - 6.000 = 32.400 | 37.776 | 0,86 |
| Jahr 1 (nach Neuvermietung) | 44.520 - 6.000 = 38.520 | 37.776 | 1,02 |
| Jahr 2 (nach Mieterhoehung) | 49.080 - 6.000 = 43.080 | 57.660 | 0,75 |
| Jahr 3 (nach Modernisierung) | 52.800 - 7.200 = 45.600 | 57.660 | 0,79 |
| **Jahr 3 (Szenario A)** | **52.800 - 7.200 = 45.600** | **57.660** | **1,42** |

> **Hinweis:** Die Bank bewertet die DSCR typischerweise auf Basis der nachhaltigen Miete. Zeige sowohl Ist als auch Soll.

#### Stresstest: Zinsanstieg +2% nach Zinsbindung

| Parameter | Wert |
|-----------|------|
| Restschuld nach 10 Jahren | 812.340 EUR |
| Neuer Sollzins | 5,80% |
| Annuitaet (neu, 2% Tilgung) | 5.280 EUR/Monat |
| Mieteinnahmen (konservativ) | 52.800 EUR/Jahr |
| DSCR (Stresstest) | 1,18 |

---

### 8. Eigenkapital-Rueckfluss

| Position | Jahr 1 | Jahr 3 | Jahr 5 | Jahr 10 |
|----------|--------|--------|--------|---------|
| Cashflow kumuliert | 6.744 | 24.000 | 52.000 | 120.000 |
| Tilgung kumuliert | 0 | 40.600 | 82.000 | 181.800 |
| Steuerersparnis kumuliert (geschaetzt) | 4.000 | 15.000 | 28.000 | 55.000 |
| **Vermoegensaufbau gesamt** | **10.744** | **79.600** | **162.000** | **356.800** |

> Bei 0 EUR Eigenkapitaleinsatz: Unendliche EK-Rendite (mathematisch). De facto: reiner Vermoegensaufbau aus dem Objekt heraus.

---

### 9. Exit-Szenarien

#### Szenario A: Bestandshaltung (25+ Jahre)

- Vollstaendige Entschuldung ueber Laufzeit
- Langfristiger Cashflow steigt mit Mieterhoehungen
- Objektwert steigt mit Inflation und Massnahmen

#### Szenario B: Verkauf nach 10 Jahren

| Parameter | Wert |
|-----------|------|
| Jahresmiete (Jahr 10) | 55.000 EUR |
| Verkaufsfaktor | 18x |
| Geschaetzter Verkaufspreis | 990.000 EUR |
| Restschuld | 812.340 EUR |
| Erloees nach Tilgung | 177.660 EUR |
| + kumulierter Cashflow | 120.000 EUR |
| **Gesamtertrag** | **297.660 EUR** |

#### Szenario C: Aufteilung in ETW

| Parameter | Wert |
|-----------|------|
| Kosten Abgeschlossenheitserklaerung | 15.000 EUR |
| Geschaetzter ETW-Preis/qm | 2.200 EUR |
| Gesamtverkaufserloees | 1.144.000 EUR |
| Restschuld + Kosten | 830.000 EUR |
| **Nettoerloees** | **314.000 EUR** |

---

### 10. Referenzobjekte

| Objekt | Kaufpreis | EUR/qm | Miete EUR/qm | Faktor | Anmerkung |
|--------|-----------|--------|--------------|--------|-----------|
| Beispielstr. 5 | 900.000 | 1.650 | 8,20 | 18,5 | Vergleichbar, saniert |
| Musterweg 12 | 720.000 | 1.440 | 7,00 | 17,1 | Gleiche Lage, unsaniert |
| **Unser Objekt** | **780.000** | **1.500** | **5,85 → 8,50** | **20,3 → 14,8** | **Unterbewertetes Potenzial** |

---

### Anlagen

- [ ] Mietliste / Mietaufstellung
- [ ] Grundbuchauszug
- [ ] Energieausweis
- [ ] Fotos (Aussen + Innen)
- [ ] Lageplan / Flurkarte
- [ ] Wirtschaftsplan (falls WEG)
- [ ] Sanierungskostenaufstellung (Handwerkerangebote)
- [ ] Selbstauskunft Investor
- [ ] Bestandsportfolio-Uebersicht
```

---

## Qualitaetspruefung

Pruefe das Konzept gegen diese Kriterien:

- [ ] **Plausibilitaet der Mieterhoehungen:** Sind die Zielmieten realistisch und durch Mietspiegel gedeckt?
- [ ] **Kappungsgrenze beachtet:** Max. 15% (angespannter Markt) oder 20% in 3 Jahren (§558 Abs. 3 BGB)
- [ ] **Modernisierungsumlage korrekt:** Max. 8% p.a. der umlagefaehigen Kosten, Kappungsgrenze 2-3 EUR/qm (§559 BGB)
- [ ] **DSCR realistisch:** Ist die DSCR > 1,0 erreichbar? Wann?
- [ ] **Stresstest bestanden:** Haelt das Konzept +2% Zinsanstieg aus?
- [ ] **Nicht umlagefaehige Kosten vollstaendig:** Instandhaltung, Verwaltung, Leerstandsrisiko beruecksichtigt?
- [ ] **Zeitplan realistisch:** Koennen die Massnahmen in der geplanten Zeit umgesetzt werden?
- [ ] **Sanierungskosten marktgerecht:** Sind die Kostenansaetze realistisch (nicht zu niedrig geschaetzt)?
- [ ] **Bankenperspektive eingenommen:** Wuerde ein Firmenkundenberater dieses Konzept als fundiert bewerten?

---

## Warnsignale & Dealbreaker

| Warnsignal | Bewertung | Handlungsempfehlung |
|------------|-----------|---------------------|
| DSCR < 1,0 im Ist-Zustand ohne klaren Pfad zu > 1,0 | KRITISCH | Finanzierung wird schwierig, Konzept ueberarbeiten |
| Beleihungsauslauf > 130% ohne Zusatzsicherheiten | HOCH | Weitere Sicherheiten einbringen oder Kaufpreis verhandeln |
| Zielmieten > 20% ueber Mietspiegel | KRITISCH | Unglaubwuerdig fuer die Bank, Zielmieten korrigieren |
| Sanierungskosten nicht durch Angebote belegt | MITTEL | Handwerkerangebote oder Kostenschaetzungen einholen |
| Kein Track Record als Investor | MITTEL | Bestandsportfolio oder Berufserfahrung hervorheben |
| Leerstand > 30% ohne klare Ursache | HOCH | Leerstandsgruende analysieren, Vermietbarkeit pruefen |
| Negative Cashflow-Prognose ueber > 3 Jahre | KRITISCH | Finanzierungsstruktur ueberarbeiten (mehr Tilgungsfrei, weniger Tilgung) |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Mietspiegel | Lokalen Mietspiegel recherchieren oder konservativ mit Durchschnitt der Region arbeiten |
| Sanierungskosten | Marktbenchmarks verwenden: Vollsanierung 800-1.200 EUR/qm, Teilsanierung 300-600 EUR/qm |
| Sollzins | Aktuellen Markt einschaetzen (Stand pruefen), Szenario mit Bandbreite rechnen |
| Beleihungswert | Konservativ mit 80-90% des Kaufpreises ansetzen |
| Energieausweis | Auf Basis des Baujahrs und Zustands schaetzen, aber als Luecke markieren |
| Bestandsportfolio | Konzept auch ohne Portfolio erststellbar, aber Bonitas-Einschaetzung wird schwieriger |

> **Wichtig:** Fehlende Daten immer transparent kennzeichnen. Banken schaetzen Ehrlichkeit mehr als Luecken zu kaschieren.

---

## Konfidenz-Bewertung

Bewerte die Gesamtqualitaet des Konzepts:

| Konfidenz | Kriterien |
|-----------|-----------|
| **HOCH** (90%+) | Vollstaendige Mietliste, Mietspiegel vorhanden, Handwerkerangebote fuer Sanierung, DSCR > 1,2 ab Jahr 2, Bestandsportfolio vorhanden |
| **MITTEL** (70-89%) | Mietliste vorhanden aber Mietspiegel geschaetzt, Sanierungskosten auf Basis Benchmarks, DSCR > 1,0 ab Jahr 2 |
| **NIEDRIG** (< 70%) | Wesentliche Daten fehlen (z.B. keine Mietliste), Zielmieten nicht durch Mietspiegel gedeckt, DSCR < 1,0 auch nach Massnahmen |

---

## Verwandte Wissensdatenbanken

- `knowledge/kalkulationsformeln.md` -- Renditekennzahlen, Faktoren, DSCR-Berechnung
- `knowledge/rechtsgrundlagen.md` -- §558 BGB (Mieterhoehung), §559 BGB (Modernisierungsumlage), Kappungsgrenze
- `knowledge/marktbenchmarks.md` -- Sanierungskosten, Mietbenchmarks nach Baujahr und Lage
- `knowledge/risikobewertung.md` -- Risiko-Scoring fuer Bankenpraesentation
- `skills/finanzierung/cashflow-modell.md` -- Detaillierte Cashflow-Projektion fuer dieses Konzept
- `skills/finanzierung/bankenpitch.md` -- Praesentationsdokument auf Basis dieses Konzepts
