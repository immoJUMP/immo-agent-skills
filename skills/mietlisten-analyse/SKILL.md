---
name: mietlisten-analyse
description: "Analysiert Mietlisten: Ist-Mieten gegen Mietspiegel, Erhoehungspotenzial unter Beruecksichtigung von Kappungsgrenze und Mietpreisbremse, Leerstandsanalyse und Anomalie-Erkennung. Nutze diesen Skill wenn du eine Mietaufstellung eines MFH erhalten hast und das Potenzial quantifizieren willst."
---

# Mietlisten-Analyse

> Validiert Mietlisten deutscher Wohnimmobilien, identifiziert Mieterhoehungspotenzial, prueft Mietpreisbremse und Kappungsgrenze, erkennt Anomalien und berechnet den realistischen Ertragswert. Adaptiert fuer den deutschen Markt mit BGB-Mietrecht, Mietspiegel und Kappungsgrenzen.

---

## Wann diesen Skill nutzen

- Du hast eine Mietliste (Mietaufstellung) eines Mehrfamilienhauses oder ETW-Pakets erhalten
- Du willst die Ist-Mieten gegen den Mietspiegel pruefen und Steigerungspotenzial quantifizieren
- Du brauchst eine Leerstandsanalyse und Mietausfallbewertung
- Du willst Anomalien erkennen (gleiche Einzugsdaten, verwandte Parteien, unerklaerlich niedrige Mieten)
- Du willst die Mietliste fuer deine Cashflow-Kalkulation validieren

---

## Was du bereitstellen musst

### Pflicht-Eingaben
- **Mietliste** (CSV, Excel, PDF oder manuell) mit moeglichst folgenden Spalten:
  - Wohnungsnummer / Lage im Haus (z.B. 1. OG links)
  - Wohnflaeche in qm
  - Anzahl Zimmer
  - Kaltmiete (Nettokaltmiete) in EUR
  - Nebenkosten-Vorauszahlung in EUR
  - Mietbeginn (Datum)
  - Name des Mieters (oder anonymisiert)
  - Befristet ja/nein, ggf. Befristungsende

### Optionale Eingaben (erhoehen Analysequalitaet deutlich)
- **Mietspiegel** der Kommune (qualifizierter Mietspiegel falls vorhanden)
- **Standort/Adresse** (fuer Mietspiegel-Zuordnung und Mietpreisbremse-Check)
- Angaben zur Ausstattung pro Einheit (Bad, Balkon, Aufzug, Bodenbelag)
- Wohnflaechenberechnung nach WoFlV
- Staffelmiet- oder Indexmiet-Vereinbarungen
- Letzte Mieterhoehungen pro Einheit
- Mietrueckstaende / Zahlungshistorie
- Wirtschaftsplan / Hausgeldabrechnung (fuer nicht-umlagefaehige Kosten)

### Kontext
- Kaufpreis (fuer Renditberechnung)
- Investmentstrategie (Buy & Hold, Value-Add, Aufteilung)
- Eigene Zielmiete oder Mindestrendite

---

## Auftrag

Du bist ein spezialisierter Mietrechtsexperte und Analyst fuer deutsche Wohnimmobilien. Analysiere die Mietliste systematisch, vergleiche Ist-Mieten mit der ortsueblichen Vergleichsmiete, berechne das Mieterhoehungspotenzial unter Beruecksichtigung aller rechtlichen Grenzen (Kappungsgrenze, Mietpreisbremse) und identifiziere Anomalien und Risiken.

---

## Strategie

### Schritt 1: Mietliste normalisieren und validieren
- Konvertiere alle Daten in ein einheitliches Format
- Berechne fehlende Werte: Miete pro qm, Mietdauer in Monaten/Jahren
- Pruefe auf Vollstaendigkeit: Fehlen Einheiten? Luecken in der Nummerierung?
- Validiere Plausibilitaet: Wohnflaechen realistisch? Mieten im erwartbaren Bereich?

**Plausibilitaetspruefung Wohnflaeche:**
| Zimmer | Plausible Wohnflaeche | Auffaellig wenn |
|--------|----------------------|-----------------|
| 1 Zimmer | 25-45 qm | < 20 qm oder > 55 qm |
| 2 Zimmer | 40-70 qm | < 35 qm oder > 80 qm |
| 3 Zimmer | 60-95 qm | < 50 qm oder > 110 qm |
| 4 Zimmer | 80-130 qm | < 65 qm oder > 150 qm |
| 5+ Zimmer | 100-180 qm | < 80 qm oder > 200 qm |

### Schritt 2: Ist-Miete vs. Mietspiegel vergleichen

Fuer jede Einheit berechne:
```
Abweichung = (Ist-Miete_EUR_qm / Mietspiegel_EUR_qm - 1) * 100
```

**Kategorisierung:**
| Abweichung vom Mietspiegel | Bewertung | Bedeutung |
|---------------------------|-----------|-----------|
| > +20% | UEBER MARKT | Rueckfallrisiko bei Mieterwechsel, Mietpreisbremse pruefen |
| +5% bis +20% | MARKTKONFORM OBERER BEREICH | Geringes Steigerungspotenzial |
| -5% bis +5% | MARKTKONFORM | Moderates Steigerungspotenzial |
| -20% bis -5% | UNTER MARKT | Gutes Steigerungspotenzial |
| < -20% | DEUTLICH UNTER MARKT | Hohes Steigerungspotenzial, aber Kappungsgrenze beachten |

**Wichtig bei der Mietspiegel-Zuordnung:**
- Qualifizierter Mietspiegel nach §558d BGB ist rechtsverbindlich
- Einfacher Mietspiegel ist Orientierung, aber nicht bindend
- Ohne Mietspiegel: Vergleichsmieten ueber Datenbanken oder 3 Vergleichswohnungen
- Mietspiegel-Zuordnung beruecksichtigen: Baujahr, Lage, Ausstattung, Wohnungsgroesse

### Schritt 3: Mieterhoehungspotenzial berechnen

#### 3a: Mieterhoehung bis zur ortsueblichen Vergleichsmiete (§ 558 BGB)

**Voraussetzungen:**
- Miete seit mindestens 15 Monaten unveraendert
- Mieterhoehung darf fruehestens 12 Monate nach letzter Erhoehung verlangt werden
- Begruendung: Mietspiegel, Gutachten oder 3 Vergleichswohnungen

**Kappungsgrenze (§ 558 Abs. 3 BGB):**
```
Maximale Erhoehung = Miete_vor_3_Jahren * Kappungsgrenze_Prozent

Standard: 20% in 3 Jahren
Verschaerft (in vielen Grossstaedten): 15% in 3 Jahren
```

**Staedte mit abgesenkter Kappungsgrenze (15%) -- Auswahl:**
Berlin, Hamburg, Muenchen, Koeln, Frankfurt, Stuttgart, Duesseldorf, Freiburg, Heidelberg, Muenster, Regensburg, Tuebingen, Potsdam, Darmstadt und weitere (Landesverordnungen pruefen)

**Berechnung pro Einheit:**
```
Ist-Miete: 4.50 EUR/qm
Mietspiegel: 7.20 EUR/qm
Differenz: 2.70 EUR/qm (60% unter Markt)

Kappungsgrenze 20%:
  Maximale Erhoehung sofort: 4.50 * 20% = 0.90 EUR/qm
  Neue Miete nach Erhoehung: 5.40 EUR/qm
  
  Nach weiteren 3 Jahren:
  Maximale Erhoehung: 5.40 * 20% = 1.08 EUR/qm
  Neue Miete: 6.48 EUR/qm
  
  Noch 3 Jahre:
  Maximale Erhoehung: 6.48 * 20% = 1.30 EUR/qm
  Neue Miete: 7.20 EUR/qm (= Mietspiegel, begrenzt)
  
Zeitraum bis Mietspiegel erreicht: ca. 6-9 Jahre
```

#### 3b: Mietpreisbremse pruefen (§ 556d BGB)

**Wann greift die Mietpreisbremse?**
- In Gebieten mit angespanntem Wohnungsmarkt (Landesverordnung)
- Bei Neuvermietung: Miete maximal 10% ueber ortsueblicher Vergleichsmiete
- NICHT bei: Neubau (Erstbezug nach 01.10.2014), umfassende Modernisierung, Vormiete war bereits hoeher

**Ausnahmen von der Mietpreisbremse:**
1. Neubau (Erstbezug ab 01.10.2014)
2. Umfassend modernisiert (ca. 1/3 des Neubauaufwands)
3. Vormiete lag bereits ueber der Grenze (Bestandsschutz)
4. Moebilierte Vermietung (umstritten, Einzelfallpruefung)

**Berechnung bei Neuvermietung:**
```
Mietspiegel: 7.20 EUR/qm
Maximalmiete bei Neuvermietung: 7.20 * 1.10 = 7.92 EUR/qm
```

#### 3c: Staffelmiete / Indexmiete identifizieren

| Mietart | Merkmale | Potenzial | Risiko |
|---------|----------|-----------|--------|
| Staffelmiete (§ 557a BGB) | Fest vereinbarte Erhoehungen zu festen Zeitpunkten | Planbar, keine Zustimmung noetig | Keine zusaetzliche Erhoehung moeglich, Mietpreisbremse gilt |
| Indexmiete (§ 557b BGB) | Miete gekoppelt an Verbraucherpreisindex | Inflationsschutz | Keine Mietspiegel-Erhoehung moeglich, nur bei Index-Aenderung |
| Freie Miete | Keine automatische Anpassung | Mietspiegel-Erhoehung moeglich | Kappungsgrenze, Zustimmung erforderlich |

### Schritt 4: Leerstandsanalyse

Unterscheide:

**Physischer Leerstand:**
```
Leerstandsquote_physisch = Leere_Einheiten / Gesamte_Einheiten * 100
```

**Wirtschaftlicher Leerstand:**
```
Leerstandsquote_wirtschaftlich = Mietausfall_EUR / Soll-Miete_EUR * 100
```

*Wirtschaftlicher Leerstand ist hoeher als physischer, wenn teure Einheiten leerstehen.*

**Bewertung:**
| Leerstand | Bewertung | Typische Ursache |
|-----------|-----------|------------------|
| 0% | Sehr gut, aber: Ist die Miete zu niedrig? | -- |
| 1-3% | Normal (Fluktuationsreserve) | Mieterwechsel |
| 3-5% | Leicht erhoerht | Renovierungsstau, Marktlage |
| 5-10% | Erhoerht | Standort, Zustand, Miete zu hoch |
| > 10% | Kritisch | Strukturelles Problem |

**Fuer jede leerstehende Einheit dokumentiere:**
- Seit wann leer?
- Grund (Sanierung, kein Mieter gefunden, Strategie-Leerstand?)
- Vermietbarer Zustand?
- Geschaetzte Miete bei Vermietung

### Schritt 5: Anomalien-Erkennung

Suche systematisch nach folgenden Auffaelligkeiten:

| Anomalie | Was pruefen | Warnsignal |
|----------|-------------|------------|
| Gleiche Einzugsdaten | Mehrere Mieter am selben Tag eingezogen | Scheinmieter, Verkaeufer-nahe Personen |
| Verwandte Parteien | Gleiche Nachnamen, gleiche Adressen | Gefaelligkeitsmieten, nicht marktgerecht |
| Unerklaerlich niedrige Mieten | Einzelne Einheiten weit unter Markt ohne erkennbaren Grund | Sondervereinbarungen, Gegenleistungen |
| Unerklaerlich hohe Mieten | Einzelne Einheiten weit ueber Markt | Aufgeblaehte Mietliste vor Verkauf |
| Sehr kurze Mietdauer | Viele Mieter < 12 Monate | Hohe Fluktuation, Problem-Objekt |
| Sehr lange Mietdauer + niedrige Miete | Mieter > 15 Jahre, nie Erhoehung | Starker Kuendigungsschutz, schwer zu steigern |
| Befristete Mietvertraege | Mehrere befristete Vertraege | Pruefung ob Befristungsgrund wirksam |
| Clustered lease expirations | Mehrere Vertraege enden gleichzeitig | Leerstandsrisiko |
| Gewerbliche Zwischenmiete | Firma als Mieter, Weitervermietung | Regulatorische Risiken, Kuendigung anders |
| Wohnflaechen-Unstimmigkeiten | Grosse Abweichungen zur TE | Miete ggf. zu hoch/niedrig berechnet, Minderungsanspruch |

### Schritt 6: Wohnflaechenberechnung verifizieren

**Relevanz:** Weicht die tatsaechliche Wohnflaeche um mehr als 10% von der im Mietvertrag vereinbarten ab, hat der Mieter Minderungsansprueche (BGH-Rechtsprechung).

**Pruefraster:**
| Flaechentyp | Anrechnung nach WoFlV |
|------------|----------------------|
| Raeume > 2m Hoehe | 100% |
| Raeume 1-2m Hoehe (Dachschraege) | 50% |
| Raeume < 1m Hoehe | 0% |
| Balkone, Loggien, Terrassen | 25% (bis zu 50% bei guter Qualitaet) |
| Wintergarten beheizt | 100% |
| Wintergarten unbeheizt | 50% |
| Kellerraeume | 0% (nicht Wohnflaeche) |
| Waschkueche, Trockenraum | 0% |

**Risiko-Check:**
- Vergleiche Wohnflaeche aus Mietliste mit Teilungserklaerung
- Vergleiche mit Grundrissen (falls vorhanden)
- Bei Abweichung > 5%: Nachberechnung empfehlen
- Bei Abweichung > 10%: Mieter hat Minderungsanspruch -- Mieteinnahme-Risiko

### Schritt 7: Ertragswert und Rendite berechnen

```
Ist-Miete Kalt (jaehrlich):           X EUR
+ Mieterhoehungspotenzial Jahr 1-3:   Y EUR
= Prognostizierte Miete nach 3 Jahren: Z EUR

Leerstandsrisiko (2-5% der Soll-Miete): -A EUR
Mietausfallrisiko (1-2%):               -B EUR

= Bereinigte Jahresnettomiete:          W EUR

Bruttomietrendite Ist:   Ist-Miete / Kaufpreis * 100
Bruttomietrendite Soll:  Soll-Miete (nach Erhoehung) / Kaufpreis * 100
Kaufpreisfaktor Ist:     Kaufpreis / Ist-Miete
Kaufpreisfaktor Soll:    Kaufpreis / Soll-Miete
```

---

## Ausgabeformat

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext.

Liefere die Ergebnisse in folgendem Format:

### Analysebericht

```markdown
# Mietlisten-Analyse: Strasse Hausnummer, PLZ Ort

**Analysedatum:** 15.04.2026 | **Gesamtrisiko: 🟡 MITTEL** | Konfidenz: 80%

## Objekt

| | |
|---|---|
| Adresse | Strasse Hausnummer, PLZ Ort |
| Einheiten gesamt | 12 WE, 0 GE |
| Wohnflaeche gesamt | 850,5 qm |
| Angebotspreis | 750.000 EUR |

## Mietlisten-Ueberblick

| Kennzahl | Wert |
|----------|------|
| Kaltmiete monatlich | 4.833 EUR |
| Kaltmiete jaehrlich | 58.000 EUR |
| Durchschnittsmiete | 5,68 EUR/qm |
| Median-Miete | 5,45 EUR/qm |
| Niedrigste / hoechste Miete | 3,20 / 8,10 EUR/qm (Spreizung 4,90 EUR) |
| Vermietete Einheiten | 11 |
| Leerstehende Einheiten | 1 |
| Physischer Leerstand | 8,3% |
| Wirtschaftlicher Leerstand | 9,1% |
| Durchschnittliche Mietdauer | 7,2 Jahre |
| Gewichtete Restmietdauer | 5,8 Jahre |

## Einheiten im Detail

| Einheit | Lage | Zimmer | qm | Kaltmiete | EUR/qm | NK | Warmmiete | Mietbeginn | Vertragstyp | Mietspiegel EUR/qm | Abweichung | Position |
|---------|------|--------|-----|-----------|--------|-----|-----------|------------|-------------|--------------------|-----------|----------|
| WE 01 | EG links | 3 | 72,5 | 435 EUR | 6,00 | 180 EUR | 615 EUR | 01.03.2018 (8,1 J., Mieter A) | unbefristet | 7,20 | -16,7% | 🟢 unter Markt |
| ... | | | | | | | | | | | | |

(Pro Einheit zusaetzlich angeben, falls vorhanden: Anomalien und Risiko-Flags.)

**Erhoehungspotenzial WE 01:** Zielmiete 7,20 EUR/qm, max. Erhoehung Jahr 1:
0,90 EUR/qm (Kappungsgrenze 20%), Marktmiete erreicht in 6 Jahren,
Mehreinnahmen 780 EUR/Jahr. Mietpreisbremse greift: max. Neuvermietungsmiete
7,92 EUR/qm.

## Mietspiegel-Vergleich

| Kennzahl | Wert |
|----------|------|
| Quelle | Qualifizierter Mietspiegel Stadt XY 2024 (Stand 01.01.2024) |
| Durchschnittliche Mietspiegel-Miete | 7,20 EUR/qm |
| Durchschnittliche Abweichung | -21,1% |
| Einheiten unter / auf / ueber Markt | 9 / 2 / 0 |
| Erhoehungspotenzial monatlich | 1.250 EUR |
| Erhoehungspotenzial jaehrlich | 15.000 EUR |
| Realistisch erreichbar Jahr 1 | 5.400 EUR |
| Realistisch erreichbar Jahr 3 | 11.200 EUR |
| Mietpreisbremse-Gebiet | Ja |
| Kappungsgrenze | 15% |

## Leerstandsanalyse

| Einheit | qm | Leer seit | Dauer | Grund | Marktmiete | Vermietbar | Sanierungskosten |
|---------|-----|-----------|-------|-------|------------|------------|-------------------|
| WE 07 | 55 | 01.09.2025 | 7 Monate | Sanierung | 7,50 EUR/qm (ca. 412 EUR/Monat) | Nein | ca. 15.000 EUR |

**Leerstandskosten jaehrlich:** 4.950 EUR | **Trend:** stabil

## Auffaelligkeiten

### 🔴 A001: Identische Mietbeginn-Daten (Schweregrad HOCH)

WE 03, WE 05 und WE 09 haben identisches Mietbeginn-Datum 01.01.2024.

Moegliche Erklaerungen:
- Verkaeufer hat kurz vor Verkauf Mietvertraege abgeschlossen
- Umstellung auf neue Vertragsform
- Scheinmieter

**Empfohlene Massnahme:** Mietvertraege einsehen, Bonitaet der Mieter pruefen,
Zahlungseingaenge der letzten 6 Monate anfordern.

## Wohnflaechen-Abgleich

| | |
|---|---|
| Flaeche laut Mietliste | 850,5 qm |
| Flaeche laut Teilungserklaerung | 823,0 qm |
| Abweichung | 3,3% |
| Einheiten mit Abweichung > 5% | WE 11, WE 12 |
| Einheiten mit Abweichung > 10% | keine |

**Bewertung: 🟡 MITTEL** -- Wohnflaechenberechnung nach WoFlV empfohlen.

## Mieterkonzentration

| | |
|---|---|
| Groesster Mieter | 14,2% der Gesamtmiete |
| Top-3-Mieter | 38,5% der Gesamtmiete |
| Konzentrationsrisiko | 🟢 NIEDRIG |
| Verdacht auf verbundene Personen | Nein |

## Vertragsauslauf-Clusterung

Keine Haeufung von Vertragsenden erkennbar — **Risiko: 🟢 NIEDRIG**.
(Falls Clusterung vorhanden: betroffene Zeitraeume und Einheiten auflisten.)

## Finanzielle Zusammenfassung

| Kennzahl | Wert |
|----------|------|
| Bruttomietrendite Ist | 7,73% |
| Bruttomietrendite nach Erhoehung | 8,93% |
| Kaufpreisfaktor Ist | 12,93 |
| Kaufpreisfaktor nach Erhoehung | 11,20 |
| Erhoehungspotenzial jaehrlich | 15.000 EUR |
| Realistisch in 3 Jahren | 11.200 EUR |
| Leerstandskosten jaehrlich | 4.950 EUR |
| Netto-Betriebsergebnis (NOI) | 48.000 EUR |
| Value-Add-Potenzial | 🟢 HOCH |

## Risiko-Zusammenfassung

**Gesamtrisiko: 🟡 MITTEL**

Zentrale Risiken:
- 3 Einheiten mit identischem Mietbeginn -- Scheinmieter pruefen
- WE 03: Mieter seit 26 Jahren, 3,20 EUR/qm -- Erhoehung nur ueber Kappungsgrenze

Chancen:
- 9 von 11 Einheiten unter Marktmiete -- Steigerungspotenzial 15.000 EUR/Jahr
- WE 07 nach Sanierung vermietbar fuer ca. 412 EUR/Monat

## Konfidenz

**Gesamt: 80%** | Datenqualitaet Mietliste: hoch | Mietspiegel-Genauigkeit:
qualifizierter Mietspiegel

Einschraenkende Faktoren:
- Keine Zahlungshistorie vorliegend
- Ausstattungsmerkmale fuer exakte Mietspiegel-Zuordnung fehlen
```

---

## Qualitaetspruefung

Vor Ausgabe des Ergebnisses pruefe:

- [ ] Alle Einheiten aus der Mietliste sind erfasst (Summe stimmt)
- [ ] Miete-pro-qm ist korrekt berechnet (Kaltmiete / Wohnflaeche)
- [ ] Mietspiegel-Vergleich nutzt korrekte Einordnung (Baujahr, Lage, Ausstattung, Groesse)
- [ ] Kappungsgrenze korrekt angewandt (20% oder 15% je nach Stadt)
- [ ] Mietpreisbremse nur in Gebieten mit Verordnung angewandt
- [ ] Leerstand korrekt als physisch UND wirtschaftlich berechnet
- [ ] Anomalien sind plausibel begruendet (nicht jede Auffaelligkeit ist ein Problem)
- [ ] Wohnflaechen-Abgleich mit Teilungserklaerung durchgefuehrt (falls vorhanden)
- [ ] Finanzielle Zusammenfassung ist konsistent mit Einzelwerten
- [ ] Keine Verwechslung Kaltmiete / Warmmiete

---

## Warnsignale & Dealbreaker

| Signal | Risikostufe | Auswirkung |
|--------|-------------|------------|
| Mehrere Mieten > 20% ueber Mietspiegel | HOCH | Rueckfallrisiko bei Mieterwechsel, Mietpreisbremse-Verstoss |
| Leerstand > 15% | HOCH | Strukturelles Vermietungsproblem |
| 3+ Einheiten mit identischem Mietbeginn (< 12 Monate) | HOCH | Scheinmieter-Verdacht, Mietliste moeglicherweise manipuliert |
| Groesster Mieter > 30% der Gesamtmiete | HOCH | Klumpenrisiko bei Auszug |
| Mietrueckstaende > 3 Monatsmieten | HOCH | Raeumungsverfahren, Mietausfall |
| Alle Mieten weit unter Markt + alte Mieter | MITTEL | Potenzial vorhanden aber nur langsam realisierbar |
| Wohnflaechen-Abweichung > 10% bei einzelnen Einheiten | MITTEL | Mietminderungsanspruch des Mieters |
| Viele befristete Mietvertraege ohne klaren Grund | MITTEL | Befristung moeglicherweise unwirksam |
| Indexmiete in Niedriginflationsphase | NIEDRIG | Miete steigt langsamer als bei freier Miete |

---

## Bei fehlenden Daten

1. **Ohne Mietspiegel:** Vergleichsmieten ueber Online-Portale schaetzen (ImmoScout24, Homeday, Wohnungsboerse). Confidence Score auf max. 0.60 setzen. Empfehlung: Qualifizierten Mietspiegel der Kommune anfordern.
2. **Ohne Mietbeginn-Daten:** Kappungsgrenze nicht berechenbar. Alle Mieten als "Erhoehungspotenzial unbestimmt" markieren.
3. **Ohne Wohnflaechenangaben:** Miete pro qm nicht berechenbar. Aus Grundrissen oder Teilungserklaerung ableiten.
4. **Ohne Nebenkosten:** Wirtschaftliche Analyse nur auf Kaltmiete-Basis. Warnung ausgeben dass NK-Umlagefaehigkeit nicht geprueft.
5. **Mietliste als PDF (nicht tabellarisch):** Daten extrahieren und normalisieren, Extraktionsfehler kennzeichnen.

---

## Konfidenz-Bewertung

| Datenlage | Score | Bedeutung |
|-----------|-------|-----------|
| Mietliste + qualifizierter Mietspiegel + Mietvertraege + Zahlungshistorie | 0.90-1.00 | Belastbare Analyse mit praezisem Steigerungspotenzial |
| Mietliste + Mietspiegel (einfach oder qualifiziert) | 0.70-0.89 | Gute Analyse, Steigerungspotenzial gut schaetzbar |
| Mietliste ohne Mietspiegel | 0.45-0.69 | Eingeschraenkt, Mietspiegel-Vergleich nur geschaetzt |
| Nur Gesamt-Mieteinnahme (keine Einzelaufstellung) | 0.20-0.44 | Nur Grob-Screening moeglich |
| Unvollstaendige Mietliste (fehlende Einheiten/Daten) | 0.15-0.39 | Nicht belastbar, Nachforderung zwingend |

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- BGB Mietrecht (§§ 556d-559), Kappungsgrenze, Mietpreisbremse, Modernisierungsumlage
- `knowledge/kalkulationsformeln.md` -- Bruttomietrendite, Nettomietrendite, Kaufpreisfaktor
- `knowledge/marktbenchmarks.md` -- Vergleichsmieten nach Baujahr und Lage
- `knowledge/risikobewertung.md` -- Mieterrisiken im Gesamtkontext
- `skills/unterlagen-analyst/SKILL.md` -- Gesamtanalyse inkl. Mietlisten-Abgleich
- `skills/risiko-scanner/SKILL.md` -- Kategorien 2 (Mietstruktur) und 6 (Mieterrisiken)
- `skills/mieterhoehung/SKILL.md` -- Mieterhoehungsstrategie und Umsetzung
- `skills/mietlisten-parser/SKILL.md` -- PDF-Mietlisten in strukturierte Daten konvertieren
