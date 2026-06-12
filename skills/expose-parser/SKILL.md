---
name: expose-parser
description: "Extrahiert alle investitionsrelevanten Daten aus Makler-Exposes in eine uebersichtliche Eckdaten-Tabelle. Nutze diesen Skill wenn du neue Angebote schnell auf Kennzahlen reduzieren, mehrere Exposes screenen oder Daten fuer die Bierdeckel-Kalkulation aufbereiten willst."
---

# Expose-Parser

> Eckdaten aus Makler-Exposes strukturiert extrahieren -- Kaufpreis, Flaechen, Mieteinnahmen, Zustand und Besonderheiten auf einen Blick, fertig fuer den Deal-Screener.

---

## Wann nutzen?

- Bei neuen Angeboten: Expose schnell auf die wesentlichen Kennzahlen reduzieren
- Bei Massenscreening: Mehrere Exposes gleichzeitig auswerten und vergleichen
- Vor der Besichtigung: Alle relevanten Daten strukturiert verfuegbar haben
- Fuer die Bierdeckel-Kalkulation: Daten direkt in den Deal-Screener uebergeben

---

## Inputs

Stelle folgende Informationen bereit:

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| `expose` | Ja | Expose-Dokument (PDF, Scan, Link, Freitext) |
| `ankaufskriterien` | Optional | Eigene Ankaufskriterien zum Sofort-Abgleich |
| `marktdaten` | Optional | Lokale Vergleichsdaten (Mietspiegel, Bodenrichtwerte, Angebotspreise) |

---

## Auftrag

Du bist ein erfahrener Immobilienanalyst mit Fokus auf deutsche Wohnimmobilien-Investments. Extrahiere aus dem uebergebenen Expose alle investitionsrelevanten Daten in ein strukturiertes Format. Berechne Standard-Kennzahlen. Identifiziere Besonderheiten, Risiken und fehlende Informationen. Die Ausgabe muss direkt als Input fuer den Deal-Screener verwendbar sein.

---

## Strategie

1. **Kerndaten extrahieren**
   - **Kaufpreis:** Angebotspreis in EUR
   - **Wohnflaeche:** Gesamtwohnflaeche in qm
   - **Nutzflaeche:** Gewerbeflaeche, Lagerflaeche in qm (falls vorhanden)
   - **Grundstuecksflaeche:** in qm
   - **Baujahr:** Urspruengliches Baujahr
   - **Anzahl Einheiten:** Wohnungen, Gewerbeeinheiten, Garagen/Stellplaetze
   - **Geschosse:** Anzahl Stockwerke
   - **Dachform:** Flachdach, Satteldach, Walmdach (relevant fuer Sanierungskosten)

2. **Mietdaten extrahieren**
   - **Ist-Miete (Jahresnettokaltmiete):** Aktuelle Mieteinnahmen p.a.
   - **Soll-Miete:** Mieteinnahmen bei Vollvermietung p.a. (falls angegeben)
   - **Miete pro qm:** Durchschnittliche Kaltmiete EUR/qm
   - **Leerstandsquote:** Aktueller Leerstand in Prozent
   - **Mietliste:** Falls im Expose enthalten, an mietlisten-parser weiterleiten

3. **Zustand und Ausstattung erfassen**
   - **Gesamtzustand:** Erstbezug, neuwertig, gepflegt, renovierungsbeduerftig, sanierungsbeduerftig
   - **Letzte Sanierung:** Jahr und Umfang (Dach, Fassade, Heizung, Fenster, Leitungen)
   - **Heizungstyp:** Gas-Zentralheizung, Oelheizung, Fernwaerme, Waermepumpe, Etagenheizung
   - **Energiekennwert:** kWh/(m2a)
   - **Energieeffizienzklasse:** A+ bis H
   - **Energieausweis-Typ:** Bedarfsausweis oder Verbrauchsausweis
   - **Fenster:** Material, Verglasung (Einfach, Doppel, Dreifach), Baujahr
   - **Dach:** Zustand, letzte Sanierung
   - **Fassade:** Daemmung vorhanden, WDVS, Klinker, Putz
   - **Leitungen:** Steigleitungen erneuert (Wasser, Abwasser, Elektro)
   - **Aufzug:** Vorhanden/nicht vorhanden, Baujahr

4. **Finanzielle Rahmendaten**
   - **Hausgeld:** Monatlich/jaehrlich (bei WEG)
   - **Instandhaltungsruecklage:** Hoehe (gesamt und pro Einheit/qm)
   - **Nicht umlagefaehige Kosten:** Verwaltung, Instandhaltung
   - **Grundsteuer:** Jaehrlicher Betrag (falls angegeben)
   - **Maklercourtage:** Prozent und Betrag
   - **Kaufnebenkosten-Schaetzung:** Grunderwerbsteuer (je Bundesland), Notar, Grundbuch

5. **Besonderheiten identifizieren**
   - **Erbbaurecht:** Erbbauzins, Restlaufzeit, Vertragskonditionen
   - **Denkmalschutz:** Eingetragenes Denkmal, Auflagen, steuerliche Vorteile (§7i EStG)
   - **Baulasten:** Oeffentlich-rechtliche Verpflichtungen
   - **Wohnungsbindung:** Sozialbindung, Mietobergrenze, Restlaufzeit
   - **Niesbrauch / Wohnrecht:** Bestehende Rechte Dritter
   - **Teilungserklaerung:** Auffaelligkeiten (z.B. eingeschraenktes Sondereigentum)
   - **Geplante Massnahmen:** Beschlossene Sonderumlagen, anstehende Sanierungen
   - **Altlasten:** Hinweise auf Bodenkontamination
   - **Mischnutzung:** Wohnen + Gewerbe, Aufteilung

6. **Standard-Kennzahlen berechnen**
   - **Kaufpreisfaktor:** Kaufpreis / Jahresnettokaltmiete (Ist)
   - **Bruttomietrendite:** Jahresnettokaltmiete / Kaufpreis x 100
   - **Kaufpreis pro qm:** Kaufpreis / Wohnflaeche
   - **Kaufpreis pro Einheit:** Kaufpreis / Anzahl Wohneinheiten
   - **Soll-Rendite:** Jahresnettokaltmiete (Soll) / Kaufpreis x 100
   - **Hausgeld-Ratio:** Hausgeld / Gesamtmiete (Anteil nicht umlagefaehig)

7. **Informationsluecken identifizieren**
   - Welche Daten fehlen im Expose?
   - Was muss vor einer Kaufentscheidung noch geklaert werden?
   - Welche Unterlagen muessen angefordert werden?

---

## Ausgabeformat

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext.

### Extraktionsbericht

```markdown
# Expose-Auswertung: MFH Musterstrasse 12, 40210 Duesseldorf

**Quelle:** Expose ABC Makler, Objekt-ID 12345 | Konfidenz: Mittel (88%)

## Eckdaten

| | |
|---|---|
| Kaufpreis | 580.000 EUR |
| Adresse | Musterstrasse 12, 40210 Duesseldorf-Stadtmitte (NRW) |
| Wohnflaeche | 425 qm |
| Gewerbeflaeche | 0 qm |
| Grundstueck | 310 qm |
| Baujahr | 1965 |
| Geschosse | 3 |
| Dachform | Satteldach |
| Einheiten | 6 WE, 0 GE, 2 Garagen (gesamt 8) |

## Mietdaten

| | |
|---|---|
| Ist-Miete (JNKM) | 41.040 EUR/Jahr |
| Soll-Miete bei Vollvermietung | 46.650 EUR/Jahr |
| Durchschnittsmiete | 8,05 EUR/qm |
| Leerstand | 12,5% (1 WE) |
| Mietliste | Vorhanden (Stand 01.01.2025) |

## Zustand und Ausstattung

| | |
|---|---|
| Gesamtzustand | Gepflegt |
| Letzte Sanierung | 2015 (Dach, Fassadendaemmung WDVS) |
| Heizung | Gas-Zentralheizung, Baujahr 2010 |
| Energieausweis | Bedarfsausweis, 142 kWh/(qm*a), Klasse E, gueltig bis 15.05.2030 |
| Fenster | Kunststoff, Doppelverglasung, 2005 |
| Dach | Guter Zustand, saniert 2015 |
| Fassade | Gedaemmt (WDVS, 2015) |
| Leitungen | Wasser erneuert 2008, Elektro erneuert 2010, Abwasser nicht erneuert |
| Aufzug | Nein |

## Finanzielle Rahmendaten

| | |
|---|---|
| Hausgeld | Nicht angegeben |
| Instandhaltungsruecklage | Nicht angegeben |
| Nicht umlagefaehige Kosten | Nicht angegeben |
| Grundsteuer | 890 EUR/Jahr |
| Maklercourtage | 3,57% (20.706 EUR) |

**Geschaetzte Kaufnebenkosten:**

| Position | Betrag |
|----------|--------|
| Grunderwerbsteuer (6,5% NRW) | 37.700 EUR |
| Notar | 8.700 EUR |
| Grundbuch | 2.900 EUR |
| Maklercourtage | 20.706 EUR |
| **Gesamt** | **70.006 EUR (12,07%)** |

## Berechnete Kennzahlen

| Kennzahl | Wert |
|----------|------|
| Kaufpreisfaktor (Ist) | 14,1 |
| Bruttomietrendite (Ist) | 7,08% |
| Bruttomietrendite (Soll) | 8,04% |
| Kaufpreis pro qm | 1.365 EUR |
| Kaufpreis pro Wohneinheit | 96.667 EUR |

## Besonderheiten

Erbbaurecht: Nein | Denkmalschutz: Nein | Sozialbindung: Nein | Niessbrauch/Wohnrecht: Nein | Mischnutzung: Nein | Geplante Massnahmen: Keine erwaehnt

- Baulasten: Nicht erwaehnt -- **Baulastenverzeichnis anfordern**
- Altlasten: Nicht erwaehnt -- **Altlastenkataster pruefen**

## Fehlende Informationen

| Wichtigkeit | Was fehlt | Hinweis |
|-------------|-----------|---------|
| 🔴 Hoch | Hausgeld | Hausgeld/Wirtschaftsplan nicht im Expose enthalten -- anfordern |
| 🔴 Hoch | Instandhaltungsruecklage | Hoehe unbekannt |
| 🔴 Hoch | Teilungserklaerung | Fuer Due Diligence erforderlich |
| 🔴 Hoch | Grundbuchauszug | Belastungen in Abt. II und III pruefen |
| 🟡 Mittel | Abwasserleitungen | Zustand nicht erwaehnt -- ggf. Kamerabefahrung |
| 🟡 Mittel | Protokolle Eigentuemerversammlungen | Letzte 3 Jahre anfordern fuer Beschlusscheck |

## Naechster Schritt

Daten sind vollstaendig genug fuer den Deal-Screener. Empfehlung: Deal-Screening durchfuehren, parallel Hausgeld und Mietliste anfordern.
```

### Strukturierte Daten fuer Folge-Skills (nur als Datei)

Falls die extrahierten Daten fuer einen Folge-Skill (insbesondere `deal-screener`, `bierdeckel-kalkulation`) oder eine sonstige Weiterverarbeitung gebraucht werden: Schreibe die strukturierten Daten als Datei neben das Quell-Expose (z.B. JSON-Datei `expose-musterstrasse-12.json` im selben Ordner) -- inklusive aller extrahierten Felder und des fertigen Deal-Screener-Inputs (Kaufpreis, Wohnflaeche, Baujahr, Einheiten, Ist-/Soll-Miete, Leerstand, Zustand, Heizungstyp, Energiekennwert, Maklercourtage, GrESt-Satz, Grundsteuer, Bundesland). Gib diese strukturierten Daten niemals im Chat aus -- im Chat erscheint ausschliesslich der lesbare Bericht. Erwaehne im Bericht kurz, wohin die Datei geschrieben wurde.

---

## Qualitaetspruefung

Vor der Ausgabe pruefen:

- [ ] Alle im Expose erkennbaren Daten sind extrahiert
- [ ] Kaufpreis und Flaechen sind korrekt uebernommen (keine Einheitenfehler)
- [ ] Kennzahlen sind rechnerisch korrekt (Rendite, Faktor, Preis/qm)
- [ ] Kaufnebenkosten-Schaetzung verwendet den korrekten GrESt-Satz fuer das Bundesland
- [ ] Besonderheiten sind vollstaendig erfasst (Erbbaurecht, Denkmal, Baulasten)
- [ ] Fehlende Informationen sind klar benannt mit Wichtigkeit
- [ ] Deal-Screener-Input ist vollstaendig und konsistent
- [ ] Bruttomietrendite basiert auf Ist-Miete (nicht Soll-Miete)

---

## Warnsignale

| Signal | Bedeutung | Aktion |
|--------|-----------|--------|
| Rendite > 10% | Entweder sehr guter Deal oder versteckte Probleme | Besonders kritisch pruefen |
| Rendite < 4% | In den meisten Maerkten nicht cashflow-positiv | Nur bei Wertsteigerungsstrategie |
| Baujahr vor 1950 ohne Sanierung | Erheblicher Sanierungsstau wahrscheinlich | Sanierungskosten einplanen |
| Energieklasse F-H | Hohe Heizkosten, GEG-Sanierungspflicht moeglich | Energetische Sanierung kalkulieren |
| Erbbaurecht | Erbbauzins reduziert Rendite, Vertragsende beachten | Erbbaurechtsvertrag anfordern |
| Denkmalschutz | Einschraenkungen bei Sanierung, aber steuerliche Vorteile | Denkmalschutzbescheid anfordern |
| Hohe Maklercourtage (> 5%) | Ueberdurchschnittliche Ankaufsnebenkosten | Verhandeln oder einkalkulieren |
| Leerstand > 15% | Vermietungsprobleme oder Sanierungsstau | Ursache klaeren vor Angebot |
| Expose ohne Mietliste | Wichtigste Kalkulationsgrundlage fehlt | Mietliste anfordern |
| Keine Angabe Hausgeld | Bei WEG: Kritische Kosteninformation fehlt | Wirtschaftsplan anfordern |
| Viele Sanierungen gleichzeitig noetig | Investitionsstau = hoher Kapitalbedarf | Sanierungsfahrplan erstellen |
| Expose-Fotos zeigen andere Realitaet als Text | Zustandsbeschreibung moeglicherweise geschoent | Besichtigung mit Checkliste |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Jahresnettokaltmiete | Aus Miete/qm x Flaeche x 12 schaetzen (wenn Miete/qm angegeben) |
| Baujahr | Aus Architekturstil und Fotos schaetzen, als "geschaetzt" markieren |
| Grundstuecksflaeche | Als "nicht angegeben" markieren, fuer Bewertung noetig |
| Hausgeld | Als "nicht angegeben" markieren, vor Angebot anfordern |
| Maklercourtage | Landesueblichen Satz ansetzen, als "Annahme" markieren |
| Energiekennwert | Als "nicht angegeben" markieren, Energieausweis anfordern |
| Sanierungshistorie | Als "nicht angegeben" markieren, vor Ort pruefen |
| Grunderwerbsteuer-Satz | Nach Bundesland automatisch ansetzen |

**Grunderwerbsteuersaetze nach Bundesland (Stand 2025):**

| Bundesland | Satz |
|------------|------|
| Baden-Wuerttemberg | 5,0% |
| Bayern | 3,5% |
| Berlin | 6,0% |
| Brandenburg | 6,5% |
| Bremen | 5,0% |
| Hamburg | 5,5% |
| Hessen | 6,0% |
| Mecklenburg-Vorpommern | 6,0% |
| Niedersachsen | 5,0% |
| Nordrhein-Westfalen | 6,5% |
| Rheinland-Pfalz | 5,0% |
| Saarland | 6,5% |
| Sachsen | 5,5% |
| Sachsen-Anhalt | 5,0% |
| Schleswig-Holstein | 6,5% |
| Thueringen | 5,0% |

---

## Konfidenz-Bewertung

| Stufe | Wert | Bedeutung |
|-------|------|-----------|
| Hoch | >= 0.90 | Professionelles Expose, alle Kerndaten klar angegeben |
| Mittel | 0.70 - 0.89 | Die meisten Daten vorhanden, einzelne Werte geschaetzt |
| Niedrig | 0.50 - 0.69 | Minimales Expose, viele Werte fehlen oder sind unklar |
| Unsicher | < 0.50 | Expose nicht auswertbar (zu wenig Informationen, unleserlich) |

---

## Verwandte Wissensdatenbanken

- `knowledge/kalkulationsformeln.md` -- Renditekennzahlen, Kaufpreisfaktoren
- `knowledge/marktbenchmarks.md` -- Vergleichswerte nach Lage und Baujahr
- `knowledge/risikobewertung.md` -- Risiko-Scoring-Framework
- `skills/deal-screener/SKILL.md` -- Naechster Schritt: Deal-Screening mit extrahierten Daten
- `skills/bierdeckel-kalkulation/SKILL.md` -- Schnellbewertung auf Basis der Expose-Daten
- `skills/dokument-klassifizierer/SKILL.md` -- Allgemeine Dokumentklassifizierung
- `skills/mietlisten-parser/SKILL.md` -- Mietliste aus Expose weiterverarbeiten
