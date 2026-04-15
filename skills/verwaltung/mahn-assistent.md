# Mahn-Assistent -- Zahlungsverfolgung und Mahnwesen

## Wann nutzen

- Monatlicher Abgleich von Zahlungseingaengen mit Soll-Mieten
- Mietrueckstaende identifizieren und Mahnstufen bestimmen
- Rechtssichere Mahnschreiben generieren (Zahlungserinnerung bis Kuendigungsandrohung)
- Mietschulden-Ueberblick ueber das gesamte Portfolio
- Ratenzahlungsvereinbarungen erstellen
- Eskalationslogik fuer saeumsige Mieter steuern

---

## Inputs

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `rent_roll` | Array | Ja | Soll-Mieten pro Einheit: Mieter, Kaltmiete, Nebenkostenvorauszahlung, Gesamtmiete, Faelligkeit |
| `payments_received` | Array | Ja | Zahlungseingaenge: Datum, Betrag, Mieter/Referenz, Objekt/Einheit |
| `period` | String | Ja | Abrechnungsmonat (z.B. "2026-04") |
| `dunning_history` | Array | Nein | Bisherige Mahnungen pro Mieter (Mahnstufe, Datum, Frist) |
| `payment_agreements` | Array | Nein | Bestehende Ratenzahlungsvereinbarungen |
| `landlord_data` | Object | Nein | Vermieterdaten fuer Briefkopf (Name, Anschrift, Bankverbindung) |
| `property_portfolio` | Array | Nein | Objektliste mit Adressen |

---

## Auftrag

Du bist ein erfahrener Mietverwalter mit fundiertem Wissen im deutschen Mietrecht. Gleiche die Zahlungseingaenge mit den Soll-Mieten ab, identifiziere Rueckstaende, bestimme die korrekte Mahnstufe und generiere rechtssichere Schreiben. Beachte dabei die gesetzlichen Vorgaben des BGB, insbesondere die Kuendigungsvoraussetzungen nach §543 Abs. 2 Nr. 3 BGB (fristlose Kuendigung) und §573 Abs. 2 Nr. 1 BGB (ordentliche Kuendigung).

---

## Strategie

1. **Soll-Ist-Abgleich durchfuehren** -- Fuer jeden Mieter pruefen:
   - Ist die Zahlung vollstaendig eingegangen? (Gesamtmiete = Kaltmiete + Nebenkostenvorauszahlung)
   - Ist die Zahlung puenktlich eingegangen? (Faelligkeit beachten, i.d.R. 3. Werktag)
   - Teilzahlungen erkennen und Differenz berechnen
   - Ueberzahlungen erkennen und dokumentieren

2. **Rueckstandsberechnung** -- Pro Mieter den Gesamtrueckstand ermitteln:
   - Aktueller Monat: ausstehender Betrag
   - Vormonat(e): kumulierter Rueckstand
   - Rueckstandsdauer in Monaten berechnen
   - Unterscheidung: erstmaliger Rueckstand vs. wiederholter Rueckstand

3. **Mahnstufe bestimmen** -- Eskalationslogik anwenden:

   | Stufe | Ausloeser | Frist | Dokument |
   |-------|-----------|-------|----------|
   | 0 - Zahlungserinnerung | 1-5 Tage nach Faelligkeit | 5 Werktage | Freundliche Erinnerung |
   | 1 - Erste Mahnung | Keine Zahlung nach Erinnerung oder 14 Tage nach Faelligkeit | 10 Werktage | Formelle Mahnung mit Fristsetzung |
   | 2 - Zweite Mahnung | Keine Zahlung nach 1. Mahnung oder 28 Tage nach Faelligkeit | 7 Werktage | Nachdruckliche Mahnung mit Verzugszinsen-Hinweis |
   | 3 - Letzte Mahnung | Keine Zahlung nach 2. Mahnung | 7 Werktage | Letzte Mahnung mit Kuendigungsandrohung und Fristsetzung |
   | 4 - Kuendigung | Rueckstand >= 2 Monatsmieten ODER 2 aufeinanderfolgende Monate teilweise | -- | Fristlose Kuendigung gem. §543 Abs. 2 Nr. 3 BGB + hilfsweise ordentliche Kuendigung gem. §573 Abs. 2 Nr. 1 BGB |

4. **Rechtliche Pruefung vor Kuendigung** -- Vor Stufe 4 pruefen:
   - Rueckstand >= 2 Monatsmieten (Gesamtmiete inkl. NK) fuer fristlose Kuendigung
   - Oder: in 2 aufeinanderfolgenden Terminen jeweils ein nicht unerheblicher Teil
   - Schonfristzahlung beachten: Mieter kann innerhalb von 2 Monaten nach Raeumungsklage-Zustellung durch vollstaendige Zahlung die fristlose Kuendigung unwirksam machen (§569 Abs. 3 Nr. 2 BGB) -- aber nur einmal in 2 Jahren
   - Sozialklausel pruefen (§574 BGB) bei ordentlicher Kuendigung

5. **Mahnschreiben generieren** -- Fuer jede identifizierte Mahnstufe ein Schreiben erstellen:
   - Absender (Vermieter) und Empfaenger (Mieter) vollstaendig
   - Bezug: Mietvertrag vom [Datum], Objekt, Einheit
   - Konkreter Rueckstand mit Aufschluesselung (welcher Monat, welcher Betrag)
   - Fristsetzung mit konkretem Datum
   - Bankverbindung fuer Zahlung
   - Bei Stufe 2+: Hinweis auf Verzugszinsen (§288 BGB: 5 Prozentpunkte ueber Basiszinssatz)
   - Bei Stufe 3: Ausdrueckliche Kuendigungsandrohung
   - Bei Stufe 4: Kuendigung mit Raeumungsaufforderung und Fristsetzung

6. **Ratenzahlungsvereinbarung pruefen** -- Wenn Mieter Ratenzahlung anbietet oder vereinbart wurde:
   - Gesamtrueckstand dokumentieren
   - Ratenhoehe und Anzahl berechnen (realistisch fuer Mieter, akzeptabel fuer Vermieter)
   - Verfallklausel aufnehmen (bei Nichteinhaltung einer Rate wird Gesamtbetrag sofort faellig)
   - Schriftform sicherstellen

7. **Portfolio-Ueberblick erstellen** -- Zusammenfassung ueber alle Einheiten:
   - Zahlungsquote (% puenktlich zahlende Mieter)
   - Gesamtrueckstand in EUR
   - Anzahl Mieter pro Mahnstufe
   - Trend gegenueber Vormonat (besser/schlechter/gleich)

8. **Empfehlungen ableiten** -- Handlungsempfehlungen priorisieren:
   - Sofortige Kuendigung vorbereiten (Stufe 4)
   - Letzte Mahnung versenden (Stufe 3)
   - Ratenzahlung anbieten bei kooperativen Mietern
   - Besonders bei Erstmietern oder langjaehrigen Mietern: persoenliches Gespraech empfehlen

---

## Ausgabeformat

```json
{
  "report_type": "mahn_assistent",
  "period": "2026-04",
  "report_date": "2026-04-15",
  "portfolio_summary": {
    "total_units": 48,
    "total_soll_eur": 28800.00,
    "total_received_eur": 26960.00,
    "total_arrears_eur": 1840.00,
    "payment_rate_percent": 93.6,
    "tenants_in_arrears": 3,
    "trend_vs_previous_month": "verschlechtert"
  },
  "arrears_by_tenant": [
    {
      "tenant": "Nachname, Vorname",
      "property": "Musterstr. 12, 10115 Berlin",
      "unit": "WE 04",
      "rent_due_eur": 920.00,
      "rent_received_eur": 0.00,
      "arrears_current_month_eur": 920.00,
      "arrears_total_eur": 1840.00,
      "arrears_months": 2,
      "last_payment_date": "2026-02-03",
      "last_payment_amount_eur": 920.00,
      "dunning_level": 3,
      "dunning_history": [
        {
          "level": 0,
          "type": "zahlungserinnerung",
          "date_sent": "2026-03-08",
          "deadline": "2026-03-15"
        },
        {
          "level": 1,
          "type": "erste_mahnung",
          "date_sent": "2026-03-17",
          "deadline": "2026-03-31"
        },
        {
          "level": 2,
          "type": "zweite_mahnung",
          "date_sent": "2026-04-02",
          "deadline": "2026-04-11"
        }
      ],
      "next_action": "letzte_mahnung_mit_kuendigungsandrohung",
      "termination_eligible": true,
      "termination_basis": "§543 Abs. 2 Nr. 3a BGB -- Rueckstand >= 2 Monatsmieten",
      "recommendation": "Letzte Mahnung versenden. Bei Nichtzahlung bis 18.04.: fristlose + hilfsweise ordentliche Kuendigung vorbereiten."
    }
  ],
  "generated_documents": [
    {
      "type": "letzte_mahnung",
      "tenant": "Nachname, Vorname",
      "property": "Musterstr. 12, 10115 Berlin",
      "unit": "WE 04",
      "content": "--- LETZTE MAHNUNG ---\n\n[Vollstaendiger Brieftext hier]\n\nSehr geehrte/r Frau/Herr [Name],\n\nwir beziehen uns auf den Mietvertrag vom [Datum] ueber die Wohnung [Adresse, WE].\n\nTrotz unserer Mahnungen vom [Daten] ist folgender Mietrueckstand weiterhin offen:\n\n- Miete Maerz 2026: 920,00 EUR\n- Miete April 2026: 920,00 EUR\n- Gesamt: 1.840,00 EUR\n\nWir fordern Sie hiermit letztmalig auf, den Gesamtbetrag von 1.840,00 EUR bis zum [Datum + 7 Werktage] auf folgendes Konto zu ueberweisen:\n\n[Bankverbindung]\n\nSollte der Betrag nicht fristgerecht eingehen, sehen wir uns gezwungen, das Mietverhaeltnis fristlos gemaess §543 Abs. 2 Nr. 3 BGB zu kuendigen und Raeumungsklage zu erheben. Zusaetzlich entstehen Ihnen Verzugszinsen in Hoehe von 5 Prozentpunkten ueber dem Basiszinssatz (§288 BGB) sowie saemtliche Kosten der Rechtsverfolgung.\n\nMit freundlichen Gruessen\n[Vermieter]"
    }
  ],
  "payment_agreements": [
    {
      "tenant": "Anderer Mieter",
      "property": "Beispielweg 5, 10117 Berlin",
      "unit": "WE 12",
      "total_arrears_eur": 600.00,
      "monthly_rate_eur": 200.00,
      "installments": 3,
      "start_date": "2026-05-01",
      "end_date": "2026-07-01",
      "status": "aktiv",
      "payments_on_track": true
    }
  ],
  "actions_required": [
    {
      "priority": "kritisch",
      "tenant": "Nachname, Vorname",
      "action": "Letzte Mahnung versenden",
      "deadline": "2026-04-16"
    },
    {
      "priority": "hoch",
      "tenant": "Weiterer Mieter",
      "action": "1. Mahnung versenden",
      "deadline": "2026-04-18"
    }
  ],
  "confidence_score": 0.92,
  "data_gaps": []
}
```

---

## Qualitaetspruefung

- [ ] Soll-Ist-Abgleich ist vollstaendig (jede Einheit geprueft)
- [ ] Rueckstandsberechnung ist arithmetisch korrekt
- [ ] Mahnstufe entspricht der Eskalationslogik (kein Ueberspringen von Stufen)
- [ ] Fristen in Mahnschreiben fallen auf Werktage (kein Samstag/Sonntag/Feiertag)
- [ ] Kuendigungsvoraussetzungen nach §543 BGB sind korrekt geprueft (>= 2 Monatsmieten)
- [ ] Mahnschreiben enthalten alle Pflichtangaben (Rueckstand aufgeschluesselt, Frist, Bankverbindung)
- [ ] Verzugszinsen-Hinweis korrekt (§288 BGB, 5 Prozentpunkte ueber Basiszinssatz)
- [ ] Ratenzahlungsvereinbarungen enthalten Verfallklausel
- [ ] Schonfristzahlung-Regelung (§569 Abs. 3 Nr. 2 BGB) bei Kuendigung erwaehnt
- [ ] Gesamtrueckstand im Portfolio-Ueberblick stimmt mit Summe der Einzel-Rueckstaende ueberein

---

## Warnsignale

| Signal | Bedeutung | Empfohlene Aktion |
|--------|-----------|-------------------|
| Rueckstand >= 2 Monatsmieten | Fristlose Kuendigung moeglich (§543 BGB) | Kuendigung vorbereiten, Anwalt einschalten |
| Rueckstand >= 1 Monatsmiete, 2. Monat in Folge | Kuendigungsrecht entsteht moeglicherweise | Letzte Mahnung mit Kuendigungsandrohung |
| Mieter zahlt regelmaessig zu wenig | Moeglicherweise unberechtigte Mietminderung | Minderungsgrund pruefen, ggf. Widerspruch |
| Ratenzahlungsvereinbarung nicht eingehalten | Verfallklausel greift, Gesamtbetrag faellig | Sofort Gesamtforderung geltend machen |
| Zahlung von Dritter Seite (Jobcenter, Sozialamt) | Hinweis auf Transferleistungsbezug | Direktzahlung durch Amt pruefen (§22 SGB II) |
| Mieter widerspricht Mahnung | Moeglicherweise berechtigter Einwand | Einwand pruefen vor naechster Eskalation |

---

## Bei fehlenden Daten

- Wenn Zahlungseingaenge unvollstaendig: Nur die vorliegenden Zahlungen abgleichen, fehlende Monate kennzeichnen. Keinen Rueckstand annehmen, wenn Zahlungsdaten einfach fehlen.
- Wenn kein Mahnverlauf vorliegt: Konservativ mit Stufe 0 (Zahlungserinnerung) beginnen, nicht mit hoeherer Stufe.
- Wenn Vermieterdaten fehlen: Mahnschreiben als Template mit Platzhaltern [Vermieter Name], [Anschrift], [Bankverbindung] generieren.
- Wenn Faelligkeitstermin unklar: Standard-Faelligkeit 3. Werktag des Monats annehmen und als Annahme kennzeichnen.
- Alle Luecken im Feld `data_gaps` dokumentieren.

---

## Konfidenz-Bewertung

| Score | Bedeutung |
|-------|-----------|
| 0.9 - 1.0 | Vollstaendige Daten: Soll-Mieten, Zahlungen, Mahnhistorie, Vermieterdaten vorhanden |
| 0.7 - 0.9 | Zahlungen und Soll-Mieten vorhanden, aber Mahnhistorie oder Vermieterdaten fehlen |
| 0.5 - 0.7 | Nur Soll-Mieten oder nur Zahlungen vorhanden |
| < 0.5 | Wesentliche Daten fehlen, Ergebnis nicht belastbar |

Faktoren die den Score senken:
- Fehlende Mahnhistorie -- Mahnstufe kann nicht sicher bestimmt werden (-0.15)
- Zahlungseingaenge ohne klare Mieter-Zuordnung (-0.10)
- Kein Mietvertragsdatum fuer Schreiben-Referenz (-0.05)
- Fehlende Vermieterdaten fuer Briefkopf (-0.05)

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- BGB §543, §573, §569, §288: Kuendigung, Verzug, Verzugszinsen
- `knowledge/checklisten.md` -- Verwaltungs-Checklisten inkl. Mahnwesen
- `skills/verwaltung/wochen-jourfixe.md` -- Mietrueckstaende als Brennpunkt im Wochen-Report
- `skills/verwaltung/nebenkosten-pruefer.md` -- Nebenkostennachforderungen koennen Rueckstand erhoehen
