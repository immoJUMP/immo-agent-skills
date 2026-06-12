---
name: mietlisten-parser
description: "Extrahiert und strukturiert Mietlisten-Daten (Mieter, Flaeche, Miete, Vertragsdaten) in einheitliches Format. Nutze diesen Skill bei Kaufpruefung, Objektuebernahme, Quartalscheck oder Aufbereitung fuers Bankkonzept."
---

# Mietlisten-Parser

> Strukturierte Daten aus Mietlisten-PDFs, Excel-Exporten und gescannten Dokumenten extrahieren -- einheitlich, vollstaendig und sofort weiterverarbeitbar.

---

## Wann nutzen?

- Bei Ankaufspruefung: Mietliste des Verkaeufers analysieren und validieren
- Bei Uebernahme: Bestandsmietliste digitalisieren
- Quartalsweise: Aktuelle Mietliste aus Verwaltungssoftware pruefen
- Fuer Bankenpitch: Mieteinnahmen strukturiert aufbereiten

---

## Inputs

Stelle folgende Informationen bereit:

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| `mietliste` | Ja | Mietliste als PDF, Excel, CSV oder Scan |
| `objekt` | Empfohlen | Adresse und Eckdaten des Objekts |
| `stichtag` | Empfohlen | Stichtag der Mietliste (z.B. 01.01.2025) |
| `mietspiegel_median` | Optional | Ortsuebliche Vergleichsmiete (EUR/qm kalt) fuer Potenzialanalyse |
| `format_hinweis` | Optional | Hinweise zum Format (z.B. "Hausverwaltung XY Standardformat") |

---

## Auftrag

Du bist ein erfahrener Immobilienanalyst. Extrahiere aus der uebergebenen Mietliste alle relevanten Daten pro Einheit in ein einheitliches, strukturiertes Format. Berechne Kennzahlen, pruefe die Datenqualitaet und weise auf Auffaelligkeiten hin. Die Ausgabe muss sofort fuer Deal-Screening, Bankenpitch und Steuererklaerung verwendbar sein.

---

## Strategie

1. **Format erkennen und Struktur analysieren**
   - PDF-Tabelle (strukturiert, aus Software exportiert)
   - Excel/CSV-Export (Spaltenstruktur erkennen)
   - Gescanntes Dokument (OCR-Qualitaet bewerten)
   - Freitextformat (z.B. Makler-Email mit Mietdaten)
   - Spaltenueberschriften identifizieren und zuordnen
   - Synonyme erkennen (z.B. "Nettokaltmiete" = "Kaltmiete" = "Grundmiete" = "NK-Miete")

2. **Daten pro Einheit extrahieren**
   - **Einheit:** Bezeichnung (WE 1, Laden EG, Garage 1, etc.)
   - **Lage:** Geschoss, links/rechts/mitte
   - **Nutzungsart:** Wohnung, Gewerbe, Buero, Laden, Garage, Stellplatz, Keller, Sonstiges
   - **Mieter:** Name (anonymisieren wenn gewuenscht)
   - **Wohnflaeche / Nutzflaeche:** qm
   - **Zimmer:** Anzahl Zimmer
   - **Kaltmiete:** EUR/Monat (Nettokaltmiete)
   - **Nebenkosten-Vorauszahlung:** EUR/Monat
   - **Heizkosten-Vorauszahlung:** EUR/Monat (wenn separat ausgewiesen)
   - **Gesamtmiete:** EUR/Monat (Bruttowarmmiete)
   - **Miete pro qm:** EUR/qm kalt (berechnet)
   - **Mietbeginn:** Datum des Mietvertrags
   - **Letzte Mieterhoehung:** Datum und Betrag
   - **Befristung:** Befristungsende (falls vorhanden)
   - **Kaution:** Hoehe der hinterlegten Kaution
   - **Besonderheiten:** Staffelmiete, Indexmiete, Gewerbe-USt, Mietrueckstand, Eigennutzung

3. **Leerstand erfassen**
   - Leerstehende Einheiten identifizieren
   - Leerstand seit wann (wenn angegeben)
   - Grund fuer Leerstand (Sanierung, Mieterwechsel, Dauerleerstand)
   - Marktmiete fuer leerstehende Einheiten schaetzen (wenn Mietspiegel vorhanden)

4. **Kennzahlen berechnen**
   - Gesamtflaeche (Wohnen + Gewerbe + Sonstiges)
   - Jahresnettokaltmiete (Ist-Miete)
   - Jahresnettokaltmiete (Soll-Miete, inkl. Marktmiete fuer Leerstand)
   - Durchschnittsmiete EUR/qm (gesamt und nach Nutzungsart)
   - Leerstandsquote (Flaeche und Anzahl Einheiten)
   - Mietausfallwagnis (geschaetzt bei Mietrueckstand)
   - Mietpotenzial (Differenz Ist-Miete zu Marktmiete, wenn Mietspiegel vorhanden)
   - WALT (Weighted Average Lease Term) bei Gewerbemietern

5. **Datenqualitaet pruefen**
   - Summen pruefen: Kaltmiete + NK = Gesamtmiete?
   - Flaechen plausibel? (z.B. 15 qm Wohnung oder 300 qm Wohnung)
   - Miete pro qm plausibel? (z.B. unter 3 EUR oder ueber 20 EUR fuer Wohnung)
   - Alle Einheiten erfasst? (Luecken in Nummerierung?)
   - Doppelte Einheiten?
   - Fehlende Pflichtfelder markieren
   - Formatfehler (z.B. Datum als Text, Betrag mit Punkt statt Komma)

---

## Ausgabeformat

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext.

**Weitergabe an Folge-Skills:** Werden die extrahierten Daten fuer einen Folge-Skill gebraucht (z.B. Deal-Screening, Bankenpitch, Steuer), dann schreibe die strukturierten Daten zusaetzlich als DATEI -- z.B. eine JSON- oder CSV-Datei neben dem Quelldokument (etwa `mietliste-musterstrasse-12.json`). Gib diese strukturierten Daten niemals im Chat aus; nenne im Bericht nur den Dateipfad, unter dem die Datei abgelegt wurde.

Liefere die Ergebnisse im Chat in folgendem Format:

### Ergebnisbericht

```markdown
# Mietliste: Musterstrasse 12, 40210 Duesseldorf

**Objekt-ID:** OBJ-001 | **Stichtag:** 01.01.2025 |
**Quelle:** PDF Hausverwaltung ABC GmbH | **Datenqualitaet:** gut

## Mietliste

| Einheit | Lage | Nutzung | Zimmer | qm | Mieter | Kaltmiete | EUR/qm | NK-VZ | Heizk.-VZ | Gesamtmiete | Kaltmiete p.a. | Status |
|---------|------|---------|--------|-----|--------|-----------|--------|-------|-----------|-------------|----------------|--------|
| WE 1 | EG links | Wohnung | 3 | 72,50 | Schmidt, Thomas | 520,00 | 7,17 | 180,00 | 80,00 | 780,00 | 6.240,00 | 🟢 vermietet |
| WE 5 | 2.OG rechts | Wohnung | 2 | 55,00 | -- | 0,00 | -- | -- | -- | 0,00 | 0,00 | 🔴 Leerstand |
| Garage 1 | UG | Garage | -- | 15,00 | Schmidt, Thomas | 60,00 | 4,00 | -- | -- | 60,00 | 720,00 | 🟢 vermietet |

## Vertragsdetails

| Einheit | Mietbeginn | Vertragstyp | Letzte Erhoehung | Index / Staffel | Kaution | Rueckstand | Anmerkung |
|---------|------------|-------------|------------------|-----------------|---------|------------|-----------|
| WE 1 | 01.04.2019 | unbefristet | 01.07.2022 (+35,00 EUR) | nein / nein | 1.560,00 EUR (Barkaution) | 0,00 EUR | -- |
| WE 5 | -- | -- | -- | -- | -- | -- | Leer seit 01.11.2024 (Mieterwechsel). Renovierung abgeschlossen, Neuvermietung ab sofort moeglich. Geschaetzte Marktmiete 8,50 EUR/qm = 467,50 EUR/Monat. |
| Garage 1 | 01.04.2019 | unbefristet | -- | -- | -- | 0,00 EUR | Separat vermietet -- USt-pflichtig beachten |

## Summen

| Kennzahl | Wert |
|----------|------|
| Einheiten gesamt | 8 (6 Wohnungen, 0 Gewerbe, 2 Garagen) |
| Flaeche gesamt | 425,00 qm (davon Wohnen 395,00 qm) |
| Vermietet / Leerstand | 7 / 1 Einheiten |
| Leerstandsquote (Einheiten) | 12,5% |
| Leerstandsquote (Flaeche) | 12,9% |
| Ist-Kaltmiete monatlich | 3.420,00 EUR |
| Ist-Kaltmiete jaehrlich | 41.040,00 EUR |
| Potenzial-Kaltmiete monatlich | 3.887,50 EUR |
| Potenzial-Kaltmiete jaehrlich | 46.650,00 EUR |
| Durchschnittsmiete Wohnen | 7,85 EUR/qm |
| Durchschnittsmiete gesamt | 8,05 EUR/qm |
| NK-Vorauszahlungen monatlich | 1.080,00 EUR (12.960,00 EUR p.a.) |
| Bruttomiete monatlich | 4.500,00 EUR (54.000,00 EUR p.a.) |
| Kautionen gesamt | 9.360,00 EUR |
| Rueckstaende gesamt | 0,00 EUR |
| Upside-Potenzial | 467,50 EUR/Monat = 5.610,00 EUR/Jahr (+13,7%) |

## Mietverteilung

| Mietniveau | Einheiten | Flaeche |
|------------|-----------|---------|
| unter 5 EUR/qm | 0 | 0,00 qm |
| 5-7 EUR/qm | 1 | 85,00 qm |
| 7-9 EUR/qm | 4 | 255,00 qm |
| 9-11 EUR/qm | 0 | 0,00 qm |
| ueber 11 EUR/qm | 0 | 0,00 qm |

## Auffaelligkeiten

- ℹ️ **WE 3:** Miete 5,80 EUR/qm liegt deutlich unter Durchschnitt (7,85 EUR/qm)
  -- Mieterhoehungspotenzial?
- ℹ️ **Garage 1:** Separat vermietete Garage -- USt-Pflicht pruefen
  (§4 Nr.12 S.2 UStG)

## Strukturierte Daten fuer Folge-Skills

Datei abgelegt unter: `./mietliste-musterstrasse-12.json`
(nur falls Daten fuer einen Folge-Skill gebraucht werden)
```

---

## Qualitaetspruefung

Vor der Ausgabe pruefen:

- [ ] Alle Einheiten aus dem Quelldokument sind erfasst (keine Luecken)
- [ ] Summen stimmen: Einzel-Kaltmieten = Gesamt-Kaltmiete
- [ ] Kaltmiete + NK = Gesamtmiete (pro Einheit)
- [ ] Flaechen sind plausibel (keine negativen Werte, keine unrealistischen Groessen)
- [ ] Mieten pro qm sind plausibel (Ausreisser sind markiert)
- [ ] Leerstand ist korrekt erfasst (Einheiten mit 0 EUR Miete = Leerstand)
- [ ] Jahresnettokaltmiete = Monatswert x 12 (bzw. anteilig bei Mietbeginn im Jahr)
- [ ] Datenqualitaets-Flags sind gesetzt bei Auffaelligkeiten

---

## Warnsignale

| Signal | Bedeutung | Aktion |
|--------|-----------|--------|
| Hoher Leerstand (> 10%) | Vermietungsprobleme moeglich | Ursache klaeren (Lage, Zustand, Mietniveau) |
| Sehr niedrige Mieten (< 5 EUR/qm) | Entweder Potenzial oder schlechte Lage | Mit Mietspiegel vergleichen |
| Sehr hohe Mieten (> 12 EUR/qm B/C-Lage) | Moeglicherweise nicht nachhaltig | Marktmiete gegenchecken |
| Mietrueckstaende | Liquiditaetsrisiko | Mahnwesen pruefen, bei Ankauf: Kalkulation anpassen |
| Alle Mieter kuerzlich eingezogen | Moeglicherweise kuenstlich erhoehte Mieten vor Verkauf | Kritisch hinterfragen |
| Fehlende Mietbeginn-Daten | Mietdauer und Kuendigungsfristen unklar | Mietvertraege anfordern |
| Identische Mieten bei unterschiedlichen Groessen | Datenfehler wahrscheinlich | Quelldokument erneut pruefen |
| Summe Einheiten ≠ Teilungserklaerung | Einheiten fehlen oder wurden zusammengelegt | Mit Teilungserklaerung abgleichen |
| Gewerbemieter ohne Indexklausel | Mietanpassung eingeschraenkt | Mietvertrag pruefen |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Miete pro qm | Aus Kaltmiete und Flaeche berechnen |
| Gesamtmiete | Aus Kaltmiete + NK + Heizkosten-VZ berechnen |
| NK-Vorauszahlung | Als "nicht angegeben" markieren, Gesamtmiete nicht berechenbar |
| Mietbeginn | Als "unbekannt" markieren, Hinweis auf fehlende Information |
| Flaeche einzelner Einheiten | Summe pruefen, ggf. aus Teilungserklaerung ergaenzen |
| Mietspiegel | Potenzialberechnung als "nicht moeglich" markieren |
| Leerstandsgrund | Als "Grund unbekannt" markieren |
| Kaution | Als "nicht angegeben" markieren |

---

## Konfidenz-Bewertung

| Stufe | Wert | Bedeutung |
|-------|------|-----------|
| Hoch | >= 0.90 | Alle Daten eindeutig extrahiert, Summen plausibel |
| Mittel | 0.70 - 0.89 | Ueberwiegend korrekt, einzelne Felder unklar oder geschaetzt |
| Niedrig | 0.50 - 0.69 | Mehrere Felder unklar, OCR-Qualitaet eingeschraenkt |
| Unsicher | < 0.50 | Daten nicht zuverlaessig extrahierbar, manuelle Erfassung empfohlen |

---

## Verwandte Wissensdatenbanken

- `knowledge/marktbenchmarks.md` -- Vergleichsmieten nach Lage und Baujahr
- `knowledge/kalkulationsformeln.md` -- Renditeberechnung auf Basis der Mietliste
- `skills/deal-screener/SKILL.md` -- Deal-Screening mit extrahierten Mietdaten
- `skills/mieterhoehung/SKILL.md` -- Mieterhoehungspotenzial berechnen
- `skills/mahn-assistent/SKILL.md` -- Mietrueckstaende weiterverarbeiten

