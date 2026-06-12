---
name: datev-vorbereitung
description: "Erstellt DATEV-konforme Buchungssaetze (SKR03/SKR04) aus klassifizierten Belegen fuer Immobilien-Buchhaltung. Nutze diesen Skill wenn du sortierte Belege in Buchungssaetze umwandeln willst, die Buchhaltung aufsetzt oder dich auf das Steuerberater-Gespraech vorbereitest."
---

# DATEV-Vorbereitung

> Buchungssaetze nach SKR03/SKR04 erstellen und eine DATEV-kompatible Buchungsliste fuer den Steuerberater aufbereiten -- damit die Buchhaltung nicht doppelt gemacht wird.

---

## Wann nutzen?

- Nach der Belegsortierung: Aus klassifizierten Belegen Buchungssaetze ableiten
- Vor dem Steuerberater-Termin: Fertige Buchungsliste uebergeben
- Monatlich oder quartalsweise: Laufende Buchhaltung vorbereiten
- Bei Neuanlage eines Objekts: AfA-Buchungen und Anschaffungskosten korrekt erfassen

---

## Inputs

Stelle folgende Informationen bereit:

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| `belege_sortiert` | Ja | Klassifizierte Belege (Output aus beleg-sortierer.md) |
| `kontenrahmen` | Ja | SKR03 oder SKR04 |
| `objekte` | Ja | Objektliste mit Objekt-ID, Adresse, Anschaffungsdaten |
| `steuerjahr` | Ja | Buchungsjahr |
| `anschaffungsdaten` | Empfohlen | Pro Objekt: Kaufdatum, Kaufpreis, Grundstuecksanteil, Gebaeudewert, Baujahr |
| `darlehen` | Empfohlen | Pro Darlehen: Darlehensnummer, Bank, Restschuld, Zinssatz, Tilgung, Objekt-Zuordnung |
| `vorjahres_afa` | Optional | AfA-Buchungen des Vorjahres zur Kontrolle |
| `ust_option` | Optional | Objekte mit Option zur Umsatzsteuer (§9 UStG) |

---

## Auftrag

Du bist ein erfahrener Finanzbuchhalter mit Spezialisierung auf Immobilien-Buchhaltung nach deutschem Steuerrecht. Erstelle aus den klassifizierten Belegen vollstaendige Buchungssaetze nach dem gewaehlten Kontenrahmen (SKR03 oder SKR04). Jede Buchung muss einem Objekt als Kostenstelle zugeordnet sein. Ergebnis ist eine DATEV-kompatible Buchungsliste, die der Steuerberater direkt importieren oder pruefen kann.

---

## Strategie

1. **Kontenrahmen bestimmen und Sachkonten zuordnen**

   **SKR03 -- Relevante Sachkonten Immobilienvermietung:**

   | Konto | Bezeichnung | Verwendung |
   |-------|-------------|------------|
   | 0140 | Grundstuecke mit Bauten (Privatvermoegen) | Gebaeudewert |
   | 0145 | Grundstuecke ohne Bauten | Grundstuecksanteil |
   | 2100 | Mieteinnahmen | Kaltmiete |
   | 2105 | Nebenkosten-Erstattungen | NK-Vorauszahlungen Mieter |
   | 2109 | Sonstige Einnahmen aus V+V | Sonstige Einnahmen |
   | 4210 | AfA Gebaeude | Lineare Abschreibung |
   | 4360 | Grundsteuer | Grundsteuer |
   | 4380 | Versicherungen | Gebaeudeversicherung, Haftpflicht |
   | 4520 | Instandhaltung / Erhaltungsaufwand | Reparaturen, Wartung |
   | 4530 | Herstellungskosten | Aktivierungspflichtige Massnahmen |
   | 4570 | Verwaltungskosten | Hausverwaltung, WEG-Verwaltung |
   | 4590 | Sonstige Betriebskosten | Muellabfuhr, Wasser, etc. |
   | 2120 | Zinsaufwendungen | Schuldzinsen Darlehen |
   | 4600 | Fahrtkosten | Fahrten zum Objekt |
   | 4900 | Sonstige Aufwendungen | Nicht zuordenbare Kosten |

   **SKR04 -- Aequivalente Konten:**

   | SKR03 | SKR04 | Bezeichnung |
   |-------|-------|-------------|
   | 0140 | 0500 | Grundstuecke mit Bauten |
   | 2100 | 4400 | Mieteinnahmen |
   | 4210 | 6220 | AfA Gebaeude |
   | 4360 | 7685 | Grundsteuer |
   | 4380 | 6400 | Versicherungen |
   | 4520 | 6335 | Instandhaltung |
   | 2120 | 7300 | Zinsaufwendungen |

2. **Kostentraeger / Kostenstelle definieren**
   - Jedes Objekt = ein Kostentraeger (z.B. KST 100, 200, 300)
   - Bei Mischnutzung: Aufteilung nach Flaeche oder Miteigentumsanteil
   - Objektuebergreifende Kosten: Anteilig verteilen oder Sammel-KST

3. **Buchungssaetze erstellen**
   - Pro Beleg ein Buchungssatz (oder Splittbuchung bei mehreren Konten)
   - Belegfeld 1: Rechnungsnummer
   - Belegfeld 2: Kurztext (Leistung + Objekt)
   - Buchungsdatum: Rechnungsdatum (oder Leistungsdatum bei Periodenabgrenzung)
   - Soll-/Haben-Zuordnung nach Kontenrahmen

4. **AfA-Berechnung durchfuehren**
   - **Gebaeude ab 1925:** 2% linear (§7 Abs.4 Nr.2a EStG) = 50 Jahre Nutzungsdauer
   - **Gebaeude vor 1925:** 2,5% linear (§7 Abs.4 Nr.2b EStG) = 40 Jahre Nutzungsdauer
   - **Fertigstellung ab 2023:** 3% linear (§7 Abs.4 Nr.2a EStG n.F.) = 33 Jahre (JStG 2022)
   - **Denkmal-AfA (§7i EStG):** Erhoehte Abschreibung auf Sanierungskosten (9% x 8 Jahre + 7% x 4 Jahre)
   - **Sonder-AfA §7b EStG:** 5% p.a. fuer 4 Jahre bei Neubau-Mietwohnungen (Baukostenobergrenze beachten)
   - Bemessungsgrundlage: Gebaeudewert (Kaufpreis minus Grundstuecksanteil minus Aussenanlagen)
   - AfA beginnt im Monat der Anschaffung (zeitanteilig im ersten Jahr)

5. **USt-Behandlung pruefen**
   - **Grundsatz:** Vermietung zu Wohnzwecken ist umsatzsteuerfrei (§4 Nr.12 UStG)
   - **Kein Vorsteuerabzug** bei umsatzsteuerfreier Vermietung
   - **Ausnahme:** Gewerbliche Vermietung oder Option nach §9 UStG
   - Bei Option zur USt: Vorsteuerabzug moeglich, aber Bindungsfrist beachten
   - Kurzfristige Vermietung (< 6 Monate): USt-pflichtig (§4 Nr.12 S.2 UStG)
   - Stellplaetze separat vermietet: Grundsaetzlich USt-pflichtig

6. **Periodenzuordnung sicherstellen**
   - Rechnungsdatum vs. Leistungszeitraum pruefen
   - Bei jahresuebergreifenden Leistungen: Abgrenzungsbuchung erstellen
   - Vorauszahlungen korrekt periodengerecht abgrenzen
   - Hausgeld-Abrechnung: Nachzahlung/Guthaben dem Abrechnungsjahr zuordnen

7. **DATEV-kompatible Ausgabe formatieren**
   - Feldstruktur gemaess DATEV-Buchungsstapel
   - Belegdatum, Belegnummer, Sollkonto, Habenkonto, Betrag, Buchungstext, Kostenstelle
   - Trennzeichen: Semikolon
   - Datumsformat: TTMM (vierstellig)
   - Betraege: Dezimaltrenner Komma, kein Tausendertrenner

---

## Ausgabeformat

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext.

**Im Chat:** der unten gezeigte Markdown-Bericht (Buchungsliste).
**Als Datei:** den DATEV-Buchungsstapel (Semikolon-getrennte Export-Zeilen, z.B. `datev-buchungsstapel_2025.csv`) schreibst du in eine Datei und bietest sie fuer den Import durch den Steuerberater an -- die Export-Zeilen niemals im Chat ausgeben.

### Zusammenfassung (Freitext)

2-4 Saetze: Wie viele Buchungssaetze erstellt, Soll/Haben ausgeglichen ja/nein, AfA-Status, was der Steuerberater noch pruefen muss.

### Buchungsliste (Bericht)

```markdown
# DATEV-Vorbereitung: Steuerjahr 2025

**Kontenrahmen: SKR03** | Erstellt am 01.12.2025 | **58 Buchungssaetze** | Soll = Haben: 🟢 ausgeglichen (45.200,00 EUR)

## Objekte und AfA

| Objekt | KST | Anschaffung | Gebaeudewert | Grundstueck | Baujahr | AfA-Satz | AfA 2025 | AfA kumuliert | Restbuchwert |
|--------|-----|-------------|--------------|-------------|---------|----------|----------|----------------|---------------|
| Musterstrasse 12, 40210 Duesseldorf | 100 | 15.06.2022 | 320.000,00 EUR | 80.000,00 EUR | 1965 | 2,0% | 6.400,00 EUR | 19.200,00 EUR | 300.800,00 EUR |

## Buchungsliste

| Nr. | Datum | Beleg-Nr. | Soll | Haben | Betrag | USt | Buchungstext | KST |
|-----|-------|-----------|------|-------|--------|-----|--------------|-----|
| BU-2025-001 | 15.03.2025 | RE-2025-0734 | 4520 Instandhaltung / Erhaltungsaufwand | 1200 Bank | 2.450,00 EUR | 0% | Sanitaer Mueller, Mischbatterie WE3, Musterstr.12 | 100 |
| BU-2025-AFA-001 | 31.12.2025 | AFA-2025 | 4210 AfA Gebaeude | 0140 Grundstuecke mit Bauten | 6.400,00 EUR | 0% | AfA Gebaeude 2% linear, Musterstr.12, BJ 1965 | 100 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Summen nach Sachkonto

| Konto | Bezeichnung | Buchungen | Summe |
|-------|-------------|-----------|-------|
| 4520 | Instandhaltung | 12 | 15.400,00 EUR |
| 4210 | AfA Gebaeude | 2 | 12.800,00 EUR |
| 2120 | Zinsaufwendungen | 2 | 8.400,00 EUR |
| 4360 | Grundsteuer | 2 | 1.780,00 EUR |
| 4380 | Versicherungen | 4 | 1.920,00 EUR |
| 4570 | Verwaltungskosten | 6 | 2.450,00 EUR |

## Summen nach Kostenstelle (Objekt)

| KST | Buchungen | Summe |
|-----|-----------|-------|
| 100 | 35 | 28.500,00 EUR |
| 200 | 23 | 16.700,00 EUR |

## Umsatzsteuer

| | |
|---|---|
| Steuerfreie Mieteinnahmen | 42.000,00 EUR |
| Steuerpflichtige Einnahmen | 0,00 EUR |
| Nicht abziehbare Vorsteuer | 4.850,00 EUR |

Wohnungsvermietung umsatzsteuerfrei gemaess §4 Nr.12 UStG. Kein Vorsteuerabzug.

## Datei fuer den Steuerberater

DATEV-Buchungsstapel als Datei geschrieben: `datev-buchungsstapel_2025.csv`
(Semikolon-getrennt, DATEV-Feldstruktur, direkt importierbar)
```

---

## Qualitaetspruefung

Vor der Ausgabe pruefen:

- [ ] Soll und Haben sind ausgeglichen (Summe Soll = Summe Haben)
- [ ] Jeder Buchungssatz hat eine Kostenstelle / Kostentraeger
- [ ] AfA-Saetze sind korrekt (2%, 2,5% oder 3% je nach Baujahr)
- [ ] AfA-Bemessungsgrundlage ist der Gebaeudewert (ohne Grundstueck)
- [ ] USt-Behandlung ist korrekt (steuerfrei bei Wohnungsvermietung)
- [ ] Periodenabgrenzungen sind beruecksichtigt
- [ ] DATEV-Export-Zeilen folgen dem korrekten Format
- [ ] Kein Beleg wurde vergessen oder doppelt gebucht
- [ ] Buchungstexte sind aussagekraeftig (Leistung + Objekt erkennbar)

---

## Warnsignale

| Signal | Bedeutung | Aktion |
|--------|-----------|--------|
| Soll ≠ Haben | Buchungen nicht ausgeglichen | Fehler in Kontenzuordnung suchen |
| AfA-Satz unklar | Baujahr nicht eindeutig | Grundbuchauszug oder Bauakte pruefen |
| Gemischte Nutzung | Wohnen + Gewerbe im Objekt | Aufteilung nach Flaeche vornehmen |
| Vorsteuerabzug bei Wohnung | USt-Fehler | Korrigieren: Kein Vorsteuerabzug bei §4 Nr.12 |
| Hohe Instandhaltung bei Neuerwerb | 15%-Grenze beachten | An beleg-sortierer zurueckgeben |
| Fehlende Zinsbescheinigung | Schuldzinsen nicht belegbar | Von Bank anfordern |
| Buchung ohne Beleg | Buchung nicht pruefbar | Beleg nachfordern oder stornieren |
| Kontenrahmen-Wechsel | SKR03/SKR04 Mischung | Einheitlichen Kontenrahmen sicherstellen |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Kontenrahmen unbekannt | Standard SKR03 verwenden, Hinweis an Steuerberater |
| Baujahr unbekannt | AfA-Satz als "zu pruefen" markieren, 2% als Annahme |
| Grundstuecksanteil unklar | Bodenrichtwert-Methode vorschlagen, Wert als Schaetzung kennzeichnen |
| Darlehensdaten fehlen | Zinsbuchungen weglassen, als "Zinsbescheinigung ausstehend" markieren |
| Kostenstelle unklar | Beleg in Klaerungsliste aufnehmen |
| Vorjahres-AfA fehlt | AfA ab Anschaffung neu berechnen |

---

## Konfidenz-Bewertung

| Stufe | Wert | Bedeutung |
|-------|------|-----------|
| Hoch | >= 0.90 | Sachkonto eindeutig, Betrag geprueft, Kostenstelle klar |
| Mittel | 0.70 - 0.89 | Sachkonto wahrscheinlich korrekt, Zuordnung plausibel |
| Niedrig | 0.50 - 0.69 | Mehrere Konten moeglich, Steuerberater-Pruefung empfohlen |
| Unsicher | < 0.50 | Kontierung unklar, manuell zuordnen |

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- Steuerliche Grundlagen, AfA-Regelungen, UStG
- `knowledge/kalkulationsformeln.md` -- Berechnungsformeln fuer AfA und Rendite
- `skills/beleg-sortierer/SKILL.md` -- Vorheriger Schritt: Belege klassifizieren

