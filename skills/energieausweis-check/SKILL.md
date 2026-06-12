---
name: energieausweis-check
description: "Analysiert Energieausweise (Bedarfs-/Verbrauchsausweis), bewertet energetischen Zustand, prueft GEG-2024-Konformitaet und berechnet Wirtschaftlichkeit energetischer Massnahmen (Kosten vs. Mieterhoehung vs. Wertsteigerung). Nutze diesen Skill wenn du einen Energieausweis vorliegen hast."
---

# Energieausweis-Check

> Analysiert Energieausweise deutscher Wohnimmobilien, bewertet GEG-Konformitaet, ermittelt energetischen Sanierungsbedarf und quantifiziert Kosten sowie Auswirkungen auf Mieterhoehungspotenzial durch energetische Modernisierung.

---

## Wann diesen Skill nutzen

- Du hast einen Energieausweis (Bedarfs- oder Verbrauchsausweis) als Dokument erhalten
- Du willst die energetische Qualitaet einer Immobilie einschaetzen
- Du brauchst eine Kostenschaetzung fuer energetische Sanierung
- Du willst pruefen, ob die Heizungsanlage GEG-konform ist oder ausgetauscht werden muss
- Du willst das Mieterhoehungspotenzial durch energetische Modernisierung berechnen

---

## Was du bereitstellen musst

### Pflicht-Eingaben
- **Energieausweis** (als Upload oder Daten)
  - Typ: Bedarfsausweis oder Verbrauchsausweis
  - Endenergiebedarf/-verbrauch in kWh/(qm*a)
  - Energieeffizienzklasse (A+ bis H)
  - Primaerer Energietraeger (Gas, Oel, Fernwaerme, Strom, Pellet etc.)
  - Ausstellungsdatum und Gueltigkeitsdauer

### Optionale Eingaben (erhoehen Analysequalitaet)
- Baujahr des Gebaeudes
- Baujahr und Typ der Heizungsanlage
- Angaben zu Daemmung (Fassade, Dach, Kellerdecke, Fenster)
- Modernisierungsempfehlungen aus dem Energieausweis
- Standort / Adresse (fuer kommunale Waermeplanung)
- Aktuelle Kaltmiete pro qm (fuer Modernisierungsumlage-Berechnung)
- Anzahl Wohneinheiten und Gesamtwohnflaeche

### Kontext
- Investmentstrategie (Buy & Hold, Value-Add)
- Geplanter Haltezeitraum
- Budget fuer energetische Sanierung

---

## Auftrag

Du bist ein Energieberater mit Schwerpunkt Wohnimmobilien als Kapitalanlage. Analysiere den Energieausweis, bewerte den energetischen Zustand, identifiziere Handlungsbedarf nach GEG 2024 und berechne die wirtschaftliche Sinnhaftigkeit energetischer Massnahmen aus Investorensicht (Kosten vs. Mieterhoehungspotenzial vs. Wertsteigerung).

---

## Strategie

### Schritt 1: Energieausweis-Typ bestimmen und bewerten

#### Bedarfsausweis vs. Verbrauchsausweis

| Merkmal | Bedarfsausweis | Verbrauchsausweis |
|---------|----------------|-------------------|
| Grundlage | Berechneter Energiebedarf auf Basis der Gebaeudehuelle und Anlagentechnik | Tatsaechlicher Energieverbrauch der letzten 3 Jahre |
| Aussagekraft | Gebaeudequalitaet, unabhaengig vom Nutzerverhalten | Beeinflusst durch Nutzerverhalten, Leerstand, Klima |
| Pflicht | Bei Wohngebaeuden < 5 WE (Bauantrag vor 1.11.1977, nicht saniert) | Bei Wohngebaeuden >= 5 WE oder Neubauten nach 1.11.1977 |
| Kosten Erstellung | 300-500 EUR | 50-100 EUR |
| Verlaesslichkeit fuer Investor | HOCH | MITTEL (Leerstand verfaelscht nach unten, Dauerbewohner nach oben) |

**Wichtiger Hinweis bei Verbrauchsausweis:**
- Leerstand drueckt den Verbrauch kuenstlich nach unten -- der reale Bedarf ist hoeher
- Bei hohem Leerstand (> 20%) ist der Verbrauchswert nicht belastbar
- Klimabereinigung pruefen (wurde der Verbrauch auf Referenzklima normiert?)

### Schritt 2: Energieeffizienzklasse einordnen

| Klasse | Endenergie kWh/(qm*a) | Bewertung | Typisches Gebaeude |
|--------|----------------------|-----------|---------------------|
| A+ | < 30 | Exzellent | Passivhaus, KfW 40 |
| A | 30-49 | Sehr gut | KfW 55-70, gut sanierter Neubau |
| B | 50-74 | Gut | Neubau nach EnEV 2014, gut sanierter Altbau |
| C | 75-99 | Durchschnitt | Neubau 2002-2014, teilsanierter Altbau |
| D | 100-129 | Unterdurchschnittlich | Aelterer Bestand, teilsaniert |
| E | 130-159 | Schlecht | Unsanierter Bestand ab 1970 |
| F | 160-199 | Sehr schlecht | Unsanierter Altbau, schlechte Anlagentechnik |
| G | 200-249 | Kritisch | Komplett unsaniert, Oel-/Nachtspeicherheizung |
| H | > 250 | Worst Case | Denkmal unsaniert, keine Daemmung, alte Heizung |

**Einordnung fuer den Investor:**
- **A+ bis C:** Kein akuter energetischer Handlungsbedarf. Zukunftssicher.
- **D bis E:** Mittelfristig Massnahmen sinnvoll. Heizungstausch pruefen.
- **F bis H:** Erheblicher Sanierungsbedarf. In Kaufpreiskalkulation einbeziehen.

### Schritt 3: GEG 2024 Compliance-Check (Gebaeudeenergiegesetz)

Pruefe systematisch die folgenden GEG-Anforderungen:

#### 3a: Heizungsregelungen (GEG 2024, "Heizungsgesetz")

| Regelung | Bedingung | Frist |
|----------|-----------|-------|
| Neuanlagen in Neubau (Neubaugebiet) | Mind. 65% erneuerbare Energien | Ab 01.01.2024 |
| Neuanlagen in Bestandsgebaeuden (Grossstaedte > 100.000 EW) | Mind. 65% erneuerbare Energien | Ab 30.06.2026 (nach kommunaler Waermeplanung) |
| Neuanlagen in Bestandsgebaeuden (Staedte < 100.000 EW) | Mind. 65% erneuerbare Energien | Ab 30.06.2028 (nach kommunaler Waermeplanung) |
| Bestehende funktionierende Heizungen | Kein Austauschzwang | Weiterbetrieb erlaubt |
| Konstanttemperaturkessel (Oel/Gas) aelter 30 Jahre | Austauschpflicht | Sofort (Ausnahmen: selbstgenutztes 1-2 FH seit vor 01.02.2002) |
| Defekte Heizung ohne Reparaturmoeglichkeit | Uebergangsregelung: 5 Jahre fossiler Weiterbetrieb | Dann 65%-EE-Pflicht |

#### 3b: Daemmungs-Nachruestpflichten (GEG)

| Pflicht | Bedingung |
|---------|-----------|
| Oberste Geschossdecke / Dach | Daemmung Pflicht, wenn nicht begehbar und ungedaemmt (U-Wert > 0.24 W/m2K) |
| Heizungs- und Warmwasserleitungen | Daemmung in unbeheizten Raeumen Pflicht |
| Hydraulischer Abgleich | Bei Einbau neuer Heizung Pflicht |

#### 3c: EU-Gebaeuderichtlinie (EPBD) -- Ausblick

| Zeitrahmen | Anforderung |
|------------|-------------|
| Ab 2030 | Worst-performing buildings (Klasse G/H) muessen verbessert werden |
| Ab 2033 | Naechste Stufe: mindestens Klasse E erreichen |
| Ab 2040 | Nullemissions-Standard fuer alle Gebaeude (Ziel) |

**Wichtig:** Die nationale Umsetzung der EPBD steht noch aus. Die konkreten Anforderungen koennen abweichen. Stand der Analyse vermerken.

### Schritt 4: Heizungsanalyse und Austausch-Timeline

| Heizungstyp | Typische Lebensdauer | Handlungsbedarf | Geschaetzte Austauschkosten |
|-------------|---------------------|-----------------|----------------------------|
| Oel-Heizung (Konstanttemperatur) | 20-25 Jahre | SOFORT (Austauschpflicht wenn > 30 Jahre) | 15.000-30.000 EUR (Waermepumpe) + Demontage Oeltank 2.000-5.000 EUR |
| Oel-Brennwert | 20-25 Jahre | Mittelfristig (spaetstens bei Defekt 65%-EE-Pflicht) | 15.000-30.000 EUR |
| Gas-Niedertemperatur | 20-25 Jahre | HOCH (wenn > 25 Jahre) | 12.000-25.000 EUR |
| Gas-Brennwert | 20-30 Jahre | Mittelfristig | 12.000-25.000 EUR |
| Nachtspeicherheizung | 25-30 Jahre | HOCH (hohe Betriebskosten, ineffizient) | 20.000-40.000 EUR (Zentralheizung nachrüsten) |
| Fernwaerme | Uebergabestation 20-30 Jahre | NIEDRIG | 5.000-15.000 EUR (Uebergabestation) |
| Waermepumpe | 15-25 Jahre | NIEDRIG | 15.000-30.000 EUR |
| Pellet-Heizung | 15-20 Jahre | NIEDRIG | 20.000-35.000 EUR |

**Bei MFH zusaetzlich beachten:**
- Kosten skalieren nicht linear -- groessere Anlagen sind pro qm guenstiger
- Foerderung pruefen (BEG/KfW: bis zu 70% Foerderung moeglich)
- Platz fuer Waermepumpe (Aussengeraet) vorhanden?
- Bei WEG: Beschluss der Eigentuememergemeinschaft erforderlich

### Schritt 5: Sanierungskosten-Schaetzung

Erstelle eine Kostenschaetzung fuer energetische Massnahmen basierend auf dem Energieausweis:

| Massnahme | Kosten EUR/qm Wohnflaeche | Energieeinsparung | Typische Amortisation |
|-----------|---------------------------|--------------------|-----------------------|
| Fassadendaemmung (WDVS 14cm) | 100-180 | 15-25% | 15-25 Jahre |
| Dachdaemmung / oberste Geschossdecke | 40-100 | 10-20% | 8-15 Jahre |
| Kellerdeckendaemmung | 25-50 | 5-10% | 5-10 Jahre |
| Fenster (3-fach Verglasung) | 50-80 | 10-15% | 15-25 Jahre |
| Heizungstausch (Gas -> Waermepumpe) | 50-120 (bezogen auf WF) | 20-40% | 10-15 Jahre (mit Foerderung) |
| Hydraulischer Abgleich | 3-8 | 5-10% | 2-5 Jahre |
| Daemmung Heizleitungen | 2-5 | 3-5% | 1-3 Jahre |

**Foerdermoeglichkeiten (Stand 2024/2025):**
- BEG Einzelmassnahmen: 15-20% Zuschuss
- Heizungstausch: Grundfoerderung 30% + Geschwindigkeitsbonus 20% + Einkommensbonus 30% = max. 70%
- KfW-Kredit: Bis zu 150.000 EUR je Wohneinheit
- Steuerliche Foerderung: 20% ueber 3 Jahre (Alternative zu Zuschuss)

### Schritt 6: Auswirkung auf Mieterhoehung (energetische Modernisierungsumlage)

Berechne das Mieterhoehungspotenzial nach BGB § 559:

**Formel:**
```
Jaehrliche Mieterhoehung = Modernisierungskosten * 8% / 12 Monate
Abzueglich: Foerderung und Instandhaltungsanteil
Kappungsgrenze: Max. 2 EUR/qm innerhalb von 6 Jahren
                 Max. 3 EUR/qm wenn Ausgangsmiete > 7 EUR/qm
```

**Rechenbeispiel:**
```
Fassadendaemmung: 150.000 EUR
- Instandhaltungsanteil (30%): -45.000 EUR
- KfW-Foerderung (15%): -22.500 EUR
= Umlegbare Kosten: 82.500 EUR

Mieterhoehung: 82.500 * 8% = 6.600 EUR/Jahr
Bei 850 qm = 0.65 EUR/qm/Monat

Pruefung Kappungsgrenze (2 EUR/qm):
0.65 EUR/qm < 2.00 EUR/qm -> zulaessig
```

**Wichtige Einschraenkungen:**
- Modernisierungsumlage nur fuer Verbesserungen, nicht fuer Instandsetzung
- Instandhaltungsanteil muss herausgerechnet werden (typisch 20-50%)
- Haerteeinwand des Mieters moeglich (§ 559 Abs. 4 BGB)
- Ankuendigung 3 Monate vorher mit detaillierter Berechnung erforderlich
- Mietpreisbremse gilt NICHT fuer Modernisierungsumlage (aber Kappungsgrenze schon)

---

## Ausgabeformat

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext.

### Zusammenfassung (Freitext)

Kurze Zusammenfassung in 3-5 Saetzen: Energetischer Zustand, dringendster Handlungsbedarf, wirtschaftliches Fazit aus Investorensicht.

### Ergebnisbericht

```markdown
# Energieausweis-Check: MFH Musterstrasse 12, 40210 Duesseldorf

**Energetisches Risiko: 🔴 HOCH** | Effizienzklasse: F | Konfidenz: 75%

## Objekt

| | |
|---|---|
| Adresse | Musterstrasse 12, 40210 Duesseldorf |
| Baujahr | 1965 |
| Wohnflaeche | 850 qm |
| Einheiten | 12 WE |

## Energieausweis

| | |
|---|---|
| Typ | Verbrauchsausweis |
| Ausstellungsdatum | 15.05.2023 |
| Gueltig bis | 14.05.2033 (🟢 gueltig) |
| Endenergie | 185 kWh/(qm*a) |
| Primaerenergie | 210 kWh/(qm*a) |
| Effizienzklasse | F (sehr schlecht) |
| Energietraeger | Erdgas |
| CO2-Emissionen | 42 kg/(qm*a) |
| Verlaesslichkeit | 🟡 Mittel -- Verbrauchsausweis bei 8% Leerstand, realer Bedarf ca. 10-15% hoeher |

## Heizungsanlage

| | |
|---|---|
| Typ | Gas-Niedertemperatur |
| Einbaujahr | 1998 (Alter: 28 Jahre) |
| Erwartete Restlebensdauer | 0 Jahre |
| GEG-konform | 🔴 Nein -- Austauschpflicht |
| Austauschfrist | Sofort (Konstanttemperaturkessel > 30 Jahre) |
| Empfohlener Ersatz | Luft-Wasser-Waermepumpe |
| Geschaetzte Austauschkosten | 85.000 EUR |
| Verfuegbare Foerderung | 42.500 EUR |
| Netto-Kosten nach Foerderung | 42.500 EUR |

## GEG-Konformitaet

**Gesamtstatus: 🔴 NICHT KONFORM**

| Anforderung | Rechtsgrundlage | Status | Frist | Geschaetzte Kosten |
|-------------|-----------------|--------|-------|--------------------|
| Austauschpflicht Konstanttemperaturkessel > 30 Jahre | GEG § 72 | 🔴 Nicht erfuellt | Sofort | 85.000 EUR |

**Kommende Anforderungen:**

| Anforderung | Erwartet ab | Auswirkung |
|-------------|-------------|------------|
| Kommunale Waermeplanung -- 65% EE bei Heizungstausch | 30.06.2026 | Bei naechstem Heizungstausch muessen 65% erneuerbare Energien erfuellt werden |

## Daemmzustand

| Bauteil | Zustand | Geschaetzter U-Wert | Handlungsbedarf |
|---------|---------|---------------------|-----------------|
| Fassade | Ungedaemmt | 1,5 W/m2K | 🔴 Ja |
| Dach | Teilgedaemmt | 0,8 W/m2K | 🔴 Ja |
| Kellerdecke | Ungedaemmt | 1,0 W/m2K | 🔴 Ja |
| Fenster | Zweifachverglasung | 2,8 W/m2K | 🔴 Ja |

## Sanierungsfahrplan

| Massnahme | Prioritaet | Kosten | Foerderung | Netto | Einsparung | Amortisation | Mieterhoehungspotenzial | Klasse danach |
|-----------|-----------|--------|------------|-------|------------|--------------|--------------------------|----------------|
| Heizungstausch Gas -> Waermepumpe | SOFORT | 85.000 EUR | 42.500 EUR | 42.500 EUR | 30% (47.000 kWh/a, 5.600 EUR/a) | 7,6 Jahre | +0,33 EUR/qm/Monat | D |

## Wirtschaftliche Gesamtbetrachtung

| Kennzahl | Wert |
|----------|------|
| Gesamtkosten Sanierung | 285.000 EUR |
| Foerderungen gesamt | 95.000 EUR |
| Netto-Kosten | 190.000 EUR |
| Jaehrliche Energiekosteneinsparung | 12.500 EUR |
| Jaehrliches Mieterhoehungspotenzial | 9.600 EUR |
| Jaehrlicher Gesamtnutzen | 22.100 EUR |
| Einfache Amortisation | 8,6 Jahre |
| Ziel-Energieklasse | C |
| Geschaetzte Wertsteigerung | ca. 8% |

## Risiken und Chancen

**Risiken:**
- Heizungstausch-Pflicht nicht erfuellt -- Bussgeld moeglich
- EU-EPBD koennte ab 2030 weitere Sanierung erzwingen

**Chancen:**
- Durch Sanierung von F auf C: Wertsteigerung ca. 8%
- Modernisierungsumlage: +0,94 EUR/qm/Monat moeglich

## Einschraenkungen der Analyse

Konfidenz: 75%. Begrenzende Faktoren:
- Verbrauchsausweis weniger aussagekraeftig als Bedarfsausweis
- Daemmzustand nur geschaetzt (keine Vor-Ort-Pruefung)
```

---

## Qualitaetspruefung

Vor Ausgabe des Ergebnisses pruefe:

- [ ] Energieausweis-Typ korrekt identifiziert und Einschraenkungen benannt
- [ ] Energieeffizienzklasse korrekt zugeordnet
- [ ] GEG-Anforderungen auf aktuellem Stand (GEG 2024)
- [ ] Heizungsalter korrekt berechnet und Austauschpflicht geprueft
- [ ] Kostenschaetzungen in realistischen Bandbreiten (nicht zu optimistisch)
- [ ] Foerderungen mit aktuellem Stand angegeben (BEG/KfW)
- [ ] Modernisierungsumlage korrekt berechnet (8%, Instandhaltungsanteil abgezogen, Kappungsgrenze geprueft)
- [ ] Keine Verwechslung zwischen Endenergie und Primaerenergie
- [ ] Amortisationsrechnung nachvollziehbar

---

## Warnsignale & Dealbreaker

| Signal | Risikostufe | Auswirkung |
|--------|-------------|------------|
| Energieklasse G oder H | HOCH | EU-EPBD erzwingt Sanierung ab 2030, hohe Kosten |
| Oelheizung > 25 Jahre | HOCH | Sofortige Austauschpflicht, Oeltank-Entsorgung |
| Nachtspeicherheizung | HOCH | Ineffizient, hohe Betriebskosten, Asbestrisiko |
| Kein Energieausweis vorhanden | MITTEL | Bussgeld bis 10.000 EUR moeglich, Pflichtversaeumnis |
| Energieausweis abgelaufen | MITTEL | Neuerstellung erforderlich (Verkaeufer-Pflicht) |
| Fernwaerme nicht verfuegbar + Waermepumpe nicht moeglich | MITTEL | Eingeschraenkte Optionen fuer 65%-EE-Erfuellung |
| Denkmalschutz + schlechte Energieklasse | HOCH | Fassadendaemmung moeglicherweise nicht genehmigungsfaehig |
| Einrohrheizung | MITTEL | Hydraulischer Abgleich schwierig, Austausch teuer |

---

## Bei fehlenden Daten

1. **Ohne Energieausweis:** Schaetzung auf Basis von Baujahr und typischer Ausstattung der Baujahrsklasse
   - Vor 1949: Typisch Klasse F-H (180-300+ kWh/qm*a)
   - 1950-1969: Typisch Klasse E-G (140-220 kWh/qm*a)
   - 1970-1989: Typisch Klasse D-F (120-190 kWh/qm*a)
   - 1990-2001: Typisch Klasse C-D (90-130 kWh/qm*a)
   - 2002-2013: Typisch Klasse B-C (60-100 kWh/qm*a)
   - Ab 2014: Typisch Klasse A-B (30-75 kWh/qm*a)

2. **Ohne Heizungsdaten:** Auf Fotos achten (Keller), Verkaeufer/Makler fragen
3. **Ohne Wohnflaeche:** Kostenschaetzung in EUR/qm angeben, absolute Kosten nicht berechenbar
4. **Confidence Score reduzieren** und fehlende Daten explizit benennen

---

## Konfidenz-Bewertung

| Datenlage | Score | Bedeutung |
|-----------|-------|-----------|
| Bedarfsausweis + Heizungsdaten + Fotos | 0.85-1.00 | Belastbare Analyse |
| Verbrauchsausweis + Heizungsdaten | 0.65-0.84 | Gute Grundlage, Verbrauchswert eingeschraenkt |
| Nur Energieausweis (ohne Details) | 0.45-0.64 | Grobe Einschaetzung moeglich |
| Kein Energieausweis, nur Baujahr | 0.20-0.44 | Nur Schaetzung auf Basis Baujahrsklasse |

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- GEG-Anforderungen, Modernisierungsumlage (§ 559 BGB)
- `knowledge/kalkulationsformeln.md` -- Renditeberechnung inkl. Sanierungskosten
- `knowledge/marktbenchmarks.md` -- Sanierungskosten-Benchmarks nach Baujahr
- `skills/unterlagen-analyst/SKILL.md` -- Gesamtanalyse der Objektunterlagen
- `skills/risiko-scanner/SKILL.md` -- Kategorie 4: Energetische Risiken (Zusammenspiel)
- `skills/besichtigung-prep/SKILL.md` -- Heizungs- und Daemmungs-Check bei Besichtigung
- `skills/mieterhoehung/SKILL.md` -- Modernisierungsumlage in Mieterhoehungsstrategie integrieren
