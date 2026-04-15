# Nebenkosten-Pruefer -- Nebenkostenabrechnung validieren

## Wann nutzen

- Nebenkostenabrechnung vor Versand an Mieter pruefen
- Abrechnung vom Verwalter oder WEG auf Fehler kontrollieren
- Umlagefaehigkeit einzelner Kostenpositionen pruefen (BetrKV)
- Heizkosten-Verteilung auf Compliance mit HeizKV pruefen
- Vorauszahlungsanpassung fuer die naechste Periode berechnen
- Einwendungen von Mietern gegen die Abrechnung bewerten

---

## Inputs

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `billing_statement` | Object/Text | Ja | Nebenkostenabrechnung (strukturiert oder als Text/PDF-Extrakt) |
| `billing_period` | Object | Ja | Abrechnungszeitraum: `start_date`, `end_date` |
| `delivery_date` | String | Nein | Datum der Zustellung an den Mieter |
| `property_data` | Object | Nein | Objektdaten: Gesamtflaeche, Einheitenzahl, Personenzahl je Einheit |
| `unit_data` | Object | Nein | Daten der abgerechneten Einheit: Flaeche, Personenzahl, Verbrauchswerte |
| `prepayment_monthly_eur` | Number | Nein | Monatliche Nebenkostenvorauszahlung des Mieters |
| `lease_agreement_clauses` | Text | Nein | Relevante Mietvertragsklauseln zur Nebenkostenumlage |
| `previous_billing` | Object | Nein | Vorjahresabrechnung zum Vergleich |

---

## Auftrag

Du bist ein erfahrener Immobilienverwalter mit Expertise in der Nebenkostenabrechnung nach deutschem Mietrecht. Pruefe die uebergebene Abrechnung systematisch auf formelle und materielle Fehler. Beachte die Vorgaben des §556 BGB, der Betriebskostenverordnung (BetrKV) und der Heizkostenverordnung (HeizKV). Identifiziere Fehler, berechne die korrekten Werte und empfehle Korrekturen.

---

## Strategie

1. **Formelle Pruefung (§556 Abs. 3 BGB)** -- Ohne korrekte Form ist die Abrechnung unwirksam:
   - Absender und Empfaenger korrekt und vollstaendig?
   - Abrechnungszeitraum angegeben und exakt 12 Monate? (Ausnahme: Erstabrechnung bei Mietbeginn, Endabrechnung bei Mietende)
   - Abrechnungsobjekt eindeutig bezeichnet?
   - Zustellungsfrist eingehalten? Abrechnung muss innerhalb von 12 Monaten nach Ende des Abrechnungszeitraums zugehen (§556 Abs. 3 S. 2 BGB). Nach Fristablauf: keine Nachforderung moeglich, Guthaben muss trotzdem ausgezahlt werden.
   - Gesamtkosten je Position angegeben?
   - Umlageschluessel je Position angegeben und nachvollziehbar?
   - Berechnung des Mieteranteils nachvollziehbar?
   - Vorauszahlungen korrekt angerechnet?
   - Saldo (Nachzahlung/Guthaben) korrekt berechnet?

2. **Abrechnungszeitraum pruefen** -- Detail-Check:
   - Zeitraum ist exakt 12 Monate (z.B. 01.01.2025 - 31.12.2025)
   - Bei unterjaerigem Mietbeginn/-ende: anteilige Berechnung korrekt (tagesgenau)?
   - Kein Ueberlappen mit vorheriger Abrechnung
   - Alle Kostenpositionen beziehen sich auf den Abrechnungszeitraum (keine periodfremden Kosten)

3. **Umlagefaehigkeit pruefen (BetrKV §1-2)** -- Jede Kostenposition gegen die Betriebskostenverordnung pruefen:

   | Umlagefaehig (BetrKV §2) | Nicht umlagefaehig |
   |--------------------------|-------------------|
   | Grundsteuer | Verwaltungskosten |
   | Wasserversorgung | Instandhaltung / Reparaturen |
   | Entwasserung | Instandsetzung |
   | Heizung | Bankgebuehren |
   | Warmwasser | Leerstandskosten (traegt Vermieter) |
   | Aufzug | Mietausfallversicherung |
   | Strassenreinigung | Rechtsschutzversicherung |
   | Muellabfuhr | Porto / Telefonkosten des Verwalters |
   | Hausreinigung | Einmalige Kosten (keine laufenden Betriebskosten) |
   | Gartenpflege | |
   | Allgemeinbeleuchtung | |
   | Schornsteinfeger | |
   | Sach-/Haftpflichtversicherung | |
   | Hauswart (nur Betriebskosten-Anteil) | |
   | Gemeinschaftsantenne / Kabel | |
   | Wascheinrichtung | |
   | Sonstige (nur wenn im Mietvertrag vereinbart) | |

4. **Umlageschluessel validieren** -- Pruefen ob der verwendete Schluessel zulaessig und korrekt angewendet ist:
   - Nach Wohnflaeche (qm): Mieteranteil = Wohnflaeche Einheit / Gesamtwohnflaeche
   - Nach Personenzahl: Mieteranteil = Personen in Einheit / Gesamtpersonenzahl
   - Nach Einheiten: Mieteranteil = 1 / Anzahl Einheiten
   - Nach Verbrauch: individuelle Zaehler erforderlich
   - Stimmt der verwendete Schluessel mit dem Mietvertrag ueberein?
   - Ist der Schluessel fuer die jeweilige Kostenart sachgerecht?
   - Aenderung des Umlageschluessels nur unter bestimmten Voraussetzungen zulaessig

5. **Heizkosten-Verordnung (HeizKV) pruefen** -- Spezialregeln fuer Heiz- und Warmwasserkosten:
   - Verbrauchsabhaengiger Anteil: mindestens 50%, maximal 70% (§7 HeizKV)
   - Grundkostenanteil: 30% - 50% (nach Flaeche)
   - Verbrauchserfassung korrekt? (Heizkostenverteiler, Waermemengenzaehler)
   - Warmwasserkostenberechnung nach §9 HeizKV (Formel: Warmwasseranteil = 2,5 x V x (tw - 10) / Brennstoffverbrauch gesamt)
   - Rohrwaermeabzug beruecksichtigt?
   - Bei fehlender Verbrauchserfassung: Kuerzungsrecht des Mieters um 15% (§12 HeizKV)

6. **Rechnerische Pruefung** -- Jede Berechnung nachrechnen:
   - Gesamtkosten x Umlageschluessel = Mieteranteil (pro Position)
   - Summe aller Mieteranteile = Gesamtbetriebskosten Mieter
   - Gesamtbetriebskosten Mieter - geleistete Vorauszahlungen = Nachzahlung/Guthaben
   - Vorauszahlungen: 12 x monatliche Vorauszahlung (bei 12 Monaten Abrechnungszeitraum)
   - Rundungsdifferenzen pruefen (maximal wenige Cent)

7. **Vergleich mit Vorjahr** -- Falls Vorjahresabrechnung vorliegt:
   - Kostensteigerungen > 10% je Position identifizieren
   - Neue Positionen pruefen (waren sie im Mietvertrag vereinbart?)
   - Weggefallene Positionen pruefen
   - Plausibilitaetscheck: Sind Steigerungen erklaerbar (Energiepreise, Versicherung)?

8. **Vorauszahlungsanpassung berechnen** -- Neue monatliche Vorauszahlung empfehlen:
   - Basis: Tatsaechliche Kosten des abgelaufenen Zeitraums / 12
   - Aufschlag fuer erwartete Kostensteigerungen (optional, max. 10-15%)
   - Anpassungsrecht: §560 BGB -- Anpassung nach jeder Abrechnung zulaessig
   - Anpassungsbetrag berechnen und begruenden

9. **Fehler-Report erstellen** -- Alle Befunde strukturiert dokumentieren:
   - Schwere Fehler (formell unwirksam, falsche Betraege)
   - Mittlere Fehler (falsche Umlageschluessel, nicht umlagefaehige Kosten)
   - Leichte Fehler (Rundungsdifferenzen, fehlende Angaben)
   - Korrekturempfehlung je Fehler

---

## Ausgabeformat

```json
{
  "report_type": "nebenkosten_pruefung",
  "report_date": "2026-04-15",
  "billing_period": {
    "start": "2025-01-01",
    "end": "2025-12-31",
    "duration_months": 12,
    "duration_valid": true
  },
  "delivery_check": {
    "delivery_date": "2026-04-10",
    "deadline_date": "2026-12-31",
    "within_deadline": true,
    "days_remaining": 265
  },
  "property": "Musterstr. 12, 10115 Berlin",
  "unit": "WE 04",
  "tenant": "Nachname, Vorname",
  "formal_check": {
    "passed": true,
    "issues": []
  },
  "cost_positions": [
    {
      "position": "Grundsteuer",
      "total_cost_eur": 4800.00,
      "allocation_key": "wohnflaeche",
      "unit_share": 0.125,
      "tenant_share_eur": 600.00,
      "allocable": true,
      "betrkv_reference": "§2 Nr. 1 BetrKV",
      "calculation_correct": true,
      "issues": []
    },
    {
      "position": "Verwaltungskosten",
      "total_cost_eur": 3600.00,
      "allocation_key": "einheiten",
      "unit_share": 0.0833,
      "tenant_share_eur": 300.00,
      "allocable": false,
      "betrkv_reference": "nicht in §2 BetrKV enthalten",
      "calculation_correct": true,
      "issues": [
        {
          "severity": "schwer",
          "description": "Verwaltungskosten sind nicht umlagefaehig (§1 Abs. 2 Nr. 1 BetrKV)",
          "correction": "Position streichen, Mieteranteil um 300,00 EUR reduzieren"
        }
      ]
    }
  ],
  "heating_check": {
    "consumption_share_percent": 60,
    "base_share_percent": 40,
    "heizkv_compliant": true,
    "consumption_recording_method": "heizkostenverteiler",
    "warm_water_separated": true,
    "issues": []
  },
  "calculation_summary": {
    "total_costs_billed_eur": 2400.00,
    "total_costs_corrected_eur": 2100.00,
    "prepayments_eur": 1800.00,
    "balance_billed_eur": 600.00,
    "balance_corrected_eur": 300.00,
    "difference_eur": -300.00,
    "overpayment_by_tenant_eur": 300.00
  },
  "prepayment_adjustment": {
    "current_monthly_eur": 150.00,
    "recommended_monthly_eur": 175.00,
    "adjustment_eur": 25.00,
    "basis": "Tatsaechliche Kosten 2025 zzgl. 5% Puffer fuer Kostensteigerungen",
    "legal_basis": "§560 BGB"
  },
  "year_over_year_comparison": {
    "total_costs_previous_year_eur": 2000.00,
    "total_costs_current_year_eur": 2100.00,
    "change_percent": 5.0,
    "significant_changes": [
      {
        "position": "Heizkosten",
        "previous_eur": 800.00,
        "current_eur": 960.00,
        "change_percent": 20.0,
        "plausible": true,
        "explanation": "Energiepreissteigerung"
      }
    ]
  },
  "errors_found": {
    "critical": 1,
    "moderate": 0,
    "minor": 0,
    "total": 1,
    "errors": [
      {
        "severity": "schwer",
        "position": "Verwaltungskosten",
        "description": "Nicht umlagefaehige Kosten abgerechnet",
        "financial_impact_eur": -300.00,
        "correction": "Position aus Abrechnung entfernen"
      }
    ]
  },
  "overall_result": {
    "status": "fehlerhaft",
    "action_required": "Abrechnung korrigieren und erneut zustellen",
    "financial_impact_tenant_eur": -300.00
  },
  "confidence_score": 0.88,
  "data_gaps": [
    "Mietvertragsklauseln zur Umlage nicht vorhanden -- Umlageschluessel-Pruefung basiert auf gesetzlicher Standardregelung"
  ]
}
```

---

## Qualitaetspruefung

- [ ] Abrechnungszeitraum ist exakt 12 Monate (oder begruendet abweichend)
- [ ] Zustellungsfrist (12 Monate nach Abrechnungsende) korrekt berechnet
- [ ] Jede Kostenposition gegen BetrKV §2 geprueft
- [ ] Umlageschluessel-Berechnung stimmt (Mieteranteil = Einheit / Gesamt)
- [ ] Heizkosten: verbrauchsabhaengiger Anteil zwischen 50% und 70%
- [ ] Alle Rechenoperationen nachgeprueft (keine Rundungsfehler > 1 EUR)
- [ ] Vorauszahlungen korrekt angerechnet (Anzahl Monate x Monatsbetrag)
- [ ] Saldo (Nachzahlung/Guthaben) arithmetisch korrekt
- [ ] Nicht umlagefaehige Kosten erkannt und beanstandet
- [ ] Vorauszahlungsanpassung auf Basis tatsaechlicher Kosten berechnet

---

## Warnsignale

| Signal | Bedeutung | Empfohlene Aktion |
|--------|-----------|-------------------|
| Zustellungsfrist < 30 Tage | Fristversaeumnis droht, Nachforderung verfaellt | Sofort zustellen (nachweisbar: Einschreiben oder Bote) |
| Zustellungsfrist abgelaufen | Keine Nachforderung mehr moeglich | Guthaben auszahlen, keine Nachforderung stellen |
| Verwaltungskosten umgelegt | Nicht umlagefaehig nach BetrKV | Position entfernen, Abrechnung korrigieren |
| Heizkosten 100% nach Flaeche | HeizKV-Verstoss, Kuerzungsrecht 15% | Verbrauchserfassung installieren oder korrekten Split anwenden |
| Reparaturkosten in NK | Instandhaltung ist nicht umlagefaehig | Position entfernen |
| Kostenposition > 30% Steigerung zum Vorjahr | Ungewoehnlich, Mieter wird nachfragen | Steigerung begruenden oder Beleg pruefen |
| Leerstandskosten auf Mieter umgelegt | Leerstandsrisiko traegt der Vermieter | Leerstandsanteil herausrechnen |

---

## Bei fehlenden Daten

- Wenn kein Mietvertrag vorliegt: Gesetzliche Umlageschluessel annehmen (Wohnflaeche), als Annahme kennzeichnen.
- Wenn Gesamtflaeche fehlt: Umlageschluessel-Berechnung nicht moeglich, Fehler melden und Daten anfordern.
- Wenn kein Zustellungsdatum vorliegt: Fristpruefung ueberspringen, Hinweis geben dass Zustellung nachweisbar erfolgen muss.
- Wenn keine Vorjahresabrechnung vorliegt: Vergleich ueberspringen, Positionen einzeln auf Plausibilitaet pruefen.
- Wenn Verbrauchsdaten fuer Heizkosten fehlen: HeizKV-Pruefung als "nicht pruefbar" kennzeichnen.
- Alle Luecken im Feld `data_gaps` dokumentieren.

---

## Konfidenz-Bewertung

| Score | Bedeutung |
|-------|-----------|
| 0.9 - 1.0 | Vollstaendige Abrechnung mit Mietvertrag, Objektdaten, Verbrauchswerten und Vorjahresvergleich |
| 0.7 - 0.9 | Abrechnung vollstaendig, aber Mietvertrag oder Vorjahr fehlen |
| 0.5 - 0.7 | Abrechnung unvollstaendig, einzelne Positionen nicht pruefbar |
| < 0.5 | Wesentliche Daten fehlen, Pruefung nur oberflaechlich moeglich |

Faktoren die den Score senken:
- Fehlende Mietvertragsklauseln zur Umlage (-0.10)
- Fehlende Gesamtflaeche / Einheitenzahl (-0.15)
- Keine Verbrauchsdaten fuer Heizkosten (-0.10)
- Kein Zustellungsdatum (-0.05)
- Keine Vorjahresabrechnung (-0.05)

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- §556 BGB, BetrKV, HeizKV: Nebenkostenrecht im Detail
- `knowledge/checklisten.md` -- Checkliste Nebenkostenabrechnung
- `skills/verwaltung/wochen-jourfixe.md` -- NK-Abrechnungsfristen im Wochen-Report
- `skills/verwaltung/mahn-assistent.md` -- Nachforderungen aus NK-Abrechnung als Forderung tracken
