---
name: nebenkosten-pruefer
description: "Prueft Betriebskosten- und Heizkostenabrechnungen fuer deutschen Wohnraum auf Vertragsmodell, Form, Umlagefaehigkeit, Verteilung, Fristen und Rechenfehler. Nutze diesen Skill vor Versand, bei Mieter-Einwendungen oder zur Kontrolle einer WEG-/Verwalterabrechnung."
---

# Nebenkosten-Pruefer -- Betriebskostenabrechnung belastbar pruefen

## Wann nutzen

- Betriebskostenabrechnung vor Versand an Mieter pruefen
- Abrechnung eines Verwalters oder einer WEG in eine Mieterabrechnung ueberfuehren
- Mietereinwendungen und Belegeinsichtsverlangen vorsortieren
- Umlagefaehigkeit einzelner Kostenpositionen nach BetrKV pruefen
- Heiz- und Warmwasserkosten nach HeizkostenV und CO2KostAufG pruefen
- Vorauszahlung oder Betriebskostenpauschale rechtlich getrennt bewerten
- Abrechnung bei Mieterwechsel oder Eigentuemerwechsel vorbereiten

**Nicht als Standardpruefung verwenden fuer:** Gewerberaum, Mischobjekte mit wesentlicher Gewerbenutzung, preisgebundenen Wohnraum oder internationale Mietverhaeltnisse. Diese Faelle als `SPEZIALPRUEFUNG` markieren und fachkundigen Rat empfehlen.

---

## Verbindliche Referenz

Lies vor der Pruefung `references/nebenkosten-pruefung.md`. Die Datei enthaelt Rechtsanker, Stop-Regeln und Regressionstests fuer typische Fehlkonstellationen.

**Quellenhierarchie:**

1. Aktuelle Gesetze und einschlaegige hoechstrichterliche Rechtsprechung
2. Mietvertrag, Nachtraege, Abrechnung, Rechnungen und Messdaten des konkreten Falls
3. Verwalter- und Messdienstunterlagen als Tatsachenquelle
4. Regressionstests nur als Suchsignal, niemals als alleinige Rechtsgrundlage

Behaupte bei ungepruefter oder strittiger Rechtslage keine Rechtssicherheit. Markiere den Befund als `RECHTLICH PRUEFEN` und nenne die konkrete offene Frage.

---

## Inputs

| Feld | Pflicht | Beschreibung |
|---|---:|---|
| `billing_statement` | Ja | Abrechnung als PDF, Bild, Tabelle oder Text |
| `billing_period` | Ja | Beginn und Ende des Abrechnungszeitraums |
| `lease_agreement_clauses` | Fuer Endurteil | Betriebskosten-, Pauschal-, Umlage- und Heizkostenklauseln inkl. Nachtraege |
| `delivery_date` | Fuer Fristpruefung | Nachweisbares Zugangsdatum beim Mieter |
| `property_data` | Fuer Verteilung | Wohn-/Nutzflaeche, Einheiten, Leerstand, Gebaeudeart, WEG/MFH, Eigennutzung Vermieter |
| `unit_data` | Fuer Verteilung | Einheit, Flaeche, Nutzungszeitraum, Zaehlerstaende, Verbrauch, Personen nur falls Schluessel |
| `prepayments` | Fuer Saldo | Tatsaechlich geleistete Vorauszahlungen je Monat, nicht nur Sollwert |
| `invoices_and_contracts` | Fuer Materialpruefung | Rechnungen, Leistungszeitraeume, Hauswart-Taetigkeiten, Wartungs- und Messdienstvertraege |
| `heating_data` | Falls zentral | Energietraeger, Eigenversorgung/Waermelieferung, Gesamtkosten, Verbrauchswerte, Geraetetyp, Fernablesbarkeit, Warmwasser-Messung, Waermepumpen- und PV-Strom |
| `co2_data` | Falls anwendbar | CO2-Menge, CO2-Kosten, Wohnflaeche, Einstufung und Vermieteranteil |
| `weg_statement` | Bei ETW | WEG-Jahresabrechnung, Wirtschaftsplan, umlagefaehige/nicht umlagefaehige Aufteilung |
| `previous_billing` | Optional | Vorjahr fuer Trend- und Plausibilitaetspruefung |
| `tenant_objection` | Optional | Wortlaut, Zugangsdatum, betroffene Positionen und verlangte Belege |
| `ownership_change` | Optional | Grundbuchumschreibung, Nutzen-Lasten-Wechsel und Kaufvertragsregelung |

Personenbezogene Daten im Bericht minimieren. Namen, Kontodaten und unnoetige Identifikatoren nicht wiederholen.

---

## Auftrag

Pruefe die Abrechnung aus Sicht eines sorgfaeltigen deutschen Bestandshalters. Ziel ist kein juristisch klingender Text, sondern eine belastbare Entscheidung:

1. Darf ueberhaupt abgerechnet werden?
2. Ist die Abrechnung nachvollziehbar und fristgerecht?
3. Sind nur vereinbarte, laufende und umlagefaehige Kosten enthalten?
4. Stimmen Schluessel, Heizkostenregeln, CO2-Aufteilung und Berechnungen?
5. Welche Korrektur ist vor Versand oder als Antwort auf den Mieter erforderlich?

**Nie raten:** Fehlende Werte nicht erfinden. Nicht pruefbare Punkte bleiben `⚪ NICHT PRUEFBAR` und werden in einer priorisierten Datenanforderung gesammelt.

---

## Strategie

### 0. Fall eingrenzen

Ermittle zuerst:

- Nutzerrolle: Vermieter, Verwalter, Kaeufer oder Mieter
- Wohnraum oder Spezialfall
- MFH, vermietete ETW oder Gebaeude mit hoechstens zwei Wohnungen und Vermieter-Eigennutzung
- Vorauszahlung, Pauschale, Inklusivmiete, Mischmodell oder unklar
- zentrale oder dezentrale Heiz-/Warmwasserversorgung
- normaler Bestand, Mieterwechsel oder Eigentuemerwechsel

Wenn Wohnraumart oder Vertragsmodell unklar ist, keine abschliessende Ampel ausgeben. Zuerst die fehlenden Vertragsstellen anfordern.

### 1. Vertragsmodell als Stop-Gate pruefen

#### Vorauszahlung

- Ueber Vorauszahlungen ist jaehrlich abzurechnen (§ 556 Abs. 3 BGB).
- Nachforderung oder Guthaben aus der korrigierten Abrechnung ermitteln.
- Anpassung erst nach Abrechnung und nur auf angemessene Hoehe nach § 560 Abs. 4 BGB.

#### Pauschale

- Keine normale Jahresabrechnung mit Nachforderung simulieren.
- Erhoehung nur bei wirksamer Anpassungsklausel und nachvollziehbarer Erklaerung nach § 560 Abs. 1 BGB pruefen.
- Kostensenkungen muessen nach § 560 Abs. 3 BGB weitergegeben werden.
- HeizkostenV-Vorrang und Ausnahmen gesondert pruefen.

#### Inklusiv- oder Bruttowarmmiete

- Keine separate kalte Betriebskostenumlage unterstellen.
- HeizkostenV und Sonderausnahmen separat bewerten.

#### Unklare oder fehlende Klausel

- Keine Umlagefaehigkeit und keinen gesetzlichen Flaechenschluessel unterstellen.
- Ergebnis: `⚪ NICHT ABSCHLIESSEND PRUEFBAR`.
- Mietvertrag und Nachtraege anfordern.

**Wichtig:** § 556a BGB bestimmt den Schluessel, wenn Betriebskosten zu tragen sind. Die Vorschrift ersetzt nicht die vorgelagerte Umlagevereinbarung.

### 2. Formelle Nachvollziehbarkeit und Fristen

Pruefe und trenne formelle von materiellen Fehlern:

- Abrechnungsobjekt und Einheit eindeutig?
- Abrechnungszeitraum angegeben und als jaehrlicher Zeitraum plausibel? Zeitraum nicht schematisch als exakt zwoelf Monate erzwingen, sondern Abweichung begruenden und rechtlich pruefen.
- Gesamtkosten je Position erkennbar?
- Umlageschluessel je Position angegeben?
- Mieteranteil aus Gesamtkosten und Schluessel nachvollziehbar?
- Tatsaechliche Vorauszahlungen abgezogen?
- Saldo klar ausgewiesen?
- Abrechnung dem richtigen Mieter und Vertragsverhaeltnis zugeordnet?

**Zugang:**

- Fristende = Ende des zwoelften Monats nach Ende des Abrechnungszeitraums.
- Bei verspaetetem Zugang ist eine Vermieternachforderung grundsaetzlich ausgeschlossen.
- Immer abfragen, ob der Vermieter die Verspaetung nicht zu vertreten hat; Ausnahme nicht erfinden.
- Mieterguthaben nicht wegen Fristversaeumnis streichen.
- Bei Einwendungen zwoelfmonatige Einwendungsfrist ab Zugang und gesetzliche Ausnahme pruefen.
- Belegeinsicht als berechtigtes Verfahrensrecht behandeln; elektronische Bereitstellung ist nach § 556 Abs. 4 BGB moeglich.

Jeden Befund als `formell`, `materiell`, `Frist` oder `nicht pruefbar` klassifizieren.

### 3. Umlagefaehigkeit je Kostenposition

Pruefe fuer jede Position in dieser Reihenfolge:

1. Ist die Kostenart mietvertraglich uebertragen?
2. Ist sie laufend im Sinn von § 1 BetrKV?
3. Ist sie in § 2 BetrKV erfasst oder als sonstige Betriebskosten konkret vereinbart?
4. Enthalten Rechnung oder Leistungsbeschreibung nicht umlagefaehige Anteile?
5. Wurde die Position bereits an anderer Stelle angesetzt?
6. Ist der Betrag wirtschaftlich plausibel und belegt?

**Typische Trennungen:**

| Position | Pruefung |
|---|---|
| Hauswart | Lohn, Sozialbeitraege und geldwerte Leistungen nur fuer umlagefaehige Aufgaben; Verwaltung, Reparatur, Erneuerung und Instandhaltung herausrechnen; Doppelansatz verhindern |
| Wartung | Regelmaessige Funktions-/Sicherheitspruefung von Reparatur und Ersatzteilen trennen |
| Wasserzaehler / Messtechnik | Miete, Eichung, Verwendung, Kauf und Erneuerung getrennt pruefen; Kauf nicht automatisch ueber Jahre verteilen |
| Abrechnungserstellung | Kosten der Heizkosten-Berechnung/-Aufteilung von allgemeinen Kosten der Betriebskostenabrechnung trennen; allgemeine Erstellung ist Verwaltung |
| Rauchwarnmelder | Miete ist nach BGH VIII ZR 379/20 nicht umlagefaehig; Kauf und Wartung getrennt gegen Vertrag und aktuelle Rechtslage pruefen |
| Kabel / Breitband | Rechtslage seit 1. Juli 2024 anwenden; alte Grundgebuehren nicht ungeprueft weiter umlegen |
| Sonstige Betriebskosten | Konkrete Benennung im Mietvertrag und laufenden Charakter verlangen |
| Eigenleistung Vermieter | Vergleichbare Drittleistung ohne fiktive Umsatzsteuer als Obergrenze |
| Leerstand | Vermieteranteil nicht auf belegte Einheiten verteilen |
| Verwaltung / Reparatur / Bank / Recht | Entfernen oder als Vermieteranteil ausweisen |

### 4. Umlageschluessel validieren

- Vertraglichen Schluessel je Position erfassen.
- Verbrauchs- oder verursachungsabhaengige Kosten nach erfasstem Verbrauch oder Verursachung verteilen.
- Gesetzlichen Flaechenschluessel nur anwenden, wenn die Umlagepflicht feststeht und keine speziellere Regel greift.
- Bei vermieteter ETW § 556a Abs. 3 BGB pruefen: Ohne abweichende Vereinbarung kann der WEG-Massstab gelten, sofern er billigem Ermessen entspricht.
- Gesamtflaeche, Einzelflaeche, Einheiten, Personenmonate und Nutzungszeitraum gegen Belege pruefen.
- Leerstand im Nenner und als Vermieteranteil korrekt behandeln.
- Schluesselaenderungen auf Zeitpunkt, Textform und Zulassigkeit pruefen.

Rechnung je Position:

`Mieteranteil = umlagefaehige Gesamtkosten x individueller Anteil`

Bei Einheiten- oder Personenschluesseln den Nenner transparent ausweisen. Keine Personenzahl verwenden, wenn Vertrag oder sachlicher Grund fehlen.

### 5. HeizkostenV pruefen

#### Anwendungsbereich

- HeizkostenV geht Vertragsklauseln grundsaetzlich vor.
- Ausnahme des § 2 HeizkostenV fuer Gebaeude mit hoechstens zwei Wohnungen und vom Vermieter selbst bewohnter Einheit pruefen.
- Weitere Ausnahmen nach § 11 HeizkostenV nicht vermuten, sondern belegen.

#### Waermecontracting und Waermepumpen-/PV-Strom

- Zuerst feststellen, ob eine bestehende Eigenversorgung waehrend des Mietverhaeltnisses auf gewerbliche Waermelieferung umgestellt wurde.
- Bei Umstellung § 556c BGB als Stop-Gate anwenden: Betriebskostenuebertragung, Effizienzvoraussetzung, Kostenneutralitaet und Ankuendigung spaetestens drei Monate vorher in Textform muessen belegt sein.
- Kostenvergleich nach WaermeLV anhand der bisherigen Eigenversorgung und der vorgeschriebenen Vergleichszeitraeume pruefen; Contracting-Rate nicht pauschal voll freigeben.
- Bestand die Waermelieferung bereits bei Mietbeginn, Umstellungs-Gate nicht blind anwenden; Mietvertrag, BetrKV, HeizkostenV und Lieferrechnung trotzdem pruefen.
- Bei Waermepumpe den zur Waermeerzeugung verbrauchten Strom separat und nachvollziehbar erfassen. PV-Eigenstrom, Netzbezug, Einspeisung und Allgemeinstrom nicht vermischen.
- Fuer selbst erzeugten PV-Strom keinen frei erfundenen Orts-, Markt- oder Rabattpreis einsetzen. Ohne belastbare Kosten- und Rechtsgrundlage `RECHTLICH PRUEFEN` ausgeben.
- Investition, Abschreibung, Finanzierung und Wartung nicht ungeprueft als Strom- oder Heizkosten tarnen.

#### Verbrauchs-/Grundkostenanteil

- Grundregel: 50 bis 70 Prozent nach erfasstem Verbrauch (§ 7 Abs. 1 HeizkostenV).
- Pflicht zu 70 Prozent im speziellen Altbau-Fall des § 7 Abs. 1 Satz 2 anhand aller Voraussetzungen pruefen.
- Restlichen Anteil nach zulaessiger Flaechen-/Raumgroesse verteilen.

#### Messausstattung und Verbrauchsinformation

- Neuinstallationen seit Dezember 2021 grundsaetzlich fernablesbar.
- Nicht fernablesbare Bestandsausstattung grundsaetzlich bis 31. Dezember 2026 nachruesten oder austauschen; Technik-/Haerteausnahme pruefen.
- Bei Fernablesbarkeit monatliche Verbrauchsinformationen nach § 6a HeizkostenV pruefen.
- Bei Waermepumpen besondere Verbrauchserfassungsfrist und ersten betroffenen Abrechnungszeitraum nach § 12 Abs. 3 HeizkostenV pruefen.

#### Schaetzung bei Erfassungsausfall

- Schaetzung nur bei Geraeteausfall oder anderem zwingenden Grund akzeptieren.
- Nur die Methoden aus § 9a HeizkostenV verwenden: betroffener Raum in vergleichbarem Zeitraum, vergleichbarer Raum im selben Zeitraum oder Gebaeude-/Nutzergruppen-Durchschnitt.
- Schaetzgrund, Bezugsdaten, betroffene Flaeche und Rechenweg anfordern; Simulation oder frei gewaehlter Pauschalwert reicht nicht.
- Bei mehr als 25 Prozent betroffener massgeblicher Flaeche die Sonderverteilung nach § 9a Abs. 2 HeizkostenV anwenden.

#### Nutzerwechsel

- Zwischenablesung fuer die betroffenen Raeume als Regelfall verlangen (§ 9b HeizkostenV).
- Verbrauchskosten nach Zwischenablesung verteilen; uebrige Heizkosten nach Gradtagszahlen oder zeitanteilig, uebrige Warmwasserkosten zeitanteilig.
- Gradtagszahlen nicht anstelle vorhandener Verbrauchswerte fuer den Verbrauchsanteil verwenden.
- Wenn Zwischenablesung technisch unmoeglich oder ungenau ist, Ersatzmassstab und Begruendung dokumentieren.

#### Warmwasser bei verbundener Anlage

- Warmwasser-Waermemenge grundsaetzlich mit Waermezaehler messen.
- Formel `Q = 2,5 x V x (tw - 10)` nur bei unzumutbar aufwaendiger Messung.
- Flaechenersatz nur im weiteren gesetzlichen Ausnahmefall.
- Aktuelle Korrekturfaktoren fuer Erdgas, Waermelieferung und Waermepumpen anwenden.

#### Kuerzungsrechte

Als moeglichen Befund markieren, nicht blind anwenden:

- 15 Prozent bei entgegen der HeizkostenV nicht verbrauchsabhaengiger Abrechnung
- 3 Prozent bei pflichtwidrig fehlender Fernablesbarkeit
- 3 Prozent bei fehlender oder unvollstaendiger Verbrauchsinformation
- 3 Prozent nach CO2KostAufG bei fehlender Aufteilung oder fehlenden Pflichtangaben

Tatbestand, Ausnahme, Bemessungsgrundlage und Ueberschneidung pruefen. Bei Streit `RECHTLICH PRUEFEN` ausgeben.

### 6. CO2-Kosten pruefen

Wenn CO2KostAufG anwendbar ist:

- CO2-Ausstoss pro Quadratmeter und Jahr nach Abrechnungsdaten bestimmen.
- Stufe und Aufteilungsverhaeltnis pruefen.
- Vermieteranteil vor dem Mieteranteil abziehen.
- Mieteranteil, Einstufung und Berechnungsgrundlagen in der Heizkostenabrechnung pruefen.
- Selbstversorgung des Mieters oder Nichtwohngebaeude nicht mit dem Wohngebaeude-Standardfall vermischen.

Fehlen CO2-Angaben trotz erkennbar betroffenem Brennstoff, als schweren Pruefbefund ausweisen.

### 7. Rechnerische Vollpruefung

Rechne jede Position neu, nicht nur Stichproben:

1. Belegsumme und moegliche Gutschriften
2. nicht umlagefaehige Anteile abziehen
3. Leerstands-/Vermieteranteil beruecksichtigen
4. Umlageschluessel anwenden
5. Heiz-/Warmwasser- und CO2-Regeln anwenden
6. alle Mieteranteile summieren
7. tatsaechlich geleistete Vorauszahlungen abziehen
8. korrigierten Saldo berechnen

**Unterjaehrige Nutzung:**

- Zeitabhaengige kalte Kosten sachgerecht zeitanteilig verteilen.
- Verbrauchskosten anhand Zwischenablesung verteilen.
- Fehlen Heiz-Zwischenwerte, zulaessige Schaetz- oder Gradtagsverfahren pruefen.
- Heizkosten nicht pauschal wie kalte Kosten tagesgleich verteilen.

**Leistungszeitraum:** Rechnung, Verbrauchszeitraum und gewaehltes Abrechnungsprinzip dokumentieren. Periodenabweichungen nicht automatisch als Fehler deklarieren; Heizkosten und Sonderfaelle gesondert beurteilen.

Rundungen erst am Ende der jeweiligen Rechenstufe vornehmen. Jede Abweichung in Euro und mit Rechenweg ausweisen.

### 8. WEG-Abrechnung transformieren

Eine WEG-Jahresabrechnung ist nur Rohmaterial:

- Verwaltungskosten, Erhaltungsruecklage und WEG-Sonderumlagen nicht als Zahlungspositionen uebernehmen; zugrunde liegende Ausgaben separat auf Umlagefaehigkeit pruefen. Instandhaltung und Reparaturen entfernen.
- Tatsaechlich angefallene Kosten und Gutschriften pruefen; Wirtschaftsplan, Hausgeldvorauszahlung oder Simulationsrechnung nicht als endgueltigen Kostenbeleg behandeln.
- Gemischte Positionen aufteilen.
- Mietvertraglichen oder nach § 556a Abs. 3 BGB massgeblichen Schluessel anwenden.
- Vorauszahlungen des Mieters abziehen, nicht Hausgeldzahlungen des Eigentuemers.
- Heizkostenabrechnung und CO2-Aufteilung gesondert einbinden.

Bei Eigentuemerwechsel Aussenverhaeltnis zum Mieter und Innenausgleich zwischen Kaeufer/Verkaeufer trennen. Ohne Grundbuchdatum, Nutzen-Lasten-Wechsel und Kaufvertragsregelung keine pauschale Zustaendigkeitsaussage treffen.

### 9. Vorjahres- und Wirtschaftlichkeitspruefung

Falls Vorjahr vorliegt:

- Veraenderung je Position in Euro und Prozent berechnen.
- Neue oder entfallene Positionen identifizieren.
- Schluessel- und Flaechenaenderungen erkennen.
- Auffaellige Preise, Doppelabrechnungen oder ungewoehnliche Verbrauchsspruenge markieren.

Prozentschwellen wie 10 oder 30 Prozent sind nur Risikosignale, keine Rechtsgrenzen. Fordere bei Auffaelligkeit Beleg und Ursache an; erklaere die Steigerung nicht spekulativ mit Inflation oder Energiepreisen.

### 10. Vorauszahlung oder Pauschale anpassen

#### Vorauszahlung

Basis:

`korrigierte umlagefaehige Jahreskosten / 12`

- Tatsaechliche korrigierte Abrechnung verwenden.
- Konkrete, bereits absehbare Kostenveraenderungen nur mit nachvollziehbarer Grundlage einbeziehen.
- Keinen pauschalen 10- oder 15-Prozent-Sicherheitsaufschlag verwenden.
- Erklaerung in Textform und angemessene Hoehe nach § 560 Abs. 4 BGB pruefen.

#### Pauschale

- Nicht mit einer Vorauszahlungsanpassung verwechseln.
- Vertragsklausel, Grund, Berechnung, Wirksamkeitszeitpunkt und Kostensenkung nach § 560 Abs. 1-3 BGB pruefen.

Ziel ist weder kuenstlich niedrige Warmmiete noch Vermieterfinanzierung durch ueberhoehte Vorauszahlungen, sondern die realistisch erwartbare umlagefaehige Kostenhoehe.

### 11. Mietereinwendungen bewerten

- Zugangsdatum der Abrechnung und der Einwendung feststellen.
- Einwendungsfrist und gesetzliche Ausnahme pruefen.
- Jeden Einwand einer Position, einem Betrag und einer Fehlerklasse zuordnen.
- Belegeinsicht organisatorisch ermoeglichen; elektronische Bereitstellung ist zulaessig.
- Unstreitige Guthaben oder Korrekturen nicht wegen anderer Streitpunkte blockieren.
- Bei Klage-, Kuendigungs- oder Verjaehrungsrisiko Fachanwalt empfehlen.

---

## Ausgabeformat

**Keine Rohdaten-Antwort:** Gib kein JSON oder YAML aus. Liefere einen lesbaren Bericht mit Tabellen, Rechenwegen und klaren Aktionen.

### Statuslogik

| Status | Bedeutung |
|---|---|
| 🔴 KORREKTUR NOETIG | belastbarer Rechts-, Vertrags- oder Rechenfehler |
| 🟡 PRUEFUNG NOETIG | Rechtsfrage, Beleg oder Tatsachengrundlage offen |
| 🟢 KEIN FEHLER ERKANNT | im bereitgestellten Umfang bestanden; keine Garantie |
| ⚪ NICHT PRUEFBAR | notwendige Daten fehlen |

Keine erfundene Prozent-Konfidenz ausgeben. Stattdessen Datenabdeckung nennen: `vollstaendig`, `wesentliche Luecken` oder `nur Vorpruefung`.

### Berichtsvorlage

```markdown
# Betriebskosten-Pruefung: [Objekt / Einheit]

**Gesamtergebnis:** 🔴 KORREKTUR NOETIG
**Datenabdeckung:** wesentliche Luecken
**Finanzielle Differenz:** -300,00 EUR zugunsten des Mieters
**Naechste Aktion:** Hauswartrechnung aufteilen, CO2-Anteil korrigieren, danach neu zustellen

## 1. Vertrags- und Fallklassifikation

| Punkt | Feststellung | Status | Grundlage |
|---|---|---|---|
| Vertragsmodell | Vorauszahlung | 🟢 | Mietvertrag § 4 |
| Objektart | vermietete ETW | 🟢 | Abrechnung / Vertrag |
| HeizkostenV-Ausnahme | keine erkennbar | 🟡 | Eigennutzung nicht belegt |

## 2. Fristen und formelle Nachvollziehbarkeit

| Pruefpunkt | Feststellung | Status | Auswirkung |
|---|---|---|---|
| Zugang | 10.04.2026 | 🟢 | Frist eingehalten |
| Gesamtkosten / Schluessel | vorhanden | 🟢 | nachvollziehbar |
| Vorauszahlungen | Soll statt Ist | 🔴 | Saldo neu rechnen |

## 3. Kostenpositionen

| Position | Belegsumme | nicht umlagefaehig | Schluessel | korrigierter Mieteranteil | Status |
|---|---:|---:|---|---:|---|
| Grundsteuer | 4.800,00 EUR | 0,00 EUR | 50/400 qm | 600,00 EUR | 🟢 |
| Hauswart | 3.600,00 EUR | 1.200,00 EUR Reparatur | 1/12 | 200,00 EUR | 🔴 |

## 4. Heizkosten und CO2

| Pruefpunkt | Ergebnis | Status | Korrektur |
|---|---|---|---|
| Verbrauchsanteil | 60 Prozent | 🟢 | keine |
| CO2-Vermieteranteil | fehlt | 🔴 | Stufe und Anteil berechnen |
| Monatsinformation | nicht vorgelegt | ⚪ | Messdienstnachweis anfordern |

## 5. Rechnerische Korrektur

| Kennzahl | Abgerechnet | Korrigiert | Differenz |
|---|---:|---:|---:|
| umlagefaehige Kosten Einheit | 2.400,00 EUR | 2.100,00 EUR | -300,00 EUR |
| geleistete Vorauszahlungen | 1.800,00 EUR | 1.800,00 EUR | 0,00 EUR |
| Nachzahlung | 600,00 EUR | 300,00 EUR | -300,00 EUR |

## 6. Befunde und Aktionen

| Prio | Fehlerklasse | Befund | Grundlage | Aktion |
|---|---|---|---|---|
| 1 | materiell | Reparaturanteil im Hauswart | § 1 Abs. 2 BetrKV | 1.200,00 EUR herausrechnen |
| 2 | materiell | CO2-Anteil fehlt | § 5, § 7 CO2KostAufG | neu berechnen |
| 3 | Datenluecke | HeizKV-Information fehlt | § 6a HeizkostenV | Messdienstunterlage anfordern |

## 7. Datenluecken

1. Mietvertragsseite mit Umlageklausel
2. Hauswart-Leistungsnachweis
3. CO2-Kostenblatt des Versorgers

## 8. Rechtlicher Pruefhinweis

[Konkrete strittige Frage nennen; kein pauschaler Haftungstext als Ersatz fuer Analyse.]
```

---

## Qualitaetspruefung

Vor Ausgabe alle Punkte abhaken:

- [ ] Wohnraum/Spezialfall und Nutzerrolle bestimmt
- [ ] Vorauszahlung, Pauschale, Inklusivmiete oder Mischmodell bestimmt
- [ ] Umlagevereinbarung vor Umlageschluessel geprueft
- [ ] Formelle und materielle Fehler getrennt
- [ ] Zugang, Vermieterfrist, Ausnahme und Mieter-Einwendungsfrist geprueft
- [ ] Jede Position gegen Vertrag, § 1 und § 2 BetrKV geprueft
- [ ] Hauswart, Wartung, Messtechnik, Abrechnungserstellung, Rauchwarnmelder, Kabel und sonstige Kosten getrennt geprueft
- [ ] WEG-Kosten nicht ungeprueft uebernommen
- [ ] Leerstand nicht auf Mieter verschoben
- [ ] HeizkostenV-Anwendungsbereich und Ausnahmen geprueft
- [ ] Waermecontracting und Waermepumpen-/PV-Strom auf eigene Kosten- und Rechtsgrundlage geprueft
- [ ] Verbrauchsanteil, Messung, Fernablesbarkeit und Monatsinformation geprueft
- [ ] Schaetzgrund, §-9a-Methode und 25-Prozent-Schwelle geprueft
- [ ] Bei Nutzerwechsel Zwischenablesung und § 9b HeizkostenV geprueft
- [ ] Warmwasserformel nur im zulaessigen Ausnahmefall verwendet
- [ ] CO2-Stufe, Vermieteranteil und Pflichtangaben geprueft
- [ ] Jede Position vollstaendig nachgerechnet
- [ ] tatsaechliche Vorauszahlungen statt Sollwert verwendet
- [ ] Mieterwechsel verbrauchs- und zeitgerecht abgegrenzt
- [ ] Vorauszahlungsanpassung ohne pauschalen Sicherheitspuffer berechnet
- [ ] Jede Datenluecke als `⚪ NICHT PRUEFBAR` ausgewiesen
- [ ] Keine ungepruefte Rechtsbehauptung und keine erfundene Konfidenz

---

## Warnsignale

| Signal | Risiko | Sofortaktion |
|---|---|---|
| Pauschale plus Nachforderung | falsches Vertragsmodell | Abrechnung stoppen, Vertrag und HeizkostenV pruefen |
| Mietvertrag fehlt | Umlagepflicht unklar | kein Endurteil; Vertrag anfordern |
| Frist abgelaufen | Nachforderung moeglicherweise ausgeschlossen | Nichtvertretenmuessen-Ausnahme dokumentieren und rechtlich pruefen |
| WEG-Abrechnung 1:1 uebernommen | Verwaltung, Ruecklage, Sonderumlage, Reparatur oder falscher Schluessel | zugrunde liegende Ausgaben pruefen und in Mieterabrechnung transformieren |
| Contracting ohne Kostenvergleich oder Drei-Monats-Ankuendigung | § 556c BGB moeglicherweise nicht erfuellt | Umstellung und WaermeLV-Unterlagen als Stop-Gate pruefen |
| PV-/Waermepumpenstrom mit frei gewaehltem Marktpreis | fiktive statt belegter Kosten | Messung, Kostenbasis und Rechtsgrundlage anfordern |
| Schaetzung ohne §-9a-Bezugsdaten | materiell nicht nachvollziehbar | Schaetzgrund, Vergleichsdaten und betroffene Flaeche anfordern |
| Rauchwarnmelder-Miete umgelegt | nach BGH VIII ZR 379/20 nicht umlagefaehig | Mietkosten entfernen; Wartung separat pruefen |
| Hauswart ohne Taetigkeitsnachweis | nicht umlagefaehige Arbeit / Doppelansatz | Leistungsanteile anfordern |
| Kabel-Grundgebuehr nach 30.06.2024 | veraltete Umlage | Position nach aktueller BetrKV korrigieren |
| Heizkosten 100 Prozent nach Flaeche | moegliches 15-Prozent-Kuerzungsrecht | HeizkostenV-Ausnahme und Verbrauchsdaten pruefen |
| Fernablesbar, aber keine Monatsinfo | moegliches 3-Prozent-Kuerzungsrecht | Versand-/Portalnachweis anfordern |
| CO2-Kosten voll beim Mieter | Vermieteranteil und Pflichtangaben fehlen | CO2KostAufG neu rechnen |
| Vorauszahlung plus 10-15 Prozent | unangemessener Pauschalpuffer | nur korrigierte Ist-Basis und konkrete Prognose verwenden |
| Leerstand aus Nenner entfernt | Kostenverschiebung auf Mieter | Vermieteranteil wieder einsetzen |
| Eigentuemerwechsel pauschal bewertet | falsche Innen-/Aussen-Zuordnung | Grundbuch, Nutzen-Lasten und Kaufvertrag getrennt pruefen |

---

## Bei fehlenden Daten

- Ohne Mietvertrag: Keine Umlagepflicht oder Schluessel unterstellen.
- Ohne Gesamtkosten oder Nenner: Mieteranteil nicht berechnen.
- Ohne Zustellungsdatum: Frist als nicht pruefbar markieren.
- Ohne Ist-Vorauszahlungen: Saldo nicht final bestaetigen.
- Ohne Verbrauchs- und Messdaten: HeizkostenV-Pruefung auf belegbare Teilpunkte begrenzen.
- Ohne CO2-Daten bei betroffenem Energietraeger: schweren Datenmangel melden.
- Ohne Hauswart-Leistungsbild: nur eindeutig umlagefaehigen Anteil bestaetigen.
- Ohne WEG-Aufteilung: Hausgeld nicht als umlagefaehige Kosten behandeln.
- Ohne Vorjahr: Trendanalyse auslassen, keine Marktentwicklung erfinden.

---

## Verwandte Wissensdatenbanken und Skills

- `references/nebenkosten-pruefung.md` -- verbindliche Rechtsanker und Regressionstest-Matrix
- `knowledge/rechtsgrundlagen.md` -- allgemeines deutsches Mietrecht
- `knowledge/checklisten.md` -- Verwaltungs- und Due-Diligence-Checklisten
- `skills/mietlisten-parser/SKILL.md` -- Vorauszahlungen und Einheiten aus Mietlisten extrahieren
- `skills/inserat-generator/SKILL.md` -- realistische Nebenkosten fuer Neuvermietung
- `skills/wochen-jourfixe/SKILL.md` -- Abrechnungsfristen verfolgen
- `skills/mahn-assistent/SKILL.md` -- nur korrigierte und faellige Nachforderungen verfolgen
