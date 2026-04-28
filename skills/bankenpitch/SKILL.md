---
description: "Analysiert ein Kaufobjekt und erstellt eine bankenfertige 13-Sektionen-Praesentation mit Finanzierungskonzept, interaktivem HTML-Cashflow-Rechner, DSCR-Sensitivitaetsmatrix und Phasen-Cashflow. Nutze diesen Skill wenn du ein konkretes Objekt finanzieren willst -- von der Analyse bis zum fertigen Bankendokument in einem Schritt."
---

# Bankenpitch -- Finanzierungskonzept & Bankenpraesentation

Analysiert ein konkretes Kaufobjekt, rechnet das vollstaendige Finanzierungskonzept durch und verpackt alles in eine professionelle 13-Sektionen-Bankenpraesentation. Das Ergebnis ist ein bankenfertiges Dokument, das der Firmenkundenberater ohne Rueckfragen intern an Marktfolge und Kreditausschuss weiterreichen kann.

Dieser Skill vereint Analyse und Praesentation -- du gibst die Basisdaten ein, die KI rechnet alles durch (Kapitaldienstfaehigkeit, Szenarien, Sensitivitaet, Phasen-Cashflow) und liefert die fertige Praesentation.

> **Kategorie:** Finanzierung
> **Zielgruppe:** Wohnimmobilieninvestoren (MFH, 10-500+ Einheiten)
> **Zeitaufwand:** 10-20 Minuten

> **Praxis-Insight:** Ein Investor hat mit exakt dieser Struktur zwei 1-Mio-Euro-Deals mit NULL Eigenkapital finanziert bekommen. Die Bank sagte: "Er hat sich wirklich Gedanken gemacht." Der Schluessel: Ist-Mieten -> organische Mieterhoehung -> Modernisierung -> tilgungsfrei Jahr 1 -> Cashflow-positiv ab Jahr 2. Die Eigenleistungen des Investors (Neuvermietung, Mietverhandlungen, Projektmanagement Sanierung, Foerderkoordination) wurden marktueblich bewertet und als EK-Ersatz dargestellt -- Block 1 (Barmittel) plus Block 2 (bewertete Eigenleistungen) ergaben eine EK-Quote von ueber 15%, obwohl kein einziger Euro in Cash eingebracht wurde.

> **Ausgabeformate:** Das Ergebnis kann verwendet werden als: (a) Markdown-Dokument zur direkten Nutzung, (b) Input fuer Gamma.app zur Erzeugung einer designten PDF-Praesentation, (c) Input fuer Claude Code zur Erzeugung einer interaktiven HTML-Praesentation mit Slidern und DSCR-Matrix.

---

## Wann diesen Skill nutzen

- Du hast ein konkretes Ankaufsobjekt und brauchst eine Bankfinanzierung
- Du willst der Bank zeigen, dass du einen durchdachten Plan hast
- Du bereitest einen Ersttermin oder Zweitgespraech mit dem Firmenkundenberater vor
- Du willst eine 100%-Finanzierung oder 110%-Finanzierung (inkl. Nebenkosten) argumentieren
- Du musst die Kapitaldienstfaehigkeit nachweisen
- Du willst dem Banker ein Dokument geben, das er intern (Marktfolge, Kreditausschuss) ohne Rueckfragen weiterreichen kann
- Du willst dich mit einer professionellen Praesentation von anderen Finanzierungsanfragen abheben
- Du brauchst eine Praesentation, die DSCR-Bedienbarkeit in JEDER Phase nachweist

---

## Was du bereitstellen musst

### Pflichtangaben

```json
{
  "investor": {
    "name": "Max Mustermann",
    "company": "Mustermann Immobilien GmbH",
    "role": "Geschaeftsfuehrer",
    "description": "Bestandshalter mit Fokus auf Value-Add-Wohnimmobilien",
    "contact": {
      "phone": "+49 170 1234567",
      "email": "max@mustermann-immo.de",
      "address": "Musterstrasse 1, 03046 Cottbus"
    }
  },
  "property": {
    "address": "Beispielstrasse 10-12, 03046 Cottbus",
    "type": "MFH | ZFH | ETW-Paket | Wohn-/Geschaeftshaus",
    "units_residential": 10,
    "units_commercial": 2,
    "total_sqm": 904,
    "year_built": 1936,
    "condition": "teilsaniert | unsaniert | vollsaniert | Neubau",
    "plot_size_sqm": 1250,
    "heating_type": "Gas-Zentralheizung"
  },
  "purchase": {
    "asking_price_eur": 550000,
    "offered_price_eur": 520000,
    "buyer_commission_pct": 3.57,
    "grunderwerbsteuer_pct": 6.5,
    "notar_grundbuch_pct": 2.0
  },
  "current_rents": {
    "cold_rent_monthly_eur": 4000,
    "vacancy_units": 3,
    "vacancy_since": "2024-06-01",
    "rent_roll_available": true
  },
  "financing_preferences": {
    "equity_available_eur": 47764,
    "target_loan_to_value_pct": 100,
    "desired_fixed_rate_years": 10,
    "tilgungsfrei_months": 24,
    "sondertilgung_pct": 5
  }
}
```

### Optionale Angaben (erhoehen die Qualitaet)

```json
{
  "investor_detail": {
    "portfolio_kpis": {
      "units_total": 42,
      "experience_years": 6,
      "bestandsrendite_pct": 8.2,
      "leerstand_pct": 2.1
    },
    "werdegang_timeline": [
      { "year": 2019, "milestone": "Erste ETW als Kapitalanlage erworben" },
      { "year": 2024, "milestone": "42 WE, erste KfW-Sanierung abgeschlossen" }
    ],
    "trackrecord_highlight": {
      "property_name": "KM 59/60, Cottbus",
      "jnkm_increase_pct": 95,
      "dscr": 3.20,
      "ltv_pct": 51.7,
      "leerstand_pct": 0
    },
    "stille_reserven": {
      "freie_grundschulden_eur": 120000,
      "description": "Freie Grundschulden aus getilgten Bestandsdarlehen"
    }
  },
  "darlehensnehmer": {
    "gesellschaft": "Mustermann Immobilien GmbH",
    "gesellschafter": "Max Mustermann (100%)",
    "geschaeftsfuehrer": "Max Mustermann",
    "sitz": "Cottbus"
  },
  "rent_roll": [
    {
      "unit_id": "WE 01",
      "type": "Wohnung",
      "sqm": 65.0,
      "rent_ist_monthly": 325.00,
      "tenant": "Mueller, A.",
      "lease_start": "2018-03-01"
    }
  ],
  "planned_measures": {
    "organic_rent_increase": true,
    "modernization_planned": true,
    "modernization_budget_eur": 100000,
    "re_letting_target_rent_eur_sqm": 7.50,
    "measures": [
      { "massnahme": "Fenstertausch (10 WE)", "kosten": 35000, "programm": "KfW 261/262" },
      { "massnahme": "Heizungsoptimierung", "kosten": 12000, "programm": "BAFA BEG EM" }
    ]
  },
  "existing_portfolio": {
    "total_units": 35,
    "total_value_eur": 3500000,
    "annual_rental_income_eur": 280000,
    "existing_loans_eur": 2800000,
    "monthly_surplus_eur": 8500
  },
  "comparable_properties": [
    {
      "address": "Beispielstr. 5, gleiche Stadt",
      "purchase_price_eur": 900000,
      "units": 7,
      "price_per_sqm": 1650,
      "factor": 18.5
    }
  ],
  "mietspiegel_data": {
    "average_rent_per_sqm": 7.50,
    "upper_range_per_sqm": 9.50,
    "applicable_category": "Baujahr 1930-1950, mittlere Lage, Standardausstattung"
  }
}
```

> **Hinweis:** Je mehr optionale Daten du lieferst, desto praeziser wird die Praesentation. Fehlende Daten werden von der KI konservativ geschaetzt oder als "wird nachgereicht" gekennzeichnet.

---

## Auftrag

Analysiere das Kaufobjekt vollstaendig und erstelle eine professionelle 13-Sektionen-Bankenpraesentation, die:

1. **In der Executive Summary das Projekt auf einen Blick zusammenfasst** -- mit 5 KPI-Boxen, Kern-Argumenten und Investitionslogik
2. **Den Investor als erfahrenen, systematischen Bestandshalter positioniert** -- mit Portfolio-KPIs, Trackrecord und stillen Reserven
3. **Das Objekt mit allen technischen und wirtschaftlichen Parametern vorstellt** -- inkl. Darlehensnehmer-Struktur
4. **Die Investmentstrategie als 5-Stufen-Entwicklungspfad visualisiert** -- IST -> SOFORT -> SOLL 1 -> SOLL 2 -> SOLL 3 mit DSCR-Trajektorie
5. **Die Finanzierungsstruktur mit Eigenleistungen als EK-Ersatz darstellt** -- Block 1 + Block 2 Konzept
6. **Einen interaktiven Cashflow-Rechner mit 5 Stellschrauben bietet** -- mit Live-Berechnung
7. **Die Phasen-Cashflows mit DSCR pro Phase nachweist** -- "Kein kritisches Fenster"
8. **Eine DSCR-Sensitivitaetsmatrix mit Farbcodierung liefert** -- Gruen/Gelb/Rot
9. **Drei Szenarien nebeneinander vergleicht** -- Konservativ, Basis, Optimistisch
10. **Risiken proaktiv adressiert und Exit-Optionen mit Zahlen belegt** -- inkl. stille Reserven
11. **Eine klare Bankenentscheidungsvorlage formuliert** -- "Wir bieten / Wir wuenschen"

---

## Analysemethodik

Bevor du die Praesentation erstellst, fuehre diese Analyse durch. Die Ergebnisse fliessen in die 13 Sektionen ein.

### Schritt 1: Ist-Situation analysieren

- Aktuelle Mieteinnahmen (Ist-Miete kalt) auflisten, pro Einheit wenn moeglich
- Leerstand identifizieren und bewerten (seit wann, warum, behebbar?)
- Ist-Miete vs. Mietspiegel vergleichen: Wie viel Potenzial steckt in den Bestandsmieten?
- Zustand des Objekts bewerten: Was muss gemacht werden, was ist Kuer?
- Aktuelle Bruttomietrendite und Kaufpreisfaktor berechnen

### Schritt 2: 5-Stufen-Entwicklungspfad berechnen

Definiere fuer jede Stufe JNKM, Delta zum Vorgaenger, Rendite und DSCR:

- **IST:** Aktuelle Situation bei Uebernahme
- **SOFORT (Monat 1-3):** Leerstand beseitigen, Neuvermietung zu Marktniveau
- **SOLL 1 (Monat 4-24):** Organische Mieterhoehung Bestand (§558 BGB, Kappungsgrenze 15-20%) + Modernisierungsumlage (§559 BGB, max. 8% p.a.)
- **SOLL 2 (Jahr 2-3):** Weitere Mietanpassungen, Gewerbe-Optimierung, Neuvermietung bei Fluktuation
- **SOLL 3 (Jahr 4+):** Vollstabilisierung nach Sanierung

### Schritt 3: Massnahmenplan erstellen

- Konkrete Massnahmen mit Zeitrahmen und Kosten
- Modernisierungsumlage nach §559 BGB berechnen (max. 8% p.a. der Modernisierungskosten, Kappungsgrenze 2-3 EUR/qm beachten)
- Kappungsgrenze §558 BGB beachten (15% angespannter Markt / 20% in 3 Jahren)
- KfW/BAFA-Foerderfaehigkeit pruefen, Tilgungszuschuesse einrechnen
- Fuer jeden Schritt: Kosten, erwartete Mehrmieteinnahmen, Zeitrahmen

### Schritt 4: Finanzierungsstruktur berechnen

- Gesamtinvestitionskosten (GIK): Kaufpreis + GrESt + Notar/Grundbuch + Makler + Sanierung + Eigenleistungen (bewertet)
- Darlehensbetrag (Bank + KfW) vs. Eigenkapitaleinsatz
- Beleihungswert schaetzen (konservativ: Ertragswertverfahren, Faktor 15-18 x JNKM SOLL, dann 70% als Beleihungswert)
- Beleihungsauslauf (BLA) berechnen: Bankdarlehen / Beleihungswert
- Eigenleistungen als EK-Ersatz: Block 1 (Barmittel) + Block 2 (marktueblich bewertete Eigenleistungen) = EK-Quote
- Annuitaet berechnen (Zins + Tilgung, ggf. tilgungsfreie Anlaufphase)

### Schritt 5: Phasen-Cashflow berechnen

Fuer jede Phase (typischerweise 5 Phasen):

| Phase | Beschreibung | Was passiert |
|-------|-------------|-------------|
| 1 | IST (tilgungsfrei) | Leerstandsabbau, Anlaufphase |
| 2 | Mieterhoehung + Bank tilgt | §558/§559, Volltilgung beginnt |
| 3 | Modernisierung + KfW tilgt | Modernisierungsumlage traegt |
| 4 | SOLL 2 | Gewerbe-Optimierung, Stabilisierung |
| 5 | SOLL 3 (stabilisiert) | Vollstabilisierung, freier Cashflow |

Fuer jede Phase berechne: JNKM, Kapitaldienst/Monat, DSCR, Cashflow/Monat.

- DSCR = Nettomieteinnahmen (nach nicht umlagefaehigen Kosten) / Annuitaet
- Zielwert: DSCR >= 1,20 in JEDER Phase (Bank will min. 120% Deckung)
- Nachweis: Kein kritisches Fenster -- der DSCR darf zu keinem Zeitpunkt unter 1,0 fallen

### Schritt 6: Sensitivitaet und Szenarien

**DSCR-Matrix:**
- Zeilen = Mietentwicklung (EUR/qm in 0,50er-Schritten, von 4,00 bis 7,50)
- Spalten = Zinssatz (in 0,50er-Schritten, von 3,0% bis 6,0%)
- Farbcodierung: Gruen >= 1,20 | Gelb 1,00-1,20 | Rot < 1,00
- IST-Miete-Zeile hervorheben

**3 Szenarien nebeneinander:**
- Konservativ: Keine Mieterhoehung durchgesetzt, hoher Leerstand, hohe Bewirtschaftung
- Basis (empfohlen): Geplante Strategie mit Puffer
- Optimistisch: Volle Marktmiete, geringer Leerstand

**Stresstest:** DSCR bei +2% Zinsanstieg nach Zinsbindungsende

### Schritt 7: Exit-Szenarien und stille Reserven

- **Bestandshaltung:** Langfristiger Cashflow, Entschuldung ueber 25-30 Jahre
- **Verkauf nach Wertsteigerung:** Erwarteter Verkaufspreis (Faktor x JNKM SOLL), Erloees nach Tilgung
- **WEG-Aufteilung:** Abgeschlossenheitserklaerung -> Einzelverkauf (hoehere qm-Preise), Nettoerloees berechnen
- **Nachbeleihung / Kapitalrotation:** Freier Beleihungsraum fuer naechsten Deal
- Stille Reserven beziffern: Differenz Kaufpreis zu Ertragswert, freie Grundschulden, Grundstuecksentwicklung

### Schritt 8: Eigenkapital-Rueckfluss

- Eingesetztes Eigenkapital (ggf. 0 bei 100%-Finanzierung)
- Jaehrlicher Cashflow nach Kapitaldienst
- Tilgung als Vermoegensaufbau beruecksichtigen
- Steuerliche Effekte (AfA, Zinsabzug) grob einordnen
- EK-Rueckfluss p.a. = (Cashflow + Tilgung + Steuerersparnis) / eingesetztes EK

### Schritt 9: Ertragswert und LTV-Herleitung

- Ertragswert bei 4 Faktoren (15, 16, 17, 18) x JNKM SOLL berechnen
- Beleihungswert = 70% des Ertragswerts
- LTV Bank = Bankdarlehen / Beleihungswert
- Zeigen: Ab welchem Faktor liegt LTV unter 80%?
- Referenzobjekte zum Vergleich: Mind. 2-3 vergleichbare Objekte aus der Region

---

## Praesentationsstruktur (13 Sektionen)

Nutze die Ergebnisse der Analysemethodik und baue daraus die 13 Sektionen. Jede Sektion hat einen klaren Zweck fuer den Bankberater.

### Sektion 1: Executive Summary

- **Hero-Sektion** mit Platzhalter fuer Objektfoto
- **5 KPI-Boxen** am oberen Rand: Kreditbetrag | DSCR (SOFORT) | DSCR (ab Monat X) | LTV Bankdarlehen | EK-Quote
- **"Projekt auf einen Blick"** Tabelle: Objekt, Standort, Typ, Einheiten, Flaeche, Grundstueck, Strategie, Finanzierungswunsch
- **"Kern-Argumente fuer die Bank"** -- genau 5 Bullet Points mit Checkmarks, die die STAERKSTEN Argumente fuer den Deal zusammenfassen
- **Footer-KPIs:** JNKM IST -> SOFORT -> SOLL 1 mit jeweiliger Rendite in %
- **Investitionslogik** als praegnanter Absatz (der "Elevator Pitch" fuer den Deal)

### Sektion 2: Unternehmensprofil

- **Investor-Card:** Avatar-Platzhalter, Name, Beschreibung, Kontaktdaten
- **4 Portfolio-KPIs** als Boxen: Einheiten gesamt, Erfahrung (Jahre), Bestandsrendite (%), Leerstand (%)
- **Werdegang als Timeline:** Jahreszahl + Meilenstein
- **Trackrecord-Highlight:** Bestes Vergleichsobjekt mit JNKM-Steigerung, DSCR, LTV, Leerstand
- **Stille Reserven & Sicherheiten:** Freie Grundschulden, nachrangig beleihbar

### Sektion 3: Projektuebersicht

- **Darlehensnehmer-Tabelle:** Gesellschaft, Gesellschafter (mit Anteil), Geschaeftsfuehrer, Sitz
- **Objektfotos:** 2 Fotos nebeneinander (Platzhalter)
- **Objektparameter-Tabelle** mit mindestens 15 Zeilen: Adresse, Objektart, Baujahr, Energieeffizienz, WE, GE, Stellplaetze, Flaeche, Grundstueck, Heizung, Keller, Kaufpreis, KP/qm, IST-Miete/qm, Marktniveau
- **KPI-Badges** am unteren Rand

### Sektion 4: Investmentstrategie

- **Entwicklungspfad IST -> SOLL** als visuelles Flussdiagramm mit 5 Stufen (JNKM, Delta, Rendite, DSCR)
- **DSCR-Trajektorie** unterhalb des Flussdiagramms
- **Sanierungsaufstellung** als Tabelle: Massnahme | Kosten | Programm -- mit Gesamtsumme und KfW-Tilgungszuschuss
- **Zeitstrahl Meilensteine** als Tabelle: Zeitpunkt | Meilenstein | Wirkung
- **Investitionslogik** als erklaerenden Absatz

### Sektion 5: Wohnungsmix & Miete

- **3 Header-KPIs:** Ø IST-Miete, Ø SOLL 1, Marktniveau (je EUR/qm)
- **Vollstaendige Mieterliste** pro Einheit: Einheit | Typ | Flaeche | IST/Mo | SOLL/Mo | Mieter | Mietbeginn
- **Bei mehreren Gebaeuden:** Aufschluesselung nach Gebaeude mit IST/SOFORT/SOLL 1-3 pro Monat
- **Summenzeile** mit Totals

### Sektion 6: Finanzierung

- **Split-Layout:** Gesamtinvestitionskosten (links) | Finanzierungsstruktur (rechts)
- **GIK-Aufstellung:** Kaufpreis + KNK-Breakdown (GrESt nach Bundesland + Notar + Makler) + Sanierung + Eigenleistungen
- **Finanzierungsstruktur:** Bankdarlehen + KfW + EK (Block 1 + Block 2)
- **Konditionen-Detail:** Zinsen, Tilgung (mit tilgungsfreier Phase), KfW-Details, Sondertilgung
- **Eigenleistungen als EK-Ersatz:**
  - Block 1 (Barmittel): Cash fuer Kaufnebenkosten
  - Block 2 (marktueblich bewertete Eigenleistungen): Jede Leistung einzeln mit Marktpreis
  - Ergebnis: Block 1 + Block 2 = EK-Quote Y%
- **Footer-KPIs:** GIK gesamt, Gesamtkredit, KfW-TZ, EK-Quote
- **Ertragswert & LTV-Herleitung** als Tabelle: Faktor (15/16/17/18) x JNKM -> Ertragswert -> BW (70%) -> LTV Bank

### Sektion 7: Cashflow-Rechner (Interaktiv)

- **5 Eingabeparameter mit Slider-Bereichen:**
  - Ø Miete EUR/qm (min-max)
  - Leerstand % (0-20)
  - Bewirtschaftung % (15-35)
  - Zinssatz % (2-8)
  - Tilgung % (0-5)
- **3 live-berechnete Ausgabe-KPIs:** CF v.St. p.a. | DSCR | Rendite auf GK
- **Berechnungsdetail-Breakdown:** Mieteinnahmen brutto -> Abzug Leerstand -> Abzug Bewirtschaftung -> Netto -> Abzug Zinsen -> Abzug Tilgung -> CF v.St.
- **Farbcodierung:** Positiver CF = gruen, Negativer CF = rot

### Sektion 8: Phasen-Cashflow

- **Phase-Cards am oberen Rand:** Je Phase eine Karte mit CF/Monat
- **Phasen-Uebersicht als Tabelle:** Phase | Zeitraum | JNKM | KD/Mo | DSCR | CF/Mo
- **Typischerweise 5 Phasen:** IST (tilgungsfrei) -> Mieterhoehung + Bank tilgt -> Modernisierung + KfW tilgt -> SOLL 2 -> SOLL 3
- **Erlaeuterungstext:** "Kein kritisches Fenster. In jeder Phase uebersteigen die Mieteinnahmen den Kapitaldienst."
- Der Phasen-Cashflow ist das Herzstueck -- er beweist, dass der Deal in JEDER Phase bedienbar ist

### Sektion 9: Sensitivitaetsanalyse

- **DSCR-Matrix** als Tabelle: Zeilen = Mietentwicklung (EUR/qm), Spalten = Zinssatz
- **Farbcodierung:** Gruen >= 1,20 | Gelb 1,00-1,20 | Rot < 1,00
- **IST-Miete-Zeile hervorgehoben**
- **Lesehinweis** fuer den Bankberater

### Sektion 10: Szenarienvergleich

- **3 Spalten nebeneinander:** Konservativ | Basis (empfohlen) | Optimistisch
- **Jedes Szenario:** Beschreibung, Ø Miete, Leerstand, Bewirtschaftung, Brutto/Netto/KD/CF, DSCR, Rendite
- **Basis-Szenario visuell hervorgehoben**
- **Erlaeuterungstext** mit Kontext

### Sektion 11: Risiken & Exit

- **Risikomatrix:** Risiko | Eintrittswahrscheinlichkeit | Absicherung/Mitigation
- **Exit-Optionen & stille Reserven:** Option | Zeitpunkt | Wirkung (mit konkreten Zahlen)
- **Stille Reserven als Absatz:** Differenz Kaufpreis zu Ertragswert, freie Grundschulden, Grundstuecksentwicklung

### Sektion 12: Bankenentscheidung

- **"Wir bieten"-Box** mit 5-6 Checkmark-Items
- **"Wir wuenschen"-Tabelle:** Darlehensart, Betrag/Zins/Tilgung/Laufzeit, KfW, Sondertilgung, Sicherheit
- **4 Footer-KPIs:** DSCR (min), LTV, JNKM SOLL, EK-Quote
- **Zusammenfassung** als abschliessendes Argument (der "Closing Pitch")

### Sektion 13: Downloads / Anlagen

- **PDF-Export-Hinweis**
- **Anlagen-Liste** mit allen beigefuegten/nachzureichenden Dokumenten

---

## Ausgabeformat

```markdown
# Finanzierungsantrag: [Objektbezeichnung]
## [Adresse] | [Stadt], [Bundesland]
## Erstellt: [Datum] | Investor: [Name] | [Firma]

---

## 1. Executive Summary

![Objektfoto](foto_platzhalter.jpg)

### KPI-Boxen

| Kreditbetrag | DSCR (SOFORT) | DSCR (ab Mo 25) | LTV Bankdarlehen | EK-Quote |
|:---:|:---:|:---:|:---:|:---:|
| 680.000 EUR | 1,38 | 1,29 | 76,9% (F16) | 12,7% |

### Projekt auf einen Blick

| Parameter | Wert |
|-----------|------|
| Objekt | Mehrfamilienhaus / Wohn- und Geschaeftshaus |
| Standort | Cottbus, Brandenburg |
| Typ | Bestandsobjekt, Value-Add |
| Einheiten | 10 WE + 2 GE |
| Flaeche | 904 m2 |
| Grundstueck | 1.250 m2 |
| Strategie | Leerstandsabbau + Mieterhoehung + KfW-Modernisierung |
| Finanzierungswunsch | 680.000 EUR (Bank 620.000 + KfW 60.000) |

### Kern-Argumente fuer die Bank

- [x] DSCR >= 1,27 in ALLEN Phasen -- kein kritisches Fenster, Kapitaldienst jederzeit gesichert
- [x] Trackrecord: Vergleichsobjekt KM 59/60 Cottbus mit JNKM +95%, DSCR 3,20, Leerstand 0%
- [x] LTV unter 77% bei konservativem Faktor 16 auf JNKM SOLL 1
- [x] Sofortiger DSCR-Sprung auf 1,38 durch Leerstandsabbau in Monat 1-3
- [x] KfW-Foerderung sichert 15.000 EUR Tilgungszuschuss und reduziert effektiven Kapitaldienst

### Mietentwicklung & Rendite

| | JNKM IST | JNKM SOFORT | JNKM SOLL 1 |
|---|:---:|:---:|:---:|
| Betrag | 48.000 EUR | 57.600 EUR | 72.000 EUR |
| Rendite | 5,8% | 7,0% | 8,7% |

### Investitionslogik

Erwerb eines unterbewerteten Wohn- und Geschaeftshauses mit 20% Leerstand und 35% Mietanpassungspotenzial. Die Strategie kombiniert sofortige Leerstandsbeseitigung (DSCR-Sprung auf 1,38), organische Mieterhoehung im Bestand und selektive KfW-foerderfaehige Modernisierung. Der Kapitaldienst wird in JEDER Phase aus dem Objekt bedient. Die tilgungsfreie Anlaufphase von 24 Monaten ermoeglicht die Umsetzung ohne zusaetzlichen Liquiditaetsbedarf.

---

## 2. Unternehmensprofil

### Investor

| | |
|---|---|
| **[Avatar]** | **Max Mustermann** |
| | Geschaeftsfuehrer, Mustermann Immobilien GmbH |
| | Bestandshalter mit Fokus auf Value-Add-Wohnimmobilien in Ostdeutschland |
| Telefon | +49 170 1234567 |
| E-Mail | max@mustermann-immo.de |
| Adresse | Musterstrasse 1, 03046 Cottbus |

### Portfolio-KPIs

| Einheiten | Erfahrung | Bestandsrendite | Leerstand |
|:---:|:---:|:---:|:---:|
| 42 WE | 6 Jahre | 8,2% | 2,1% |

### Werdegang

| Jahr | Meilenstein |
|------|------------|
| 2019 | Erste ETW als Kapitalanlage erworben |
| 2020 | Erstes MFH (6 WE) -- Cottbus |
| 2021 | Gruendung Mustermann Immobilien GmbH |
| 2022 | Zwei MFH-Paketkaeufe (18 WE) -- 100% finanziert |
| 2023 | Portfolio auf 35 WE ausgebaut |
| 2024 | 42 WE, erste KfW-Sanierung abgeschlossen |

### Trackrecord-Highlight

> **KM 59/60, Cottbus** -- JNKM +95% | DSCR 3,20 | LTV 51,7% | Leerstand 0%
>
> Vergleichsobjekt im Eigenbestand. Identische Strategie (Leerstandsabbau + Mieterhoehung + Modernisierung) bereits erfolgreich umgesetzt. Nachweis, dass der Investor die hier geplante Strategie beherrscht.

### Stille Reserven & Sicherheiten

Freie Grundschulden aus dem Bestandsportfolio in Hoehe von 120.000 EUR, nachrangig beleihbar. Zusaetzlich stille Reserven im Bestandsportfolio durch Wertsteigerungen der letzten 5 Jahre.

---

## 3. Projektuebersicht

### Darlehensnehmer

| Parameter | Wert |
|-----------|------|
| Gesellschaft | Mustermann Immobilien GmbH |
| Gesellschafter | Max Mustermann (100%) |
| Geschaeftsfuehrer | Max Mustermann |
| Sitz | Cottbus |

### Objektfotos

| Foto 1: Frontansicht | Foto 2: Hofseite |
|:---:|:---:|
| ![Front](foto1_platzhalter.jpg) | ![Hof](foto2_platzhalter.jpg) |

### Objektparameter

| Parameter | Wert |
|-----------|------|
| Adresse | Beispielstrasse 10-12, 03046 Cottbus |
| Objektart | Mehrfamilienhaus / Wohn- und Geschaeftshaus |
| Baujahr | 1936 |
| Energieeffizienzklasse | H |
| Wohneinheiten | 10 |
| Gewerbeeinheiten | 2 |
| Stellplaetze | 6 |
| Wohnflaeche gesamt | 904 m2 |
| Grundstueck | 1.250 m2 |
| Heizungsart | Gas-Zentralheizung |
| Keller | Ja |
| Kaufpreis | 520.000 EUR |
| Kaufpreis/m2 | 575 EUR/m2 |
| IST-Miete (Ø) | 4,42 EUR/m2 |
| Marktniveau | 7,50 EUR/m2 |
| Grundbuch | Lastenfrei |

### KPI-Badges

`10 WE` | `2 GE` | `Bj. 1936` | `904 m2` | `1.250 m2 Grundstueck` | `Effizienz H` | `575 EUR/m2`

---

## 4. Investmentstrategie

### Entwicklungspfad IST -> SOLL

```
IST ---------> SOFORT -------> SOLL 1 -------> SOLL 2 -------> SOLL 3
48.000 EUR      57.600 EUR      72.000 EUR      78.000 EUR      82.800 EUR
                +9.600          +14.400         +6.000          +4.800
Rendite 5,8%    Rendite 7,0%    Rendite 8,7%    Rendite 9,5%    Rendite 10,0%
DSCR 1,15       DSCR 1,38       DSCR 1,50       DSCR 1,63       DSCR 1,72
```

### Sanierungsaufstellung

| Massnahme | Kosten (EUR) | Programm / Hinweis |
|-----------|:---:|---|
| Fenstertausch (10 WE) | 35.000 | KfW 261/262 |
| Heizungsoptimierung | 12.000 | BAFA BEG EM |
| Treppenhaussanierung | 8.000 | -- |
| Badsanierung (3 WE bei Mieterwechsel) | 15.000 | -- |
| Elektrik-Ertuechtigung | 10.000 | -- |
| Fassade (Teilbereich) | 20.000 | KfW 261 |
| **Gesamt** | **100.000** | |
| **KfW-Tilgungszuschuss** | **-15.000** | KfW 261 |
| **Effektive Sanierungskosten** | **85.000** | |

### Zeitstrahl Meilensteine

| Zeitpunkt | Meilenstein | Bedeutung / Wirkung |
|-----------|------------|---------------------|
| Sofort (Monat 1-3) | Leerstandsabbau + Neuvermietung | JNKM +9.600 EUR, DSCR steigt auf 1,38 |
| Monat 4-12 | Organische Mieterhoehung (§558 BGB) | Bestandsmieten +15-20% bei Mietspiegelberechtigung |
| Jahr 2 | Modernisierung + §559 Umlage | JNKM auf 72.000 EUR, DSCR 1,50 |
| Jahr 3-4 | Gewerbe-Neuvermietung + Stabilisierung | JNKM auf 78.000 EUR |
| Jahr 5+ | Vollstabilisierung | JNKM 82.800 EUR, DSCR 1,72, Option Nachbeleihung |
| Jahr 6+ | Exit-Optionen pruefen | WEG-Aufteilung oder Portfolioverkauf moeglich |

### Investitionslogik

Erwerb eines unterbewerteten Wohn- und Geschaeftshauses mit 20% Leerstand und 35% Mietanpassungspotenzial. Die Strategie kombiniert sofortige Leerstandsbeseitigung (DSCR-Sprung auf 1,38), organische Mieterhoehung im Bestand und selektive KfW-foerderfaehige Modernisierung. Der Kapitaldienst wird in JEDER Phase aus dem Objekt bedient. Die tilgungsfreie Anlaufphase von 24 Monaten ermoeglicht die Umsetzung ohne zusaetzlichen Liquiditaetsbedarf.

---

## 5. Wohnungsmix & Miete

### KPI-Header

| Ø IST-Miete | Ø SOLL 1 | Marktniveau |
|:---:|:---:|:---:|
| 4,42 EUR/m2 | 6,64 EUR/m2 | 7,50 EUR/m2 |

### Mieterliste

| Einheit | Typ | Flaeche (m2) | IST/Mo (EUR) | SOLL/Mo (EUR) | Mieter | Mietbeginn |
|---------|-----|:---:|:---:|:---:|--------|------------|
| WE 01 | Wohnung | 65,0 | 325,00 | 455,00 | Mueller, A. | 03/2018 |
| WE 02 | Wohnung | 78,0 | 390,00 | 546,00 | Schmidt, B. | 07/2020 |
| WE 03 | Wohnung | 55,0 | 275,00 | 385,00 | Weber, C. | 01/2019 |
| WE 04 | Wohnung | 90,0 | 450,00 | 630,00 | Fischer, D. | 11/2017 |
| WE 05 | Wohnung | 72,0 | 360,00 | 504,00 | Wagner, E. | 04/2021 |
| WE 06 | Wohnung | 68,0 | 340,00 | 476,00 | Becker, F. | 09/2019 |
| WE 07 | Wohnung | 82,0 | 410,00 | 574,00 | Schulz, G. | 02/2022 |
| WE 08 | Wohnung | 58,0 | 0,00 | 406,00 | **Leer** | -- |
| WE 09 | Wohnung | 76,0 | 380,00 | 532,00 | Hoffmann, H. | 06/2020 |
| WE 10 | Wohnung | 60,0 | 0,00 | 420,00 | **Leer** | -- |
| GE 01 | Gewerbe | 120,0 | 600,00 | 840,00 | **Leer** | -- |
| GE 02 | Gewerbe | 80,0 | 470,00 | 640,00 | Salon Iris | 01/2023 |
| **Gesamt** | | **904,0** | **4.000,00** | **6.408,00** | | |

### Aufschluesselung nach Gebaeude

| Gebaeude | WE | GE | IST/Mo | SOFORT/Mo | SOLL 1/Mo | SOLL 2/Mo | SOLL 3/Mo |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Haus 10 | 5 | 1 | 2.100 | 2.520 | 3.150 | 3.400 | 3.600 |
| Haus 12 | 5 | 1 | 1.900 | 2.280 | 2.850 | 3.100 | 3.300 |
| **Gesamt** | **10** | **2** | **4.000** | **4.800** | **6.000** | **6.500** | **6.900** |

---

## 6. Finanzierung

### Gesamtinvestitionskosten (GIK)

| Position | Betrag (EUR) |
|----------|:---:|
| Kaufpreis | 520.000 |
| GrESt (6,5% -- Brandenburg) | 33.800 |
| Notar + Grundbuch (2,0%) | 10.400 |
| Makler (3,57%) | 18.564 |
| **KNK gesamt** | **62.764** |
| Sanierung | 100.000 |
| Eigenleistungen (bewertet) | 45.000 |
| **GIK gesamt** | **727.764** |

### Finanzierungsstruktur

| Quelle | Betrag (EUR) | Anteil |
|--------|:---:|:---:|
| Bankdarlehen | 620.000 | 85,2% |
| KfW 261 | 60.000 | 8,2% |
| EK Barmittel (Block 1) | 47.764 | 6,6% |
| EK Eigenleistungen (Block 2) | 45.000 | -- (nicht-monetaer) |
| **Gesamt** | **727.764** | **100%** |

### Konditionen

| Parameter | Bankdarlehen | KfW 261 |
|-----------|:---:|:---:|
| Betrag | 620.000 EUR | 60.000 EUR |
| Zinssatz | 3,90% p.a. | 1,25% p.a. |
| Tilgung | 2,00% p.a. | nach Karenzzeit |
| Tilgungsfrei | 24 Monate | 36 Monate |
| Zinsbindung | 10 Jahre | Programmlaufzeit |
| Sondertilgung | 5% p.a. | -- |
| Tilgungszuschuss | -- | 15.000 EUR |

### Eigenleistungen als EK-Ersatz

**Block 1 -- Barmittel:**

| Position | Betrag (EUR) |
|----------|:---:|
| Barmittel fuer KNK (anteilig) | 47.764 |

**Block 2 -- Marktueblich bewertete Eigenleistungen:**

| Leistung | Marktpreis (EUR) |
|----------|:---:|
| Neuvermietung Leerstand (3 WE) | 8.000 |
| Mieterhoehungsgespraeche + Durchsetzung | 6.000 |
| Gewerbe-Akquise + Verhandlung | 5.000 |
| Projektmanagement Sanierung | 12.000 |
| Objektueberwachung + Baubegleitung | 6.000 |
| KfW-/BAFA-Foerderkoordination | 4.000 |
| WEG-Aufteilungsvorbereitung | 4.000 |
| **Block 2 gesamt** | **45.000** |

**EK-Quote:** Block 1 (47.764 EUR) + Block 2 (45.000 EUR) = 92.764 EUR = **12,7% der GIK**

> **Hinweis:** Die Eigenleistungen werden nicht als Cash eingebracht, sondern als vom Investor persoenlich erbrachte Leistungen, die bei Beauftragung eines Dritten den angegebenen Marktpreis kosten wuerden. Die Bank erhaelt damit den Nachweis, dass der Investor "Skin in the Game" hat -- durch Arbeitseinsatz statt durch Kapital.

### Footer-KPIs

| GIK | Gesamtkredit | KfW TZ | EK-Quote |
|:---:|:---:|:---:|:---:|
| 727.764 EUR | 680.000 EUR | 15.000 EUR | 12,7% |

### Ertragswert & LTV-Herleitung

| Faktor | x JNKM SOLL 1 | = Ertragswert | BW (70%) | LTV Bank |
|:---:|:---:|:---:|:---:|:---:|
| 15 | x 72.000 | 1.080.000 | 756.000 | 82,0% |
| **16** | **x 72.000** | **1.152.000** | **806.400** | **76,9%** |
| 17 | x 72.000 | 1.224.000 | 856.800 | 72,4% |
| 18 | x 72.000 | 1.296.000 | 907.200 | 68,3% |

> Bereits ab Faktor 16 liegt der LTV des Bankdarlehens (620.000 EUR) unter 77%. Der Beleihungswert bei Faktor 17 (856.800 EUR) uebersteigt den Gesamtkredit (680.000 EUR) um 176.800 EUR -- die Bank ist solide abgesichert.

---

## 7. Cashflow-Rechner (Interaktiv)

### Eingabeparameter (Slider)

| Parameter | Default | Min | Max | Schrittweite |
|-----------|:---:|:---:|:---:|:---:|
| Ø Miete (EUR/m2) | 6,64 | 4,00 | 9,00 | 0,25 |
| Leerstand (%) | 5 | 0 | 20 | 1 |
| Bewirtschaftung (%) | 25 | 15 | 35 | 1 |
| Zinssatz (%) | 3,90 | 2,00 | 8,00 | 0,10 |
| Tilgung (%) | 2,00 | 0 | 5,00 | 0,25 |

### Ausgabe-KPIs (live berechnet)

| CF v.St. p.a. | DSCR | Rendite auf GK |
|:---:|:---:|:---:|
| [berechnet] EUR | [berechnet] | [berechnet] % |

### Berechnungsdetail

| Position | Betrag (EUR/Jahr) |
|----------|:---:|
| Mieteinnahmen brutto (904 m2 x 6,64 EUR x 12) | 72.000 |
| - Leerstand (5%) | -3.600 |
| - Bewirtschaftung (25%) | -18.000 |
| **= Nettomieteinnahmen** | **50.400** |
| - Zinsen Bankdarlehen (620.000 x 3,90%) | -24.180 |
| - Zinsen KfW (60.000 x 1,25%) | -750 |
| - Tilgung Bank (620.000 x 2,00%) | -12.400 |
| **= CF v.St. p.a.** | **13.070** |

> Farbcodierung: **Positiver CF = GRUEN** | **Negativer CF = ROT**

---

## 8. Phasen-Cashflow

### Phase-Cards

| Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 |
|:---:|:---:|:---:|:---:|:---:|
| +795 EUR/Mo | +1.336 EUR/Mo | +1.274 EUR/Mo | +1.774 EUR/Mo | +2.174 EUR/Mo |
| IST (tilgungsfrei) | §559+Bank tilgt | §558+KfW tilgt | SOLL 2 | SOLL 3 |

### Phasen-Uebersicht

| Phase | Zeitraum | JNKM (EUR) | KD/Mo (EUR) | DSCR | CF/Mo (EUR) |
|:---:|---------|:---:|:---:|:---:|:---:|
| 1 | Mo 1-24 (tilgungsfrei) | 57.600 | 2.015 | **2,38** | +795 |
| 2 | Mo 25-36 (§559 + Bank tilgt) | 72.000 | 4.664 | **1,29** | +1.336 |
| 3 | Mo 37-48 (§558 + KfW tilgt) | 72.000 | 4.726 | **1,27** | +1.274 |
| 4 | Mo 49-72 (SOLL 2) | 78.000 | 4.726 | **1,38** | +1.774 |
| 5 | Ab Mo 73 (SOLL 3 stabilisiert) | 82.800 | 4.726 | **1,46** | +2.174 |

### Erlaeuterung

**Kein kritisches Fenster.** In jeder Phase uebersteigen die Mieteinnahmen den Kapitaldienst. Der DSCR faellt zu keinem Zeitpunkt unter 1,27 -- auch nicht beim Uebergang von der tilgungsfreien Phase zur Volltilgung. Die tilgungsfreie Anlaufphase (Phase 1) wird gezielt genutzt, um den Leerstand abzubauen und die Mietbasis auf 57.600 EUR JNKM zu heben, bevor die Tilgung einsetzt. Ab Phase 2 traegt die Modernisierungsumlage (§559 BGB) die hoehere Annuitaet. In Phase 5 (Vollstabilisierung) betraegt der freie Cashflow +2.174 EUR/Monat bei einem DSCR von 1,46.

---

## 9. Sensitivitaetsanalyse

### DSCR-Matrix

| Miete (EUR/m2) | 3,0% Zins | 3,5% Zins | 4,0% Zins | 4,5% Zins | 5,0% Zins | 5,5% Zins | 6,0% Zins |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 4,00 | 1,02 | 0,95 | 0,89 | 0,83 | 0,78 | 0,73 | 0,69 |
| **4,42 (IST)** | **1,13** | **1,05** | **0,98** | **0,92** | **0,86** | **0,81** | **0,76** |
| 4,50 | 1,15 | 1,07 | 1,00 | 0,94 | 0,88 | 0,83 | 0,78 |
| 5,00 | 1,27 | 1,19 | 1,11 | 1,04 | 0,98 | 0,92 | 0,86 |
| 5,50 | 1,40 | 1,31 | 1,22 | 1,15 | 1,08 | 1,01 | 0,95 |
| 6,00 | 1,53 | 1,43 | 1,33 | 1,25 | 1,17 | 1,10 | 1,04 |
| 6,50 | 1,66 | 1,55 | 1,45 | 1,36 | 1,27 | 1,19 | 1,12 |
| 7,00 | 1,79 | 1,67 | 1,56 | 1,46 | 1,37 | 1,29 | 1,21 |
| 7,50 | 1,91 | 1,78 | 1,67 | 1,57 | 1,47 | 1,38 | 1,30 |

> **Farbcodierung:** Gruen >= 1,20 (komfortabel) | Gelb 1,00-1,20 (bedienbar) | Rot < 1,00 (unterdeckt)

### Lesehinweis

Bei der aktuellen IST-Miete von 4,42 EUR/m2 und einem Zinssatz von 4,0% betraegt der DSCR 0,98 -- knapp unter 1,0. **Deshalb ist die sofortige Leerstandsbeseitigung und Mieterhoehung essenziell.** Bereits bei 5,50 EUR/m2 (realistisch nach §558 BGB) liegt der DSCR bei 1,22 auch bei 4,0% Zins -- komfortabel. Bei der SOLL 1-Miete von 6,64 EUR/m2 bleibt der DSCR selbst bei einem Zinsanstieg auf 5,5% ueber 1,19 (bedienbar). Erst bei einem extremen Szenario (IST-Miete + 6% Zins) wuerde der DSCR kritisch -- ein Szenario, das durch die Mieterhoehungsstrategie ausgeschlossen wird.

---

## 10. Szenarienvergleich

| Parameter | Konservativ | **Basis (empfohlen)** | Optimistisch |
|-----------|:---:|:---:|:---:|
| Beschreibung | Keine Mieterhoehung, hoher Leerstand | Geplante Strategie mit Puffer | Volle Marktmiete, geringer Leerstand |
| Ø Miete (EUR/m2) | 5,50 | **6,64** | 7,50 |
| Leerstand (%) | 10 | **5** | 3 |
| Bewirtschaftung (%) | 30 | **25** | 22 |
| **Brutto p.a.** | 59.664 | **72.000** | 81.360 |
| **Netto p.a.** | 37.688 | **51.300** | 60.869 |
| **KD p.a.** | 55.968 | **55.968** | 55.968 |
| **CF v.St. (EUR)** | -18.280 | **-4.668** | +4.901 |
| **DSCR** | 0,67 | **0,92** | 1,09 |
| **Rendite auf GK (%)** | 5,54 | **7,55** | 8,96 |

### Erlaeuterung

Das Basis-Szenario unterstellt die geplante Mieterhoehung auf 6,64 EUR/m2 (SOLL 1) -- deutlich unter dem Marktniveau von 7,50 EUR/m2. Der Leerstandspuffer von 5% ist konservativ fuer einen Standort mit unter 4% Marktleerstand. Selbst im konservativen Szenario ohne Mieterhoehung (5,50 EUR/m2) zeigt der Phasen-Cashflow (Sektion 8), dass der Kapitaldienst in der tilgungsfreien Phase vollstaendig bedient wird. Die Szenarien beziehen sich auf den stabilisierten Zustand mit voller Tilgung -- in der tilgungsfreien Anlaufphase liegt der DSCR deutlich hoeher.

---

## 11. Risiken & Exit

### Risikomatrix

| Risiko | Eintrittswahrscheinlichkeit | Absicherung / Mitigation |
|--------|:---:|--------------------------|
| Mieterhoehungen nicht durchsetzbar | Niedrig | Mietspiegel-gestuetzte Begruendung, konservatives Szenario zeigt Bedienbarkeit auch bei 60% der geplanten Erhoehungen |
| Leerstand steigt dauerhaft ueber 10% | Niedrig | Marktleerstand unter 4%, attraktive Mikrolage, Mietausfallversicherung vorhanden |
| Sanierungskosten uebersteigen Budget | Mittel | 20% Puffer eingeplant, Handwerkerangebote fuer Hauptpositionen vorliegend, KfW-Foerderung als zusaetzlicher Puffer |
| Zinsanstieg nach Zinsbindung | Mittel | 10 Jahre Zinsbindung, Sondertilgungen reduzieren Restschuld, DSCR-Matrix zeigt Bedienbarkeit bis 6% Zins |
| Regulatorische Aenderungen | Niedrig | Konservative Kalkulation ohne Ausreizung der Mietgrenzen, energetische Massnahmen im Sanierungsplan |

### Exit-Optionen & stille Reserven

| Option | Zeitpunkt | Wirkung |
|--------|-----------|---------|
| Bestandshaltung | Dauerhaft | DSCR 1,72 bei SOLL 3, CF +2.174 EUR/Mo, kontinuierlicher Vermoegensaufbau durch Tilgung |
| Nachbeleihung / Kapitalrotation | Ab Jahr 5 | Ertragswert 1,3 Mio EUR -> freier Beleihungsraum ca. 200.000 EUR fuer naechsten Deal |
| Grundstuecksentwicklung (Hinterland) | Ab Jahr 3 | 1.250 m2 Grundstueck, 800 m2 bebaut -> 450 m2 Bauerwartungsland, Potenzial fuer 4-6 Stellplaetze oder Tiny-Houses |
| WEG-Aufteilung + Einzelverkauf | Ab Jahr 5 | 12 Einheiten x Ø 85.000 EUR = 1.020.000 EUR Erloes vs. 520.000 EUR Kaufpreis -> ca. 500.000 EUR stille Reserve |
| Portfolioverkauf (en bloc) | Ab Jahr 5 | Faktor 17-18 auf JNKM SOLL 3 (82.800 EUR) = 1,4-1,5 Mio EUR Verkaufserloes |

### Stille Reserven

Neben den freien Grundschulden aus dem Bestandsportfolio (120.000 EUR) bietet das Grundstueck mit 450 m2 unbebautem Hinterland zusaetzliches Entwicklungspotenzial. Bei konservativer Bewertung (Faktor 17 auf JNKM SOLL 1) ergibt sich ein Ertragswert von 1,22 Mio EUR -- der Kaufpreis inklusive Sanierung liegt bei 620.000 EUR. Die stille Reserve betraegt somit ca. 600.000 EUR.

---

## 12. Bankenentscheidung

### Wir bieten

- [x] EK-Quote 12,7% (Barmittel + bewertete Eigenleistungen)
- [x] Grundschuld 1. Rang auf das Kaufobjekt
- [x] DSCR >= 1,27 in ALLEN Phasen -- kein kritisches Fenster
- [x] LTV unter 77% bei konservativem Faktor 16 auf JNKM SOLL 1
- [x] Voll vermietetes Objekt nach Leerstandsabbau (Monat 3)
- [x] Nachgewiesener Trackrecord: KM 59/60 Cottbus -- JNKM +95%, DSCR 3,20, Leerstand 0%

### Wir wuenschen

| Parameter | Details |
|-----------|---------|
| Art des Darlehens | Annuitaetendarlehen mit tilgungsfreier Anlaufphase |
| Bankdarlehen | 620.000 EUR, 3,90% Zins, 2,00% Tilgung, 10 Jahre Zinsbindung, 24 Monate tilgungsfrei |
| KfW 261 | 60.000 EUR, 1,25% Zins, 15.000 EUR Tilgungszuschuss, Tilgungsbeginn Monat 37 |
| Sondertilgung | Bis 5% p.a. ohne Vorfaelligkeitsentschaedigung |
| Sicherheit | Grundschuld 1. Rang auf Kaufobjekt, ggf. nachrangige Grundschuld auf Bestandsobjekt |
| Auszahlungsvoraussetzung | Kaufvertrag, Grundschuldbestellung, Eigentumsumschreibung |
| Anschlussfinanzierung | Preferred Partner bei gleicher Bank nach Zinsbindungsende |

### Footer-KPIs

| DSCR (min. alle Phasen) | LTV Bank | JNKM SOLL 1 | EK-Quote |
|:---:|:---:|:---:|:---:|
| 1,27 | 76,9% (F16) | 72.000 EUR | 12,7% |

### Zusammenfassung

Wir bieten der Bank ein durchgerechnetes Value-Add-Projekt mit nachgewiesenem Trackrecord, Cashflow-Bedienbarkeit in jeder Phase und konservativer LTV-Abdeckung. Der Investor bringt Eigenleistungen im Wert von 45.000 EUR ein, die marktueblich bewertet sind und den Projekterfolg sicherstellen. Die Kombination aus sofortiger Leerstandsbeseitigung, organischer Mieterhoehung und KfW-gefoerderter Modernisierung schafft einen klaren, nachvollziehbaren Pfad zur Vollstabilisierung. Die Bank finanziert ein Objekt, das ab Monat 3 voll vermietet ist, in jeder Phase einen DSCR >= 1,27 aufweist und bei konservativer Bewertung (Faktor 16) einen LTV von unter 77% bietet.

---

## 13. Downloads / Anlagen

### PDF-Export

Diese Praesentation kann als PDF exportiert oder in Gamma.app als designte Praesentation aufbereitet werden. Alternativ kann Claude Code daraus eine interaktive HTML-Praesentation mit Slidern (Cashflow-Rechner) und farbcodierter DSCR-Matrix generieren.

### Anlagen

| Nr. | Dokument | Status |
|:---:|---------|:---:|
| 1 | Maklerexpose | Beigefuegt |
| 2 | Mieterliste (aktuell) | Beigefuegt |
| 3 | Lageplan / Katasterauszug | Beigefuegt |
| 4 | Bestandsuebersicht Portfolio | Beigefuegt |
| 5 | Trackrecord Vergleichsobjekt (KM 59/60 Cottbus) | Beigefuegt |
| 6 | Selbstauskunft Investor | Beigefuegt |
| 7 | Grundbuchauszug | Beigefuegt |
```

---

## Qualitaetspruefung

Pruefe die Praesentation gegen diese Kriterien:

- [ ] **13 Sektionen vollstaendig:** Alle 13 Sektionen sind vorhanden und in der richtigen Reihenfolge
- [ ] **Executive Summary mit 5 KPI-Boxen:** Kreditbetrag, DSCR (SOFORT), DSCR (ab Mo X), LTV, EK-Quote
- [ ] **Kern-Argumente sind die STAERKSTEN 5 Punkte:** Nicht generisch, sondern deal-spezifisch
- [ ] **Entwicklungspfad hat 5 Stufen:** IST -> SOFORT -> SOLL 1 -> SOLL 2 -> SOLL 3 mit JNKM + Delta + Rendite + DSCR
- [ ] **Phasen-Cashflow beweist Bedienbarkeit in JEDER Phase:** DSCR nie unter 1,0 (idealerweise nie unter 1,20)
- [ ] **Eigenleistungen korrekt aufgeschluesselt:** Block 1 (Barmittel) + Block 2 (bewertete Eigenleistungen) = EK-Quote
- [ ] **Ertragswert-Tabelle mit 4 Faktoren:** Zeigt der Bank, dass LTV unter 80% liegt
- [ ] **DSCR-Matrix mit Farbcodierung:** Gruen/Gelb/Rot klar erkennbar
- [ ] **Szenarienvergleich hat 3 Spalten:** Konservativ | Basis | Optimistisch
- [ ] **Exit-Optionen mit konkreten Zahlen:** Ertragswert, Erloespot., stille Reserven
- [ ] **"Wir bieten / Wir wuenschen" ist klar formuliert:** Bank kann direkt entscheiden
- [ ] **Rechnerische Konsistenz:** KPF und Bruttomietrendite stimmen (KPF = 1 / Rendite * 100)
- [ ] **Zahlen konsistent ueber alle 13 Sektionen:** JNKM, DSCR, LTV, EK-Quote stimmen ueberall ueberein
- [ ] **Plausibilitaet der Mieterhoehungen:** Zielmieten realistisch und durch Mietspiegel gedeckt
- [ ] **Kappungsgrenze beachtet:** Max. 15% (angespannter Markt) oder 20% in 3 Jahren (§558 Abs. 3 BGB)
- [ ] **Modernisierungsumlage korrekt:** Max. 8% p.a. der umlagefaehigen Kosten, Kappungsgrenze 2-3 EUR/qm (§559 BGB)
- [ ] **Stresstest bestanden:** Haelt das Konzept +2% Zinsanstieg aus?
- [ ] **Nicht umlagefaehige Kosten vollstaendig:** Instandhaltung, Verwaltung, Leerstandsrisiko beruecksichtigt
- [ ] **Sanierungskosten marktgerecht:** Kostenansaetze realistisch (nicht zu niedrig geschaetzt)
- [ ] **Sprache professionell:** Sachlich, praezise, keine Uebertreibungen
- [ ] **Trackrecord als Beweis:** Vergleichsobjekt mit konkreten Zahlen (nicht nur "Erfahrung vorhanden")

---

## Warnsignale & Dealbreaker

| Warnsignal | Bewertung | Handlungsempfehlung |
|------------|:---------:|---------------------|
| DSCR < 1,0 in einer Phase des Phasen-Cashflows | KRITISCH | Tilgungsfreie Phase verlaengern, Sanierungsreihenfolge anpassen, oder Deal ueberarbeiten |
| DSCR < 1,0 im Ist-Zustand ohne klaren Pfad zu > 1,0 | KRITISCH | Finanzierung wird schwierig, Konzept ueberarbeiten |
| Beleihungsauslauf > 130% ohne Zusatzsicherheiten | HOCH | Weitere Sicherheiten einbringen oder Kaufpreis verhandeln |
| LTV > 100% auch bei hohem Faktor | KRITISCH | Zusatzsicherheiten einbringen oder Eigenkapitalanteil erhoehen |
| Zielmieten > 20% ueber Mietspiegel | KRITISCH | Unglaubwuerdig fuer die Bank, Zielmieten korrigieren |
| Kein Trackrecord und kein Vergleichsobjekt | HOCH | Erfahrung anders belegen: Co-Investor, Ausbildungen, Hausverwaltungserfahrung |
| Eigenleistungen nicht plausibel bewertet | HOCH | Marktpreise mit Vergleichsangeboten belegen |
| Sanierungskosten nicht durch Angebote belegt | MITTEL | Handwerkerangebote oder Kostenschaetzungen einholen |
| Sanierungskosten > 30% des Kaufpreises ohne KfW | HOCH | KfW-Foerderfaehigkeit pruefen, Sanierung in Phasen aufteilen |
| Keine Liquiditaetsreserve und kein laufendes Einkommen | KRITISCH | Bank wird ohne Sicherheitsnetz nicht finanzieren |
| Grundbuch belastet (Vormerkungen, Wegerechte, Altlasten) | HOCH | Klaeren vor Banktermin, ggf. im Kaufvertrag regeln |
| Negative Cashflow-Prognose ueber > 3 Jahre | KRITISCH | Finanzierungsstruktur ueberarbeiten (mehr tilgungsfrei, weniger Tilgung) |
| Leerstand > 30% ohne klare Ursache | HOCH | Leerstandsgruende analysieren, Vermietbarkeit pruefen |
| DSCR-Matrix zeigt grosse rote Flaeche | MITTEL | Mieterhoehungsstrategie ueberpruefen, Zinsbindung verlaengern |
| Praesentation enthaelt Widersprueche oder Rechenfehler | KRITISCH | Alle Zahlen gegenprufen, JNKM/DSCR/LTV-Konsistenz ueber alle 13 Sektionen |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Investor-Trackrecord (erster Deal) | Berufliche Qualifikation hervorheben, Netzwerk benennen (HV, Steuerberater, Handwerker), Weiterbildungen erwaehnen, ggf. Co-Investor mit Trackrecord einbinden |
| Detaillierte Mieterliste | Mindestens Summen pro Gebaeude und Gesamt-JNKM. Hinweis "Vollstaendige Mieterliste als Anlage" |
| Eigenleistungen-Bewertung | Marktpreise aus Vergleichsangeboten (HV, Makler, Bauleiter) ableiten. Transparent als "marktueblich bewertet" kennzeichnen |
| Mietspiegel | Lokalen Mietspiegel recherchieren oder konservativ mit Durchschnitt der Region arbeiten |
| Sanierungskosten | Markt-Benchmarks verwenden: Vollsanierung 800-1.200 EUR/qm, Teilsanierung 300-600 EUR/qm. Als "Schaetzung ohne Handwerkerangebot" kennzeichnen |
| KfW-Konditionen | Aktuelle Konditionen von kfw.de uebernehmen, als "Stand [Datum], vorbehaltlich Zusage" kennzeichnen |
| Sollzins | Aktuellen Markt einschaetzen, Szenario mit Bandbreite rechnen |
| Beleihungswert | Konservativ mit 70% des Ertragswerts oder 80-90% des Kaufpreises ansetzen |
| Energieausweis | Auf Basis des Baujahrs und Zustands schaetzen, aber als Luecke markieren |
| Bestandsportfolio | Konzept auch ohne Portfolio erstellbar, aber Bonitaet-Einschaetzung wird schwieriger |
| Fotos | Darauf hinweisen, dass Fotos nachgeliefert werden. Alternativ: Google Street View |
| Grundbuchauszug | Als "wird nachgereicht" markieren, aber keine Finanzierung ohne Grundbucheinsicht moeglich |
| Standortdaten | Statistisches Landesamt, kommunale Statistik, ImmoScout24-Mietpreisspiegel nutzen |
| Referenzobjekte | ImmoScout24, Immowelt, lokale Makler fuer Vergleichspreise nutzen |
| Ertragswert-Faktor | Konservativen Faktor (15-16) fuer B-/C-Standorte, hoeheren Faktor (17-20) fuer A-Standorte |

> **Wichtig:** Fehlende Daten immer transparent kennzeichnen. Banken schaetzen Ehrlichkeit mehr als Luecken zu kaschieren. Eine ehrliche Praesentation mit "wird nachgereicht" ist besser als eine vollstaendige Praesentation mit falschen Zahlen.

---

## Konfidenz-Bewertung

| Konfidenz | Kriterien |
|-----------|-----------|
| **HOCH** (90%+) | Alle 13 Sektionen mit vollstaendigen Daten befuellt. Trackrecord mit Vergleichsobjekt vorhanden. Mieterliste pro Einheit vollstaendig. DSCR > 1,20 in allen Phasen. Ertragswert-Tabelle zeigt LTV < 80%. Eigenleistungen marktueblich bewertet und belegt. Handwerkerangebote vorliegend. Grundbuchauszug eingesehen. |
| **MITTEL** (70-89%) | Kern-Sektionen (1, 4, 6, 8, 12) vollstaendig, aber Trackrecord duenn oder Mieterliste nur summarisch. Sanierungskosten geschaetzt. Eigenleistungen plausibel aber nicht mit Vergleichsangeboten belegt. DSCR > 1,0 in allen Phasen. |
| **NIEDRIG** (< 70%) | Wesentliche Sektionen unvollstaendig. Kein Trackrecord. DSCR in mindestens einer Phase < 1,0. Eigenleistungen nicht bewertet. Keine Ertragswert-Herleitung. Finanzierungskonditionen nicht abgestimmt. |

---

## Verwandte Wissensdatenbanken

- `skills/cashflow-modell/SKILL.md` -- Detaillierte Cashflow-Projektion (Basis fuer Sektionen 7, 8, 9, 10)
- `skills/marktanalyse/SKILL.md` -- Standortanalyse und Marktdaten (ergaenzend zu Sektion 3)
- `skills/bierdeckel-kalkulation/SKILL.md` -- Schnellkalkulation fuer erste Einschaetzung vor der vollstaendigen Praesentation
- `skills/unterlagen-analyst/SKILL.md` -- Analysiert Objektunterlagen fuer Sektion 3 (Projektuebersicht)
- `skills/risiko-scanner/SKILL.md` -- Identifiziert Risiken fuer Sektion 11 (Risiken & Exit)
- `skills/mietlisten-analyse/SKILL.md` -- Analysiert Mieterlisten fuer Sektion 5 (Wohnungsmix & Miete)
- `skills/expose-parser/SKILL.md` -- Parsed Maklerexposes fuer Objektdaten
- `skills/mietlisten-parser/SKILL.md` -- Parsed Mieterlisten in strukturiertes Format
- `skills/mieterhoehung/SKILL.md` -- Berechnet Mieterhoehungspotenzial (§558/§559 BGB)
- `skills/bankgespraech-coach/SKILL.md` -- Vorbereitung auf das Bankgespraech mit Formulierungen und erwartbaren Fragen
- `skills/selbstauskunft/SKILL.md` -- Strukturierte Bonitaetsunterlagen fuer die Bank
- `knowledge/kalkulationsformeln.md` -- Renditekennzahlen, DSCR-Berechnung, Ertragswertverfahren
- `knowledge/rechtsgrundlagen.md` -- §558 BGB (Mieterhoehung), §559 BGB (Modernisierungsumlage), Kappungsgrenze
- `knowledge/marktbenchmarks.md` -- Benchmarks fuer Sanierungskosten, Bewirtschaftung, Mietvergleiche
- `knowledge/risikobewertung.md` -- Risiko-Framework fuer systematische Risikoanalyse
- `knowledge/checklisten.md` -- Checklisten fuer Banktermin-Vorbereitung und Dokumentenvollstaendigkeit
