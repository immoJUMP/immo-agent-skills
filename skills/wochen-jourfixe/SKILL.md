---
description: "Erstellt automatische Wochenreports fuer Immobilien-Portfolios nach dem Pareto-Prinzip: Kritische 20% der Themen oben, priorisiert nach Handlungsbedarf. Nutze diesen Skill wenn du Team-Meetings vorbereitest, einen Portfolio-Ueberblick brauchst oder Fristen im Blick behalten willst."
---

# Wochen-Jourfixe -- Automatischer Wochenreport

## Wann nutzen

- Woechentliche Team-Meetings vorbereiten (Jour Fixe)
- Ueberblick ueber alle laufenden Vorgaenge im Bestand (10-500+ Einheiten)
- Kritische Themen identifizieren, bevor sie eskalieren
- E-Mail-Postfach / Eingangskommunikation strukturiert auswerten
- Offene Vorgaenge tracken und Fristen ueberwachen

---

## Inputs

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `emails` | Array | Ja | E-Mails / Nachrichten der letzten 7 Tage (Absender, Betreff, Datum, Inhalt oder Zusammenfassung) |
| `open_issues_previous` | Array | Nein | Offene Vorgaenge aus dem letzten Jourfixe-Report |
| `payment_data` | Object | Nein | Zahlungseingaenge der Woche (fuer Finanz-Ueberblick) |
| `calendar_entries` | Array | Nein | Kalendereintraege der naechsten 7-14 Tage |
| `property_portfolio` | Array | Nein | Liste der Objekte mit Adressen und Einheitenzahl |
| `report_date` | String | Nein | Stichtag des Reports (Default: aktuelles Datum) |

---

## Auftrag

Du bist ein erfahrener Immobilien-Assetmanager, der woechentlich einen strukturierten Jourfixe-Report fuer einen Bestandshalter mit Wohnimmobilien erstellt. Analysiere alle Eingangskommunikation der letzten Woche und erstelle einen priorisierten Report nach dem **Pareto-Prinzip**: Die kritischen 20% der Themen stehen oben -- alles, was sofortiges Handeln erfordert, kommt zuerst.

---

## Strategie

1. **Sichten und Kategorisieren** -- Jede E-Mail / Nachricht einer der sechs Kategorien zuordnen: Brennpunkte, Vermietung & Besichtigung, Finanzen & Versorger, Instandhaltung, Kalender-Highlights, Offene Anrufe / Rueckrufe.

2. **Brennpunkte identifizieren (Pareto-Filter)** -- Folgende Vorgaenge sind automatisch Brennpunkte:
   - Mahnungen und Mietrueckstaende ab 2. Monat
   - Schimmelmeldungen oder Feuchtigkeitsschaeden (Gesundheitsgefahr + Mietminderungsrisiko)
   - Wasserrohrbrueche, Heizungsausfaelle, Aufzugsstoerungen
   - Anwaltliche Schreiben oder Klagen
   - Behoerdliche Auflagen mit Fristsetzung
   - Kuendigungen (Mieter oder Vermieter)
   - Versicherungsschaeden mit Meldefrist

3. **Vermietung & Besichtigung** -- Alle laufenden Vermietungsprozesse erfassen:
   - Leerstehende Einheiten und Status (inseriert, Besichtigungen geplant, Bewerber vorhanden, Mietvertrag in Vorbereitung)
   - Geplante Besichtigungstermine
   - Neue Kuendigungseingaenge und Kuendigungsfrist-Ende
   - Mieterwechsel in Vorbereitung (Uebergaben, Renovierung)

4. **Finanzen & Versorger** -- Finanzrelevante Themen zusammenfassen:
   - Zahlungsrueckstaende (Mieter mit Rueckstand, Hoehe, seit wann)
   - Eingehende Rechnungen mit Faelligkeit
   - Versorgerkommunikation (Strom, Gas, Wasser, Muell)
   - Nebenkostenabrechnungen (Erstellung oder Einwendungen)
   - Versicherungsmeldungen

5. **Instandhaltung** -- Technische und bauliche Themen:
   - Neue Maengelmeldungen
   - Laufende Reparaturen und Status
   - Angebote / Auftraege fuer Handwerker
   - Geplante Modernisierungsmassnahmen

6. **Kalender-Highlights** -- Anstehende Termine und Fristen:
   - Gerichtstermine
   - Eigentuemer-Versammlungen (WEG)
   - Fristen (Nebenkostenabrechnung, Mietanpassung, Kuendigung)
   - Handwerkertermine
   - Behoerdentermine

7. **Offene Anrufe / Rueckrufe** -- Unbeantwortete Kommunikation:
   - Wer hat angerufen und wartet auf Rueckruf?
   - Unbeantwortete E-Mails mit Handlungsbedarf
   - Zuordnung zu Objekt und Dringlichkeit

8. **Abgleich mit Vorwoche** -- Offene Vorgaenge aus dem letzten Report pruefen:
   - Erledigt: als abgeschlossen markieren
   - Weiterhin offen: Status aktualisieren und Eskalation pruefen
   - Neu: als neuer Vorgang kennzeichnen

9. **Fristenmonitor** -- Alle Vorgaenge mit Fristsetzung pruefen:
   - Ueberfaellig (rot)
   - Faellig diese Woche (gelb)
   - Faellig naechste Woche (gruen)

10. **Report zusammenstellen** -- Strukturierten Report im Ausgabeformat generieren, priorisiert nach Dringlichkeit.

---

## Ausgabeformat

```json
{
  "report_type": "wochen_jourfixe",
  "report_date": "2026-04-15",
  "period": {
    "from": "2026-04-08",
    "to": "2026-04-15"
  },
  "summary": {
    "total_issues": 23,
    "critical": 3,
    "new_this_week": 8,
    "resolved_this_week": 5,
    "still_open": 15
  },
  "brennpunkte": [
    {
      "id": "BP-001",
      "category": "mietrueckstand",
      "property": "Musterstr. 12, 10115 Berlin",
      "unit": "WE 04",
      "tenant": "Nachname, Vorname",
      "description": "Mietrueckstand seit 2 Monaten, Gesamtrueckstand 1.840 EUR",
      "priority": "kritisch",
      "action_required": "2. Mahnung versenden, Kuendigungsandrohung pruefen",
      "deadline": "2026-04-18",
      "status": "offen"
    }
  ],
  "vermietung": {
    "leerstand_units": [
      {
        "property": "Musterstr. 12, 10115 Berlin",
        "unit": "WE 07",
        "vacant_since": "2026-03-01",
        "status": "besichtigungen_geplant",
        "next_step": "3 Besichtigungstermine am 17.04.",
        "target_rent_eur": 620.00
      }
    ],
    "kuendigungen": [],
    "uebergaben": []
  },
  "finanzen": {
    "mietrueckstaende_total_eur": 3240.00,
    "offene_rechnungen": [
      {
        "supplier": "Sanitaer Meier GmbH",
        "amount_eur": 1850.00,
        "due_date": "2026-04-20",
        "property": "Musterstr. 12, 10115 Berlin",
        "description": "Reparatur Steigleitung WE 02"
      }
    ],
    "versorger_themen": [],
    "nebenkostenabrechnung_status": []
  },
  "instandhaltung": [
    {
      "id": "IH-012",
      "property": "Musterstr. 12, 10115 Berlin",
      "unit": "WE 03",
      "issue": "Schimmelbildung Schlafzimmer Aussenwand",
      "reported_date": "2026-04-10",
      "status": "handwerker_beauftragt",
      "contractor": "Bautenschutz Mueller",
      "estimated_cost_eur": 2200.00,
      "next_step": "Termin am 16.04."
    }
  ],
  "kalender_highlights": [
    {
      "date": "2026-04-22",
      "type": "frist",
      "description": "Frist Nebenkostenabrechnung 2024 -- Objekt Beispielweg 5",
      "urgency": "gelb"
    }
  ],
  "offene_anrufe": [
    {
      "date": "2026-04-14",
      "caller": "Mieter Schmidt, WE 09",
      "property": "Musterstr. 12, 10115 Berlin",
      "topic": "Heizung funktioniert nicht",
      "urgency": "hoch",
      "callback_required": true
    }
  ],
  "fristen_monitor": {
    "ueberfaellig": [],
    "faellig_diese_woche": [],
    "faellig_naechste_woche": []
  },
  "confidence_score": 0.85,
  "data_gaps": [
    "Zahlungseingaenge fuer Objekt Beispielweg 5 nicht vorhanden"
  ]
}
```

---

## Qualitaetspruefung

- [ ] Jede E-Mail / Nachricht wurde genau einer Kategorie zugeordnet
- [ ] Brennpunkte sind tatsaechlich kritisch (kein Aufblaehen, kein Unterschlagen)
- [ ] Alle Vorgaenge haben einen klaren naechsten Schritt (`action_required` oder `next_step`)
- [ ] Fristen sind korrekt berechnet und der Fristenmonitor ist aktuell
- [ ] Offene Vorgaenge aus der Vorwoche sind abgeglichen (erledigt / weiterhin offen / eskaliert)
- [ ] Mieterrueckstaende stimmen mit den Zahlungsdaten ueberein
- [ ] Keine Duplikate (gleicher Vorgang mehrfach aufgefuehrt)
- [ ] Report ist ohne Zusatzinformationen verstaendlich (Team-Meeting-tauglich)

---

## Warnsignale

| Signal | Bedeutung | Empfohlene Aktion |
|--------|-----------|-------------------|
| Mietrueckstand >= 2 Monate | Kuendigungsrecht moeglich (§543 BGB) | Sofort Mahnung + Rechtsberatung |
| Schimmelmeldung | Mietminderung + Gesundheitsgefahr | Innerhalb 48h Handwerker beauftragen |
| Anwaltsschreiben eingegangen | Rechtsstreit droht | Sofort an Fachanwalt weiterleiten |
| Frist < 3 Tage | Drohendes Fristversaeumnis | Sofort bearbeiten oder Fristverlaengerung |
| Leerstand > 60 Tage | Ertragsausfall signifikant | Inserat und Preisstrategie ueberpruefen |
| Heizungsausfall im Winter | Notfall, Mietminderung 100% moeglich | Sofort Notdienst beauftragen |

---

## Bei fehlenden Daten

- Wenn keine E-Mails vorliegen: Report auf Basis der offenen Vorgaenge aus der Vorwoche und Kalenderdaten erstellen, fehlende Kategorie als "keine Daten" kennzeichnen.
- Wenn keine Zahlungsdaten vorliegen: Finanzen-Bereich als "Zahlungsdaten nicht verfuegbar" markieren, nicht schaetzen.
- Wenn kein Vorwochen-Report vorliegt: Alle Vorgaenge als "neu" kennzeichnen, kein Abgleich moeglich.
- Wenn Kalendereintraege fehlen: Kalender-Highlights leer lassen, Hinweis "Kalenderdaten nicht uebermittelt" ausgeben.
- Fehlende Daten immer im Feld `data_gaps` dokumentieren.

---

## Konfidenz-Bewertung

| Score | Bedeutung |
|-------|-----------|
| 0.9 - 1.0 | Vollstaendige Datenbasis: E-Mails, Zahlungen, Kalender, Vorwochen-Report vorhanden |
| 0.7 - 0.9 | Gute Datenbasis, einzelne Quellen fehlen (z.B. kein Kalender) |
| 0.5 - 0.7 | Lueckenhafte Datenbasis, mehrere Quellen fehlen |
| < 0.5 | Unzureichende Datenbasis, Report nur eingeschraenkt verwertbar |

Faktoren die den Score senken:
- Fehlende Zahlungsdaten (-0.15)
- Kein Vorwochen-Report zum Abgleich (-0.10)
- Fehlende Kalenderdaten (-0.05)
- E-Mails nur als Betreffzeilen ohne Inhalt (-0.10)
- Portfolio-Liste nicht vorhanden, Zuordnung zu Objekten unsicher (-0.10)

---

## Verwandte Wissensdatenbanken

- `knowledge/checklisten.md` -- Verwaltungs-Checklisten fuer laufende Prozesse
- `knowledge/rechtsgrundlagen.md` -- BGB-Mietrecht, Fristen, Kuendigungsrecht
- `skills/mahn-assistent/SKILL.md` -- Detail-Skill fuer Mahnwesen bei Mietrueckstaenden
- `skills/nebenkosten-pruefer/SKILL.md` -- Detail-Skill fuer Nebenkostenpruefung
- `skills/mieterhoehung/SKILL.md` -- Mieterhoehungspotenzial fuer Vermietungs-Kategorie
