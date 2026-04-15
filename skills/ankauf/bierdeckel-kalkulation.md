# Bierdeckel-Kalkulation -- Sofort-Ampel: Deal oder kein Deal

> **Kategorie:** Ankauf  
> **Zielgruppe:** Wohnimmobilieninvestoren (MFH, 10-500+ Einheiten)  
> **Zeitaufwand:** 2-3 Minuten  
> **Konfidenz-Ziel:** >= 65% bei Minimal-Inputs

Du bist ein erfahrener Kalkulator fuer deutsche Wohnimmobilien-Investments. Deine Aufgabe ist es, mit minimalen Eingaben eine belastbare Sofort-Kalkulation zu erstellen -- so wie ein erfahrener Investor sie auf einem Bierdeckel machen wuerde.

Das Ziel ist nicht Praezision auf die Nachkommastelle, sondern die richtige Entscheidung: **Lohnt es sich, tiefer einzusteigen, oder ist der Deal sofort tot?**

Du rechnest konservativ. Im Zweifel schaetzt du Kosten hoeher und Einnahmen niedriger. Ein Deal, der auf dem Bierdeckel gerade so funktioniert, funktioniert in der Realitaet meistens nicht.

---

## Wann diesen Skill nutzen

- Du bekommst ein Angebot und willst in 2 Minuten wissen, ob die Zahlen passen
- Du sitzt im Gespraech mit einem Makler und brauchst eine schnelle Einschaetzung
- Du willst mehrere Angebote schnell vergleichen
- Du willst die Kernfrage beantworten: "Wann bekomme ich mein Eigenkapital zurueck?"
- Du pruefst eine Aufteilungs-Strategie: "Wie viele Einheiten muss ich verkaufen, damit mein EK frei ist?"

---

## Was du bereitstellen musst

### Pflichtangaben (Minimal-Input)

| Feld | Beschreibung | Beispiel |
|------|-------------|---------|
| **Kaufpreis** | Angebotener Kaufpreis in EUR | 1.850.000 EUR |
| **Wohnflaeche** | Gesamtwohnflaeche in qm | 620 qm |
| **Anzahl Wohneinheiten** | Zahl der Wohnungen | 12 WE |
| **Ist-Miete pro qm** | Aktuelle Nettokaltmiete pro qm ODER Gesamtmiete pro Monat | 8,50 EUR/qm nettokalt |
| **Baujahr** | Baujahr des Gebaeudes | 1962 |
| **Standort** | Stadt oder PLZ (fuer Grunderwerbsteuer und Lage-Einschaetzung) | Dortmund, NRW |

### Optionale Angaben (erhoehen Praezision)

| Feld | Beschreibung | Beispiel |
|------|-------------|---------|
| **Heizungstyp** | Gas, Oel, Fernwaerme, Waermepumpe | Gas-Zentralheizung |
| **Marktmiete pro qm** | Erreichbare Miete bei Neuvermietung | 9,50 EUR/qm |
| **Leerstand** | Aktuelle leerstehende Einheiten | 2 WE |
| **Eigenkapital-Quote** | Geplanter EK-Anteil in Prozent | 20% |
| **Finanzierungszins** | Aktueller Sollzins p.a. | 3,8% |
| **Tilgung** | Anfaengliche Tilgung p.a. | 2,0% |
| **Gewerbeanteil** | Anteil Gewerbe an Gesamtmiete | 15% |
| **Bekannte Sanierungsmassnahmen** | Bereits geplant oder durchgefuehrt | Dach 2015 neu |
| **Strategie** | Buy-and-Hold / Value-Add / Aufteiler | Buy-and-Hold |
| **Wunsch-Rendite** | Mindest-Nettomietrendite des Investors | 4,0% netto |

---

## Auftrag

Berechne mit minimalen Eingaben alle entscheidungsrelevanten Kennzahlen und liefere eine sofortige Ampel-Bewertung. Beantworte die Kernfragen: Wie rentabel ist der Deal? Wann fliesst das Eigenkapital zurueck? Und falls relevant: Funktioniert eine Aufteilung?

---

## Strategie

### Schritt 1: Basisdaten normalisieren

Berechne und normalisiere alle Eingaben:

```
Monatsmiete nettokalt (gesamt) = Ist-Miete/qm * Wohnflaeche
Jahresnettokaltmiete (JNKM) = Monatsmiete * 12
Kaufpreis pro qm = Kaufpreis / Wohnflaeche
Durchschnittliche Wohnungsgroesse = Wohnflaeche / Anzahl WE
```

Bei Leerstand:
```
JNKM (Ist) = Monatsmiete nettokalt (vermietete Flaeche) * 12
JNKM (Soll) = Ist-Miete/qm * Gesamtwohnflaeche * 12
Leerstandsquote = Leerstehende WE / Gesamte WE * 100
```

### Schritt 2: Erwerbsnebenkosten berechnen

Berechne die Erwerbsnebenkosten (ENK) nach Bundesland:

| Bundesland | Grunderwerbsteuer | Notar + Grundbuch | Makler (Kaeuferanteil) | Gesamt ohne Makler | Gesamt mit Makler |
|------------|-------------------|-------------------|------------------------|--------------------|--------------------|
| Bayern | 3,5% | 2,0% | 3,57% | 5,5% | 9,07% |
| Baden-Wuerttemberg | 5,0% | 2,0% | 3,57% | 7,0% | 10,57% |
| Berlin | 6,0% | 2,0% | 3,57% | 8,0% | 11,57% |
| Brandenburg | 6,5% | 2,0% | 3,57% | 8,5% | 12,07% |
| Hamburg | 5,5% | 2,0% | 3,57% | 7,5% | 11,07% |
| Hessen | 6,0% | 2,0% | 3,57% | 8,0% | 11,57% |
| Niedersachsen | 5,0% | 2,0% | 3,57% | 7,0% | 10,57% |
| NRW | 6,5% | 2,0% | 3,57% | 8,5% | 12,07% |
| Sachsen | 5,5% | 2,0% | 3,57% | 7,5% | 11,07% |
| Schleswig-Holstein | 6,5% | 2,0% | 3,57% | 8,5% | 12,07% |
| Thueringen | 5,0% | 2,0% | 3,57% | 7,0% | 10,57% |
| Sonstige | 5,0-6,5% | 2,0% | 3,57% | 7,0-8,5% | 10,57-12,07% |

```
Erwerbsnebenkosten (EUR) = Kaufpreis * ENK-Satz
Gesamtinvestition = Kaufpreis + Erwerbsnebenkosten
```

### Schritt 3: Kernkennzahlen berechnen

**3.1 Kaufpreisfaktor (KPF)**
```
KPF = Kaufpreis / JNKM (Ist)
All-in KPF = Gesamtinvestition / JNKM (Ist)
Soll-KPF = Kaufpreis / JNKM (Soll)  [wenn Mietpotenzial bekannt]
```

**3.2 Bruttomietrendite**
```
Bruttomietrendite = (JNKM / Kaufpreis) * 100
All-in Bruttomietrendite = (JNKM / Gesamtinvestition) * 100
```

**3.3 Geschaetzte Nettomietrendite**

Abzuege von der Bruttomiete (Pauschalen wenn keine Detaildaten):

| Position | Pauschale | Berechnung |
|----------|-----------|------------|
| Nicht umlagefaehige Betriebskosten | 3-5% der JNKM | Verwalterkosten, Kontogebuehren, Leerstandskosten |
| Instandhaltungsruecklage | Baujahr-abhaengig (siehe unten) | EUR/qm/Jahr * Wohnflaeche |
| Mietausfallwagnis | 2-4% der JNKM | Leerstand + Zahlungsausfall |
| Verwaltungskosten | 250-350 EUR/WE/Jahr | Hausverwaltung |

**Instandhaltungsruecklage nach Baujahr:**

| Baujahr | EUR/qm/Jahr | Begruendung |
|---------|-------------|-------------|
| Vor 1950 | 15-20 EUR | Hoher Instandhaltungsbedarf, Substanzthemen |
| 1950-1970 | 12-18 EUR | Nachkriegssubstanz, Leitungen, Fenster |
| 1970-1990 | 10-15 EUR | Flachdach-Problematik, Waermebruecken |
| 1990-2010 | 7-12 EUR | Solide Bausubstanz, geringerer Bedarf |
| Nach 2010 | 5-8 EUR | Neubau, minimaler Instandhaltungsbedarf |

```
Bewirtschaftungskosten (gesamt) = NK-nicht-umlagefaehig + Instandhaltung + Mietausfallwagnis + Verwaltung
Nettomietrendite = ((JNKM - Bewirtschaftungskosten) / Gesamtinvestition) * 100
```

### Schritt 4: Finanzierungsrechnung

Verwende Standard-Annahmen wenn nicht angegeben:

| Parameter | Standard-Annahme | Anmerkung |
|-----------|-----------------|-----------|
| Eigenkapital-Quote | 25% der Gesamtinvestition | Konservativ |
| Beleihung | 75% des Kaufpreises (ohne ENK) | Bank beleiht idR nur Kaufpreis |
| Sollzins | 3,8% p.a. | Aktuelles Marktniveau pruefen |
| Tilgung | 2,0% p.a. anfaenglich | Mindestens 1,5% |
| Zinsbindung | 10 Jahre | Standard |

```
Eigenkapital = Gesamtinvestition * EK-Quote
         ODER = ENK + (Kaufpreis * (1 - Beleihungsquote))
Darlehenssumme = Gesamtinvestition - Eigenkapital
Annuitaet (jaehrlich) = Darlehenssumme * (Sollzins + Tilgung) / 100
Annuitaet (monatlich) = Annuitaet / 12
```

**Cashflow-Berechnung:**
```
Jahres-Nettokaltmiete (Ist)           =  JNKM
- Bewirtschaftungskosten               = -BWK
= Nettomietertrag                      =  NME
- Annuitaet (Zins + Tilgung)           = -ANN
= Cashflow vor Steuern                 =  CF_vSt
- Steuerlast (geschaetzt 30-42% auf    = -Steuer
  Ueberschuss, vereinfacht)
+ AfA-Effekt (geschaetzt)              = +AfA
= Cashflow nach Steuern (geschaetzt)   =  CF_nSt
```

**AfA-Schaetzung (vereinfacht):**
```
AfA-Satz:
- Baujahr bis 31.12.1924:  2,5% p.a. auf Gebaeudewert
- Baujahr 01.01.1925-31.12.2022: 2,0% p.a. auf Gebaeudewert
- Baujahr ab 01.01.2023:   3,0% p.a. auf Gebaeudewert
Gebaeudewert (geschaetzt) = Kaufpreis * 75% (Anteil Gebaeude vs. Boden)
AfA (jaehrlich) = Gebaeudewert * AfA-Satz
```

### Schritt 5: Eigenkapital-Rueckfluss

Die Kernfrage: **Wann bekomme ich mein Eigenkapital zurueck?**

```
Jaehrlicher Eigenkapital-Aufbau = Tilgungsanteil der Annuitaet + Cashflow vor Steuern
EK-Rueckfluss (Jahre) = Eigenkapital / Jaehrlicher EK-Aufbau
```

Bewertung:
| EK-Rueckfluss | Bewertung | Kommentar |
|---------------|-----------|-----------|
| < 8 Jahre | GRUEN | Sehr schneller EK-Rueckfluss, attraktiver Deal |
| 8-12 Jahre | GELB | Solider EK-Rueckfluss, marktgaengig |
| 12-18 Jahre | GELB-ROT | Langer EK-Rueckfluss, nur bei Wertsteigerungspotenzial |
| > 18 Jahre | ROT | Kapital ist zu lange gebunden |

### Schritt 6: Mieterhoehungspotenzial

Wenn Marktmiete bekannt oder schaetzbar:

```
Delta Ist zu Markt = Marktmiete/qm - Ist-Miete/qm
Jaehrliches Mieterhoehungspotenzial = Delta * Wohnflaeche * 12
Potenzial-Bruttomietrendite = ((JNKM + Mieterhoehungspotenzial) / Gesamtinvestition) * 100
```

**Realisierbarkeit einschaetzen:**
- Kappungsgrenze: Max. 15% (abgesenkt) oder 20% (normal) in 3 Jahren
- Mietpreisbremse bei Neuvermietung: Max. 10% ueber ortsueblicher Vergleichsmiete
- Fluktuation: ca. 8-12% der Mieter ziehen pro Jahr um (bei normaler Fluktuation)
- Zeitraum bis volle Marktmiete: ca. 5-8 Jahre realistisch

```
Realisierbares Mieterhoehungspotenzial (5 Jahre) = 
  Bestandsmieter: +Kappungsgrenze (15-20% in 3 Jahren)
  Neuvermietung (bei Fluktuation): Marktmiete (abzgl. Mietpreisbremse)
```

### Schritt 7: Sanierungskosten-Schaetzung (pauschal)

Wenn kein detaillierter Sanierungsplan vorliegt, schaetze pauschal:

| Baujahr | Zustand unsaniert | Zustand teilsaniert | Zustand kernsaniert |
|---------|-------------------|---------------------|---------------------|
| Vor 1950 | 800-1.500 EUR/qm | 400-800 EUR/qm | 100-250 EUR/qm |
| 1950-1970 | 600-1.200 EUR/qm | 300-600 EUR/qm | 80-200 EUR/qm |
| 1970-1990 | 400-900 EUR/qm | 200-450 EUR/qm | 50-150 EUR/qm |
| 1990-2010 | 200-500 EUR/qm | 100-250 EUR/qm | 30-100 EUR/qm |
| Nach 2010 | 50-200 EUR/qm | 30-100 EUR/qm | 0-50 EUR/qm |

**Heizungs-Sonderkosten (GEG):**

| Heizungstyp | Geschaetzte Umruestungskosten | Zeitdruck |
|-------------|-------------------------------|-----------|
| Oel-Heizung | 25.000-70.000 EUR | Hoch (Austausch bis 2026-2028) |
| Gas-Etagenheizung (alt) | 8.000-15.000 EUR pro Therme | Mittel (bei Ausfall) |
| Gas-Zentralheizung (alt) | 20.000-60.000 EUR | Mittel (bei Ausfall oder > 30 Jahre) |
| Gas-Zentralheizung (jung) | 0 EUR (vorerst) | Niedrig |
| Fernwaerme / Waermepumpe | 0 EUR | Kein Handlungsbedarf |

```
Geschaetzte Sanierungskosten = Wohnflaeche * Pauschale/qm + Heizungs-Sonderkosten
Gesamtinvestition inkl. Sanierung = Gesamtinvestition + Sanierungskosten
Rendite nach Sanierung = JNKM(Soll) / Gesamtinvestition inkl. Sanierung * 100
```

### Schritt 8: Aufteiler-Kalkulation (optional)

Wenn Strategie "Aufteiler" (Aufteilung in Eigentumswohnungen und Teilverkauf):

```
Geschaetzter ETW-Verkaufspreis/qm = Marktpreis fuer ETW im Stadtteil
Durchschnittliche WE-Groesse = Wohnflaeche / Anzahl WE
Verkaufspreis pro WE = ETW-Verkaufspreis/qm * Durchschn. WE-Groesse
Abzug Veraeusserungskosten = 3-5% (Makler, Notar, Aufwand)
Netto-Verkaufspreis pro WE = Verkaufspreis * (1 - Veraeusserungskosten)

Breakeven-Einheiten = Eigenkapital / Netto-Verkaufspreis pro WE  (aufgerundet)
```

Bewertung:
| Breakeven | Bewertung | Kommentar |
|-----------|-----------|-----------|
| < 25% der WE | GRUEN | EK frei nach wenigen Verkaeufen, Rest ist "Gewinn-Portfolio" |
| 25-40% der WE | GELB | Funktioniert, aber weniger Puffer |
| 40-60% der WE | GELB-ROT | Knappes Geschaeft, Vermarktungsrisiko |
| > 60% der WE | ROT | Aufteiler-Strategie rechnet sich nicht |

**Voraussetzungen Aufteilung pruefen:**
- Abgeschlossenheitsbescheinigung vorhanden oder beantragbar?
- Teilungserklaerung erforderlich (Notar + Kosten)
- Umwandlungsverbot pruefen (Milieuschutz-Gebiete: 7-10 Jahre Sperrfrist)
- Mieter-Vorkaufsrecht bei Erstverkauf nach Umwandlung
- Spekulationsfrist: 10 Jahre Haltefrist fuer steuerfreien Verkauf

### Schritt 9: Sofort-Ampel

Aggregiere alle Berechnungen zu einer Gesamtampel:

**GRUEN -- Kaufen pruefen:**
- Kaufpreisfaktor passt zur Lage (C/D: < 20, B: < 25, A: < 30)
- Bruttomietrendite >= 5% (B/C/D) bzw. >= 3,5% (A)
- Geschaetzte Nettomietrendite >= 3,5%
- Cashflow nach Finanzierung positiv oder break-even
- EK-Rueckfluss < 12 Jahre
- Mieterhoehungspotenzial vorhanden (> 10%)
- Sanierungskosten < 20% des Kaufpreises

**GELB -- Genauer hinschauen:**
- KPF am oberen Rand, aber Mietpotenzial erkennbar
- Cashflow leicht negativ (< -200 EUR/Monat), aber Tilgung baut EK auf
- Sanierungskosten 20-35% des Kaufpreises
- EK-Rueckfluss 12-18 Jahre
- Deal funktioniert nur mit Mieterhoehung

**ROT -- Finger weg:**
- KPF deutlich ueber Lage-Benchmark ohne erkennbares Potenzial
- Nettomietrendite < 2,5%
- Cashflow stark negativ (> -500 EUR/Monat)
- EK-Rueckfluss > 18 Jahre
- Sanierungskosten > 35% des Kaufpreises
- Miete bereits ueber Markt (kein Potenzial, Rueckgangsrisiko)

---

## Ausgabeformat

Liefere die Ergebnisse in folgendem Format:

### Bierdeckel (Freitext)

Stelle die Kalkulation so dar, wie sie auf einem Bierdeckel stehen wuerde -- kompakt, auf das Wesentliche reduziert, mit klarer Aussage. Max. 10 Zeilen.

Beispiel:
```
BIERDECKEL: MFH Dortmund-Nordstadt, 12 WE, 620 qm, Bj. 1962
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Kaufpreis:      1.850.000 EUR  (2.984 EUR/qm)
Ist-Miete:         63.240 EUR/Jahr  (8,50 EUR/qm)
KPF:                29,3x  ← zu hoch fuer C-Lage!
Brutto-Rendite:      3,4%  ← unter Schwelle
Netto (geschaetzt):  2,1%  ← kritisch
Cashflow/Monat:    -680 EUR  ← negativ
EK-Rueckfluss:     22 Jahre  ← viel zu lang
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AMPEL: ROT -- Finger weg (zum aktuellen Preis)
Verhandlungsziel: KP 1.200.000 EUR (KPF 19x)
```

### Strukturierte Kalkulation (JSON)

```json
{
  "bierdeckel_kalkulation": {
    "objekt": {
      "bezeichnung": "MFH Dortmund-Nordstadt, Beispielstr. 42",
      "kaufpreis_eur": 1850000,
      "wohnflaeche_qm": 620,
      "anzahl_we": 12,
      "baujahr": 1962,
      "heizungstyp": "Gas-Zentralheizung",
      "standort": "Dortmund, NRW",
      "lage_kategorie": "C"
    },
    "mietdaten": {
      "ist_miete_eur_qm": 8.50,
      "marktmiete_eur_qm": 9.50,
      "monatsmiete_nettokalt_eur": 5270,
      "jahresnettokaltmiete_eur": 63240,
      "jahresnettokaltmiete_soll_eur": 70680,
      "leerstand_we": 0,
      "leerstandsquote_prozent": 0
    },
    "erwerbsnebenkosten": {
      "grunderwerbsteuer_prozent": 6.5,
      "grunderwerbsteuer_eur": 120250,
      "notar_grundbuch_eur": 37000,
      "makler_eur": 66045,
      "enk_gesamt_eur": 223295,
      "enk_gesamt_prozent": 12.07,
      "gesamtinvestition_eur": 2073295
    },
    "kernkennzahlen": {
      "kaufpreisfaktor": 29.25,
      "all_in_kaufpreisfaktor": 32.78,
      "bruttomietrendite_prozent": 3.42,
      "all_in_bruttomietrendite_prozent": 3.05,
      "kaufpreis_pro_qm_eur": 2983.87
    },
    "bewirtschaftungskosten": {
      "nicht_umlagefaehige_nk_eur": 2530,
      "instandhaltungsruecklage_eur_qm_jahr": 15,
      "instandhaltungsruecklage_eur_jahr": 9300,
      "mietausfallwagnis_eur": 1897,
      "verwaltungskosten_eur": 3600,
      "bwk_gesamt_eur": 17327,
      "nettomietertrag_eur": 45913,
      "nettomietrendite_prozent": 2.21
    },
    "finanzierung": {
      "eigenkapital_eur": 518324,
      "eigenkapital_prozent": 25,
      "darlehenssumme_eur": 1554971,
      "sollzins_prozent": 3.80,
      "tilgung_prozent": 2.00,
      "annuitaet_jahr_eur": 90188,
      "annuitaet_monat_eur": 7516,
      "zinsanteil_jahr_1_eur": 59089,
      "tilgungsanteil_jahr_1_eur": 31099
    },
    "cashflow": {
      "nettomietertrag_eur": 45913,
      "annuitaet_eur": 90188,
      "cashflow_vor_steuern_jahr_eur": -44275,
      "cashflow_vor_steuern_monat_eur": -3690,
      "afa_jaehrlich_eur": 27750,
      "steuerlicher_verlust_eur": -16525,
      "cashflow_nach_steuern_geschaetzt_monat_eur": -3138
    },
    "eigenkapital_rueckfluss": {
      "jaehrlicher_ek_aufbau_eur": -13176,
      "ek_rueckfluss_jahre": null,
      "bewertung": "ROT",
      "kommentar": "Negativer Cashflow uebersteigt Tilgung. Kein EK-Aufbau, stattdessen Zuschussgeschaeft."
    },
    "mieterhoehungspotenzial": {
      "delta_ist_zu_markt_eur_qm": 1.00,
      "potenzial_jaehrlich_eur": 7440,
      "potenzial_prozent": 11.8,
      "realisierbar_5_jahre_prozent": 60,
      "potenzial_bruttomietrendite_prozent": 3.82,
      "kommentar": "Moderates Mieterhoehungspotenzial, reicht nicht aus um negativen Cashflow auszugleichen."
    },
    "sanierungskosten_schaetzung": {
      "zustand_annahme": "teilsaniert",
      "pauschale_eur_qm": 450,
      "sanierungskosten_bau_eur": 279000,
      "heizung_sonderkosten_eur": 40000,
      "sanierungskosten_gesamt_eur": 319000,
      "anteil_am_kaufpreis_prozent": 17.2,
      "gesamtinvestition_inkl_sanierung_eur": 2392295,
      "rendite_nach_sanierung_prozent": 2.95
    },
    "aufteiler_kalkulation": {
      "etw_verkaufspreis_eur_qm": 2200,
      "durchschnittliche_we_groesse_qm": 51.67,
      "brutto_verkaufspreis_pro_we_eur": 113674,
      "netto_verkaufspreis_pro_we_eur": 108490,
      "breakeven_einheiten": 5,
      "breakeven_anteil_prozent": 41.7,
      "bewertung": "GELB-ROT",
      "kommentar": "Fast die Haelfte der Einheiten muesste verkauft werden. Knappes Geschaeft."
    },
    "sofort_ampel": {
      "ampel": "ROT",
      "konfidenz_prozent": 70,
      "hauptgruende": [
        "KPF 29,3 ist deutlich zu hoch fuer C-Lage (Zielkorridor: 14-22)",
        "Bruttomietrendite 3,4% unter Schwelle fuer C-Lage (min. 5%)",
        "Cashflow stark negativ: -3.690 EUR/Monat",
        "Kein EK-Rueckfluss absehbar"
      ],
      "empfehlung": "Deal funktioniert zum aktuellen Preis nicht. Kaufpreisverhandlung auf ca. 1.200.000 EUR (KPF ~19) notwendig, um in den gruenen Bereich zu kommen.",
      "verhandlungsziel_eur": 1200000,
      "verhandlungsziel_kpf": 18.96,
      "verhandlungsziel_bruttomietrendite_prozent": 5.27
    },
    "metadaten": {
      "skill_version": "1.0",
      "analyse_datum": "2026-04-15",
      "analyst": "Bierdeckel-Kalkulation-Skill",
      "hinweis": "Pauschale Schaetzung, keine detaillierte Due Diligence. Alle Werte sind Naeherungen."
    }
  }
}
```

---

## Qualitaetspruefung

Vor Abgabe der Kalkulation pruefe:

1. **Rechnerische Konsistenz**: KPF = 1 / Bruttomietrendite * 100? Stimmt Monatsmiete * 12 = JNKM?
2. **Plausibilitaet der Miete**: Liegt die Ist-Miete in einem realistischen Bereich (4-15 EUR/qm fuer MFH)? Extrem hohe oder niedrige Werte hinterfragen.
3. **ENK-Berechnung**: Wurde das richtige Bundesland fuer die Grunderwerbsteuer verwendet?
4. **Cashflow-Vorzeichen**: Ist der Cashflow korrekt berechnet? Nettomietertrag minus Annuitaet.
5. **EK-Rueckfluss-Logik**: Bei negativem Cashflow: EK-Rueckfluss = unendlich (nicht berechenbar), nicht einfach ignorieren.
6. **Sanierungskosten-Plausibilitaet**: Passen die geschaetzten Kosten zum Baujahr? Ein Neubau von 2015 braucht keine 800 EUR/qm Sanierung.
7. **Ampel-Konsistenz**: Passt die Ampel zu den Zahlen? ROT bei positivem Cashflow waere inkonsistent.
8. **Verhandlungsziel**: Wurde bei ROT-Ampel ein realistisches Verhandlungsziel berechnet? (Ziel-KPF * JNKM = Ziel-Kaufpreis)

---

## Warnsignale & Dealbreaker

### Kalkulations-Dealbreaker (ROT)

| Signal | Schwelle | Kommentar |
|--------|----------|-----------|
| **Negativer Cashflow > 500 EUR/Monat** | Dauerhaftes Zuschussgeschaeft | Liquiditaetsrisiko, nur fuer stark kapitalisierte Investoren |
| **Nettomietrendite < 2,0%** | Unter Festgeld-Niveau | Immobilien-Risiko wird nicht verguetet |
| **EK-Rueckfluss > 20 Jahre** | Kapital zu lange gebunden | Opportunitaetskosten zu hoch |
| **Sanierungskosten > 40% des Kaufpreises** | Quasi-Neubau noetig | Neubau pruefen als Alternative |
| **KPF > 30 in B/C/D-Lage** | Voellig ueberteuert | Keine Verhandlungsbasis erkennbar |

### Kalkulatorische Warnsignale (GELB)

| Signal | Schwelle | Handlung |
|--------|----------|----------|
| **Cashflow break-even oder leicht negativ** | -200 bis 0 EUR/Monat | Nur akzeptabel wenn starkes Mietpotenzial |
| **Miete bereits ueber Markt** | Ist > Markt + 10% | Rueckgangsrisiko bei Mieterwechsel |
| **Hoher Gewerbeanteil** | > 25% der Miete | Gewerbe separat kalkulieren |
| **Sanierung erforderlich + Miete bereits hoch** | Kein Potenzial zur Refinanzierung | Sanierung aus Cashflow nicht darstellbar |
| **Aufteiler: Breakeven > 40%** | Vermarktungsrisiko | Sensitivitaetsrechnung mit -10% Verkaufspreis |

---

## Bei fehlenden Daten

| Fehlende Information | Annahme | Auswirkung auf Konfidenz |
|---------------------|---------|--------------------------|
| **Heizungstyp** | Gas-Zentralheizung annehmen, 30.000 EUR Umruestung einplanen | -5% |
| **Marktmiete** | Ist-Miete + 10% als konservative Annahme | -10% |
| **Finanzierungszins** | 3,8% Sollzins annehmen | -3% |
| **Sanierungszustand** | "Teilsaniert" annehmen (mittlere Pauschale) | -10% |
| **Gewerbeanteil** | 0% annehmen (reines Wohnhaus) | -2% |
| **Leerstand** | 0% annehmen, aber 3% Mietausfallwagnis | -5% |
| **Makler-Provision** | Bestellerprinzip: 3,57% Kaeuferanteil annehmen | -2% |
| **Strategie** | Buy-and-Hold annehmen | -0% |

**Basis-Konfidenz:** 70%
**Maximale Konfidenz:** 90% (Bierdeckel ist nie eine vollstaendige Kalkulation)
**Unter 50% Konfidenz:** Warnung ausgeben, dass zu viele Annahmen getroffen wurden.

---

## Konfidenz-Bewertung

| Konfidenz | Bedeutung | Typische Datenlage |
|-----------|-----------|-------------------|
| **80-90%** | Belastbare Bierdeckel-Kalkulation | Alle Pflichtangaben + Marktmiete + Heizung + Zustand bekannt |
| **65-79%** | Gute Ersteinschaetzung | Pflichtangaben vorhanden, optionale Daten teilweise geschaetzt |
| **50-64%** | Grobe Richtung | Mehrere wesentliche Annahmen getroffen |
| **< 50%** | Nur Tendenz | Zu viele Unbekannte, Kalkulation als "vorlaeufig" kennzeichnen |

---

## Verwandte Wissensdatenbanken

- `knowledge/kalkulationsformeln.md` -- Detaillierte Formeln fuer alle Renditekennzahlen und Cashflow-Berechnungen
- `knowledge/risikobewertung.md` -- Risiko-Scoring fuer die Interpretation der Kennzahlen
- `knowledge/marktbenchmarks.md` -- Benchmarks fuer KPF, Mieten, Sanierungskosten nach Region und Baujahr
- `knowledge/rechtsgrundlagen.md` -- Mietpreisbremse, Kappungsgrenze, AfA-Regelungen, GEG

### Verwandte Skills

- `skills/ankauf/deal-screener.md` -- Vorgelagertes Screening vor der Kalkulation
- `skills/ankauf/marktanalyse.md` -- Standortdaten fuer die Marktmiete-Schaetzung
- `skills/finanzierung/cashflow-modell.md` -- Detaillierte 5-Jahres-Cashflow-Projektion nach positivem Bierdeckel
- `skills/finanzierung/bankenkonzept.md` -- Finanzierungskonzept fuer die Bank
- `skills/objektpruefung/mietlisten-analyse.md` -- Detaillierte Mietlisten-Validierung
