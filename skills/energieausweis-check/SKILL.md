---
name: energieausweis-check
description: "Analysiert Energieausweise (Bedarfs-/Verbrauchsausweis), bewertet energetischen Zustand, prueft Pflichten nach dem Gebaeudemodernisierungsgesetz (GModG, vormals GEG) und berechnet Wirtschaftlichkeit energetischer Massnahmen (Kosten vs. Mieterhoehung vs. Wertsteigerung). Nutze diesen Skill wenn du einen Energieausweis vorliegen hast."
---

# Energieausweis-Check

> Analysiert Energieausweise deutscher Wohnimmobilien, prueft die Pflichten nach dem Gebaeudemodernisierungsgesetz (GModG), ermittelt energetischen Sanierungsbedarf und quantifiziert Kosten sowie Auswirkungen auf Mieterhoehungspotenzial durch energetische Modernisierung.

---

## Wann diesen Skill nutzen

- Du hast einen Energieausweis (Bedarfs- oder Verbrauchsausweis) als Dokument erhalten
- Du willst die energetische Qualitaet einer Immobilie einschaetzen
- Du brauchst eine Kostenschaetzung fuer energetische Sanierung
- Du willst wissen, welche gesetzlichen Pflichten fuer Heizung und Daemmung bestehen und wann die Heizung ans Ende ihrer Lebensdauer kommt
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

Du bist ein Energieberater mit Schwerpunkt Wohnimmobilien als Kapitalanlage. Analysiere den Energieausweis, bewerte den energetischen Zustand, pruefe die Pflichten nach dem Gebaeudemodernisierungsgesetz (GModG, Rechtsstand in Schritt 3) und berechne die wirtschaftliche Sinnhaftigkeit energetischer Massnahmen aus Investorensicht (Kosten vs. Mieterhoehungspotenzial vs. Wertsteigerung).

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
- Auch sparsame Nutzer oder Dauerbewohner verzerren das Bild (Nutzerverhalten dominiert den Wert)
- Bei hohem Leerstand (> 20%) ist der Verbrauchswert nicht belastbar
- Klimabereinigung pruefen (wurde der Verbrauch auf Referenzklima normiert?)

#### Formale Pruefung und Plausibilisierung

- **Gueltigkeit:** Energieausweis gilt 10 Jahre ab Ausstellung -- Ablaufdatum pruefen
- **Denkmalschutz:** Denkmalgeschuetzte Gebaeude koennen von der Ausweispflicht ausgenommen sein -- Pruefbedarf statt pauschaler Annahme
- **Fehlerquote:** Branchenschaetzungen zufolge ist rund jeder dritte Energieausweis fehlerhaft. Kennwerte daher IMMER plausibilisieren: Passt der Kennwert zu Baujahr, Daemmzustand und Heizung? Klasse B bei unsaniertem 60er-Jahre-Bau ist unplausibel
- **End- vs. Primaerenergie:** Endenergie beschreibt den Gebaeudebedarf am Zaehler, Primaerenergie gewichtet zusaetzlich den Energietraeger -- nie verwechseln
- **Modernisierungsempfehlungen im Ausweis:** Pflichtbestandteil, aber keine fertige Sanierungsplanung -- als Pruefhinweise fuer den Energieberater nutzen
- **Bank-Relevanz:** Der Energieausweis ist Bank- und Pflichtdokument; schlechte Klassen beeinflussen Beleihung und Konditionen

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

### Schritt 3: Pflichten nach dem Gebaeudemodernisierungsgesetz (GModG)

**Rechtsstand: 12.11.2026.** Seit 29.07.2026 heisst das Gebaeudeenergiegesetz "Gebaeudemodernisierungsgesetz (GModG)" (Gesetz vom 23.07.2026, BGBl. 2026 I Nr. 226, Art. 1 Nr. 1 und Art. 9 Abs. 1). Paragrafen im Bestand sind teilweise neu nummeriert. Den Stand im Bericht immer mit Datum nennen.

**Grundregel: Das Alter einer Heizung ist keine Rechtspflicht und kein rechtlicher Kaufpreisabzug.** Eine alte Heizung ist eine Renovierungsposition nach Restlebensdauer (Schritt 4). Nennen Energieausweis, Expose, Gutachten oder Verkaeuferunterlagen noch eine Pflicht zum Austausch nach 30 Jahren, eine 65-Prozent-Vorgabe oder das Ende fossiler Kessel 2044: Das ist der Stand vor dem 29.07.2026. Nicht uebernehmen, sondern im Bericht als veraltet kennzeichnen.

#### 3a: Heizung

| Regelung | Inhalt | Quelle |
|----------|--------|--------|
| Bestehende Heizung, gleich welchen Alters | Darf weiterlaufen. Das fruehere Betriebsverbot fuer 30 Jahre alte Konstanttemperaturkessel, die 65-Prozent-Vorgabe fuer neue Heizungen, die Beratungspflicht vor dem Einbau und das Ende fossiler Kessel zum 31.12.2044 sind gestrichen | Art. 1 Nr. 32 BGBl. 2026 I Nr. 226 (§§ 71 bis 73 GEG aufgehoben) |
| Ersatz der Heizung im Bestand | Freie Wahl: Gas, Heizoel, Fluessiggas, Waermepumpe, Solarthermie, Biomasse oder Wasserstoff, Hybride, KWK, Stromdirektheizung, Waermenetz, andere innovative Loesung | § 42 GModG |
| Neue Gas-, Oel- oder Fluessiggasheizung, eingebaut nach dem 29.07.2026 ("Bio-Treppe") | Anteil der Waerme aus Biomethan, Bioheizoel, biogenem Fluessiggas oder Wasserstoff: ab 01.01.2029 mind. 10 %, ab 2030 15 %, ab 2035 30 %, ab 2040 60 %. Auch erfuellbar ueber Solarthermie (bis 2034 pauschal ab 0,03-0,04 qm Aperturflaeche je qm Nutzflaeche), Lueftung mit Waermerueckgewinnung oder Waermepumpen-Hybrid. Lieferant bestaetigt die Erfuellung mit der Abrechnung | § 43 Abs. 1 bis 5 GModG, § 96 Abs. 4 und 5 |
| Bestehende Gas- und Oelheizungen | Keine Bio-Quote, solange die Anlage nicht ersetzt wird | § 43 Abs. 1 ("neu eingebaut") |
| Ersatz nach irreparablem Ausfall im Jahr 2028 | Bio-Pflicht beginnt erst zwoelf Monate nach dem Einbau | § 43 Abs. 7 |
| Vermietete Wohnungen mit neuer Gas-/Oelheizung nach § 43 | Vermieter und Mieter tragen je zur Haelfte: Gas-Netzentgelte und CO2-Kosten ab 01.01.2028, Kosten des Bio-Anteils ab 01.01.2029 (bis 30 % des Brennstoffs). Haertefallregel in § 5d | §§ 5a, 5b, 5d CO2KostAufG (Art. 5 BGBl. 2026 I Nr. 226) |
| Brennstoffmarkt | Eine Gruengas-/Gruenheizoelquote fuer die Lieferanten soll per eigenem Gesetz kommen (Vorlage bis 01.12.2026, klimaneutrale Brennstoffe ab 2045). Keine Eigentuemerpflicht, aber Preisrisiko fuer fossile Heizungen | § 42a GModG |
| Einbau einer Stromdirektheizung im Bestand | Nur wenn der Waermeschutz die Anforderungen der §§ 16, 19 um mind. 30 % unterschreitet (Ausnahmen: selbstgenutztes Haus mit max. zwei Wohnungen, Tausch einer Einzelraum-Stromdirektheizung) | § 46 GModG |

#### 3b: Nachruestpflichten, die fortbestehen

| Pflicht | Inhalt | Quelle |
|---------|--------|--------|
| Oberste Geschossdecke | Geschossdecken ueber beheizten Raeumen, die den Mindestwaermeschutz nach DIN 4108-2 nicht erfuellen, auf U <= 0,24 W/(qm*K) daemmen; alternativ das Dach darueber | § 35 Abs. 1 GModG (vormals § 47 GEG) |
| Rohrleitungen und Armaturen | Bisher ungedaemmte, zugaengliche Waermeverteilungs- und Warmwasserleitungen ausserhalb beheizter Raeume nach Anlage 8 daemmen | § 69 Abs. 2 GModG |
| Bussgeld fuer beides | Bis 50.000 EUR | § 108 Abs. 2 Nr. 1 GModG |
| Heizungspruefung (ab 6 Wohnungen) | Heizung mit Wasser als Waermetraeger, keine Waermepumpe: eingebaut vor 01.10.2009 -> Pruefung und Optimierung bis 30.09.2027; spaeter eingebaut -> innerhalb eines Jahres nach 15 Betriebsjahren | § 60b GModG |
| Hydraulischer Abgleich (ab 6 Wohnungen) | Nach Einbau einer neuen Heizungsanlage mit Wasser als Waermetraeger | § 60c GModG |
| Betriebspruefung Waermepumpe (ab 6 Wohnungen) | Waermepumpe in Betrieb seit 01.01.2024: nach einer Heizperiode, spaetestens nach zwei Jahren | § 60a GModG |

#### 3c: Pflichten beim Eigentuemerwechsel

| Fall | Inhalt | Quelle |
|------|--------|--------|
| Haus mit max. zwei Wohnungen, Verkaeufer wohnt dort seit vor dem 01.02.2002 | Der Altbesitzer war von den Nachruestpflichten fuer Geschossdecke und Leitungen befreit. Der Kaeufer muss sie innerhalb von zwei Jahren nach dem Eigentumsuebergang erfuellen | § 35 Abs. 3, § 69 Abs. 3 und 4 GModG |
| Wirtschaftlichkeitsausnahme | Bewohnt der Eigentuemer ein Haus mit max. zwei Wohnungen selbst, entfaellt die Geschossdecken-Pflicht, wenn sich die Kosten nicht in angemessener Frist durch Einsparung erwirtschaften | § 35 Abs. 4 GModG |
| Mehrfamilienhaus | Keine Sonderfrist. Die Pflichten aus 3b treffen den jeweiligen Eigentuemer, nach dem Uebergang also den Kaeufer. Offene Pflichten vor dem Kauf klaeren und einpreisen | § 35, § 69 GModG |
| Energieausweis | Verkaeufer oder Makler legen ihn spaetestens bei der Besichtigung vor und uebergeben ihn nach dem Kaufvertrag. Kaeufer eines Hauses mit max. zwei Wohnungen fuehrt ein Beratungsgespraech, wenn es unentgeltlich angeboten wird | § 80 Abs. 4 GModG |

#### 3d: EU-Gebaeuderichtlinie (EPBD) -- Ausblick

- **Wohngebaeude:** Weder die Richtlinie (EU) 2024/1275 noch das GModG schreiben eine Sanierungspflicht fuer das einzelne Wohngebaeude vor. Die Richtlinie verlangt einen nationalen Absenkpfad fuer den Durchschnitt des Bestands. Eine schlechte Effizienzklasse ist deshalb ein Markt-, Betriebskosten- und Finanzierungsrisiko, keine Rechtspflicht.
- **Nichtwohngebaeude:** Mindeststandards nach § 40 GModG (gilt ab 01.01.2027, Anforderungen ab 01.01.2030 und 01.01.2033; Art. 2 und Art. 9 Abs. 2 BGBl. 2026 I Nr. 226).
- Stand der Analyse vermerken; weitere Umsetzungsschritte sind moeglich.

### Schritt 4: Heizungsanalyse und Ersatz-Timeline (Renovierungsposition)

Der Ersatzzeitpunkt folgt aus Restlebensdauer, Zustand und Betriebskosten, nicht aus einer Rechtspflicht (Schritt 3a).

**Restlebensdauer = typische Lebensdauer - Alter.** Belege fuer den Zustand: Typenschild (Baujahr), Schornsteinfeger-Messprotokoll, Wartungsnachweise, Reparaturhistorie. Laeuft eine Anlage ueber ihre typische Lebensdauer hinaus, setze den Ersatz als Instandhaltung in den ersten ein bis drei Jahren an und rechne Ausfallrisiko im Winter (Notbetrieb, Mietminderung) mit. In der Verhandlung ist das ein Renovierungsargument mit Kosten und Zeitpunkt, kein Bussgeld- oder Pflichtargument.

| Heizungstyp | Typische Lebensdauer | Handlungsbedarf | Geschaetzte Ersatzkosten |
|-------------|---------------------|-----------------|----------------------------|
| Oel-Heizung (Konstanttemperatur) | 20-25 Jahre | HOCH, wenn die Lebensdauer erreicht ist (Ausfallrisiko, schlechter Wirkungsgrad) | 15.000-30.000 EUR (Waermepumpe) + Demontage Oeltank 2.000-5.000 EUR |
| Oel-Brennwert | 20-25 Jahre | Mittelfristig. Ersatz durch neue Oelheizung loest die Bio-Treppe aus (§ 43 GModG) | 15.000-30.000 EUR |
| Gas-Niedertemperatur | 20-25 Jahre | HOCH (wenn > 25 Jahre) | 12.000-25.000 EUR |
| Gas-Brennwert | 20-30 Jahre | Mittelfristig. Ersatz durch neue Gasheizung loest die Bio-Treppe aus (§ 43 GModG) | 12.000-25.000 EUR |
| Nachtspeicherheizung | 25-30 Jahre | HOCH (hohe Betriebskosten, ineffizient) | 20.000-40.000 EUR (Zentralheizung nachrüsten) |
| Fernwaerme | Uebergabestation 20-30 Jahre | NIEDRIG | 5.000-15.000 EUR (Uebergabestation) |
| Waermepumpe | 15-25 Jahre | NIEDRIG | 15.000-30.000 EUR |
| Pellet-Heizung | 15-20 Jahre | NIEDRIG | 20.000-35.000 EUR |

**Vergleich der Ersatzoptionen ueber 15-20 Jahre Betrieb, nicht nur Anschaffung:** Eine neue Gas- oder Oelheizung ist guenstig im Einbau, traegt aber ab 2029 den steigenden Bio-Anteil (10 % bis 60 %), den CO2-Preis, eine kuenftige Gruengasquote der Lieferanten und bei Vermietung ab 2028 die haelftige Kostenteilung nach § 5a CO2KostAufG.

**Bei MFH zusaetzlich beachten:**
- Kosten skalieren nicht linear -- groessere Anlagen sind pro qm guenstiger
- Foerderung pruefen (BEG/KfW: bis zu 70% Foerderung moeglich)
- Platz fuer Waermepumpe (Aussengeraet) vorhanden?
- Bei WEG: Beschluss der Eigentuememergemeinschaft erforderlich

**Systemregel: Heizung nie isoliert bewerten.**
Heizungstausch ist eine Systementscheidung aus Gebaeudehuelle, Heizlast, Leitungsnetz, Regulatorik und Wirtschaftlichkeit -- kein Produktkauf:
- Kein Heizungstausch ohne Huelle-, Heizlast- und GModG-Pruefung (Energieberater)
- Waermepumpe braucht Systemfit: Falsch dimensioniert oder im ungedaemmten Gebaeude kann sie wirtschaftlich scheitern. Fuer die volle Modernisierungsumlage braucht sie eine Jahresarbeitszahl von mind. 2,5 (§ 559f BGB, Schritt 6)
- Schornsteinfeger und Heizungsbauer frueh einbinden: Bestand, Pflichten und Optionen klaeren
- Neue fossile Anlagen sind erlaubt, werden aber mit Bio-Treppe, CO2-Preis und Gruengasquote teurer im Betrieb -- das ist ein Kostenrisiko, keine Rechtspflicht zum Wechsel

**Optimierung vor Austausch pruefen (guenstige Sofort-Hebel):**
- Daemmung der Heizungs- und Warmwasserleitungen in unbeheizten Raeumen
- Hydraulischer Abgleich
- Heizzeiten und Vorlauftemperaturen optimieren

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

**Foerdermoeglichkeiten (Heizung: KfW 458, Stand seit 21.07.2026; uebrige: Stand 2025):**
- BEG Einzelmassnahmen: 15-20% Zuschuss
- Heizungstausch (KfW 458, Privatpersonen und WEG; GbR und Gesellschaften: KfW 459): Grundfoerderung 30%. Klimageschwindigkeitsbonus (16% bis 31.01.2027, danach halbjaehrlich 4 Punkte weniger, ab 01.08.2028 entfallen) und Einkommensbonus (10-40%) nur fuer selbstgenutzte Wohneinheiten. Max. 70% (80% bei niedrigem Einkommen). Foerderfaehige Kosten: 28.000 EUR fuer die erste Wohneinheit, je 15.000 EUR fuer die 2. bis 6., je 8.000 EUR ab der 7.
- **Vermietete Wohnungen bekommen beim Heizungstausch nur die Grundfoerderung von 30%.** Nie mit 50% oder mehr rechnen, wenn der Kaeufer nicht selbst einzieht.
- KfW-Kredit: Bis zu 150.000 EUR je Wohneinheit
- Steuerliche Foerderung: 20% ueber 3 Jahre (Alternative zu Zuschuss)
- *Pruefbedarf: Foerderbedingungen sind zeit- und programmabhaengig -- vor Beauftragung mit DENA-gelistetem Energieeffizienz-Experten validieren (oft Foerdervoraussetzung)*

**Entscheidungsregel Variantenvergleich:**
Keine energetische Massnahme ohne Variantenvergleich und Expertenpruefung. Mindestens drei Varianten rechnen:
1. **Mindeststandard/Pflicht:** Nur was GModG und Regulatorik erzwingen (Schritt 3b und 3c)
2. **Wirtschaftliches Optimum:** Massnahmen mit bestem Verhaeltnis aus Kosten, Foerderung, Mietumlage und Wertsteigerung
3. **KfW-/Foerderstandard:** Hoeherer Aufwand, aber maximale Foerderung und Zukunftssicherheit

Die richtige Frage ist nicht "Sanieren oder nicht?", sondern: Welche Massnahme in welcher Reihenfolge fuer welches Ziel? Energetische Sanierung ist ein Business Case aus Aufwand, Foerderung, Mietumlage, Wertsteigerung, Finanzierung und Betriebskosten -- keine Ideologiefrage. Mieterkommunikation und Nachfinanzierung sind dabei genauso kritisch wie die Technik.

### Schritt 6: Auswirkung auf Mieterhoehung (energetische Modernisierungsumlage)

Berechne das Mieterhoehungspotenzial nach BGB § 559:

**Formel:**
```
Umlegbare Kosten              = Modernisierungskosten - Instandhaltungsanteil - Foerderung
Jaehrliche Mieterhoehung      = Umlegbare Kosten * 8%
Monatliche Erhoehung je qm    = Jaehrliche Mieterhoehung / 12 / Wohnflaeche
Kappungsgrenze (§ 559 Abs. 3a): Max. 3 EUR/qm innerhalb von 6 Jahren,
                                max. 2 EUR/qm bei Ausgangsmiete unter 7 EUR/qm
```

**Sonderregeln Heizung:**
```
Heizungstausch mit Foerderung (§ 559e BGB):
  Jaehrliche Mieterhoehung = (Kosten - 15% Erhaltungspauschale - Foerderung) * 10%
  Die 15%-Pauschale gilt nicht fuer den Einbau einer Gas-/Oelheizung nach § 43 GModG
  Kappung: max. 0,50 EUR/qm/Monat innerhalb von 6 Jahren, angerechnet auf die Grenzen oben
Waermepumpe (§ 559f BGB, seit 29.07.2026):
  Volle Umlage nur mit Nachweis Jahresarbeitszahl >= 2,5 durch Fachunternehmer
  (entbehrlich bei Baujahr nach 1996, WSchV-1995-Niveau, Sanierung nach § 38 GModG
  oder Vorlauf <= 55 Grad C), sonst nur 50% der Kosten umlegbar
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
| Typische Lebensdauer | 20-25 Jahre (ueberschritten) |
| Erwartete Restlebensdauer | 0 Jahre -- Ersatz in 1-3 Jahren als Instandhaltung einplanen |
| Rechtslage | Weiterbetrieb erlaubt, kein Austauschzwang (GModG, Stand 12.11.2026) |
| Zustandsbelege | Schornsteinfeger-Messprotokoll und Wartungsnachweise anfordern |
| Empfohlener Ersatz | Luft-Wasser-Waermepumpe nach Heizlastberechnung; Gas-Brennwert mit Bio-Treppe als Vergleichsvariante rechnen |
| Geschaetzte Ersatzkosten | 85.000 EUR |
| Verfuegbare Foerderung | 25.500 EUR (KfW 458, 30% Grundfoerderung; Boni nur bei Selbstnutzung) |
| Netto-Kosten nach Foerderung | 59.500 EUR |

## Pflichten nach GModG (Stand 12.11.2026)

**Gesamtstatus: 🟡 Zwei Pflichten offen, eine bei Besichtigung pruefen**

| Anforderung | Rechtsgrundlage | Status | Frist | Geschaetzte Kosten |
|-------------|-----------------|--------|-------|--------------------|
| Heizungspruefung und -optimierung (12 WE, Anlage vor 01.10.2009) | § 60b GModG | 🟡 Nachweis fehlt | 30.09.2027 | 300-800 EUR |
| Daemmung oberste Geschossdecke oder Dach | § 35 GModG | 🟡 Dach teilgedaemmt (U ca. 0,8) -- Mindestwaermeschutz vermutlich nicht erfuellt, Pflicht besteht bereits | Sofort faellig | In Dachdaemmung enthalten |
| Daemmung ungedaemmter Leitungen im Keller | § 69 Abs. 2 GModG | ⚪ Bei Besichtigung pruefen | Sofort faellig, falls ungedaemmt | 2-5 EUR/qm WF |
| Hydraulischer Abgleich | § 60c GModG | -- | Beim Einbau der neuen Heizung | In Heizungskosten enthalten |

**Kommende Anforderungen:**

| Anforderung | Ab | Auswirkung |
|-------------|----|------------|
| Bio-Treppe, falls Ersatz durch neue Gasheizung | 01.01.2029 | 10% Bio-Anteil, steigend bis 60% ab 2040 (§ 43 GModG); Vermieter traegt haelftig Netzentgelte und CO2-Kosten ab 2028 und Bio-Mehrkosten ab 2029 (§ 5a CO2KostAufG) |
| Gruengasquote der Gaslieferanten | Gesetz bis 01.12.2026 angekuendigt | Preisrisiko fuer Gas auch bei der bestehenden Anlage (§ 42a GModG) |

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
| Heizungstausch Gas -> Waermepumpe | In 1-3 Jahren (Lebensdauer erreicht) | 85.000 EUR | 25.500 EUR | 59.500 EUR | 30% (47.000 kWh/a, 5.600 EUR/a) | 10,6 Jahre | +0,46 EUR/qm/Monat (§ 559e BGB: (85.000 - 12.750 - 25.500) * 10%; nur mit JAZ-Nachweis >= 2,5) | D |

## Wirtschaftliche Gesamtbetrachtung

| Kennzahl | Wert |
|----------|------|
| Gesamtkosten Sanierung | 285.000 EUR |
| Foerderungen gesamt | 78.000 EUR |
| Netto-Kosten | 207.000 EUR |
| Jaehrliche Energiekosteneinsparung | 12.500 EUR |
| Jaehrliches Mieterhoehungspotenzial | 10.875 EUR |
| Jaehrlicher Gesamtnutzen | 23.375 EUR |
| Einfache Amortisation | 8,9 Jahre |
| Ziel-Energieklasse | C |
| Geschaetzte Wertsteigerung | ca. 8% |

## Risiken und Chancen

**Risiken:**
- Heizung am Ende der Lebensdauer: Ausfall im Winter moeglich. Ersatz als Instandhaltung in 1-3 Jahren einpreisen (59.500 EUR netto) -- ein Renovierungsargument, kein Pflicht- oder Bussgeldargument
- Heizungspruefung nach § 60b GModG bis 30.09.2027 offen (Bussgeld bis 5.000 EUR)
- Effizienzklasse F: Markt-, Betriebskosten- und Finanzierungsrisiko; fuer das einzelne Wohngebaeude keine EU-Sanierungspflicht

**Chancen:**
- Durch Sanierung von F auf C: Wertsteigerung ca. 8%
- Modernisierungsumlage: +1,07 EUR/qm/Monat moeglich (unter der Kappung von 3 EUR/qm bzw. 2 EUR/qm bei Ausgangsmiete unter 7 EUR/qm)

## Einschraenkungen der Analyse

Konfidenz: 75%. Begrenzende Faktoren:
- Verbrauchsausweis weniger aussagekraeftig als Bedarfsausweis
- Daemmzustand nur geschaetzt (keine Vor-Ort-Pruefung)
```

---

## Qualitaetspruefung

Vor Ausgabe des Ergebnisses pruefe:

- [ ] Energieausweis-Typ korrekt identifiziert und Einschraenkungen benannt
- [ ] Gueltigkeit geprueft (10 Jahre ab Ausstellung)
- [ ] Kennwert gegen Baujahr, Daemmzustand und Heizung plausibilisiert (hohe Fehlerquote bei Ausweisen)
- [ ] Energieeffizienzklasse korrekt zugeordnet
- [ ] Rechtsstand GModG mit Datum genannt; keine Pflicht zum Austausch und keine 65-Prozent-Vorgabe aus Unterlagen vor dem 29.07.2026 uebernommen
- [ ] Heizungsalter korrekt berechnet, Restlebensdauer als Renovierungsposition bewertet (kein Rechtsabzug)
- [ ] Fortbestehende Pflichten geprueft: oberste Geschossdecke (§ 35), Leitungen (§ 69), ab 6 WE Heizungspruefung (§ 60b), Fristen beim Eigentuemerwechsel
- [ ] Kostenschaetzungen in realistischen Bandbreiten (nicht zu optimistisch)
- [ ] Foerderungen mit aktuellem Stand angegeben (BEG/KfW); bei Vermietung nur Grundfoerderung
- [ ] Modernisierungsumlage korrekt berechnet (8% p.a. bzw. 10% nach § 559e, Monatswert = Jahresbetrag / 12 / qm, Instandhaltungsanteil abgezogen, Kappungsgrenzen geprueft, Waermepumpe: JAZ-Nachweis § 559f)
- [ ] Keine Verwechslung zwischen Endenergie und Primaerenergie
- [ ] Amortisationsrechnung nachvollziehbar

---

## Warnsignale & Dealbreaker

| Signal | Risikostufe | Auswirkung |
|--------|-------------|------------|
| Energieklasse G oder H | HOCH | Hohe Betriebskosten, Abschlag am Markt, schlechtere Finanzierung; Sanierungspflicht nur bei Nichtwohngebaeuden (§ 40 GModG) |
| Oelheizung > 25 Jahre | HOCH | Lebensdauer erreicht: Ersatz in 1-3 Jahren einpreisen, Oeltank-Entsorgung. Keine Rechtspflicht zum Austausch (GModG) |
| Nachtspeicherheizung | HOCH | Ineffizient, hohe Betriebskosten, Asbestrisiko |
| Kein Energieausweis vorhanden | MITTEL | Bussgeld bis 10.000 EUR moeglich (§ 108 Abs. 2 Nr. 2 GModG), Pflichtversaeumnis |
| Energieausweis abgelaufen | MITTEL | Neuerstellung erforderlich (Verkaeufer-Pflicht) |
| Modernisierungsempfehlungen im Ausweis von vor dem 29.07.2026 | NIEDRIG | Koennen auf der gestrichenen 65-Prozent-Vorgabe beruhen -- nur als Hinweis lesen, nicht als Pflicht |
| Fernwaerme nicht verfuegbar + Waermepumpe nicht moeglich | MITTEL | Ersatz nur durch Gas/Oel mit Bio-Treppe (§ 43 GModG) oder Biomasse -- steigende Betriebskosten einrechnen |
| Denkmalschutz + schlechte Energieklasse | HOCH | Fassadendaemmung moeglicherweise nicht genehmigungsfaehig |
| Einrohrheizung | MITTEL | Hydraulischer Abgleich schwierig, Austausch teuer |
| Kennwert unplausibel zu Baujahr/Zustand (z.B. Klasse B bei unsaniertem Altbau) | MITTEL | Ausweis moeglicherweise fehlerhaft -- Bedarfsausweis oder Energieberater-Pruefung anfordern |
| Verbrauchsausweis bei hohem Leerstand | MITTEL | Realer Bedarf hoeher als ausgewiesen -- Kalkulation nach oben korrigieren |

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

- `knowledge/rechtsgrundlagen.md` -- GModG-Anforderungen (Abschnitt 6), Modernisierungsumlage (§ 559 BGB)
- `knowledge/kalkulationsformeln.md` -- Renditeberechnung inkl. Sanierungskosten
- `knowledge/marktbenchmarks.md` -- Sanierungskosten-Benchmarks nach Baujahr
- `skills/unterlagen-analyst/SKILL.md` -- Gesamtanalyse der Objektunterlagen
- `skills/risiko-scanner/SKILL.md` -- Kategorie 4: Energetische Risiken (Zusammenspiel)
- `skills/besichtigung-prep/SKILL.md` -- Heizungs- und Daemmungs-Check bei Besichtigung
- `skills/mieterhoehung/SKILL.md` -- Modernisierungsumlage in Mieterhoehungsstrategie integrieren
