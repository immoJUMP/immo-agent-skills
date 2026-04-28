---
description: "Erstellt eine 5-Jahres-Cashflow-Projektion mit drei Szenarien (Best/Base/Worst Case) und Break-even-Analyse. Nutze diesen Skill wenn du wissen willst wann der Deal cashflow-positiv wird, Szenarien durchspielen oder eine Projektion fuers Bankkonzept brauchst."
---

# Cashflow-Modell -- 5-Jahres-Cashflow-Projektion mit Szenarien

Erstellt eine detaillierte 5-Jahres-Cashflow-Projektion fuer eine Wohnimmobilie mit drei Szenarien (Best Case, Base Case, Worst Case). Modelliert Mieterhoehungsrunden, Leerstandsrisiken, Instandhaltungskosten und Zinssensitivitaet. Beantwortet die zentrale Frage: "Wann bin ich Cashflow-positiv?"

> **Praxis-Insight:** Banken und erfahrene Investoren unterscheiden zwischen "der Deal sieht auf dem Papier gut aus" und "der Investor hat durchgerechnet, was passiert wenn es anders laeuft". Dieses Modell zeigt beides -- und genau das ueberzeugt Banken, auch bei 100%-Finanzierungen.

---

## Wann diesen Skill nutzen

- Du hast ein konkretes Objekt und willst den Cashflow ueber 5 Jahre modellieren
- Du willst pruefen, ob ein Deal cashflow-positiv wird (und wann)
- Du brauchst eine Cashflow-Projektion fuer den Bankenpitch
- Du willst Szenarien durchspielen: Was wenn Zinsen steigen? Was wenn Leerstand steigt?
- Du planst Mieterhoehungsrunden und willst den ROI jeder Runde sehen
- Du ueberlegst, ob sich Auszugsgeld (Mieterabfindung) fuer eine Neuvermietung lohnt

---

## Was du bereitstellen musst

### Pflichtangaben

```json
{
  "property": {
    "address": "Strasse, PLZ, Stadt",
    "units": 8,
    "total_sqm": 520
  },
  "rent_roll": [
    {
      "unit": "WE 1",
      "sqm": 65,
      "current_rent_per_sqm": 5.50,
      "current_rent_monthly": 357.50,
      "tenant_since": "2015-03-01",
      "contract_type": "unbefristet",
      "last_rent_increase": "2020-01-01"
    }
  ],
  "financing": {
    "loan_amount_eur": 994146,
    "interest_rate_pct": 3.80,
    "repayment_rate_pct": 2.00,
    "fixed_rate_period_years": 10,
    "tilgungsfrei_months": 12,
    "sondertilgung_pct": 5.0
  },
  "costs": {
    "hausgeld_monthly_eur": 1600,
    "non_recoverable_costs_monthly_eur": 500,
    "instandhaltung_per_sqm_year": 12.00,
    "verwaltung_per_unit_month": 25.00
  }
}
```

### Optionale Angaben

```json
{
  "mietspiegel": {
    "average_rent_per_sqm": 7.80,
    "upper_range_per_sqm": 9.50,
    "kappungsgrenze_pct": 20,
    "kappungsgrenze_years": 3,
    "angespannter_markt": false
  },
  "planned_measures": {
    "modernization_budget_eur": 120000,
    "modernization_start_month": 13,
    "modernization_duration_months": 6,
    "target_rent_after_modernization_per_sqm": 8.50
  },
  "assumptions": {
    "rent_increase_pct_pa": 2.0,
    "vacancy_rate_pct": 3.0,
    "inflation_pct_pa": 2.0,
    "cost_increase_pct_pa": 2.5,
    "income_tax_rate_pct": 42.0,
    "afa_pct": 2.0,
    "interest_rate_after_fixation_pct": 5.50
  },
  "auszugsgeld_scenario": {
    "unit": "WE 3",
    "current_rent_monthly": 320.00,
    "target_rent_monthly": 560.00,
    "auszugsgeld_eur": 5000,
    "renovation_cost_eur": 8000,
    "expected_vacancy_months": 2
  }
}
```

---

## Auftrag

Erstelle eine vollstaendige 5-Jahres-Cashflow-Projektion mit:

1. **Jahr-fuer-Jahr-Modell** mit allen relevanten Ein- und Ausgaben
2. **Drei Szenarien** (Best Case / Base Case / Worst Case)
3. **Mieterhoehungsrunden** modelliert als konkrete Schritte
4. **Sensitivitaetsanalyse** fuer die kritischen Variablen
5. **Auszugsgeld-ROI** wenn relevant
6. **Klare Antwort** auf die Frage: "Wann bin ich Cashflow-positiv?"

---

## Strategie

### Schritt 1: Mieteinnahmen-Entwicklung modellieren

- Aktuelle Mieteinnahmen aus Mietliste summieren
- Mieterhoehungsrunden planen:
  - **Runde 1 (Ist → Neuvermietung):** Leerstaende zu Marktmiete vermieten (sofort moeglich)
  - **Runde 2 (Mieterhoehung 1):** Bestandsmieten erhoehen nach §558 BGB (fruehestens 12 Monate nach letzter Erhoehung, Kappungsgrenze beachten)
  - **Runde 3 (Modernisierung):** Modernisierungsumlage nach §559 BGB ansetzen
  - **Runde 4 (Mieterhoehung 2):** Erneute Erhoehung nach Ablauf der Sperrfrist
- Fluktuation einrechnen: Bei Auszug zu Marktmiete neu vermieten (ca. 10% Fluktuation p.a.)
- Indexierung fuer Mietsteigerung p.a. (organisches Wachstum ueber Mietspiegel)

### Schritt 2: Kosten-Entwicklung modellieren

- **Nicht umlagefaehige Kosten:** Verwaltung, Instandhaltungsruecklage (Anteil Eigentuemer), Leerstandskosten
- **Hausgeld:** Gesamthausgeld minus umlagefaehiger Anteil = nicht umlagefaehiger Anteil
- **Instandhaltung:** 10-15 EUR/qm/Jahr (altersabhaengig), jaehrlich steigend mit Inflation
- **Sonderumlagen:** Ggf. bekannte grosse Massnahmen einplanen (Dach, Heizung)
- **Verwaltungskosten:** 20-30 EUR/WE/Monat, jaehrlich steigend
- **Mietausfallrisiko:** 2-5% der Sollmiete (abhaengig von Lage und Mieterklientel)

### Schritt 3: Annuitaet und Kapitaldienst berechnen

- Monat fuer Monat oder Jahr fuer Jahr:
  - Zinsanteil = Restschuld x Sollzins / 12
  - Tilgungsanteil = Annuitaet - Zinsanteil (0 in tilgungsfreier Phase)
  - Restschuld = Vormonat - Tilgungsanteil
- Tilgungsfreie Phase separat modellieren (nur Zinszahlung)
- Sondertilgungen einplanen wenn Cashflow-Ueberschuss vorhanden
- Anschlussfinanzierung nach Zinsbindung mit hoeherem Zins modellieren

### Schritt 4: Cashflow vor Steuern berechnen

- **Cashflow vor Steuern = Nettomieteinnahmen - Nicht umlagefaehige Kosten - Annuitaet**
- Pro Jahr auflisten, kumuliert darstellen
- Breakeven-Punkt identifizieren: Wann wird der Cashflow erstmals positiv?

### Schritt 5: Steuerliche Effekte einrechnen

- **AfA:** 2% linear (Gebaeude, BJ ab 1925) oder 2,5% (BJ vor 1925) oder 3% (BJ ab 2023)
- **Zinsabzug:** Darlehenszinsen sind Werbungskosten
- **Abschreibung Sanierung:** Anschaffungsnahe Herstellungskosten vs. Erhaltungsaufwand (15%-Grenze in 3 Jahren nach Kauf beachten)
- **Steuerersparnis** = (AfA + Zinsen + absetzbare Kosten - Mieteinnahmen) x persoenlicher Steuersatz
- **Cashflow nach Steuern** = Cashflow vor Steuern + Steuerersparnis (oder - Steuerlast)

### Schritt 6: Drei Szenarien erstellen

- **Best Case:** Zielmieten erreicht, minimaler Leerstand (2%), keine unerwarteten Kosten, Zinsniveau stabil
- **Base Case:** Mieterhoehungen zu 80% umgesetzt, moderater Leerstand (4%), normale Instandhaltung, Zinsanstieg +1%
- **Worst Case:** Mieterhoehungen verzoegert/reduziert, hoher Leerstand (8%), Sonderumlage in Jahr 3, Zinsanstieg +2%

### Schritt 7: Auszugsgeld-Rechner (wenn relevant)

- Investment: Auszugsgeld + Renovierungskosten + Mietausfall waehrend Leerstand
- Return: Differenz alte Miete vs. neue Miete (monatlich)
- ROI = (jaehrliche Mehrmieteinnahme / Gesamtinvestment) x 100
- Amortisationsdauer = Gesamtinvestment / monatliche Mehrmieteinnahme
- Entscheidungsregel: ROI > 20% und Amortisation < 3 Jahre = sinnvoll

### Schritt 8: Sensitivitaetsanalyse

- **Variable 1: Zinsen** -- Was passiert bei +1%, +2%, +3% nach Zinsbindungsende?
- **Variable 2: Leerstand** -- Was passiert bei 5%, 10%, 15% Leerstandsquote?
- **Variable 3: Mietsteigerung** -- Was passiert bei 0%, 1%, 2%, 3% p.a.?
- **Variable 4: Instandhaltungskosten** -- Was passiert bei +50%, +100% der geplanten Kosten?
- Ergebnis als Matrix: Welche Kombination fuehrt zu negativem Cashflow?

---

## Ausgabeformat

```markdown
# 5-Jahres-Cashflow-Modell: [Objektbezeichnung]
## Erstellt am: [Datum]

---

### 1. Zusammenfassung

| Kennzahl | Best Case | Base Case | Worst Case |
|----------|-----------|-----------|------------|
| Cashflow-positiv ab | Monat 3 | Monat 14 | Monat 30 |
| Kumulierter Cashflow (5 Jahre) | +85.000 EUR | +42.000 EUR | -12.000 EUR |
| DSCR Durchschnitt (5 Jahre) | 1,45 | 1,22 | 0,95 |
| EK-Rendite (Cash-on-Cash) | n/a (0 EK) | n/a (0 EK) | n/a (0 EK) |

**Kernaussage:** [z.B. "Das Objekt wird im Base Case ab Monat 14 cashflow-positiv. Selbst im Worst Case bleibt der negative Cashflow auf unter 12.000 EUR begrenzt und ist durch Liquiditaetsreserven abdeckbar."]

---

### 2. Mieterhoehungsrunden

| Runde | Zeitpunkt | Massnahme | Betroffene WE | Miete vorher (EUR/Monat) | Miete nachher (EUR/Monat) | Delta (EUR/Monat) |
|-------|-----------|-----------|---------------|--------------------------|---------------------------|-------------------|
| 1 | Monat 1-3 | Neuvermietung Leerstand | WE 8 | 0 | 510 | +510 |
| 2 | Monat 6-12 | Mieterhoehung §558 | WE 1-4 | 1.500 | 1.880 | +380 |
| 3 | Monat 13-18 | Modernisierungsumlage §559 | WE 2, 5, 6 | 1.350 | 1.560 | +210 |
| 4 | Monat 24-30 | Mieterhoehung §558 (2. Runde) | WE 1-4 | 1.880 | 2.050 | +170 |
| 5 | Fluktuation | Neuvermietung bei Auszug | variabel | variabel | Marktmiete | variabel |

**Mieteinnahmen-Entwicklung:**

| | Ist | Jahr 1 | Jahr 2 | Jahr 3 | Jahr 4 | Jahr 5 |
|--|-----|--------|--------|--------|--------|--------|
| Sollmiete (EUR/Monat) | 3.200 | 4.090 | 4.400 | 4.600 | 4.700 | 4.800 |
| Sollmiete (EUR/Jahr) | 38.400 | 49.080 | 52.800 | 55.200 | 56.400 | 57.600 |
| Ø EUR/qm | 5,85 | 7,48 | 8,08 | 8,46 | 8,65 | 8,85 |

---

### 3. Cashflow-Projektion: Base Case

| Position | Jahr 1 | Jahr 2 | Jahr 3 | Jahr 4 | Jahr 5 |
|----------|--------|--------|--------|--------|--------|
| **Mieteinnahmen (Soll)** | 49.080 | 52.800 | 55.200 | 56.400 | 57.600 |
| - Leerstandsrisiko (4%) | -1.963 | -2.112 | -2.208 | -2.256 | -2.304 |
| **= Effektive Mieteinnahmen** | **47.117** | **50.688** | **52.992** | **54.144** | **55.296** |
| | | | | | |
| - Nicht umlagefaehige NK | -6.000 | -6.150 | -6.304 | -6.461 | -6.623 |
| - Instandhaltung | -6.240 | -6.396 | -6.556 | -6.720 | -6.888 |
| - Verwaltung | -2.400 | -2.460 | -2.522 | -2.585 | -2.650 |
| **= Netto-Mieteinnahmen** | **32.477** | **35.682** | **37.610** | **38.378** | **39.135** |
| | | | | | |
| - Zinsen | -37.776 | -36.580 | -35.340 | -34.050 | -32.710 |
| - Tilgung | 0 | -19.882 | -20.536 | -21.210 | -21.905 |
| **= Cashflow vor Steuern** | **-5.299** | **-20.780** | **-18.266** | **-16.882** | **-15.480** |
| | | | | | |
| + AfA (2% auf Gebaeudeanteil) | +12.480 | +12.480 | +12.480 | +12.480 | +12.480 |
| + Zinsabzug (Steuerersparnis) | +15.866 | +15.364 | +14.843 | +14.301 | +13.738 |
| - Steuer auf Mietueberschuss | -5.200 | -5.800 | -6.200 | -6.400 | -6.600 |
| **= Steuereffekt netto** | **+23.146** | **+22.044** | **+21.123** | **+20.381** | **+19.618** |
| | | | | | |
| **= Cashflow nach Steuern** | **+17.847** | **+1.264** | **+2.857** | **+3.499** | **+4.138** |

---

### 4. Cashflow-Projektion: Best Case

| Position | Jahr 1 | Jahr 2 | Jahr 3 | Jahr 4 | Jahr 5 |
|----------|--------|--------|--------|--------|--------|
| Effektive Mieteinnahmen | 48.600 | 53.800 | 56.500 | 58.000 | 59.500 |
| - Gesamtkosten (ohne Kapital) | -13.500 | -14.000 | -14.500 | -15.000 | -15.500 |
| - Annuitaet | -37.776 | -56.462 | -55.876 | -55.260 | -54.615 |
| **Cashflow vor Steuern** | **-2.676** | **-16.662** | **-13.876** | **-12.260** | **-10.615** |
| Steuereffekt netto | +24.000 | +23.000 | +22.000 | +21.000 | +20.000 |
| **Cashflow nach Steuern** | **+21.324** | **+6.338** | **+8.124** | **+8.740** | **+9.385** |

---

### 5. Cashflow-Projektion: Worst Case

| Position | Jahr 1 | Jahr 2 | Jahr 3 | Jahr 4 | Jahr 5 |
|----------|--------|--------|--------|--------|--------|
| Effektive Mieteinnahmen | 43.200 | 46.000 | 48.000 | 49.000 | 50.000 |
| - Gesamtkosten (ohne Kapital) | -16.000 | -17.500 | -22.000 | -17.500 | -18.000 |
| - Annuitaet | -37.776 | -56.462 | -55.876 | -55.260 | -54.615 |
| **Cashflow vor Steuern** | **-10.576** | **-27.962** | **-29.876** | **-23.760** | **-22.615** |
| Steuereffekt netto | +20.000 | +19.000 | +18.500 | +18.000 | +17.500 |
| **Cashflow nach Steuern** | **+9.424** | **-8.962** | **-11.376** | **-5.760** | **-5.115** |

---

### 6. Auszugsgeld-Rechner

| Position | WE 3 |
|----------|------|
| Aktuelle Miete | 320 EUR/Monat |
| Zielmiete (Neuvermietung) | 560 EUR/Monat |
| **Mehrmieteinnahme** | **240 EUR/Monat = 2.880 EUR/Jahr** |
| | |
| Auszugsgeld | 5.000 EUR |
| Renovierungskosten | 8.000 EUR |
| Mietausfall (2 Monate) | 640 EUR |
| **Gesamtinvestment** | **13.640 EUR** |
| | |
| **ROI** | **21,1% p.a.** |
| **Amortisation** | **56,8 Monate (4,7 Jahre)** |
| **Empfehlung** | **Grenzwertig -- ROI ok, aber Amortisation > 3 Jahre** |

---

### 7. Sensitivitaetsanalyse

#### 7.1 Zinssensitivitaet (nach Zinsbindungsende)

| Zinssatz | Neue Annuitaet (EUR/Monat) | Cashflow/Monat (Jahr 11) | DSCR |
|----------|---------------------------|--------------------------|------|
| 3,80% (unveraendert) | 4.805 | +1.095 | 1,42 |
| 4,80% (+1%) | 5.480 | +420 | 1,25 |
| 5,80% (+2%) | 6.160 | -260 | 1,08 |
| 6,80% (+3%) | 6.840 | -940 | 0,92 |

> **Kritischer Zinssatz:** Ab ca. 5,50% wird der Cashflow negativ (ohne weitere Mieterhoehungen).

#### 7.2 Leerstandssensitivitaet

| Leerstandsquote | Mietausfall (EUR/Jahr) | Cashflow-Effekt vs. Base | DSCR-Effekt |
|-----------------|----------------------|--------------------------|-------------|
| 2% (Best) | -1.056 | +1.056 | +0,03 |
| 4% (Base) | -2.112 | 0 | 0 |
| 8% (Worst) | -4.224 | -2.112 | -0,06 |
| 15% (Stress) | -7.920 | -5.808 | -0,15 |

#### 7.3 Mietsteigerungssensitivitaet

| Mietsteigerung p.a. | Miete Jahr 5 (EUR/Monat) | Kumulierter Cashflow (5 Jahre) |
|---------------------|--------------------------|-------------------------------|
| 0% | 4.400 | +18.000 |
| 1% | 4.580 | +32.000 |
| 2% (Base) | 4.760 | +42.000 |
| 3% | 4.950 | +55.000 |

#### 7.4 Stress-Matrix: Zins x Leerstand

| | Leerstand 2% | Leerstand 5% | Leerstand 10% | Leerstand 15% |
|--|--------------|--------------|---------------|---------------|
| Zins 3,80% | +1.400 | +950 | +200 | -550 |
| Zins 4,80% | +720 | +270 | -480 | -1.230 |
| Zins 5,80% | +40 | -410 | -1.160 | -1.910 |
| Zins 6,80% | -640 | -1.090 | -1.840 | -2.590 |

*Werte = Cashflow/Monat in EUR, Jahr 5, Base-Case-Mieten*

> **Fazit:** Das Objekt haelt Zinsanstieg ODER Leerstand aus, aber nicht beides gleichzeitig in extremer Auspraegung.

---

### 8. Zusammenfassung: Wann bin ich Cashflow-positiv?

| Szenario | Cashflow-positiv ab (vor Steuern) | Cashflow-positiv ab (nach Steuern) |
|----------|----------------------------------|-------------------------------------|
| Best Case | Monat 3 | Monat 1 |
| Base Case | Monat 14 | Monat 1 |
| Worst Case | Monat 30 | Monat 1 (ausser Jahr 2-3) |

> **Wichtiger Hinweis:** "Cashflow-positiv" bedeutet hier den laufenden monatlichen Ueberschuss. Durch die tilgungsfreie Phase in Jahr 1 ist der Cashflow vor Steuern oft sofort positiv, kippt aber mit Tilgungsbeginn. Die nachhaltige Cashflow-Positivitaet (inkl. Tilgung) ist der relevante Wert.
```

---

## Qualitaetspruefung

Pruefe das Modell gegen diese Kriterien:

- [ ] **Mieteinnahmen plausibel:** Entsprechen die modellierten Mieten dem lokalen Mietspiegel?
- [ ] **Mieterhoehungen rechtskonform:** Kappungsgrenze, Sperrfristen, Begruendung beruecksichtigt?
- [ ] **Kosten vollstaendig:** Alle nicht umlagefaehigen Kosten erfasst (Verwaltung, Instandhaltung, Leerstand)?
- [ ] **Annuitaet korrekt:** Zins und Tilgung korrekt berechnet, tilgungsfreie Phase beruecksichtigt?
- [ ] **Steuerliche Effekte konservativ:** AfA-Satz korrekt, anschaffungsnahe Herstellungskosten beruecksichtigt?
- [ ] **Szenarien realistisch:** Best Case nicht zu optimistisch, Worst Case nicht zu extrem?
- [ ] **Sensitivitaet sinnvoll:** Kritische Variablen identifiziert und durchgerechnet?
- [ ] **Breakeven klar kommuniziert:** Eindeutige Antwort auf "Wann Cashflow-positiv?"

---

## Warnsignale & Dealbreaker

| Warnsignal | Bewertung | Handlungsempfehlung |
|------------|-----------|---------------------|
| Cashflow vor Steuern dauerhaft negativ (alle 5 Jahre) | KRITISCH | Deal ueberdenken oder Finanzierungsstruktur aendern |
| Cashflow nur durch Steuereffekte positiv | HOCH | Langfristig riskant -- Steuergesetze koennen sich aendern |
| DSCR < 1,0 im Base Case nach Jahr 2 | KRITISCH | Bank wird Finanzierung ablehnen |
| Worst Case fuehrt zu > 50.000 EUR kumuliertem Verlust | HOCH | Liquiditaetsreserve pruefen, ggf. mehr EK einbringen |
| Zinssensitivitaet: +1% Zins macht Deal negativ | HOCH | Laengere Zinsbindung waehlen oder Deal ueberdenken |
| Mieterhoehungen nur durch Modernisierung moeglich (Bestandsmieten am Mietspiegel) | MITTEL | Realistisch einschaetzen, ob Modernisierung wirtschaftlich ist |
| Auszugsgeld-ROI < 15% | NIEDRIG | Auszugsgeld vermeiden, auf natuerliche Fluktuation warten |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Detaillierte Mietliste | Gesamtmiete durch Anzahl WE teilen, Durchschnitts-qm schaetzen |
| Mietspiegel | Konservativ mit regionalen Durchschnittswerten arbeiten (ImmoScout24, Mietspiegel-Verzeichnis) |
| Nicht umlagefaehige Kosten | Benchmark: 15-20% der Bruttomiete als nicht umlagefaehig ansetzen |
| Instandhaltungskosten | Benchmark nach Baujahr: vor 1950: 15-20 EUR/qm/Jahr, 1950-1980: 12-15 EUR/qm/Jahr, nach 1980: 8-12 EUR/qm/Jahr |
| Steuersatz | Mit 42% rechnen (Spitzensteuersatz), Soli beachten |
| AfA-Bemessungsgrundlage | Gebaeudewertanteil: 70-80% des Kaufpreises (Bodenrichtwert fuer Grundstuecksanteil abziehen) |
| Zinssatz | Aktuellen Marktzins recherchieren, Szenario mit Bandbreite rechnen |

> **Wichtig:** Fehlende Daten mit konservativen Annahmen ersetzen und transparent kennzeichnen. Besser konservativ schaetzen als optimistisch raten.

---

## Konfidenz-Bewertung

| Konfidenz | Kriterien |
|-----------|-----------|
| **HOCH** (90%+) | Vollstaendige Mietliste mit Vertragsdaten, Mietspiegel vorhanden, alle Kosten bekannt, Finanzierungskonditionen fix, Handwerkerangebote fuer Modernisierung |
| **MITTEL** (70-89%) | Mietliste vorhanden aber unvollstaendig, Mietspiegel geschaetzt, Kosten auf Basis Benchmarks, Finanzierungskonditionen indikativ |
| **NIEDRIG** (< 70%) | Nur Gesamtmiete bekannt, keine Einzelaufstellung, Kosten und Mietspiegel geschaetzt, Finanzierungskonditionen unbekannt |

---

## Verwandte Wissensdatenbanken

- `knowledge/kalkulationsformeln.md` -- Renditekennzahlen, Cashflow-Formeln, AfA-Saetze
- `knowledge/rechtsgrundlagen.md` -- §558 BGB (Mieterhoehung), §559 BGB (Modernisierungsumlage), Kappungsgrenze, anschaffungsnahe Herstellungskosten
- `knowledge/marktbenchmarks.md` -- Instandhaltungskosten nach Baujahr, Verwaltungskosten-Benchmarks
- `skills/bankenpitch/SKILL.md` -- Finanzierungskonzept & Bankenpraesentation mit integrierter Cashflow-Darstellung
