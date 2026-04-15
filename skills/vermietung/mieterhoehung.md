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
   - Ankuendigung 3 Monate vor Beginn der Massnahme erforderlich (§555c BGB)

7. **Staffelmiete / Indexmiete analysieren** -- Sonderregelungen:
   - Staffelmiete (§557a BGB): Feste Erhoehungsstufen im Vertrag. Keine zusaetzliche Erhoehung nach §558 moeglich.
   - Indexmiete (§557b BGB): Kopplung an Verbraucherpreisindex. Erhoehung nur bei Indexsteigerung, Berechnung: (neuer Index / alter Index - 1) x aktuelle Miete.
   - Pruefen: Ist eine Umstellung sinnvoll? (z.B. bei stark steigenden Mietspiegeln: Staffelmiete kann nachteilig sein)

8. **Potenzialanalyse pro Einheit** -- Fuer jede Einheit berechnen:
   - Delta: Vergleichsmiete (EUR/qm) minus Ist-Miete (EUR/qm)
   - Erhoehungspotenzial EUR/Monat: Delta x Wohnflaeche
   - Erhoehungspotenzial EUR/Jahr: Monatswert x 12
   - Durch Kappungsgrenze begrenztes Potenzial (was ist JETZT moeglich?)
   - Fruehester Erhoehungszeitpunkt (Sperrfrist beachten)

9. **Prioritaetenliste erstellen** -- Einheiten sortieren nach:
   - Hoechstes Delta EUR/Monat (groesster finanzieller Effekt zuerst)
   - Sofort umsetzbar (Sperrfrist abgelaufen, keine Staffelmiete)
   - Geringes Streitrisiko (Erhoehung deutlich innerhalb Mietspiegel-Spanne)
   - Ergebnis: Rangliste mit Top-10 oder Top-20 Einheiten fuer sofortige Erhoehung

10. **Portfolio-Gesamtpotenzial berechnen** -- Aggregation:
    - Summe aller Erhoehungspotenziale EUR/Jahr (gesamt)
    - Davon sofort umsetzbar (Sperrfrist abgelaufen)
    - Davon in den naechsten 12 Monaten umsetzbar
    - Beispiel: 100 Einheiten x 50 EUR/Monat Durchschnitt = 60.000 EUR/Jahr

11. **Mieterhoehungsschreiben generieren** -- Formelle Anforderungen (§558a BGB):
    - Schriftform (Textform genuegt, §558a Abs. 1 BGB)
    - Begruendung: Verweis auf qualifizierten Mietspiegel ODER mindestens 3 Vergleichswohnungen ODER Sachverstaendigengutachten
    - Konkrete Angabe der neuen Miete (EUR/qm und EUR gesamt)
    - Wirksamkeit: ab dem dritten Kalendermonat nach Zugang
    - Zustimmungsfrist: bis zum Ablauf des zweiten Kalendermonats nach Zugang
    - Hinweis auf Zustimmungspflicht und Klagemoeglichkeit (§558b BGB)
    - Hoeflich und sachlich formuliert

12. **Timeline erstellen** -- Wann kann die naechste Erhoehung je Einheit erfolgen?
    - Fruehester Zugang des Schreibens
    - Zustimmungsfrist (2 Monate nach Zugang)
    - Wirksamkeit der neuen Miete (3. Monat nach Zugang)
    - Naechste Erhoehung moeglich (15 Monate nach dieser Erhoehung)

---

## Ausgabeformat

```json
{
  "report_type": "mieterhoehung_analyse",
  "report_date": "2026-04-15",
  "market_area": "Berlin",
  "mietpreisbremse_active": true,
  "kappungsgrenze_percent": 15,
  "mietspiegel_source": "Berliner Mietspiegel 2025, qualifiziert",
  "portfolio_summary": {
    "total_units": 100,
    "units_with_potential": 72,
    "units_at_market_rent": 18,
    "units_above_market_rent": 2,
    "units_blocked_by_sperrfrist": 8,
    "units_staffelmiete": 5,
    "units_indexmiete": 3,
    "total_potential_monthly_eur": 4820.00,
    "total_potential_annual_eur": 57840.00,
    "immediately_actionable_units": 48,
    "immediately_actionable_annual_eur": 38400.00,
    "average_delta_per_unit_eur_month": 48.20
  },
  "unit_analysis": [
    {
      "rank": 1,
      "property": "Musterstr. 12, 10115 Berlin",
      "unit": "WE 04",
      "tenant": "Nachname, Vorname",
      "area_sqm": 72.50,
      "rooms": 3,
      "construction_year": 1965,
      "condition": "mittel",
      "location_quality": "gut",
      "current_rent_sqm_eur": 6.80,
      "current_rent_total_eur": 493.00,
      "mietspiegel_range": {
        "lower_eur_sqm": 7.20,
        "middle_eur_sqm": 8.50,
        "upper_eur_sqm": 9.80
      },
      "target_rent_sqm_eur": 8.20,
      "target_rent_total_eur": 594.50,
      "delta_sqm_eur": 1.40,
      "delta_monthly_eur": 101.50,
      "delta_annual_eur": 1218.00,
      "kappungsgrenze_check": {
        "rent_3_years_ago_eur": 460.00,
        "max_increase_eur": 69.00,
        "max_rent_after_kappung_eur": 529.00,
        "kappungsgrenze_limits_increase": true,
        "achievable_increase_eur": 36.00,
        "remaining_potential_eur": 65.50
      },
      "last_increase": {
        "date": "2024-10-01",
        "amount_eur": 33.00
      },
      "sperrfrist_until": "2026-01-01",
      "sperrfrist_expired": true,
      "earliest_effective_date": "2026-07-01",
      "contract_type": "standard",
      "actionable": true,
      "priority": "hoch",
      "recommendation": "Mieterhoehung auf 529,00 EUR (Kappungsgrenze). Verbleibendes Potenzial von 65,50 EUR in 15 Monaten realisierbar."
    }
  ],
  "modernization_surcharges": [
    {
      "property": "Musterstr. 12, 10115 Berlin",
      "measure": "Fassadendaemmung WDVS",
      "total_cost_eur": 180000.00,
      "maintenance_deduction_percent": 35,
      "modernization_cost_eur": 117000.00,
      "affected_units": 12,
      "cost_per_unit_eur": 9750.00,
      "annual_surcharge_per_unit_eur": 780.00,
      "monthly_surcharge_per_unit_eur": 65.00,
      "cap_check": {
        "current_avg_rent_sqm": 6.80,
        "max_surcharge_sqm_6_years": 3.00,
        "surcharge_sqm": 0.90,
        "within_cap": true
      }
    }
  ],
  "generated_documents": [
    {
      "type": "mieterhoehungsschreiben",
      "tenant": "Nachname, Vorname",
      "unit": "WE 04",
      "content": "--- MIETERHOEHUNGSVERLANGEN ---\n\nSehr geehrte/r Frau/Herr [Name],\n\nwir beziehen uns auf den Mietvertrag vom [Datum] ueber die Wohnung [Adresse], bestehend aus [Zimmer] Zimmern mit einer Wohnflaeche von [qm] qm.\n\nDie derzeitige Nettokaltmiete betraegt [aktuelle Miete] EUR monatlich ([EUR/qm] EUR/qm).\n\nGemaess §558 BGB verlangen wir Ihre Zustimmung zur Erhoehung der Nettokaltmiete auf [neue Miete] EUR monatlich ([neuer EUR/qm] EUR/qm) ab dem [Wirksamkeitsdatum].\n\nBegruendung:\nDie Erhoehung entspricht der ortsueblichen Vergleichsmiete gemaess dem [Mietspiegel-Name] (qualifizierter Mietspiegel). Ihre Wohnung ist einzuordnen in:\n- Baujahrsklasse: [Klasse]\n- Wohnlage: [Lage]\n- Ausstattung: [Ausstattung]\n- Mietspiegel-Spanne: [unterer Wert] bis [oberer Wert] EUR/qm\n\nDie verlangte Miete von [neuer EUR/qm] EUR/qm liegt innerhalb dieser Spanne. Die Kappungsgrenze von [15/20]% in 3 Jahren wird eingehalten.\n\nWir bitten Sie, Ihre Zustimmung bis zum [Fristdatum -- 2 Monate nach Zugang] zu erklaeren.\n\nSollten Sie der Mieterhoehung nicht zustimmen, koennen wir gemaess §558b Abs. 2 BGB innerhalb von 3 Monaten nach Ablauf der Zustimmungsfrist Klage auf Zustimmung erheben.\n\nMit freundlichen Gruessen\n[Vermieter]"
    }
  ],
  "timeline": [
    {
      "unit": "WE 04",
      "send_letter_by": "2026-04-30",
      "consent_deadline": "2026-06-30",
      "effective_date": "2026-07-01",
      "next_increase_possible": "2027-10-01"
    }
  ],
  "confidence_score": 0.90,
  "data_gaps": []
}
```

---

## Qualitaetspruefung

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

---

## Bei fehlenden Daten

- Wenn kein Mietspiegel vorliegt: Vergleichswohnungen als Alternative nutzen (mindestens 3 vergleichbare Wohnungen mit Adresse, Groesse, Ausstattung, Miete). Alternativ auf Sachverstaendigengutachten verweisen.
- Wenn letzte Mieterhoehung unbekannt: Konservativ annehmen, dass Sperrfrist noch laeuft. Mietvertragsdatum als fruehestes Erhoehungsdatum nutzen.
- Wenn Kappungsgrenze-Status (15% vs. 20%) unklar: Die strengere Grenze (15%) annehmen.
- Wenn Mietpreisbremse-Status unklar: Als aktiv annehmen und darauf hinweisen, dass die Landesverordnung geprueft werden muss.
- Wenn Baujahr oder Ausstattung unklar: Mietspiegel-Einordnung als "unsicher" kennzeichnen und Spanne angeben.
- Alle Luecken im Feld `data_gaps` dokumentieren.

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
- `skills/vermietung/inserat-generator.md` -- Bei Neuvermietung nach Kuendigung: Mietpreisbremse beachten
- `skills/verwaltung/wochen-jourfixe.md` -- Mieterhoehungsfristen im Wochen-Report tracken
