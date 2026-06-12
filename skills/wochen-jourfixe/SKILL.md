---
name: wochen-jourfixe
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

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext.

### Wochenreport

```markdown
# Wochen-Jourfixe: 08.04. - 15.04.2026

**23 Vorgaenge gesamt** | 🔴 3 kritisch | 8 neu diese Woche | 5 erledigt | 15 weiterhin offen

## 🔴 Brennpunkte (sofort handeln)

| Nr. | Thema | Objekt / Einheit | Beschreibung | Naechster Schritt | Frist | Status |
|-----|-------|------------------|--------------|--------------------|-------|--------|
| BP-001 | Mietrueckstand | Musterstr. 12, Berlin / WE 04 (Mieter: Nachname, Vorname) | Mietrueckstand seit 2 Monaten, Gesamtrueckstand 1.840 EUR | 2. Mahnung versenden, Kuendigungsandrohung pruefen | 18.04.2026 | offen |

## Vermietung & Besichtigung

**Leerstand:**

| Objekt / Einheit | Leer seit | Status | Naechster Schritt | Zielmiete |
|------------------|-----------|--------|--------------------|-----------|
| Musterstr. 12, Berlin / WE 07 | 01.03.2026 | Besichtigungen geplant | 3 Besichtigungstermine am 17.04. | 620 EUR |

**Kuendigungen:** Keine neuen Kuendigungen diese Woche.

**Uebergaben:** Keine anstehenden Uebergaben.

## Finanzen & Versorger

**Mietrueckstaende gesamt: 3.240 EUR**

**Offene Rechnungen:**

| Lieferant | Betrag | Faellig | Objekt | Beschreibung |
|-----------|--------|---------|--------|--------------|
| Sanitaer Meier GmbH | 1.850 EUR | 20.04.2026 | Musterstr. 12, Berlin | Reparatur Steigleitung WE 02 |

**Versorger-Themen:** Keine.

**Nebenkostenabrechnungen:** Keine offenen Vorgaenge.

## Instandhaltung

| Nr. | Objekt / Einheit | Problem | Gemeldet | Status | Handwerker | Geschaetzte Kosten | Naechster Schritt |
|-----|------------------|---------|----------|--------|------------|--------------------|--------------------|
| IH-012 | Musterstr. 12, Berlin / WE 03 | Schimmelbildung Schlafzimmer Aussenwand | 10.04.2026 | Handwerker beauftragt | Bautenschutz Mueller | 2.200 EUR | Termin am 16.04. |

## Kalender-Highlights

| Datum | Art | Beschreibung | Dringlichkeit |
|-------|-----|--------------|---------------|
| 22.04.2026 | Frist | Frist Nebenkostenabrechnung 2024 -- Objekt Beispielweg 5 | 🟡 diese Woche |

## Offene Anrufe / Rueckrufe

| Datum | Anrufer | Objekt | Thema | Dringlichkeit | Rueckruf noetig |
|-------|---------|--------|-------|----------------|------------------|
| 14.04.2026 | Mieter Schmidt, WE 09 | Musterstr. 12, Berlin | Heizung funktioniert nicht | 🔴 hoch | Ja |

## Fristenmonitor

| Status | Vorgaenge |
|--------|-----------|
| 🔴 Ueberfaellig | Keine |
| 🟡 Faellig diese Woche | Frist Nebenkostenabrechnung 2024 (22.04.) |
| 🟢 Faellig naechste Woche | Keine |

## Datenluecken

Konfidenz: 85%
- Zahlungseingaenge fuer Objekt Beispielweg 5 nicht vorhanden
```

---

## Qualitaetspruefung

- [ ] Jede E-Mail / Nachricht wurde genau einer Kategorie zugeordnet
- [ ] Brennpunkte sind tatsaechlich kritisch (kein Aufblaehen, kein Unterschlagen)
- [ ] Alle Vorgaenge haben einen klaren naechsten Schritt (Spalte "Naechster Schritt" befuellt)
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
- Fehlende Daten immer im Berichtsabschnitt "Datenluecken" dokumentieren.

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
