# Mietlisten-Parser

> Strukturierte Daten aus Mietlisten-PDFs, Excel-Exporten und gescannten Dokumenten extrahieren -- einheitlich, vollstaendig und sofort weiterverarbeitbar.

---

## Wann nutzen?

- Bei Ankaufspruefung: Mietliste des Verkaeufers analysieren und validieren
- Bei Uebernahme: Bestandsmietliste digitalisieren
- Quartalsweise: Aktuelle Mietliste aus Verwaltungssoftware pruefen
- Fuer Bankenkonzept: Mieteinnahmen strukturiert aufbereiten

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

Du bist ein erfahrener Immobilienanalyst. Extrahiere aus der uebergebenen Mietliste alle relevanten Daten pro Einheit in ein einheitliches, strukturiertes Format. Berechne Kennzahlen, pruefe die Datenqualitaet und weise auf Auffaelligkeiten hin. Die Ausgabe muss sofort fuer Deal-Screening, Bankenkonzept und Steuererklaerung verwendbar sein.

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

```json
{
  "rent_roll": {
    "property": {
      "property_id": "OBJ-001",
      "address": "Musterstrasse 12, 40210 Duesseldorf",
      "reference_date": "2025-01-01",
      "data_source": "PDF Hausverwaltung ABC GmbH",
      "data_quality": "gut"
    },
    "units": [
      {
        "unit_id": "WE-01",
        "unit_label": "WE 1",
        "floor": "EG",
        "position": "links",
        "usage_type": "wohnung",
        "rooms": 3,
        "area_sqm": 72.50,
        "tenant": {
          "name": "Schmidt, Thomas",
          "anonymized": false
        },
        "rent": {
          "cold_rent_monthly": 520.00,
          "cold_rent_per_sqm": 7.17,
          "utility_prepayment_monthly": 180.00,
          "heating_prepayment_monthly": 80.00,
          "total_rent_monthly": 780.00,
          "cold_rent_annual": 6240.00
        },
        "lease": {
          "lease_start": "2019-04-01",
          "lease_type": "unbefristet",
          "lease_end": null,
          "last_increase_date": "2022-07-01",
          "last_increase_amount": 35.00,
          "index_clause": false,
          "graduated_rent": false
        },
        "deposit": {
          "amount": 1560.00,
          "type": "barkaution"
        },
        "status": "vermietet",
        "arrears": 0.00,
        "notes": ""
      },
      {
        "unit_id": "WE-05",
        "unit_label": "WE 5",
        "floor": "2.OG",
        "position": "rechts",
        "usage_type": "wohnung",
        "rooms": 2,
        "area_sqm": 55.00,
        "tenant": null,
        "rent": {
          "cold_rent_monthly": 0.00,
          "cold_rent_per_sqm": 0.00,
          "utility_prepayment_monthly": 0.00,
          "heating_prepayment_monthly": 0.00,
          "total_rent_monthly": 0.00,
          "cold_rent_annual": 0.00,
          "estimated_market_rent_per_sqm": 8.50,
          "estimated_market_rent_monthly": 467.50
        },
        "lease": {
          "lease_start": null,
          "lease_type": null,
          "lease_end": null
        },
        "deposit": null,
        "status": "leerstand",
        "vacancy_since": "2024-11-01",
        "vacancy_reason": "mieterwechsel",
        "notes": "Renovierung abgeschlossen, Neuvermietung ab sofort moeglich"
      },
      {
        "unit_id": "GAR-01",
        "unit_label": "Garage 1",
        "floor": "UG",
        "position": null,
        "usage_type": "garage",
        "rooms": null,
        "area_sqm": 15.00,
        "tenant": {
          "name": "Schmidt, Thomas",
          "anonymized": false
        },
        "rent": {
          "cold_rent_monthly": 60.00,
          "cold_rent_per_sqm": 4.00,
          "utility_prepayment_monthly": 0.00,
          "heating_prepayment_monthly": 0.00,
          "total_rent_monthly": 60.00,
          "cold_rent_annual": 720.00
        },
        "lease": {
          "lease_start": "2019-04-01",
          "lease_type": "unbefristet"
        },
        "deposit": null,
        "status": "vermietet",
        "notes": "Separat vermietet -- USt-pflichtig beachten"
      }
    ],
    "summary": {
      "total_units": 8,
      "residential_units": 6,
      "commercial_units": 0,
      "garage_units": 2,
      "total_area_sqm": 425.00,
      "residential_area_sqm": 395.00,
      "occupied_units": 7,
      "vacant_units": 1,
      "vacancy_rate_units_percent": 12.5,
      "vacancy_rate_area_percent": 12.9,
      "actual_cold_rent_monthly": 3420.00,
      "actual_cold_rent_annual": 41040.00,
      "potential_cold_rent_monthly": 3887.50,
      "potential_cold_rent_annual": 46650.00,
      "average_rent_per_sqm_residential": 7.85,
      "average_rent_per_sqm_all": 8.05,
      "total_utility_prepayments_monthly": 1080.00,
      "total_utility_prepayments_annual": 12960.00,
      "total_gross_rent_monthly": 4500.00,
      "total_gross_rent_annual": 54000.00,
      "total_deposits": 9360.00,
      "total_arrears": 0.00,
      "upside_potential_monthly": 467.50,
      "upside_potential_annual": 5610.00,
      "upside_potential_percent": 13.7
    },
    "rent_distribution": {
      "below_5_eur": { "count": 0, "area_sqm": 0.00 },
      "5_to_7_eur": { "count": 1, "area_sqm": 85.00 },
      "7_to_9_eur": { "count": 4, "area_sqm": 255.00 },
      "9_to_11_eur": { "count": 0, "area_sqm": 0.00 },
      "above_11_eur": { "count": 0, "area_sqm": 0.00 }
    },
    "data_quality_flags": [
      {
        "unit_id": "WE-03",
        "flag_type": "low_rent",
        "severity": "info",
        "message": "Miete 5.80 EUR/qm liegt deutlich unter Durchschnitt (7.85 EUR/qm) -- Mieterhoehungspotenzial?"
      },
      {
        "unit_id": "GAR-01",
        "flag_type": "ust_relevant",
        "severity": "info",
        "message": "Separat vermietete Garage -- USt-Pflicht pruefen (§4 Nr.12 S.2 UStG)"
      }
    ]
  }
}
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
- `skills/ankauf/deal-screener.md` -- Deal-Screening mit extrahierten Mietdaten
- `skills/vermietung/mieterhoehung.md` -- Mieterhoehungspotenzial berechnen
- `skills/verwaltung/mahn-assistent.md` -- Mietrueckstaende weiterverarbeiten
- `skills/buchhaltung/anlage-v-assistent.md` -- Mieteinnahmen fuer Steuererklaerung
