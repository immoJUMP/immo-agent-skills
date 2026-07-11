---
name: beleg-sortierer
description: "Klassifiziert und sortiert Belege fuer Wohnimmobilien-Portfolios nach steuerlicher Wirkung: sofort abziehbarer Erhaltungsaufwand vs. Herstellungskosten vs. anschaffungsnahe Herstellungskosten (15%-Grenze), inkl. Anlage-V-Zuordnung und Objekt-Zuordnung. Nutze diesen Skill wenn du unsortierte Belege hast, Handwerkerrechnungen steuerlich einordnen willst oder die 15%-Grenze nach einem Kauf ueberwachen musst."
---

# Beleg-Sortierer

> Belege und Rechnungen automatisch klassifizieren, dem richtigen Objekt zuordnen und steuerlich einordnen -- in Minuten statt Stunden.

---

## Wann nutzen?

- Vor der Steuererklaerung: Jahresbelege sortieren und kategorisieren
- Laufend: Neue Belege sofort richtig ablegen
- Nach Handwerker-Einsaetzen: Rechnungen steuerlich einordnen (Erhaltungsaufwand vs. Herstellungskosten)
- Wenn der Steuerberater ein fertiges Paket statt einen Schuhkarton bekommen soll

---

## Inputs

Stelle folgende Informationen bereit:

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| `belege` | Ja | Ein oder mehrere Belege (PDF, Scan, Foto) |
| `objekte` | Ja | Liste der eigenen Objekte mit Adresse und Einheiten |
| `steuerjahr` | Ja | Zuordnungsjahr (z.B. 2025) |
| `anschaffungskosten_gebaeude` | Empfohlen | Gebaeude-Anschaffungskosten pro Objekt inkl. anteiliger Kaufnebenkosten (fuer 15%-Grenze) |
| `uebergang_nutzen_lasten` | Empfohlen | Datum Uebergang Besitz/Nutzen/Lasten pro Objekt -- Startpunkt der 3-Jahres-Frist |
| `bisherige_erhaltungsaufwendungen` | Empfohlen | Bereits gebuchte Erhaltungsaufwendungen der letzten 3 Jahre pro Objekt (netto) |
| `zuschuesse` | Optional | Erhaltene/beantragte Foerderungen (KfW, BAFA) und Versicherungserstattungen pro Massnahme |
| `bekannte_lieferanten` | Optional | Liste bekannter Handwerker/Dienstleister mit Zuordnung |

---

## Auftrag

Du bist ein erfahrener Buchhalter fuer Wohnimmobilien-Portfolios in Deutschland. Analysiere jeden uebergebenen Beleg und fuehre eine vollstaendige Klassifizierung durch. Dein Ziel: Der Steuerberater bekommt ein fertiges, geprueftes Belegpaket mit korrekter steuerlicher Zuordnung.

---

## Strategie

1. **Beleg lesen und Grunddaten extrahieren**
   - Rechnungsdatum, Rechnungsnummer, Aussteller
   - Leistungsbeschreibung, Leistungszeitraum
   - Nettobetrag, USt-Betrag, Bruttobetrag
   - Adresse/Objekt-Bezug auf dem Beleg

2. **Dokumenttyp erkennen**
   - Handwerkerrechnung (Sanitaer, Elektro, Maler, Dachdecker, Heizung, etc.)
   - Versicherungsbeitrag (Gebaeudeversicherung, Haftpflicht, Rechtsschutz)
   - Hausgeld-Abrechnung / Wirtschaftsplan
   - Grundsteuerbescheid
   - Zinsbescheinigung / Darlehensabrechnung
   - Verwaltergebuehr
   - Maklerprovision
   - Notar-/Gerichtskosten
   - Gutachterkosten
   - Fahrtkosten-Beleg
   - Buero-/Verwaltungskosten
   - Sonstiger Beleg

3. **Objekt-Zuordnung**
   - Adresse auf dem Beleg mit Objektliste abgleichen
   - Bei Mehrfamilienhaus: Zuordnung zu Gesamtobjekt oder einzelner Einheit
   - Bei unklarer Zuordnung: Als "Zuordnung pruefen" markieren
   - Bei objektuebergreifenden Kosten: Verteilungsschluessel vorschlagen

4. **Steuerliche Klassifizierung**

   Alle Regeln in diesem Abschnitt sind Einordnungshilfen -- die endgueltige steuerliche
   Behandlung immer mit dem Steuerberater validieren.

   **Die fuenf Kategorien:**

   - **Erhaltungsaufwand** (sofort absetzbar als Werbungskosten):
     Reparaturen, Instandhaltung, Erneuerung vorhandener Teile in zeitgemaesser Form.
     Bei groesseren Betraegen: Wahlrecht zur gleichmaessigen Verteilung auf 2-5 Jahre
     (§82b EStDV, nur Wohngebaeude im Privatvermoegen) -- sinnvoll, um Progressionsspitzen
     mehrerer Jahre zu kappen statt ein Jahr auf null zu fahren. Als Option vermerken.
   - **Herstellungskosten** (Abschreibung ueber Nutzungsdauer):
     Erweiterung (Anbau, Aufstockung, Vergroesserung der nutzbaren Flaeche, Substanzmehrung)
     oder Standardhebung. **Standardhebungs-Pruefanker (BFH-Rechtsprechung):** Werden bei
     mindestens 3 der 4 zentralen Ausstattungsmerkmale (Heizung, Sanitaer, Elektro, Fenster)
     innerhalb eines 5-Jahres-Betrachtungszeitraums deutlich verbessert, droht Standardhebung
     -- auch bei "Sanierung in Raten".
     **Bagatellgrenze:** Einzelmassnahmen bis 4.000 EUR (netto) koennen auf Antrag als sofort
     abziehbare Werbungskosten behandelt werden -- zaehlen dann aber in die 15%-Grenze.
   - **Anschaffungsnahe Herstellungskosten** (§6 Abs.1 Nr.1a EStG):
     Wenn Instandsetzungs-/Modernisierungskosten (netto, ohne USt) innerhalb von 3 Jahren
     ab Uebergang Besitz/Nutzen/Lasten 15% der Gebaeude-Anschaffungskosten uebersteigen.
     Details siehe eigener Abschnitt "15%-Grenze im Detail".
   - **Anschaffungskosten** (Teil der AfA-Bemessungsgrundlage):
     Grunderwerbsteuer, Notar, Grundbuch, Makler bei Erwerb. Ausserdem: Baumassnahmen
     **vor erstmaliger Nutzung** bzw. zur Herstellung der Funktionstuechtigkeit -- z.B.
     Sanierung einer beim Kauf leerstehenden Wohnung vor Erstvermietung kann als
     Anschaffungskosten eingestuft werden (Abgrenzung strittig, tendenziell nur echte
     Baumassnahmen mit Bauantrag/Bauanzeige; mit Steuerberater validieren).
     Achtung: Auch so klassifizierte Kosten verbrauchen die 15%-Grenze mit.
   - **Nicht abzugsfaehig**:
     Private Anteile, Tilgung, Bewirtungskosten ohne Geschaeftsbezug,
     Einzahlungen in die WEG-Instandhaltungsruecklage (erst die Entnahme/Verwendung
     durch die WEG ist abziehbar, nicht die Einzahlung).

   **Entscheidungsbaum fuer Handwerker-/Baubelege:**

   1. Bewegliches Wirtschaftsgut (Einbaukueche, Geraete, Moebel)? -> Eigene AfA, zaehlt
      NICHT in die 15%-Grenze des Gebaeudes. Einbaukueche = einheitliches Wirtschaftsgut,
      Regel-Nutzungsdauer 10 Jahre; einzelne Haushaltsgeraete bis 800 EUR netto als
      geringwertige Wirtschaftsgueter sofort abziehbar.
   2. Erweiterung der nutzbaren Flaeche oder Substanzmehrung? -> Herstellungskosten
      (zaehlen NICHT in die 15%-Grenze; unter 4.000 EUR netto Sofortabzugs-Antrag moeglich,
      dann zaehlen sie rein).
   3. Eines der 4 zentralen Ausstattungsmerkmale (Heizung/Sanitaer/Elektro/Fenster) und schon
      2 weitere davon in den letzten 5 Jahren modernisiert? -> Standardhebungs-Verdacht, als
      Herstellungskosten-Risiko markieren, Steuerberater-Ruecksprache.
   4. Objekt vor weniger als 3 Jahren erworben (ab Nutzen-/Lastenwechsel)? -> In
      15%-Grenzen-Tracking aufnehmen (Netto-Betrag).
   5. Sonst -> Erhaltungsaufwand, sofort abziehbar (ggf. §82b-Verteilung als Option).

   **Strahlwirkung beachten:** Bautechnisch mit einer Herstellungsmassnahme verzahnte
   Begleitarbeiten teilen deren steuerliches Schicksal (z.B. Malerarbeiten im Zuge einer
   Dachaufstockung). Nicht verzahnte Arbeiten bleiben Erhaltungsaufwand. Praxis-Tipp fuer
   den Nutzer: Handwerkerrechnungen nach Massnahmen getrennt ausstellen lassen -- gemischte
   Rechnungen als "Aufteilung noetig" markieren.

4b. **15%-Grenze im Detail** (§6 Abs.1 Nr.1a EStG -- alle Punkte mit Steuerberater validieren)

   **Grundmechanik:**
   - Bemessungsgrundlage: Gebaeudeanteil der Anschaffungskosten INKL. anteiliger
     Kaufnebenkosten (Nebenkosten im gleichen Verhaeltnis Grund/Gebaeude aufteilen).
   - Vergleichswert: Netto-Sanierungskosten (ohne USt). Faustregel: 15% netto entsprechen
     ca. 17,85% brutto bei 19% USt.
   - Fristbeginn: Uebergang Besitz/Nutzen/Lasten (nicht Notartermin, nicht Kaufpreiszahlung).
   - Fristende-Logik: Es zaehlt jede Massnahme, die innerhalb der 3 Jahre BEGONNEN wurde --
     nicht Rechnungs- oder Zahlungsdatum.
   - Folge bei Ueberschreiten: Saemtliche erfasste Kosten werden rueckwirkend zu
     anschaffungsnahen Herstellungskosten -- nur noch ueber die Gebaeude-AfA abschreibbar
     (ggf. verkuerzbar per Restnutzungsdauer-Gutachten).

   **Was zaehlt rein, was nicht:**

   | Zaehlt in die 15%-Grenze | Zaehlt NICHT rein |
   |--------------------------|-------------------|
   | Instandsetzungs- und Modernisierungskosten (netto) | Jaehrlich anfallende Erhaltungsarbeiten (Wartung) |
   | Auch als Anschaffungskosten eingestufte Renovierung (verbraucht Grenze mit) | Erweiterungen / Flaechenvergroesserung (echte HK) |
   | Herstellungskosten unter 4.000 EUR bei Sofortabzugs-Antrag | Einbaukueche und andere selbststaendige bewegliche Wirtschaftsgueter |
   | Entnahmen aus der WEG-Instandhaltungsruecklage fuer Sanierungen (WEG-Protokolle pruefen!) | Selbststaendige Nebengebaeude (freistehende Garagen, Huetten) inkl. deren Abriss |
   | Bauabzugsteuer- und Reverse-Charge-Betraege auf Bauleistungen | Entruempelung / Entmuellung |
   | Abriss alter Gebaeudeteile im Zuge der Modernisierung (z.B. Terrasse) | Beseitigung von Schaeden, die nachweislich erst NACH Anschaffung durch Dritte verursacht wurden (BFH IX R 6/16), inkl. mutwilliger Mieterschaeden |

   **Korrekturposten:** Zuschuesse (KfW, BAFA) und Versicherungserstattungen werden von den
   Kosten abgezogen -- sie schaffen Luft in der 15%-Grenze. Zufluss und Zuordnung dokumentieren.

   **Umgehungs-Red-Flags** (nicht selbst empfehlen, nur erkennen und markieren):
   - Sanierung vor dem Nutzen-/Lastenwechsel: Fristbeginn strittig, nur mit Steuerberater.
   - Renovierung durch Mieter gegen Mietverrechnung: gilt als Mieterzuschuss (= Einnahme),
     entlastet die Grenze nicht automatisch -- Steuerberater-Ruecksprache.

5. **Namenskonvention anwenden**
   - Format: `YYYY-MM-DD_Dokumenttyp_BetragEUR`
   - Beispiele:
     - `2024-03-15_Handwerkerrechnung_2450EUR`
     - `2024-01-02_Grundsteuerbescheid_890EUR`
     - `2024-06-30_Zinsbescheinigung_4200EUR`
     - `2024-09-01_Versicherung_320EUR`

6. **Werbungskosten-Kategorie zuweisen (Anlage V)**
   - AfA (Zeile 33-34)
   - Schuldzinsen (Zeile 37) -- auch Disagio (sofort im Zahlungsjahr, Deckelung beachten)
     und Finanzierungsnebenkosten wie Notarkosten der Grundschuldbestellung
   - Erhaltungsaufwand (Zeile 39-40) -- ggf. §82b-Verteilung auf 2-5 Jahre vermerken
   - Grundsteuer (Zeile 46)
   - Versicherungen (Zeile 47)
   - Verwaltungskosten (Zeile 48)
   - Sonstige Werbungskosten (Zeile 49-50) -- Fahrtkosten, Fortbildung, Buerokosten

   **Zeitliche Zuordnung:** Bei privater Vermietung gilt das Zufluss-/Abflussprinzip --
   massgeblich ist das ZAHLUNGSdatum, nicht Rechnungs- oder Leistungsdatum. Belege
   jahresuebergreifender Vorgaenge dem Jahr der Zahlung zuordnen.

   **Typische Zuordnungsfehler vermeiden** (mit Steuerberater validieren):

   | Fehler | Richtig |
   |--------|---------|
   | Grunderwerbsteuer als Werbungskosten gebucht | Grunderwerbsteuer = Anschaffungskosten (AfA); nur Grundsteuer ist sofort abziehbar |
   | Hausgeld komplett als Werbungskosten | Zufuehrung zur Instandhaltungsruecklage herausrechnen -- erst die VERWENDUNG durch die WEG ist abziehbar (Eigentuemerabrechnung pruefen) |
   | Notarkosten pauschal als Anschaffungskosten | Notarkosten der Grundschuldbestellung sind Finanzierungskosten (sofort abziehbar), Notarkosten des Kaufvertrags sind Anschaffungskosten |
   | Fahrtkosten pauschal 30 Cent/km bei Dienstwagen | Bei Dienstwagen (1%-Regelung) keine km-Pauschale ansetzbar; beim Privat-PKW sind tatsaechliche km-Kosten moeglich (Verwaltungspraxis deckelt hohe Saetze) |
   | Tilgung als Aufwand | Nur Zinsen sind Werbungskosten, Tilgung nie |
   | Einbaukueche in Erhaltungsaufwand | Eigenes Wirtschaftsgut mit eigener AfA (Regel: 10 Jahre; gebrauchte Kueche: kuerzere Restnutzungsdauer begruendbar) |
   | Kosten vor dem Kauf verworfen | Besichtigungsfahrten, Gutachten, Fortbildung koennen vorweggenommene Werbungskosten sein -- sammeln und kennzeichnen |

7. **Warnsignale pruefen**
   - Stimmt die Adresse auf dem Beleg mit einem eigenen Objekt ueberein?
   - Gibt es bereits eine Rechnung mit gleicher Rechnungsnummer (Duplikat)?
   - Ist der Betrag ungewoehnlich hoch fuer die Leistungsart?
   - Fehlt eine Leistungsbeschreibung?
   - Stimmt der Leistungszeitraum mit dem Steuerjahr ueberein?
   - Ist der Aussteller ein bekannter Lieferant?
   - Ist die USt korrekt ausgewiesen (7% vs. 19%)?

---

## Ausgabeformat

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext.

**Im Chat:** der unten gezeigte Markdown-Bericht (Beleguebersicht).
**Als Datei:** maschinenlesbare Daten fuer die Weiterverarbeitung (z.B. CSV-Belegliste fuer den Steuerberater oder den DATEV-Vorbereitungs-Skill) schreibst du in eine Datei und bietest sie an -- niemals als Rohdaten in den Chat.

### Zusammenfassung (Freitext)

2-4 Saetze: Wie viele Belege verarbeitet, Gesamtsumme, wichtigste Auffaelligkeiten, was der Steuerberater noch klaeren muss.

### Beleguebersicht (Bericht)

```markdown
# Beleg-Sortierung: Steuerjahr 2025

**Verarbeitet am:** 15.11.2025 | **47 Belege** | **Gesamtsumme brutto: 34.250,00 EUR**

## Belegliste

| Nr. | Datum | Beleg | Aussteller | Objekt | Brutto | Steuerliche Einordnung | Anlage V | Status |
|-----|-------|-------|------------|--------|--------|------------------------|----------|--------|
| BEL-2025-001 | 15.03.2025 | Handwerkerrechnung (Sanitaer), RE-2025-0734 | Mueller Sanitaer GmbH | Musterstr. 12, Duesseldorf, WE 3 | 2.450,00 EUR | Erhaltungsaufwand (sofort absetzbar) | Zeile 39 | 🟢 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Beleg im Detail: BEL-2025-001

| | |
|---|---|
| Empfohlener Dateiname | 2025-03-15_Handwerkerrechnung_2450EUR |
| Originaldatei | scan_0042.pdf |
| Belegtyp | Handwerkerrechnung (Sanitaer) |
| Rechnungsdatum / -nummer | 15.03.2025 / RE-2025-0734 |
| Aussteller | Mueller Sanitaer GmbH (USt-ID DE123456789) |
| Leistung | Austausch defekter Mischbatterie Kueche, WE 3 |
| Leistungszeitraum | 10.03.2025 - 15.03.2025 |
| Betraege | Netto 2.058,82 EUR + 19% USt 391,18 EUR = Brutto 2.450,00 EUR |
| Objekt-Zuordnung | Musterstrasse 12, 40210 Duesseldorf, WE 3 (Konfidenz 95% -- Adresse und Einheit auf Rechnung genannt) |
| Steuerliche Einordnung | **Erhaltungsaufwand**, sofort absetzbar -- Austausch defekter Armatur = Reparatur, keine Verbesserung ueber urspruenglichen Zustand |
| Anlage V | Zeile 39 (Erhaltungsaufwand) |
| 15%-Grenze (anschaffungsnah) | Relevant (Anschaffung vor 2 Jahren). Kumuliert 8,5% von 15% -- 🟢 unter Grenze, Restbudget 9.750,00 EUR |
| Auffaelligkeiten | Keine |
| Konfidenz | 92% |

(Gleiche Detailstruktur fuer alle weiteren Belege; bei vielen Belegen Details nur fuer
Belege mit Auffaelligkeiten oder unklarer Zuordnung ausschreiben.)

## Summen nach Kategorie

| Kategorie | Anzahl | Summe brutto |
|-----------|--------|--------------|
| Erhaltungsaufwand | 12 | 15.400,00 EUR |
| Herstellungskosten | 2 | 8.500,00 EUR |
| Schuldzinsen | 1 | 4.200,00 EUR |
| Grundsteuer | 2 | 1.780,00 EUR |
| Versicherungen | 4 | 1.920,00 EUR |
| Verwaltungskosten | 6 | 2.450,00 EUR |

## Summen nach Objekt

| Objekt | Belege | Summe brutto |
|--------|--------|--------------|
| Musterstrasse 12, 40210 Duesseldorf | 28 | 22.100,00 EUR |
| Beispielweg 5, 50667 Koeln | 19 | 12.150,00 EUR |

## Zu klaerende Belege

| Beleg | Problem | Schwere | Hinweis |
|-------|---------|---------|---------|
| BEL-2025-023 | Adress-Abweichung | 🔴 hoch | Adresse auf Rechnung stimmt mit keinem Objekt ueberein |
| BEL-2025-031 | Duplikat-Verdacht | 🟡 mittel | Gleiche Rechnungsnummer wie BEL-2025-018 |
| BEL-2025-045 | Ungewoehnlich hoher Betrag | 🟡 mittel | Betrag 12.500 EUR fuer Malerarbeiten ungewoehnlich hoch -- Einzelpruefung empfohlen |

## Datei fuer den Steuerberater

Belegliste als CSV geschrieben: `beleg-sortierung_2025.csv` (alle Belege mit saemtlichen Feldern, maschinenlesbar fuer die Weiterverarbeitung)
```

---

## Qualitaetspruefung

Vor der Ausgabe pruefen:

- [ ] Jeder Beleg hat einen eindeutigen Dokumenttyp
- [ ] Jeder Beleg ist genau einem Objekt zugeordnet (oder als unklar markiert)
- [ ] Steuerliche Klassifizierung ist begruendet (nicht nur benannt)
- [ ] Dateiname folgt der Konvention YYYY-MM-DD_Typ_BetragEUR
- [ ] Anlage-V-Zeile ist fuer jeden Beleg angegeben
- [ ] 15%-Grenze fuer anschaffungsnahe Herstellungskosten ist geprueft (wenn Anschaffung < 3 Jahre ab Nutzen-/Lastenwechsel), Tracking mit NETTO-Betraegen
- [ ] Die 4 zentralen Ausstattungsmerkmale (Heizung/Sanitaer/Elektro/Fenster) der letzten 5 Jahre sind gezaehlt (Standardhebungs-Check nach BFH)
- [ ] Bewegliche Wirtschaftsgueter (Einbaukueche etc.) sind aus der 15%-Grenze herausgenommen
- [ ] Zufluss-/Abflussprinzip: Belege sind dem Jahr der Zahlung zugeordnet
- [ ] Alle Betraege sind rechnerisch korrekt (Netto + USt = Brutto)
- [ ] Steuerlich strittige Einordnungen tragen den Hinweis "mit Steuerberater validieren"
- [ ] Zusammenfassung nach Kategorie und Objekt stimmt mit Einzelbelegen ueberein

---

## Warnsignale

| Signal | Bedeutung | Aktion |
|--------|-----------|--------|
| Adresse stimmt nicht | Beleg gehoert moeglicherweise nicht zum Portfolio | Manuell pruefen |
| Doppelte Rechnungsnummer | Moegliches Duplikat | Mit Original vergleichen |
| Ungewoehnlich hoher Betrag | Betrag > 200% des Durchschnitts fuer diese Kategorie | Einzelpruefung |
| Fehlende Leistungsbeschreibung | Steuerliche Zuordnung unsicher | Beim Lieferanten nachfragen |
| Leistungszeitraum passt nicht | Zufluss/Abfluss pruefen | Dem Jahr der Zahlung zuordnen |
| 15%-Grenze nahe (> 10% kumuliert) | Anschaffungsnahe Herstellungskosten drohen | Steuerberater informieren, weitere Massnahmen vor Beauftragung pruefen |
| 3 von 4 zentralen Ausstattungsmerkmalen in 5 Jahren | Standardhebung = Herstellungskosten droht | Steuerberater-Ruecksprache VOR weiterer Beauftragung |
| Gemischte Rechnung (HK + Erhaltung) | Strahlwirkung moeglich | Aufteilung anfordern, getrennte Rechnungen empfehlen |
| Rechnung auslaendischer Bauleister | Reverse-Charge-USt (Steuerschuld wechselt) | Steuerberater einbinden, Betrag zaehlt in 15%-Grenze |
| Fehlende Freistellungsbescheinigung Bauleistung (§48b) | Bauabzugsteuer-Risiko (15% einbehalten) | Bescheinigung vom Handwerker anfordern |
| Sanierungsbeleg vor Nutzen-/Lastenwechsel | Fristbeginn und Zuordnung strittig | Steuerberater-Ruecksprache |
| WEG-Sonderumlage oder Ruecklagen-Entnahme fuer Sanierung | Zaehlt in die 15%-Grenze | WEG-Protokolle anfordern, in Tracking aufnehmen |
| Zuschuss/Foerderung (KfW, BAFA) auf Massnahme | Kuerzt Kosten und 15%-Volumen | Zuschuss der Massnahme zuordnen, Behandlung mit Steuerberater klaeren |
| USt-Ausweis fehlt | Vorsteuerabzug nicht moeglich | Korrigierte Rechnung anfordern |
| Eigenleistung vermutet | Materialrechnung ohne Arbeitskosten | Als Eigenleistung kennzeichnen (nur Material abziehbar) |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Adresse auf Beleg unklar | Beleg als "Zuordnung pruefen" markieren, alle moeglichen Objekte auflisten |
| Anschaffungskosten unbekannt | 15%-Pruefung als "nicht durchfuehrbar" markieren, Hinweis an Nutzer |
| Leistungsbeschreibung vage | Konservativ als "steuerliche Einordnung unsicher" markieren |
| Steuerjahr unklar | Nach Rechnungsdatum UND Leistungszeitraum aufteilen |
| Objektliste fehlt | Adressen aus Belegen extrahieren und zur Bestaetigung vorlegen |

---

## Konfidenz-Bewertung

| Stufe | Wert | Bedeutung |
|-------|------|-----------|
| Hoch | >= 0.90 | Alle Daten eindeutig, Zuordnung sicher |
| Mittel | 0.70 - 0.89 | Zuordnung wahrscheinlich, einzelne Unsicherheiten |
| Niedrig | 0.50 - 0.69 | Mehrere Interpretationen moeglich, manuelle Pruefung noetig |
| Unsicher | < 0.50 | Beleg nicht lesbar oder nicht zuordenbar |

---

## Grenzen des Skills

Dieser Skill sortiert und markiert -- er ersetzt keine Steuerberatung. Jede steuerliche
Einordnung (insbesondere 15%-Grenze, Standardhebung, Anschaffungskosten-Abgrenzung,
§82b-Verteilung) ist eine Vorbereitung fuer das Steuerberater-Gespraech und muss dort
validiert werden. Grenzwerte und Verwaltungsauffassungen koennen sich aendern.

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- BGB-Mietrecht, steuerliche Grundlagen
- `knowledge/checklisten.md` -- Belegpruefung, Jahresabschluss
- `skills/datev-vorbereitung/SKILL.md` -- Naechster Schritt: Buchungssaetze erstellen
- `skills/dokument-klassifizierer/SKILL.md` -- Dokumenttyp-Erkennung fuer unbekannte Belege
- `skills/kaufvertrag-pruefung/SKILL.md` -- Kaufpreisaufteilung und Inventarausweis im Kaufvertrag (Basis fuer 15%-Grenze und AfA)
- `skills/nebenkosten-pruefer/SKILL.md` -- Hausgeld-/Nebenkostenabrechnungen im Detail
- `skills/ordner-architekt/SKILL.md` -- Ablagestruktur fuer das sortierte Belegpaket
