---
name: mieterhoehung
description: "Portfolioweite Mieterhoehungsanalyse ueber alle 5 Erhoehungswege: Vergleichsmiete (Par. 558 BGB), Modernisierungsumlage (Par. 559), Indexmiete, Staffelmiete und einvernehmliche Erhoehung. Prueft Kappungsgrenze, Sperrfristen, Mietpreisbremse und erstellt rechtssichere Mieterhoehungsschreiben plus Gespraechsstrategie. Nutze diesen Skill wenn du Mieterhoehungspotenzial ermitteln, den richtigen Erhoehungsweg waehlen oder Erhoehungsschreiben erstellen willst."
---

# Mieterhoehung -- Strategie, Potenzialanalyse und Schreiben

## Wann nutzen

- Mieterhoehungspotenzial im Portfolio systematisch identifizieren (10-500+ Einheiten)
- Ist-Miete gegen ortsbuebliche Vergleichsmiete (Mietspiegel) abgleichen
- Kappungsgrenze und Mietpreisbremse pruefen
- Mieterhoehungsschreiben rechtssicher erstellen
- Modernisierungsumlage nach §559 BGB berechnen
- Prioritaetenliste erstellen: Welche Einheiten zuerst erhoehen? (hoechster ROI)
- Portfolio-weite Potenzialanalyse: Gesamtes Uplift-Potenzial in EUR/Jahr berechnen

---

## Inputs

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `rent_roll` | Array | Ja | Ist-Mieten: Einheit, Mieter, Kaltmiete/qm, Kaltmiete gesamt, Wohnflaeche, Zimmer, Ausstattung, letzte Erhoehung (Datum + Betrag) |
| `mietspiegel` | Object | Ja | Ortsuebliche Vergleichsmiete: Quelle (qualifizierter Mietspiegel, einfacher Mietspiegel, Vergleichswohnungen), Werte nach Baujahr/Lage/Ausstattung |
| `property_data` | Array | Ja | Objektdaten: Adresse, Baujahr, Lage (einfach/mittel/gut), Ausstattungsklasse, Zustand |
| `market_area` | String | Ja | Stadt/Gemeinde (fuer Mietpreisbremse-Check und Kappungsgrenze) |
| `mietpreisbremse_active` | Boolean | Nein | Gilt die Mietpreisbremse (§556d BGB) im Gebiet? |
| `kappungsgrenze_reduced` | Boolean | Nein | Gilt die reduzierte Kappungsgrenze von 15% statt 20%? |
| `modernization_costs` | Array | Nein | Durchgefuehrte Modernisierungen: Massnahme, Kosten, Datum, betroffene Einheiten |
| `staffelmiete_agreements` | Array | Nein | Bestehende Staffelmietvereinbarungen |
| `indexmiete_agreements` | Array | Nein | Bestehende Indexmietvereinbarungen mit Basisindex |

---

## Auftrag

Du bist ein erfahrener Immobilienoekonom und Mietrechtsexperte. Analysiere das gesamte Portfolio auf Mieterhoehungspotenzial, priorisiere die Einheiten nach ROI und erstelle rechtssichere Mieterhoehungsschreiben. Beachte dabei alle gesetzlichen Vorgaben: §558 BGB (Mieterhoehung bis Vergleichsmiete), §558a BGB (formelle Anforderungen), §559 BGB (Modernisierungsumlage), §556d BGB (Mietpreisbremse), sowie Kappungsgrenze und Sperrfristen.

**Pruefbedarf-Hinweis:** Mietrecht aendert sich laufend (Gesetzesnovellen, Landesverordnungen, BGH-Rechtsprechung). Jede mietrechtliche Aussage in diesem Skill ist als Arbeitsgrundlage zu verstehen -- vor Versand formeller Schreiben aktuelle Rechtslage pruefen, im Zweifel Fachanwalt fuer Mietrecht oder Hausverwaltung einbinden. Diesen Hinweis auch im Ergebnisbericht ausgeben.

---

## Die 5 Erhoehungswege im Bestand (Entscheidungsbaum)

Mieterhoehung ist kein Bauchthema, sondern ein Entscheidungsbaum: Rechtsgrundlage, Frist und Begruendung entscheiden. Formfehler oder die falsche Strategie kosten Zeit, Geld und die Mieterbeziehung. Vor jeder Erhoehung ZUERST den Weg bestimmen:

| Weg | Rechtsgrundlage | Voraussetzung | Grenze | Zustimmung Mieter noetig? |
|-----|-----------------|---------------|--------|---------------------------|
| 1. Vergleichsmiete | §558 BGB | Miete unter ortsueblicher Vergleichsmiete, 15 Monate Sperrfrist, Begruendung (Mietspiegel / 3 Vergleichswohnungen / Gutachten) | Kappungsgrenze 20% bzw. 15% in 3 Jahren; Vergleichsmiete basiert auf den Mieten der letzten 6 Jahre (Pruefbedarf: aktueller Betrachtungszeitraum) | Ja (§558b BGB, notfalls Zustimmungsklage) |
| 2. Modernisierungsumlage | §559 BGB | Durchgefuehrte Modernisierung (nicht Instandhaltung), 3 Monate vorher angekuendigt (§555c BGB) | 8% der Modernisierungskosten p.a.; Kappung 3 EUR/qm (bzw. 2 EUR/qm bei Ausgangsmiete < 7 EUR/qm) in 6 Jahren | Nein (einseitige Erklaerung, Haertefall-Einwand moeglich) |
| 3. Indexmiete | §557b BGB | Indexklausel im Mietvertrag (Schriftform), Kopplung an Verbraucherpreisindex | Nur bei Indexsteigerung; sperrt §558-Erhoehung; Modernisierungsumlage nur eingeschraenkt | Nein (Erklaerung in Textform mit Indexangabe) |
| 4. Staffelmiete | §557a BGB | Staffelvereinbarung im Mietvertrag (Schriftform), min. 1 Jahr zwischen Staffeln | Feste Stufen; sperrt §558-Erhoehung waehrend der Laufzeit | Nein (Erhoehung tritt automatisch ein) |
| 5. Einvernehmliche Erhoehung | Vertragsfreiheit (§557 Abs. 1 BGB) | Einigung mit dem Mieter, idealerweise verbunden mit Gegenleistung (Modernisierung, Mieterwunsch, Mangelbeseitigung) | Keine Kappungsgrenze, aber Angemessenheit und faire Kommunikation; Schriftform und ggf. Widerrufsbelehrung beachten (Pruefbedarf) | Ja (per Definition) |

**Wenn/Dann-Entscheidungsregeln:**

| Wenn | Dann |
|------|------|
| Indexmiete oder laufende Staffel im Vertrag | Weg 1 (§558) ist gesperrt -- nur Index-/Staffellogik anwenden |
| Modernisierung durchgefuehrt oder geplant | Weg 2 pruefen; bei Kosten bis 10.000 EUR/Wohnung vereinfachtes Verfahren §559c (pauschal 30% Instandhaltungsabzug) |
| Miete weit unter Markt UND langjaehriger, kooperativer Mieter | Weg 5 zuerst versuchen: Gespraech mit Gegenleistung (z.B. Bad-Modernisierung, Wunscherfuellung) -- oft schneller, konfliktaermer und ohne Kappungsstreit |
| Miete unter Markt, kein Sonderweg, Sperrfrist abgelaufen | Weg 1 mit Mietspiegel-Begruendung |
| Mieter zahlt unpuenktlich oder Konflikt laeuft | Erst Konflikt loesen, dann erhoehen -- Erhoehung im Konflikt provoziert Widerspruch und Klage |
| Neuvermietung steht an | Nicht dieser Skill: Mietpreisbremse-Logik in `skills/inserat-generator/SKILL.md` und `skills/mietlisten-analyse/SKILL.md` |

---

## Strategie

1. **Ist-Zustand erfassen** -- Fuer jede Einheit dokumentieren:
   - Aktuelle Kaltmiete (EUR/qm und EUR gesamt)
   - Wohnflaeche in qm
   - Baujahr des Gebaeudes
   - Ausstattungsklasse (einfach, mittel, gut, gehoben)
   - Lage (einfach, mittel, gut)
   - Datum und Betrag der letzten Mieterhoehung
   - Art des Mietvertrags (Standard, Staffelmiete, Indexmiete)

2. **Ortsbuebliche Vergleichsmiete bestimmen** -- Fuer jede Einheit die maximal zulaessige Miete ermitteln:
   - Qualifizierter Mietspiegel: Einordnung nach Baujahr, Lage, Ausstattung, Wohnflaeche
   - Mietspiegel-Spanne: unterer Wert, Mittelwert, oberer Wert
   - Ziel: Einordnung im Mietspiegel-Feld (wo steht die Einheit realistisch?)
   - Zu- und Abschlaege nach Ausstattungsmerkmalen beruecksichtigen

3. **Kappungsgrenze pruefen (§558 Abs. 3 BGB)** -- Die Miete darf innerhalb von 3 Jahren maximal steigen um:
   - Standard: 20% (bezogen auf die Miete vor 3 Jahren)
   - In Gebieten mit angespanntem Wohnungsmarkt (Landesverordnung): 15%
   - Berechnung: Miete vor 3 Jahren x Kappungsgrenze = maximale aktuelle Miete
   - Wenn Kappungsgrenze die Erhoehung auf Vergleichsmiete begrenzt: Differenz fuer spaetere Erhoehung vormerken

4. **Mietpreisbremse pruefen (§556d BGB)** -- Nur bei Neuvermietung relevant:
   - Gilt nur in per Landesverordnung bestimmten Gebieten mit angespanntem Wohnungsmarkt
   - Maximal: ortsbuebliche Vergleichsmiete + 10%
   - Ausnahmen: Erstvermietung nach Neubau, umfassende Modernisierung, Vormiete war bereits hoeher
   - Bei Bestandsmietern: Mietpreisbremse nicht relevant (nur Kappungsgrenze und Vergleichsmiete)

5. **Sperrfrist pruefen** -- Mieterhoehung fruehestens:
   - 12 Monate nach Einzug (§558 Abs. 1 BGB)
   - 15 Monate nach der letzten Mieterhoehung (12 Monate Sperrfrist + Wirksamkeit fruehestens nach Ablauf des 2. Monats nach Zugang)
   - Bei Staffelmiete: keine Mieterhoehung nach §558 moeglich, solange Staffel laeuft
   - Bei Indexmiete: Erhoehung nur bei Indexsteigerung (§557b BGB)

6. **Modernisierungsumlage berechnen (§559 BGB)** -- Falls Modernisierungen durchgefuehrt:
   - Maximal 8% der fuer die Wohnung aufgewendeten Modernisierungskosten auf die Jahresmiete
   - Seit 2019: Kappungsgrenze Modernisierungsumlage: max. 3 EUR/qm innerhalb von 6 Jahren (bei Ausgangsmiete < 7 EUR/qm: max. 2 EUR/qm)
   - Nur wertverbessernde Massnahmen und Energieeinsparung (nicht: Instandhaltungsanteil abziehen)
   - Instandhaltungsanteil herausrechnen (typisch: 30-50% bei kombinierten Massnahmen)
   - Foerdermittel abziehen
   - Vereinfachtes Verfahren (§559c BGB): bei Kosten bis 10.000 EUR pro Wohnung pauschal 30% Instandhaltungsabzug, vereinfachte Berechnung und Ankuendigung
   - Ankuendigung 3 Monate vor Beginn der Massnahme erforderlich (§555c BGB)
   - Haertefall-Einwand des Mieters moeglich (§559 Abs. 4 BGB)

7. **Staffelmiete / Indexmiete analysieren** -- Sonderregelungen:
   - Staffelmiete (§557a BGB): Feste Erhoehungsstufen im Vertrag. Keine zusaetzliche Erhoehung nach §558 moeglich.
   - Indexmiete (§557b BGB): Kopplung an Verbraucherpreisindex. Erhoehung nur bei Indexsteigerung, Berechnung: (neuer Index / alter Index - 1) x aktuelle Miete.
   - Pruefen: Ist eine Umstellung sinnvoll? (z.B. bei stark steigenden Mietspiegeln: Staffelmiete kann nachteilig sein)

8. **Einvernehmliche Erhoehung pruefen (Weg 5)** -- Vor jedem formellen Verlangen bewerten, ob eine Einigung der bessere Weg ist:
   - Kandidaten: langjaehrige Mieter deutlich unter Markt, Mieter mit offenen Wuenschen (neues Bad, Balkonsanierung, Haustier-Erlaubnis), frisch uebernommene Bestaende nach Kauf
   - Mechanik: Gegenleistung anbieten (Modernisierung, Mangelbeseitigung, Wunscherfuellung) und dafuer moderate Erhoehung vereinbaren -- Win-win statt Konfrontation
   - Marktmiete als Anker im Gespraech nutzen, nie als Drohung -- Druck zerstoert Vertrauen und erzeugt langfristige Verwaltungskosten
   - Formalien: Vereinbarung schriftlich fixieren; bei Vereinbarungen ausserhalb von Geschaeftsraeumen (z.B. an der Wohnungstuer) Widerrufsrecht des Mieters beachten -- fehlende oder falsche Widerrufsbelehrung kann lange Widerrufsfristen ausloesen (Pruefbedarf: rechtssichere Vorlage verwenden)
   - Faustregel: Der Ertrag einer maximalen Erhoehung ist schnell aufgezehrt durch Rechtsstreit, Fluktuation und Leerstand -- Erhoehungshoehe gegen Beziehungskosten abwaegen

9. **Potenzialanalyse pro Einheit** -- Fuer jede Einheit berechnen:
   - Delta: Vergleichsmiete (EUR/qm) minus Ist-Miete (EUR/qm)
   - Erhoehungspotenzial EUR/Monat: Delta x Wohnflaeche
   - Erhoehungspotenzial EUR/Jahr: Monatswert x 12
   - Durch Kappungsgrenze begrenztes Potenzial (was ist JETZT moeglich?)
   - Fruehester Erhoehungszeitpunkt (Sperrfrist beachten)

10. **Prioritaetenliste erstellen** -- Einheiten sortieren nach:
   - Hoechstes Delta EUR/Monat (groesster finanzieller Effekt zuerst)
   - Sofort umsetzbar (Sperrfrist abgelaufen, keine Staffelmiete)
   - Geringes Streitrisiko (Erhoehung deutlich innerhalb Mietspiegel-Spanne)
   - Ergebnis: Rangliste mit Top-10 oder Top-20 Einheiten fuer sofortige Erhoehung

11. **Portfolio-Gesamtpotenzial berechnen** -- Aggregation:
    - Summe aller Erhoehungspotenziale EUR/Jahr (gesamt)
    - Davon sofort umsetzbar (Sperrfrist abgelaufen)
    - Davon in den naechsten 12 Monaten umsetzbar
    - Beispiel: 100 Einheiten x 50 EUR/Monat Durchschnitt = 60.000 EUR/Jahr

12. **Mieterhoehungsschreiben generieren** -- Formelle Anforderungen (§558a BGB):
    - Schriftform (Textform genuegt, §558a Abs. 1 BGB)
    - Begruendung: Verweis auf qualifizierten Mietspiegel ODER mindestens 3 Vergleichswohnungen ODER Sachverstaendigengutachten
    - Konkrete Angabe der neuen Miete (EUR/qm und EUR gesamt)
    - Wirksamkeit: ab dem dritten Kalendermonat nach Zugang
    - Zustimmungsfrist: bis zum Ablauf des zweiten Kalendermonats nach Zugang
    - Hinweis auf Zustimmungspflicht und Klagemoeglichkeit (§558b BGB)
    - Hoeflich und sachlich formuliert

13. **Timeline erstellen** -- Wann kann die naechste Erhoehung je Einheit erfolgen?
    - Fruehester Zugang des Schreibens
    - Zustimmungsfrist (2 Monate nach Zugang)
    - Wirksamkeit der neuen Miete (3. Monat nach Zugang)
    - Naechste Erhoehung moeglich (15 Monate nach dieser Erhoehung)

---

## Mieterkommunikation: fair und rechtssicher

Der Mieter ist Kunde und Vertragspartner zugleich -- Konflikt ist Ultima Ratio, nicht Standardwerkzeug. Gute Kommunikation entscheidet ueber die Zustimmungsquote:

**Gespraechsleitfaden vor dem formellen Schreiben (empfohlen bei Erhoehungen > 10% oder sensiblen Mietern):**
1. Anlass transparent machen: gestiegene Kosten, Marktentwicklung, durchgefuehrte/geplante Verbesserungen
2. Marktmiete als sachlichen Anker nennen (Mietspiegel-Wert), nie als Drohung
3. Wuensche und Maengel des Mieters aktiv abfragen -- oft Basis fuer einvernehmliche Loesung (Weg 5)
4. Zeit zur Ueberlegung geben, keine Unterschrift an der Tuer fordern (Widerrufsrisiko, Vertrauensschaden)
5. Ergebnis schriftlich bestaetigen, danach ggf. formelles Verlangen nach §558a nachziehen

**Typische Konfliktpfade und Eskalationsstufen:**

| Stufe | Situation | Reaktion |
|-------|-----------|----------|
| 1 | Mieter reagiert nicht auf Erhoehungsverlangen | Freundliche Erinnerung vor Fristablauf, Gespraechsangebot |
| 2 | Mieter widerspricht mit Sachargumenten (Einordnung, Wohnwertmerkmale) | Argumente ernsthaft pruefen -- Mietspiegel-Einordnung ist oft angreifbar; ggf. Verlangen anpassen |
| 3 | Mieter verweigert ohne Begruendung | Zustimmungsklage binnen 3 Monaten nach Ablauf der Zustimmungsfrist (§558b Abs. 2 BGB) -- vorher Kosten/Nutzen und Prozessrisiko abwaegen (Anwalt) |
| 4 | Mieter kuendigt nach Erhoehung | Sonderkuendigungsrecht beachten; Leerstands- und Neuvermietungskosten gegen Erhoehungsertrag rechnen |

---

## Ausgabeformat

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext. Die Mieterhoehungsschreiben sind direkt kopierbare, druckfertige Textbloecke -- nicht in Datenfelder verpackt.

Liefere die Ergebnisse in folgendem Format:

### Ergebnisbericht

```markdown
# Mieterhoehungs-Analyse: Portfolio Berlin

**Analysedatum:** 15.04.2026 | Konfidenz: 90%

| Rahmenbedingung | Wert |
|-----------------|------|
| Marktgebiet | Berlin |
| Mietpreisbremse | Aktiv |
| Kappungsgrenze | 15% |
| Mietspiegel-Quelle | Berliner Mietspiegel 2025, qualifiziert |

## Portfolio-Ueberblick

| Kennzahl | Wert |
|----------|------|
| Einheiten gesamt | 100 |
| Einheiten mit Erhoehungspotenzial | 72 |
| Einheiten auf Marktniveau | 18 |
| Einheiten ueber Marktniveau | 2 |
| Einheiten in Sperrfrist | 8 |
| Einheiten mit Staffelmiete | 5 |
| Einheiten mit Indexmiete | 3 |
| **Gesamtpotenzial monatlich** | **4.820,00 EUR** |
| **Gesamtpotenzial jaehrlich** | **57.840,00 EUR** |
| Sofort umsetzbar (Einheiten) | 48 |
| Sofort umsetzbar (jaehrlich) | 38.400,00 EUR |
| Durchschnittliches Delta pro Einheit | 48,20 EUR/Monat |

## Prioritaetenliste der Einheiten

| Rang | Objekt / Einheit | Mieter | qm | Ist-Miete | Ziel-Miete | Delta/Monat | Delta/Jahr | Prioritaet |
|------|------------------|--------|-----|-----------|------------|-------------|------------|------------|
| 1 | Musterstr. 12, WE 04 | Nachname, Vorname | 72,5 | 493,00 EUR (6,80 EUR/qm) | 594,50 EUR (8,20 EUR/qm) | 101,50 EUR | 1.218,00 EUR | 🔴 hoch |
| ... | | | | | | | | |

### Detail Rang 1: Musterstr. 12, 10115 Berlin, WE 04

| | |
|---|---|
| Mieter | Nachname, Vorname |
| Wohnflaeche / Zimmer | 72,50 qm / 3 Zimmer |
| Baujahr / Zustand / Lage | 1965 / mittel / gut |
| Ist-Miete | 493,00 EUR (6,80 EUR/qm) |
| Mietspiegel-Spanne | 7,20 - 9,80 EUR/qm (Mittelwert 8,50) |
| Ziel-Miete | 594,50 EUR (8,20 EUR/qm) |
| Delta | 1,40 EUR/qm = 101,50 EUR/Monat = 1.218,00 EUR/Jahr |
| Vertragstyp | Standard |
| Letzte Erhoehung | 01.10.2024 (+33,00 EUR) |
| Sperrfrist | abgelaufen (bis 01.01.2026) |
| Fruehestes Wirksamkeitsdatum | 01.07.2026 |
| Umsetzbar | Ja |

**Kappungsgrenzen-Pruefung:**

| | |
|---|---|
| Miete vor 3 Jahren | 460,00 EUR |
| Maximale Erhoehung (15%) | 69,00 EUR |
| Maximale Miete nach Kappung | 529,00 EUR |
| Kappungsgrenze begrenzt Erhoehung | Ja |
| Jetzt erreichbare Erhoehung | 36,00 EUR |
| Verbleibendes Potenzial | 65,50 EUR |

**Empfehlung:** Mieterhoehung auf 529,00 EUR (Kappungsgrenze). Verbleibendes
Potenzial von 65,50 EUR in 15 Monaten realisierbar.

## Modernisierungsumlagen

| Objekt | Massnahme | Gesamtkosten | Instandhaltungsabzug | Modernisierungskosten | Einheiten | Kosten/Einheit | Umlage/Einheit |
|--------|-----------|--------------|----------------------|------------------------|-----------|----------------|----------------|
| Musterstr. 12 | Fassadendaemmung WDVS | 180.000 EUR | 35% | 117.000 EUR | 12 | 9.750 EUR | 65,00 EUR/Monat (780 EUR/Jahr) |

**Kappungs-Check Umlage:** Ist-Miete Durchschnitt 6,80 EUR/qm, Umlage 0,90 EUR/qm,
zulaessig max. 3,00 EUR/qm in 6 Jahren — 🟢 innerhalb der Kappung.

## Mieterhoehungsschreiben (druckfertig)

### Schreiben fuer WE 04, Nachname, Vorname

---

**MIETERHOEHUNGSVERLANGEN**

Sehr geehrte/r Frau/Herr [Name],

wir beziehen uns auf den Mietvertrag vom [Datum] ueber die Wohnung [Adresse],
bestehend aus [Zimmer] Zimmern mit einer Wohnflaeche von [qm] qm.

Die derzeitige Nettokaltmiete betraegt [aktuelle Miete] EUR monatlich
([EUR/qm] EUR/qm).

Gemaess §558 BGB verlangen wir Ihre Zustimmung zur Erhoehung der Nettokaltmiete
auf [neue Miete] EUR monatlich ([neuer EUR/qm] EUR/qm) ab dem [Wirksamkeitsdatum].

Begruendung:
Die Erhoehung entspricht der ortsueblichen Vergleichsmiete gemaess dem
[Mietspiegel-Name] (qualifizierter Mietspiegel). Ihre Wohnung ist einzuordnen in:
- Baujahrsklasse: [Klasse]
- Wohnlage: [Lage]
- Ausstattung: [Ausstattung]
- Mietspiegel-Spanne: [unterer Wert] bis [oberer Wert] EUR/qm

Die verlangte Miete von [neuer EUR/qm] EUR/qm liegt innerhalb dieser Spanne.
Die Kappungsgrenze von [15/20]% in 3 Jahren wird eingehalten.

Wir bitten Sie, Ihre Zustimmung bis zum [Fristdatum -- 2 Monate nach Zugang]
zu erklaeren.

Sollten Sie der Mieterhoehung nicht zustimmen, koennen wir gemaess §558b
Abs. 2 BGB innerhalb von 3 Monaten nach Ablauf der Zustimmungsfrist Klage
auf Zustimmung erheben.

Mit freundlichen Gruessen
[Vermieter]

---

## Timeline

| Einheit | Schreiben versenden bis | Zustimmungsfrist | Wirksam ab | Naechste Erhoehung moeglich |
|---------|-------------------------|------------------|------------|------------------------------|
| WE 04 | 30.04.2026 | 30.06.2026 | 01.07.2026 | 01.10.2027 |

## Datenluecken

Keine. (Falls vorhanden: jede Luecke auflisten mit Auswirkung auf die Bewertung.)
```

---

## Qualitaetspruefung

- [ ] Erhoehungsweg korrekt gewaehlt (Entscheidungsbaum der 5 Wege durchlaufen, Sperrwirkung Index/Staffel geprueft)
- [ ] Einvernehmliche Loesung (Weg 5) bei geeigneten Einheiten als Alternative genannt
- [ ] Pruefbedarf-Hinweis (aktuelle Rechtslage / Anwalt) im Bericht enthalten
- [ ] Mietspiegel-Einordnung plausibel (Baujahr, Lage, Ausstattung korrekt zugeordnet)
- [ ] Kappungsgrenze korrekt berechnet (Miete vor 3 Jahren als Basis, 15% oder 20%)
- [ ] Sperrfrist korrekt berechnet (15 Monate ab letzter Erhoehung)
- [ ] Staffelmiete-/Indexmiete-Einheiten korrekt ausgeschlossen von §558-Erhoehung
- [ ] Modernisierungsumlage: Instandhaltungsanteil abgezogen, 8%-Berechnung korrekt, Kappung 3 EUR/qm (bzw. 2 EUR/qm) beachtet
- [ ] Mieterhoehungsschreiben enthaelt: Begruendung, Mietspiegel-Verweis, neue Miete, Zustimmungsfrist
- [ ] Zustimmungsfrist: korrekt 2 Monate nach Zugang
- [ ] Wirksamkeit: ab dem 3. Kalendermonat nach Zugang
- [ ] Portfolio-Summen stimmen mit Einzelwerten ueberein
- [ ] Prioritaetenliste ist nach Delta EUR/Monat sortiert (hoechster Wert zuerst)

---

## Warnsignale

| Signal | Bedeutung | Empfohlene Aktion |
|--------|-----------|-------------------|
| Ist-Miete > Mietspiegel-Obergrenze | Miete bereits ueber Vergleichsmiete | Keine Erhoehung moeglich, ggf. Mietsenkungsrisiko |
| Kappungsgrenze fast ausgeschoepft | Wenig Spielraum fuer diese Erhoehungsrunde | Kleine Erhoehung jetzt, Rest in 15 Monaten |
| Letzte Erhoehung < 15 Monate | Sperrfrist laeuft noch | Erhoehung vormerken, nicht jetzt versenden |
| Staffelmiete mit hoher Reststaffel | Staffel koennte guenstiger sein als Mietspiegel-Erhoehung | Staffel auslaufen lassen, dann §558 pruefen |
| Mietpreisbremse aktiv + Neuvermietung | Miete max. Vergleichsmiete + 10% | Vormiete oder Ausnahmetatbestand pruefen |
| Mietspiegel aelter als 2 Jahre | Veralteter Mietspiegel, angreifbar | Aktuellen Mietspiegel recherchieren oder Vergleichswohnungen nutzen |
| Hohe Fluktuation nach Erhoehungen | Mieter kuendigen nach Erhoehung | Erhoehung moderat halten, Leerstandskosten gegenueberstellen |
| Laufender Konflikt / Mangelanzeige offen | Erhoehung im Konflikt provoziert Widerspruch und Klage | Erst Mangel beheben bzw. Konflikt loesen, dann erhoehen |
| Erhoehung nur an der Wohnungstuer vereinbart | Widerrufsrisiko bei Haustuervereinbarungen, Formmangel | Schriftliche Vereinbarung mit korrekter Widerrufsbelehrung (Pruefbedarf: Anwalt/Vorlage) |
| Mieter mit Transferleistungsbezug (KdU) | Amt zahlt nur bis lokale Angemessenheitsgrenze -- Erhoehung kann Zahlungsausfall ausloesen | KdU-Grenze der Kommune pruefen, Erhoehung ggf. darunter halten |

---

## Bei fehlenden Daten

- Wenn kein Mietspiegel vorliegt: Vergleichswohnungen als Alternative nutzen (mindestens 3 vergleichbare Wohnungen mit Adresse, Groesse, Ausstattung, Miete). Alternativ auf Sachverstaendigengutachten verweisen.
- Wenn letzte Mieterhoehung unbekannt: Konservativ annehmen, dass Sperrfrist noch laeuft. Mietvertragsdatum als fruehestes Erhoehungsdatum nutzen.
- Wenn Kappungsgrenze-Status (15% vs. 20%) unklar: Die strengere Grenze (15%) annehmen.
- Wenn Mietpreisbremse-Status unklar: Als aktiv annehmen und darauf hinweisen, dass die Landesverordnung geprueft werden muss.
- Wenn Baujahr oder Ausstattung unklar: Mietspiegel-Einordnung als "unsicher" kennzeichnen und Spanne angeben.
- Alle Luecken im Berichtsabschnitt "Datenluecken" dokumentieren.

---

## Konfidenz-Bewertung

| Score | Bedeutung |
|-------|-----------|
| 0.9 - 1.0 | Qualifizierter Mietspiegel vorhanden, alle Einheitendaten komplett, Mahnhistorie und Mietvertraege verfuegbar |
| 0.7 - 0.9 | Mietspiegel vorhanden, aber einzelne Einheitendaten unvollstaendig (z.B. letzte Erhoehung unbekannt) |
| 0.5 - 0.7 | Nur einfacher Mietspiegel oder Vergleichswohnungen, mehrere Datenluecken |
| < 0.5 | Kein Mietspiegel, wesentliche Objektdaten fehlen |

Faktoren die den Score senken:
- Kein qualifizierter Mietspiegel verfuegbar (-0.15)
- Letzte Mieterhoehung bei >30% der Einheiten unbekannt (-0.10)
- Kappungsgrenze-Status (15% vs. 20%) unklar (-0.05)
- Wohnflaechen nicht verifiziert (Abweichungen moeglich) (-0.10)
- Ausstattungsmerkmale nicht detailliert erfasst (-0.05)

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- §558, §558a, §559, §556d, §557a, §557b BGB: Mieterhoehungsrecht komplett
- `knowledge/marktbenchmarks.md` -- Benchmarks fuer Mieten nach Baujahr, Lage, Zustand
- `knowledge/kalkulationsformeln.md` -- Renditekennzahlen zur Bewertung des Erhoehungseffekts
- `skills/mietlisten-parser/SKILL.md` -- Schritt 1 der Kette: Mietliste in strukturierte Daten ueberfuehren
- `skills/mietlisten-analyse/SKILL.md` -- Schritt 2 der Kette: Under-Rent erkennen und Potenzial quantifizieren (dieser Skill ist Schritt 3: Umsetzung)
- `skills/inserat-generator/SKILL.md` -- Bei Neuvermietung nach Kuendigung: Mietpreisbremse beachten
- `skills/energieausweis-check/SKILL.md` -- Energetische Modernisierung als Basis fuer §559-Umlage
- `skills/wochen-jourfixe/SKILL.md` -- Mieterhoehungsfristen im Wochen-Report tracken
