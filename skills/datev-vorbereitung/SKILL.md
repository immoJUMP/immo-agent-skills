---
name: datev-vorbereitung
description: "Erstellt DATEV-konforme Buchungssaetze (SKR03/SKR04) aus klassifizierten Belegen fuer Immobilien-Buchhaltung, inkl. AfA-Berechnung (Gebaeude, bewegliche Wirtschaftsgueter, Kaufpreisaufteilung) und USt-Logik bei Vermietung. Nutze diesen Skill wenn du sortierte Belege in Buchungssaetze umwandeln willst, die Buchhaltung aufsetzt oder dich auf das Steuerberater-Gespraech vorbereitest."
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
| `anschaffungsdaten` | Empfohlen | Pro Objekt: Kaufdatum, Nutzen-/Lastenwechsel, Kaufpreis, Grundstuecksanteil, Gebaeudewert, Baujahr, Kaufpreisaufteilung laut Notarvertrag |
| `darlehen` | Empfohlen | Pro Darlehen: Darlehensnummer, Bank, Restschuld, Zinssatz, Tilgung, Objekt-Zuordnung, Verwendungszweck (Objekt vs. privat) |
| `bewegliche_wg` | Optional | Mitgekaufte/angeschaffte bewegliche Wirtschaftsgueter (Einbaukueche, Geraete, Moebel) mit Wert laut Kaufvertrag/Rechnung |
| `rnd_gutachten` | Optional | Restnutzungsdauer-Gutachten pro Objekt (Gutachter-Qualifikation, festgestellte Restnutzungsdauer) |
| `vorjahres_afa` | Optional | AfA-Buchungen des Vorjahres zur Kontrolle |
| `ust_option` | Optional | Objekte/Einheiten mit Option zur Umsatzsteuer (§9 UStG) inkl. Flaechenanteil |

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
   | 2120 | Zinsaufwendungen | Schuldzinsen Darlehen, Disagio |
   | 4600 | Fahrtkosten | Fahrten zum Objekt |
   | 0410 | Geschaeftsausstattung / bewegliche WG | Einbaukueche, Geraete, Moebel (Aktivierung) |
   | 4830 | AfA bewegliche Wirtschaftsgueter | Abschreibung Einbaukueche etc. |
   | 4855 | Sofortabschreibung GWG | Geraete bis 800 EUR netto |
   | 4900 | Sonstige Aufwendungen | Nicht zuordenbare Kosten |

   Hinweis: Kontenzuordnung ist ein Vorschlag -- finale Kontierung (insbesondere fuer
   bewegliche Wirtschaftsgueter, Ruecklagen-Verrechnung und Abgrenzungskonten) mit dem
   Steuerberater abstimmen, da Kanzleien eigene Kontenplaene pflegen.

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

   Alle AfA-Saetze und Grenzwerte sind gesetzlichen Aenderungen unterworfen -- vor
   Verwendung mit Steuerberater und aktueller Rechtslage validieren.

   **Gebaeude-AfA-Saetze:**
   - **Baujahr 1925-2022:** 2% linear (§7 Abs.4 EStG) = 50 Jahre Nutzungsdauer
   - **Baujahr vor 1925:** 2,5% linear = 40 Jahre Nutzungsdauer
   - **Fertigstellung ab 2023:** 3% linear = 33 Jahre
   - **Degressive AfA (§7 Abs.5a EStG):** 6% fuer Neubauten mit Baubeginn 10/2023-9/2029
     (bei Kauf: nur im Jahr der Fertigstellung); spaeter Wechsel zur linearen AfA pruefen
   - **Denkmal-AfA (§7i EStG):** 8 x 9% + 4 x 7% -- nur auf den von der Denkmalbehoerde
     anerkannten Sanierungsanteil, Bescheinigung erforderlich
   - **Sonder-AfA §7b EStG:** 5% p.a. fuer 4 Jahre bei Neubau-Mietwohnungen
     (Effizienz- und Baukostenobergrenzen beachten, mit Steuerberater pruefen)
   - **Verkuerzte Restnutzungsdauer (§7 Abs.4 S.2 EStG):** Nachgewiesene kuerzere
     Nutzungsdauer erhoeht die AfA. Finanzaemter erkennen Gutachten regelmaessig nur an,
     wenn der Gutachter oeffentlich bestellt und vereidigt oder nach DIN EN ISO/IEC 17024
     zertifiziert ist -- Gutachter-Qualifikation VOR Beauftragung pruefen (Streitrisiko).

   **Bemessungsgrundlage und Kaufpreisaufteilung:**
   - Bemessungsgrundlage: Gebaeudeanteil der Anschaffungskosten (Kaufpreis minus
     Grundstuecksanteil minus separat aktivierte Wirtschaftsgueter)
   - Kaufnebenkosten (GrESt, Notar, Makler) im gleichen Verhaeltnis Grund/Gebaeude aufteilen
   - Aufteilung idealerweise im Notarvertrag festgeschrieben; Plausibilisierung ueber die
     BMF-Arbeitshilfe. Rechtsprechung akzeptiert moderate, begruendete Abweichungen vom
     BMF-Tool zugunsten des Gebaeudes -- groessere Abweichungen nur mit Gutachten
     (mit Steuerberater validieren)
   - Nachtraegliche Herstellungskosten erhoehen die Bemessungsgrundlage bei gleichem
     AfA-Satz; bei anerkanntem Restnutzungsdauer-Gutachten werden sie ueber die verkuerzte
     Dauer abgeschrieben
   - AfA beginnt zeitanteilig ab Uebergang Besitz/Nutzen/Lasten (pro rata temporis)

   **Bewegliche Wirtschaftsgueter mit eigener AfA (nicht in die Gebaeude-AfA mischen):**

   | Wirtschaftsgut | AfA-Logik (Richtwerte, mit Steuerberater validieren) |
   |----------------|------------------------------------------------------|
   | Einbaukueche | Einheitliches Wirtschaftsgut, Regel-Nutzungsdauer 10 Jahre; gebraucht mitgekauft: kuerzere Restnutzungsdauer (oft 3-5 Jahre) begruendbar |
   | Haushaltsgeraete einzeln | Bis 800 EUR netto: GWG, Sofortabschreibung im Anschaffungsjahr |
   | Freistehende Garage | Eigenes Wirtschaftsgut, ca. 20 Jahre (5%) |
   | Im Gebaeude integrierte Garage | Teil des Gebaeudes, Gebaeude-AfA |
   | Moebel / Inventar | Eigene AfA; mindert zudem GrESt-Bemessung |
   | Gartenanlage | Eigenes Wirtschaftsgut; Zaun, Parkplatz, Muelleinhausung beim Neubau dagegen i.d.R. unselbststaendig (Gebaeude-Herstellungskosten) |

   Wichtig: Bewegliche Wirtschaftsgueter koennen nur separat abgeschrieben werden, wenn
   ihr Kaufpreisanteil im Kaufvertrag ausgewiesen ist -- eine nachtraegliche Zuordnung
   ist nicht moeglich. Fehlt der Ausweis: als Pruefpunkt fuer den Steuerberater markieren.

   **Red Flag Kernsanierung:** Nach umfassender Sanierung sind drei Faelle zu unterscheiden
   (nachtraegliche HK ueber Rest-AfA / neues Wirtschaftsgut mit neuer AfA / steuerlicher
   Neubau mit neuen Saetzen). Diese Abgrenzung nie selbst entscheiden -- Buchung als
   "AfA-Einordnung durch Steuerberater" kennzeichnen.

5. **USt-Behandlung pruefen** (alle Punkte mit Steuerberater validieren)
   - **Grundsatz:** Vermietung zu Wohnzwecken ist umsatzsteuerfrei (§4 Nr.12 UStG)
   - **Kein Vorsteuerabzug** bei umsatzsteuerfreier Vermietung -- die nicht abziehbare
     Vorsteuer ist Teil der Kosten (brutto buchen)
   - **Option nach §9 UStG:** Nur moeglich bei Vermietung an Unternehmer, die das Objekt
     fuer vorsteuerunschaedliche Umsaetze nutzen. Lohnt vor allem als Vorsteuer-Hebel bei
     hohen Sanierungs-/Anschaffungskosten; erzeugt laufende Erklaerungspflichten
   - **Teiloption (Gewerbe + Wohnen im selben Objekt):** Vorsteuer aus gemischten
     Rechnungen (z.B. Dachsanierung) nach Flaechenanteil der optierten Einheiten aufteilen
   - **Vorsteuerberichtigung §15a UStG:** 10-Jahres-Zeitraum -- Nutzungsaenderung
     (z.B. Gewerbe zu Wohnen) loest anteilige Rueckzahlung gezogener Vorsteuer aus;
     pro Objekt einen 10-Jahres-Tracker fuehren
   - **Kurzfristige Vermietung (< 6 Monate):** USt-pflichtig (§4 Nr.12 S.2 UStG);
     bei geringen Umsaetzen Kleinunternehmerregelung (§19 UStG) pruefen lassen
   - **Stellplaetze:** An den eigenen Wohnungsmieter mitvermietet = umsatzsteuerfreie
     Nebenleistung zur Wohnraummiete. Isoliert an Dritte vermietet = grundsaetzlich
     USt-pflichtig. Getrennte Vertraege koennen gewollt sein (Vorsteuer aus
     Stellplatz-Herstellung) -- Gestaltung dem Steuerberater ueberlassen
   - **Bauleistungen:** Fehlende Freistellungsbescheinigung (§48b EStG) loest
     Bauabzugsteuer aus; auslaendische Bauleister loesen Reverse-Charge-USt (§13b UStG)
     aus -- beide Betraege zaehlen in die 15%-Grenze des Objekts

6. **Zeitliche Zuordnung sicherstellen**
   - **Private Vermietung (Anlage V):** Zufluss-/Abflussprinzip (§11 EStG) -- massgeblich
     ist das Zahlungsdatum, keine Periodenabgrenzung wie in der Bilanz. Regelmaessig
     wiederkehrende Zahlungen um den Jahreswechsel: 10-Tage-Regel beachten
   - **Bilanzierende Gesellschaft (z.B. GmbH):** Periodengerechte Abgrenzung; Achtung:
     Disagio ist dort NICHT sofort abziehbar (nur beim Zufluss-/Abflussprinzip)
   - Disagio bei privater V+V: sofort im Zahlungsjahr abziehbar, marktuebliche
     Deckelung beachten (Richtwert: 5% bei 5 Jahren, 10% bei 10 Jahren Zinsbindung --
     mit Steuerberater validieren)
   - Groesserer Erhaltungsaufwand: Wahlrecht zur Verteilung auf 2-5 Jahre (§82b EStDV)
     als Gestaltungsoption fuer den Steuerberater vermerken, nicht selbst entscheiden
   - **Hausgeld korrekt zerlegen:** Laufendes Hausgeld buchen, aber die Zufuehrung zur
     Instandhaltungsruecklage ist NICHT sofort abziehbar -- erst die tatsaechliche
     Verwendung durch die WEG (laut Eigentuemerabrechnung) wird Werbungskosten.
     Nachzahlung/Guthaben aus der Abrechnung dem Jahr des Zu-/Abflusses zuordnen

6b. **Zins-Zuordnung und 2-Konten-Modell (Praxis-Hinweis)**
   - Schuldzinsen sind nur abziehbar, soweit das Darlehen nachweisbar fuer das
     Vermietungsobjekt verwendet wurde -- die Zuordnung folgt dem Verwendungszweck,
     nicht den gestellten Sicherheiten
   - Wird ein 2-Konten-Modell gefuehrt (Mieteinnahmen auf separatem Einnahmenkonto,
     Objektausgaben kreditiert), muss die Kontentrennung in der Buchhaltung sauber
     abgebildet sein: Zinsen des Vermietungs-Kontokorrents abziehbar, private
     Verwendungen strikt getrennt halten. Vermischte Konten als Red Flag markieren --
     Gestaltung und Anerkennung mit Steuerberater validieren
   - Notarkosten der Grundschuldbestellung sind Finanzierungskosten (sofort abziehbar),
     nicht Anschaffungskosten

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
- [ ] AfA-Saetze sind korrekt (2%, 2,5%, 3% oder degressiv/Sonder-AfA je nach Fall)
- [ ] AfA-Bemessungsgrundlage ist der Gebaeudewert (ohne Grundstueck, ohne separat aktivierte Wirtschaftsgueter); Kaufnebenkosten anteilig enthalten
- [ ] Bewegliche Wirtschaftsgueter (Einbaukueche etc.) laufen auf eigenen AfA-Konten
- [ ] USt-Behandlung ist korrekt (steuerfrei bei Wohnungsvermietung; Teiloption nach Flaeche aufgeteilt)
- [ ] Zeitliche Zuordnung folgt dem richtigen Prinzip (privat: Zufluss/Abfluss; GmbH: Abgrenzung)
- [ ] Hausgeld: Zufuehrung zur Instandhaltungsruecklage nicht als Werbungskosten gebucht
- [ ] Steuerlich strittige Buchungen tragen den Hinweis "mit Steuerberater validieren"
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
| Hohe Instandhaltung bei Neuerwerb (< 3 Jahre ab Nutzen-/Lastenwechsel) | 15%-Grenze beachten | An beleg-sortierer zurueckgeben, Steuerberater informieren |
| Restnutzungsdauer-Gutachten ohne geeignete Gutachter-Qualifikation | Anerkennungsrisiko beim Finanzamt | Qualifikation pruefen (oeffentlich bestellt/vereidigt oder ISO 17024), Steuerberater einbinden |
| Kernsanierung im Steuerjahr | AfA-Einordnung (Rest-AfA / neues WG / Neubau) offen | Nicht selbst entscheiden, Steuerberater-Pruefpunkt |
| Inventar/Einbaukueche ohne Ausweis im Kaufvertrag | Separate AfA nicht moeglich | Als Pruefpunkt markieren, keine eigenmaechtige Aufteilung |
| Darlehen mit gemischter Verwendung (privat + Objekt) | Zinsabzug teilweise gefaehrdet | Verwendungsnachweis anfordern, Steuerberater einbinden |
| Nutzungsaenderung bei Objekt mit USt-Option | Vorsteuerberichtigung §15a droht | 10-Jahres-Tracker pruefen, Steuerberater informieren |
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

## Grenzen des Skills

Dieser Skill bereitet Buchhaltung vor -- er ersetzt keine Steuerberatung. AfA-Saetze,
Grenzwerte, USt-Regeln und Verwaltungsauffassungen aendern sich; jede als "pruefen"
markierte Position und jede Gestaltung (USt-Option, 2-Konten-Modell, §82b-Verteilung,
Restnutzungsdauer-Gutachten) muss der Steuerberater final entscheiden.

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- Steuerliche Grundlagen, AfA-Regelungen, UStG
- `knowledge/kalkulationsformeln.md` -- Berechnungsformeln fuer AfA und Rendite
- `skills/beleg-sortierer/SKILL.md` -- Vorheriger Schritt: Belege klassifizieren (inkl. 15%-Grenzen-Tracking)
- `skills/kaufvertrag-pruefung/SKILL.md` -- Kaufpreisaufteilung und Inventarausweis als AfA-Basis
- `skills/dokument-klassifizierer/SKILL.md` -- Zinsbescheinigungen, Bescheide und Abrechnungen erkennen

