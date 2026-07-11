---
name: wochen-jourfixe
description: "Erstellt automatische Wochenreports fuer Immobilien-Portfolios nach dem Pareto-Prinzip: Kritische 20% der Themen oben, priorisiert nach Handlungsbedarf. Enthaelt den Wochenrhythmus eines professionellen Investors (feste Akquise-Slots, Follow-up-Zyklen, Pipeline-Review), Wochen-KPIs (Angebote gesichtet, Grobkalkulationen, Besichtigungen, LOIs) und ein Fristen-Monitoring inkl. strategischer Fristen wie Zinsbindungsablauf, Mietanpassungsfenster und Nebenkostenabrechnung. Nutze diesen Skill wenn du Team-Meetings oder deinen Wochen-Jourfixe vorbereitest, einen Portfolio- und Pipeline-Ueberblick brauchst oder Fristen im Blick behalten willst."
---

# Wochen-Jourfixe -- Automatischer Wochenreport

## Wann nutzen

- Woechentliche Team-Meetings vorbereiten (Jour Fixe)
- Ueberblick ueber alle laufenden Vorgaenge im Bestand (10-500+ Einheiten)
- Kritische Themen identifizieren, bevor sie eskalieren
- E-Mail-Postfach / Eingangskommunikation strukturiert auswerten
- Offene Vorgaenge tracken und Fristen ueberwachen (operativ UND strategisch: Zinsbindung, Mietanpassung, NK-Abrechnung)
- Akquise-Pipeline reviewen: Was ist diese Woche in den Funnel gekommen, was liegt fest, was versandet?

---

## Inputs

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `emails` | Array | Ja | E-Mails / Nachrichten der letzten 7 Tage (Absender, Betreff, Datum, Inhalt oder Zusammenfassung) |
| `open_issues_previous` | Array | Nein | Offene Vorgaenge aus dem letzten Jourfixe-Report |
| `payment_data` | Object | Nein | Zahlungseingaenge der Woche (fuer Finanz-Ueberblick) |
| `calendar_entries` | Array | Nein | Kalendereintraege der naechsten 7-14 Tage |
| `property_portfolio` | Array | Nein | Liste der Objekte mit Adressen und Einheitenzahl |
| `pipeline_data` | Array | Nein | Akquise-Pipeline: Angebote, Funnel-Stufe, letzte Aktion, Wiedervorlagen, LOI-Status |
| `loan_data` | Array | Nein | Darlehen mit Zinsbindungsende und Restschuld (fuer strategisches Fristen-Monitoring) |
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
   - **Strategische Fristen zusaetzlich mitfuehren** (die operative Wochenlogik uebersieht sie sonst, weil sie weit weg wirken -- teuer werden sie trotzdem):

   | Frist | Vorlauf / Ampellogik | Warum kritisch |
   |-------|----------------------|----------------|
   | Zinsbindungsablauf je Darlehen | 🟡 ab 24 Monate vorher (Prolongation/Umschuldung vorbereiten), 🔴 ab 12 Monate ohne Plan | Anschlussfinanzierung entscheidet ueber den Cashflow der naechsten Dekade |
   | Nebenkostenabrechnung | 🟡 3 Monate vor Ablauf der 12-Monats-Frist, 🔴 danach | Nachforderungen verfallen bei verspaeteter Abrechnung -- Guthaben des Mieters bleibt |
   | Mietanpassungsfenster | 🟡 sobald letzte Erhoehung > 12 Monate her und Potenzial vorhanden | Nicht gezogene Erhoehungen sind dauerhafter Ertragsverlust (Kappungsgrenze beachten) |
   | Kuendigungsfristen (Mieter/Verwalter/Versicherung) | 🟡 8 Wochen vorher | Verpasste Fristen binden ein weiteres Jahr |
   | Energieausweis-Gueltigkeit | 🟡 6 Monate vor Ablauf | Pflicht bei Neuvermietung und Verkauf |

10. **Akquise- & Pipeline-Review** (wenn `pipeline_data` vorhanden) -- Der Jourfixe ist nicht nur Bestandsverwaltung, sondern auch der Wochentakt der Akquise:
   - Neue Angebote im Funnel diese Woche (Anzahl, Quelle)
   - Offene Follow-ups und ueberfaellige Wiedervorlagen (aeltester zuerst)
   - Besichtigungen: durchgefuehrt und geplant
   - LOIs / Angebote: rausgegangen, angenommen, abgelehnt
   - Liegengebliebene Deals: Welche Funnel-Stufe sammelt Karteileichen? (typischer Engpass-Indikator)
   - Unbeantwortete Zuleitungen von Tippgebern/Maklern (Warnsignal: wer Tipps ignoriert, verliert die Quelle)
   - Learnings der Woche (Absagegruende, Marktbeobachtungen)

11. **Report zusammenstellen** -- Strukturierten Report im Ausgabeformat generieren, priorisiert nach Dringlichkeit.

---

## Wochenrhythmus eines professionellen Investors (Referenz)

Der Jourfixe-Report ist der Kontrollpunkt eines festen Wochenrhythmus -- verlaesslicher Dealflow und saubere Verwaltung entstehen durch wiederholbare Zeitbloecke, nicht durch sporadisches Reagieren. Wenn der Nutzer noch keinen Rhythmus hat, biete dieses Raster als Startpunkt an (Umfang nach Investorentyp skalieren):

| Slot | Rhythmus | Inhalt |
|------|----------|--------|
| Portalcheck & Screening | 2-3x pro Woche, fester Block | Neue Inserate sichten, Grobkalkulation ("Bierdeckel") fuer passende Objekte |
| Telefon-/Nachfass-Slot | 1-2x pro Woche | Makler- und Tippgeber-Kontakte, offene Wiedervorlagen abtelefonieren |
| Follow-up-Zyklus | laufend, max. 48h Reaktionszeit | Jede Zuleitung und jede Unterlagen-Lieferung bekommt eine Antwort -- ohne Ausnahme |
| Besichtigungen | gebuendelt (z.B. ein Nachmittag) | Fahrzeit minimieren, Besichtigungsbericht direkt danach |
| Wochen-Jourfixe | 1x pro Woche, fester Termin | Dieser Report: Brennpunkte, Bestand, Finanzen, Fristen, Pipeline-Review |
| Fristen-/Zahlenblick | 1x pro Woche (im Jourfixe) | Mieteingaenge, Fristenmonitor inkl. Zinsbindung, NK-Frist, Mietanpassung |

**Zeitbudget als Realitaetscheck** (Erfahrungswerte): Nebenberuflicher Investor mindestens 3-4 h/Woche; ambitionierter Aufbau eher ein voller Immobilientag pro Woche. Wenn der Report woechentlich null Akquise-Aktivitaet zeigt, ist das kein Zufall, sondern ein Zeitbudget-Problem -- offen ansprechen.

### Wochen-KPIs (Vorschlag)

Wenige Zahlen, jede Woche dieselben -- Trend schlaegt Momentaufnahme:

| KPI | Woche | Vorwoche | Kommentar |
|-----|-------|----------|-----------|
| Angebote gesichtet | | | Funnel-Eingang |
| Grobkalkulationen ("Bierdeckel") | | | Screening-Durchsatz |
| Kontaktaufnahmen / Nachfaesse | | | Netzwerkpflege |
| Besichtigungen | | | Funnel-Mitte |
| LOIs / Angebote abgegeben | | | Funnel-Ausgang |
| Unbeantwortete Zuleitungen | | | Ziel: 0 |
| Mieteingangsquote | | | Bestand |
| Offene Maengel > 14 Tage | | | Verwaltung |

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

## Akquise & Pipeline

**Wochen-KPIs:** 14 Angebote gesichtet | 6 Bierdeckel gerechnet | 2 Besichtigungen | 1 LOI abgegeben | 0 unbeantwortete Zuleitungen

| Funnel-Stufe | Anzahl | Aeltester Eintrag | Auffaellig |
|--------------|--------|-------------------|------------|
| Screening | 8 | 3 Tage | -- |
| Unterlagen angefordert | 4 | 12 Tage | 2 Nachfaesse ueberfaellig |
| Besichtigung geplant | 2 | -- | Termine 17.04. |
| LOI / Verhandlung | 1 | 5 Tage | Rueckmeldung Makler steht aus |

**Learnings der Woche:** Absage Beispielweg 5 wegen Hausgeld -- Suchprofil um Hausgeld-Obergrenze ergaenzen?

## Fristenmonitor

| Status | Vorgaenge |
|--------|-----------|
| 🔴 Ueberfaellig | Keine |
| 🟡 Faellig diese Woche | Frist Nebenkostenabrechnung 2024 (22.04.) |
| 🟢 Faellig naechste Woche | Keine |

**Strategische Fristen (Vorlauf-Radar):**

| Frist | Objekt | Termin | Status |
|-------|--------|--------|--------|
| Zinsbindungsablauf Darlehen Sparkasse | Musterstr. 12, Berlin | 30.06.2027 | 🟡 14 Monate -- Prolongationsangebote einholen |
| Mietanpassung moeglich | Beispielweg 5 / WE 02 | ab sofort | 🟡 letzte Erhoehung 2023, Potenzial lt. Mietspiegel |

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
| Zinsbindung endet < 12 Monate ohne Plan | Anschlussfinanzierungs-Risiko, Verhandlungsposition schwindet | Prolongationsangebot anfordern, Vergleichsangebote einholen |
| NK-Abrechnungsfrist < 3 Monate | Nachforderungen drohen zu verfallen | Abrechnung sofort priorisieren oder Verwalter eskalieren |
| Zuleitung/Tipp > 48h unbeantwortet | Tippgeber- und Maklerbeziehung stirbt leise | Sofort antworten, auch wenn Absage |
| 0 Akquise-Aktivitaet in der Woche | Dealflow reisst ab -- Wiederanlauf kostet Wochen | Zeitbudget und Akquise-Slots im Kalender pruefen |
| Deals > 14 Tage ohne Statuswechsel in einer Funnel-Stufe | Pipeline wird zum Friedhof | Stufe im Jourfixe durchgehen: nachfassen oder sauber absagen |

---

## Bei fehlenden Daten

- Wenn keine E-Mails vorliegen: Report auf Basis der offenen Vorgaenge aus der Vorwoche und Kalenderdaten erstellen, fehlende Kategorie als "keine Daten" kennzeichnen.
- Wenn keine Zahlungsdaten vorliegen: Finanzen-Bereich als "Zahlungsdaten nicht verfuegbar" markieren, nicht schaetzen.
- Wenn kein Vorwochen-Report vorliegt: Alle Vorgaenge als "neu" kennzeichnen, kein Abgleich moeglich.
- Wenn Kalendereintraege fehlen: Kalender-Highlights leer lassen, Hinweis "Kalenderdaten nicht uebermittelt" ausgeben.
- Wenn keine Pipeline-Daten vorliegen: Abschnitt "Akquise & Pipeline" weglassen (nicht mit leeren Tabellen aufblaehen), aber einmalig anbieten, die Pipeline kuenftig mitzufuehren.
- Wenn keine Darlehensdaten vorliegen: strategische Fristen als "Zinsbindungsdaten nicht verfuegbar" markieren -- nicht schaetzen.
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
- `skills/prozess-designer/SKILL.md` -- verankert den Wochenrhythmus als wiederkehrende Aufgaben (Pipeline-Review, Mieteingangs-Kontrolle) direkt im System
- `skills/ordner-architekt/SKILL.md` -- Ablagestruktur, aus der Fristen-Dokumente (Darlehensvertraege, NK-Abrechnungen) sauber auffindbar sind
