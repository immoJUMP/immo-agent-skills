# Kalkulationsformeln - Deutsche Immobilieninvestition

## 1. Kaufpreisfaktor (Vervielfältiger)

```
Kaufpreisfaktor = Kaufpreis / Jahresnettokaltmiete
```

**Interpretation:**
- < 15: Sehr günstig (meist C/D-Lagen oder sanierungsbedürftig)
- 15-20: Günstig / fair bewertet
- 20-25: Marktüblich in guten Lagen
- 25-30: Teuer, typisch für A-Lagen / Top-7-Städte
- > 30: Sehr teuer, nur bei starkem Wertsteigerungspotenzial

**Beispiel:**
- Kaufpreis: 250.000 EUR
- Monatliche Nettokaltmiete: 850 EUR
- Jahresnettokaltmiete: 850 × 12 = 10.200 EUR
- Kaufpreisfaktor: 250.000 / 10.200 = **24,5**

---

## 2. Bruttomietrendite

```
Bruttomietrendite (%) = (Jahresnettokaltmiete / Kaufpreis) × 100
```

**Beispiel:**
- Jahresnettokaltmiete: 10.200 EUR
- Kaufpreis: 250.000 EUR
- Bruttomietrendite: (10.200 / 250.000) × 100 = **4,08%**

---

## 3. Nettomietrendite

```
Nettomietrendite (%) = ((Jahresnettokaltmiete - nicht umlagefähige Kosten) / (Kaufpreis + Erwerbsnebenkosten)) × 100
```

**Nicht umlagefähige Kosten (typisch):**
- Instandhaltungsrücklage
- Verwaltungskosten (Hausverwaltung)
- Mietausfallwagnis (ca. 2-4% der Jahresnettokaltmiete)
- Nicht umlagefähige Betriebskosten

**Beispiel:**
- Jahresnettokaltmiete: 10.200 EUR
- Nicht umlagefähige Kosten: 2.400 EUR/Jahr
- Kaufpreis: 250.000 EUR
- Erwerbsnebenkosten: 28.750 EUR (11,5%)
- Nettomietrendite: ((10.200 - 2.400) / (250.000 + 28.750)) × 100 = **2,80%**

---

## 4. Erwerbsnebenkosten nach Bundesland

### Grunderwerbsteuer (Stand 2026)

| Bundesland | Grunderwerbsteuer |
|---|---|
| Bayern | 3,5% |
| Sachsen | 3,5% |
| Hamburg | 5,5% |
| Baden-Württemberg | 5,0% |
| Berlin | 6,0% |
| Brandenburg | 6,5% |
| Bremen | 5,0% |
| Hessen | 6,0% |
| Mecklenburg-Vorpommern | 6,0% |
| Niedersachsen | 5,0% |
| Nordrhein-Westfalen | 6,5% |
| Rheinland-Pfalz | 5,0% |
| Saarland | 6,5% |
| Sachsen-Anhalt | 5,0% |
| Schleswig-Holstein | 6,5% |
| Thüringen | 5,0% |

### Weitere Erwerbsnebenkosten

| Position | Kosten |
|---|---|
| Notarkosten | ca. 1,5% des Kaufpreises |
| Grundbuchkosten | ca. 0,5% des Kaufpreises |
| Maklercourtage | 0% - 7,14% (inkl. MwSt.) |

**Hinweis Maklercourtage:** Seit 23.12.2020 gilt bei Kaufverträgen über Wohnungen und Einfamilienhäuser das Halbteilungsprinzip (§656d BGB). Der Makler darf vom Käufer maximal den gleichen Anteil verlangen wie vom Verkäufer.

### Gesamtberechnung Erwerbsnebenkosten

```
Erwerbsnebenkosten = Kaufpreis × (Grunderwerbsteuer + Notar + Grundbuch + Makler)
```

**Beispiel NRW mit Makler:**
- Kaufpreis: 250.000 EUR
- Grunderwerbsteuer: 6,5% = 16.250 EUR
- Notar: 1,5% = 3.750 EUR
- Grundbuch: 0,5% = 1.250 EUR
- Makler (Käuferanteil): 3,57% = 8.925 EUR
- **Gesamt: 30.175 EUR (12,07%)**

**Beispiel Bayern ohne Makler:**
- Kaufpreis: 250.000 EUR
- Grunderwerbsteuer: 3,5% = 8.750 EUR
- Notar: 1,5% = 3.750 EUR
- Grundbuch: 0,5% = 1.250 EUR
- **Gesamt: 13.750 EUR (5,5%)**

---

## 5. Cashflow-Berechnung

```
Monatlicher Cashflow = Nettokaltmiete
                     - Hausgeld (nicht umlagefähiger Anteil)
                     - Annuität (Zins + Tilgung)
                     - Instandhaltungsrücklage (falls nicht im Hausgeld)
                     - Verwaltungskosten (falls nicht im Hausgeld)
                     - Mietausfallwagnis
```

**Beispiel:**
- Nettokaltmiete: 850 EUR/Monat
- Hausgeld (nicht umlagefähig): 120 EUR/Monat
- Annuität: 625 EUR/Monat (siehe Berechnung unten)
- Instandhaltungsrücklage: 80 EUR/Monat (im Hausgeld enthalten)
- Verwaltungskosten: 30 EUR/Monat (im Hausgeld enthalten)
- Mietausfallwagnis (3%): 25,50 EUR/Monat
- **Monatlicher Cashflow: 850 - 120 - 625 - 25,50 = 79,50 EUR**
- **Jährlicher Cashflow: 954 EUR**

---

## 6. Annuitätenberechnung

### Vereinfachte Formel (Praxisüblich)

```
Monatliche Annuität = Darlehensbetrag × (Sollzins + Tilgung) / 12
```

**Beispiel:**
- Darlehensbetrag: 200.000 EUR
- Sollzins: 3,5% p.a.
- Anfängliche Tilgung: 1,25% p.a.
- Jährliche Annuität: 200.000 × (0,035 + 0,0125) = 9.500 EUR
- **Monatliche Annuität: 9.500 / 12 = 791,67 EUR**

### Exakte Annuitätenformel

```
Monatliche Rate = Darlehensbetrag × (q^n × (q - 1)) / (q^n - 1)
wobei q = 1 + (Sollzins / 12) und n = Laufzeit in Monaten
```

---

## 7. Debt Service Coverage Ratio (DSCR)

```
DSCR = Jahresnettomieteinnahmen / Jährlicher Kapitaldienst (Zins + Tilgung)
```

**Bewertung:**
- < 1,0: Negativer Cashflow - Zuschuss erforderlich
- 1,0 - 1,1: Knapp tragfähig, kaum Puffer
- 1,1 - 1,3: Solide Tragfähigkeit
- > 1,3: Komfortable Tragfähigkeit

**Beispiel:**
- Jahresnettomieteinnahmen (nach nicht umlagefähigen Kosten): 7.800 EUR
- Jährlicher Kapitaldienst: 9.500 EUR
- DSCR: 7.800 / 9.500 = **0,82** (negativer Cashflow!)

---

## 8. Beleihungswert und Beleihungsauslauf

### Beleihungswert

```
Beleihungswert = Kaufpreis × Abschlagsfaktor (Bank-individuell, typisch 80-90%)
```

Alternativ ermittelt die Bank den Beleihungswert über ein eigenes Verfahren (Ertragswert, Sachwert).

### Beleihungsauslauf (BLA)

```
Beleihungsauslauf (%) = Darlehensbetrag / Beleihungswert × 100
```

**Typische Grenzen:**
- Bis 60% BLA: Beste Konditionen
- 60-80% BLA: Standardkonditionen
- 80-90% BLA: Zinsaufschlag
- 90-100% BLA: Hoher Zinsaufschlag
- > 100% BLA: Vollfinanzierung, selten vergeben

**Beispiel:**
- Kaufpreis: 250.000 EUR
- Beleihungswert (Bank): 225.000 EUR (90% des KP)
- Darlehensbetrag: 200.000 EUR
- Beleihungsauslauf: 200.000 / 225.000 × 100 = **88,9%**

---

## 9. Eigenkapitalrendite (EK-Rendite)

```
EK-Rendite (%) = Jährlicher Cashflow / Eingesetztes Eigenkapital × 100
```

**Eingesetztes Eigenkapital:**
```
EK = Kaufpreis - Darlehensbetrag + Erwerbsnebenkosten + ggf. Sanierungskosten
```

**Beispiel:**
- Kaufpreis: 250.000 EUR
- Darlehensbetrag: 200.000 EUR
- Erwerbsnebenkosten: 28.750 EUR
- Eigenkapital: 250.000 - 200.000 + 28.750 = 78.750 EUR
- Jährlicher Cashflow: 954 EUR
- EK-Rendite: 954 / 78.750 × 100 = **1,21%**

**Erweiterte EK-Rendite (inkl. Tilgung und Wertsteigerung):**
```
Erweiterte EK-Rendite = (Cashflow + jährliche Tilgung + Wertsteigerung) / EK × 100
```

- Jährliche Tilgung: ca. 2.500 EUR
- Angenommene Wertsteigerung (1%): 2.500 EUR
- Erweiterte EK-Rendite: (954 + 2.500 + 2.500) / 78.750 × 100 = **7,56%**

---

## 10. EK-Rückfluss in Jahren

```
EK-Rückfluss (Jahre) = Eingesetztes Eigenkapital / Jährlicher Cashflow
```

**Beispiel:**
- Eigenkapital: 78.750 EUR
- Jährlicher Cashflow: 954 EUR
- EK-Rückfluss: 78.750 / 954 = **82,5 Jahre** (zu lang!)

**Hinweis:** Ein EK-Rückfluss von > 20 Jahren deutet auf eine schwache Cashflow-Performance hin. Zielwert für Kapitalanleger: 10-15 Jahre.

---

## 11. Modernisierungsumlage (§559 BGB)

```
Monatliche Mieterhöhung pro Einheit = (Modernisierungskosten × 8%) / 12
```

**Seit 01.01.2019 gelten folgende Grenzen:**
- Maximal 8% der Modernisierungskosten dürfen auf die Jahresmiete umgelegt werden (vorher 11%)
- Kappungsgrenze: Mieterhöhung darf innerhalb von 6 Jahren nicht mehr als 3 EUR/qm betragen
- Bei Mieten unter 7 EUR/qm: max. 2 EUR/qm innerhalb von 6 Jahren

**Beispiel:**
- Modernisierungskosten (Heizungstausch): 25.000 EUR
- Abzug Instandhaltungsanteil: 8.000 EUR
- Umlagefähige Kosten: 17.000 EUR
- Jährliche Umlage: 17.000 × 8% = 1.360 EUR
- Monatliche Mieterhöhung: 1.360 / 12 = **113,33 EUR**
- Wohnfläche: 65 qm
- Erhöhung pro qm: 113,33 / 65 = **1,74 EUR/qm** (unter Kappungsgrenze)

---

## 12. Kappungsgrenze (§558 Abs. 3 BGB)

```
Maximale Mieterhöhung = Ausgangsmiete × Kappungsgrenze (%) über 3 Jahre
```

**Reguläre Kappungsgrenze:** 20% in 3 Jahren
**Abgesenkte Kappungsgrenze:** 15% in 3 Jahren (in Gebieten mit angespanntem Wohnungsmarkt, durch Landesverordnung bestimmt)

**Voraussetzungen für Mieterhöhung nach §558:**
- Miete liegt unter ortsüblicher Vergleichsmiete
- Letzte Mieterhöhung mindestens 15 Monate her
- Mieterhöhungsverlangen muss begründet werden (Mietspiegel, Gutachten, Vergleichswohnungen)

**Beispiel:**
- Aktuelle Nettokaltmiete: 600 EUR (9,23 EUR/qm bei 65 qm)
- Ortsübliche Vergleichsmiete: 780 EUR (12,00 EUR/qm)
- Kappungsgrenze (abgesenkt): 15% in 3 Jahren
- Maximale Erhöhung: 600 × 15% = 90 EUR
- Neue Miete: maximal 690 EUR (obwohl Vergleichsmiete höher)
- Nach weiteren 3 Jahren: nächste Erhöhung auf max. 690 × 1,15 = 793,50 EUR

---

## 13. AfA-Berechnung (Absetzung für Abnutzung)

### Gebäudeanteil ermitteln

```
Gebäudeanteil = Kaufpreis - Bodenwert
Bodenwert = Grundstücksfläche × Bodenrichtwert
```

**Alternativ:** Aufteilung nach BMF-Arbeitshilfe (Excel-Tool des Bundesfinanzministeriums)

### AfA-Sätze

| Baujahr | AfA-Satz | Nutzungsdauer |
|---|---|---|
| Ab 1925 | 2,0% p.a. | 50 Jahre |
| Vor 1925 | 2,5% p.a. | 40 Jahre |
| Ab 2023 (Neubau) | 3,0% p.a. | 33 Jahre |
| Denkmal-AfA (§7i EStG) | bis 9% (8 Jahre) + 7% (4 Jahre) | Sonderregelung |

### Berechnung

```
Jährliche AfA = Gebäudeanteil × AfA-Satz
```

**Beispiel:**
- Kaufpreis: 250.000 EUR
- Bodenwert: 60.000 EUR
- Gebäudeanteil: 190.000 EUR
- Baujahr: 1965
- AfA-Satz: 2,0%
- Jährliche AfA: 190.000 × 2,0% = **3.800 EUR**
- Steuerersparnis (bei 42% Grenzsteuersatz): 3.800 × 42% = **1.596 EUR/Jahr**

### Denkmal-AfA (§7i EStG)

Für denkmalgeschützte Gebäude können Sanierungskosten erhöht abgeschrieben werden:

**Vermietung:**
- 9% jährlich über 8 Jahre = 72%
- 7% jährlich über 4 Jahre = 28%
- Gesamt: 100% der Sanierungskosten in 12 Jahren

**Eigennutzung (§10f EStG):**
- 9% jährlich über 10 Jahre = 90%

**Beispiel Denkmal-AfA:**
- Sanierungskosten: 150.000 EUR
- Jahre 1-8: 150.000 × 9% = 13.500 EUR/Jahr
- Jahre 9-12: 150.000 × 7% = 10.500 EUR/Jahr
- Steuerersparnis Jahr 1-8 (42% Steuersatz): 5.670 EUR/Jahr

---

## 14. Vollständige Beispielkalkulation

### Objektdaten
- Eigentumswohnung in Leipzig, Baujahr 1962
- Wohnfläche: 65 qm, 3 Zimmer
- Kaufpreis: 130.000 EUR
- Nettokaltmiete: 520 EUR/Monat (8,00 EUR/qm)

### Erwerbsnebenkosten (Sachsen)
- Grunderwerbsteuer (3,5%): 4.550 EUR
- Notar (1,5%): 1.950 EUR
- Grundbuch (0,5%): 650 EUR
- Makler (3,57% Käuferanteil): 4.641 EUR
- **Gesamt: 11.791 EUR (9,07%)**

### Finanzierung
- Eigenkapital: 11.791 EUR (nur Nebenkosten)
- Darlehen: 130.000 EUR (100% Finanzierung)
- Sollzins: 3,8% p.a.
- Tilgung: 2,0% p.a.
- Monatliche Annuität: 130.000 × (0,038 + 0,02) / 12 = **628,33 EUR**

### Monatlicher Cashflow
- Nettokaltmiete: +520,00 EUR
- Hausgeld (nicht umlagefähig): -95,00 EUR
- Annuität: -628,33 EUR
- Mietausfallwagnis (3%): -15,60 EUR
- **Monatlicher Cashflow: -218,93 EUR**
- **Jährlicher Cashflow: -2.627,16 EUR**

### Steuerliche Betrachtung
- Mieteinnahmen: 6.240 EUR/Jahr
- Abzugsfähige Kosten: -1.140 EUR (nicht umlagefähig)
- Zinsen: -4.940 EUR (130.000 × 3,8%)
- AfA: -2.400 EUR (120.000 Gebäudeanteil × 2%)
- **Steuerliches Ergebnis: -2.240 EUR**
- Steuerersparnis (42%): **940,80 EUR**

### Cashflow nach Steuern
- Cashflow vor Steuern: -2.627,16 EUR
- Steuerersparnis: +940,80 EUR
- **Cashflow nach Steuern: -1.686,36 EUR/Jahr (-140,53 EUR/Monat)**

### Vermögensaufbau
- Jährliche Tilgung: 2.600 EUR
- Angenommene Wertsteigerung (1,5%): 1.950 EUR
- Cashflow nach Steuern: -1.686,36 EUR
- **Netto-Vermögensaufbau: 2.863,64 EUR/Jahr**
- **EK-Rendite (auf EK von 11.791 EUR): 24,3%**
