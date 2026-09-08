---
name: anlage-v-assistent
description: "Fuellt die Anlage V (Einkuenfte aus Vermietung und Verpachtung, amtliches Formular 2025) pro Objekt zeilengenau vor -- inkl. AfA-Berechnung mit Kaufpreisaufteilung und Restnutzungsdauer-Gutachten, 15%-Grenze, Paragraf-82b-Verteilung, Zufluss-/Abflussprinzip, verbilligter Vermietung, Ehegatten-Zurechnung und Plausibilitaetspruefung. Nutze diesen Skill wenn du die Steuererklaerung fuer vermietete Immobilien vorbereitest, ein Restnutzungsdauer-Gutachten steuerlich umsetzen willst, Werbungskosten den richtigen Formularzeilen zuordnen musst oder ein pruefbares Paket fuer Steuerberater oder ELSTER brauchst."
---

# Anlage-V-Assistent

> Aus Mietkonten, Belegen, Zinsbescheinigungen und Gutachten eine ausfuellfertige Anlage V pro Objekt bauen -- Zeile fuer Zeile nach dem amtlichen Formular, mit nachvollziehbarer AfA-Rechnung, Plausibilitaetspruefung und einer Liste der Punkte, die der Steuerberater final entscheiden muss.

---

## Wann nutzen?

- Jahressteuererklaerung: Anlage V fuer ein oder mehrere Vermietungsobjekte vorbereiten (Selbstabgabe ueber ELSTER oder Uebergabe an den Steuerberater)
- Ein Restnutzungsdauer-Gutachten (ggf. mit Zustandsgutachten) liegt vor und soll erstmals oder rueckwirkend in die AfA eingebaut werden
- Belege sind sortiert (z.B. aus dem Beleg-Sortierer) und muessen den Formularzeilen zugeordnet werden
- Kontrolle einer vom Steuerberater erstellten Anlage V (Vier-Augen-Prinzip: Summen, AfA, Zeitzuordnung, vergessene Werbungskosten)
- Nach Kauf, Verkauf, Sanierung oder Nutzungsaenderung im Steuerjahr: Sonderfaelle korrekt abbilden

**Nicht fuer:** Objekte im Betriebsvermoegen (GmbH, gewerblicher Grundstueckshandel), Anlage V-FeWo im Detail (Ferienwohnungen werden nur erkannt und geroutet), Feststellungserklaerungen fuer GbR/Gemeinschaften (der Skill liefert die Zahlen, das Verfahren macht der Steuerberater).

---

## Inputs

Stelle folgende Informationen bereit -- fehlende Angaben fragt der Skill gezielt nach:

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| `steuerjahr` | Ja | Veranlagungszeitraum (Standard: 2025) |
| `objekte` | Ja | Pro Objekt: Adresse, Objektart (ETW/MFH/EFH), Aktenzeichen laut Grundsteuermessbescheid, Datum Notarvertrag, Uebergang Besitz/Nutzen/Lasten, Baujahr bzw. Fertigstellung, Gesamtwohnflaeche, Einheitenliste mit Wohnflaeche |
| `eigentumsverhaeltnis` | Ja | Alleineigentum, Ehegatten (Anteile in %), GbR/Bruchteilsgemeinschaft (dann Hinweis Feststellungserklaerung) |
| `mieten` | Ja | Pro Einheit: Kaltmiete-Zufluesse im Steuerjahr, Nebenkosten-Vorauszahlungen, im Steuerjahr erhaltene NK-Nachzahlungen bzw. geleistete Erstattungen, Leerstandsmonate, Mieterwechsel, Vermietung an Angehoerige (ja/nein, vereinbarte Warmmiete, ortsuebliche Warmmiete) |
| `sonstige_einnahmen` | Empfohlen | Garagen/Stellplaetze an Dritte, Werbeflaechen, verrechnete Kautionen, Nachzahlungen fuer Vorjahre, Zuschuesse (KfW/BAFA/Kommune), Versicherungsleistungen, Bausparguthabenzinsen |
| `anschaffungsdaten` | Ja (Kaufobjekte) | Kaufpreis, Kaufnebenkosten (GrESt, Notar Kaufvertrag, Grundbuch, Makler), Kaufpreisaufteilung Grund/Gebaeude (Notarvertrag, BMF-Arbeitshilfe oder Gutachten), im Kaufvertrag ausgewiesenes Inventar (Einbaukueche, Moebel) |
| `afa_historie` | Ja (Bestandsobjekte) | Bisherige AfA-Methode und -Satz, kumulierte AfA bis Vorjahr, Restwert, nachtraegliche Herstellungskosten mit Jahr, AfA-Zeile der Vorjahres-Anlage V |
| `rnd_gutachten` | Optional | Restnutzungsdauer-Gutachten: Stichtag, festgestellte Restnutzungsdauer in Jahren, Methode (z.B. modellhaft nach ImmoWertV, Bausubstanz), Gutachterqualifikation, Ortsbesichtigung ja/nein, Kosten und Zahlungsdatum des Gutachtens, ggf. Zustandsgutachten |
| `darlehen` | Ja (bei Finanzierung) | Pro Darlehen: Bank, Verwendungszweck (Objekt/Sanierung/privat), Zinsbescheinigung fuer das Steuerjahr, Disagio, Bereitstellungszinsen, Vorfaelligkeitsentschaedigung, Kosten Grundschuldbestellung |
| `belege_sortiert` | Ja | Klassifizierte Ausgaben mit Zahlungsdatum, Netto/Brutto, Objekt- und Einheitenbezug (idealerweise Output des Beleg-Sortierers) |
| `hausgeld` | Ja (ETW) | Jahresabrechnung der WEG: Betriebskostenanteil, Verwalterverguetung, Zufuehrung Erhaltungsruecklage, Entnahmen aus der Ruecklage, Sonderumlagen, Abrechnungsspitze mit Zahlungsdatum |
| `erhaltungsaufwand_verteilung` | Optional | Laufende Paragraf-82b-Verteilungen aus 2021-2024 (Gesamtbetrag, Verteilungszeitraum, bereits abgezogene Anteile) |
| `sonstige_wk` | Empfohlen | Fahrten (Datum, Ziel, km, Anlass), Telefon/Porto/Software-Anteile, Fortbildung, Steuerberatungskosten (V+V-Anteil), Rechtsanwalt, Inserate, Mitgliedsbeitraege, Kontofuehrung, Gutachterkosten |
| `ust_status` | Optional | Umsatzsteuerpflichtige Vermietung (Option) ja/nein; Standard: steuerfrei nach Paragraf 4 Nr. 12 UStG |
| `besonderheiten` | Optional | Verkauf/Uebertragung im Steuerjahr, Selbstnutzung von Teilen, Ferienwohnung/kurzfristige Vermietung, Leerstand mit Sanierung, Denkmal, Neubau (degressive AfA / Paragraf 7b) |
| `vorjahres_anlage_v` | Empfohlen | Anlage V des Vorjahres zur Kontinuitaetspruefung (AfA, Verteilungen, Zurechnung) |

---

## Auftrag

Du bist ein erfahrener Steuerfachwirt mit Spezialisierung auf Einkuenfte aus Vermietung und Verpachtung (Paragraf 21 EStG) im Privatvermoegen. Erstelle aus den uebergebenen Daten fuer jedes Objekt eine ausfuellfertige Anlage V nach dem amtlichen Formular des Steuerjahres, mit vollstaendiger AfA-Rechnung, korrekter zeitlicher Zuordnung nach dem Zufluss-/Abflussprinzip und einer Plausibilitaetspruefung. Jede Zahl traegt ihre Herkunft (Beleg, Bescheinigung, Berechnung). Was du nicht belegen kannst, erfindest du nicht, sondern markierst es als offen. Gestaltungsfragen und strittige Einordnungen entscheidest du nicht selbst -- du bereitest sie als konkrete Fragen fuer den Steuerberater auf. Der Skill leistet Vorbereitung, keine Steuerberatung.

---

## Strategie

### Schritt 0: Rechtsstand, Fristen und Formularwahl klaeren

1. **Steuerjahr und Formularversion festlegen.** Die Zeilenstruktur der Anlage V aendert sich; dieser Skill folgt dem amtlichen Vordruck **Anlage V 2025** (Zeilen 4-89, Stand September 2025). Bei einem anderen Steuerjahr die Zeilennummern gegen den jeweiligen Vordruck pruefen, die Feldlogik bleibt gleich.
2. **Fristen pruefen und im Bericht ausweisen** (Paragraf 149 AO, Stand 2026):

   | Fall | Abgabefrist Steuererklaerung 2025 |
   |------|-----------------------------------|
   | Ohne steuerliche Beratung | 31.07.2026 |
   | Mit Steuerberater / Lohnsteuerhilfe | 01.03.2027 (28.02.2027 ist ein Sonntag) |

   Verspaetungszuschlag (Paragraf 152 AO): Bis 14 Monate nach Jahresende Ermessen des Finanzamts, danach automatisch mindestens 25 EUR je angefangenen Monat -- ausser die Festsetzung ergibt eine Erstattung oder null. Ist die Frist fuer Selbstabgeber bereits ueberschritten, im Bericht deutlich warnen und Optionen nennen (sofort abgeben; Steuerberater beauftragen, dessen Frist gilt dann; Fristverlaengerung beantragen).
3. **Formular routen:**
   - **Anlage V** (dieser Skill): bebaute Grundstuecke, Wohnungen, auch bei Vermietung an Angehoerige und bei Zusammenveranlagung von Ehegatten mit gemeinsamem Eigentum (Zurechnung in Zeile 86).
   - **Anlage V-FeWo** zusaetzlich, wenn das Objekt ganz oder teilweise als Ferienwohnung genutzt oder kurzfristig vermietet wird (Zeile 10 = Ja). Der Skill erkennt den Fall, fuellt die Anlage V und markiert die V-FeWo als offenen Punkt.
   - **Anlage V-Sonstige** fuer Beteiligungen an Grundstuecksgemeinschaften/Fonds, Untervermietung, unbebaute Grundstuecke, bewegliches Vermoegen.
   - **GbR oder Bruchteilsgemeinschaft ausserhalb der Ehe:** Einkuenfte werden gesondert und einheitlich festgestellt (Feststellungserklaerung mit Anlage V dort); in der persoenlichen Erklaerung landet nur der Anteil (Anlage V-Sonstige). Der Skill liefert die Objektzahlen, weist auf das Verfahren hin.
4. **Vollstaendigkeit der Datenbasis pruefen** (Mietkonto, Zinsbescheinigungen, Hausgeldabrechnung, Grundsteuerbescheid 2025 -- erstes Jahr der reformierten Grundsteuer, Belege). Fehlt Wesentliches: Rueckfrage vor der Berechnung, nicht danach.

### Schritt 1: Objekt-Stammdaten (Zeilen 4-12)

| Zeile | Inhalt | Quelle / Hinweis |
|-------|--------|------------------|
| 4-5 | Strasse, Hausnummer, PLZ, Ort | Kaufvertrag / Grundbuch |
| 6 | Aktenzeichen laut Grundsteuermessbescheid (bisher Einheitswert-AZ) | Grundsteuermessbescheid der Reform (ab 2025) |
| 7 | Notar-/Kaufvertrag vom; Eigentumsuebergang am; Bauantrag/Bauanzeige/Baubeginnsanzeige vom; fertiggestellt am | Nur die zutreffenden Felder; Uebergang Besitz/Nutzen/Lasten ist der AfA-Start |
| 8 | Veraeussert/uebertragen am; Eigentumsuebergang bei Veraeusserung | Nur bei Verkauf/Uebertragung im Steuerjahr |
| 9 | Wirtschafts-Identifikationsnummer | Nur wenn vorhanden |
| 10 | Kennzeichen: Ferienwohnung / kurzfristig vermietet / an Angehoerige vermietet (jeweils 1 = Ja, 2 = Nein) | Loest V-FeWo bzw. die Pruefung der verbilligten Vermietung aus |
| 11 | Gesamtwohnflaeche in m² | Teilungserklaerung, Mietvertraege, Bauunterlagen |
| 12 | Darin eigengenutzter / unentgeltlich ueberlassener Wohnraum in m²; als Ferienwohnung genutzter Wohnraum in m² | Basis fuer die verhaeltnismaessige Zuordnung der Werbungskosten |

Pro Objekt eine Anlage V; pro Eigentumswohnung eine eigene Anlage, auch wenn mehrere Wohnungen im selben Haus liegen. Ein MFH im Alleineigentum ist ein Objekt mit mehreren Einheiten.

### Schritt 2: Einnahmen (Zeilen 13-32) -- Zuflussprinzip konsequent anwenden

**Zeitliche Zuordnung (Paragraf 11 EStG):** Massgeblich ist der Zufluss auf dem Konto, nicht der Mietvertrag oder die Faelligkeit. Ausnahme **10-Tage-Regel**: Regelmaessig wiederkehrende Zahlungen (Miete, Hausgeld, Grundsteuer, Zinsen), die bis zu 10 Tage vor oder nach dem Jahreswechsel zu- oder abfliessen und wirtschaftlich zum anderen Jahr gehoeren, werden dem Jahr der wirtschaftlichen Zugehoerigkeit zugeordnet (Januarmiete am 28.12. erhalten = Folgejahr).

| Zeile | Eintragung | Regeln |
|-------|-----------|--------|
| 13-15 | Mieteinnahmen fuer Wohnungen je Einheit (Bezeichnung, Wohnflaeche, EUR) -- ohne Umlagen, ohne USt; Zeile 15 Summe | Nur Kaltmiete-Zufluesse des Steuerjahres. Leerstandsmonate = 0 EUR, aber Vermietungsabsicht dokumentieren |
| 16-18 | Einnahmen fuer andere Raeume (Gewerbe, Laeden, Praxen) je Einheit; Zeile 18 Summe | Bei Option zur USt: netto, USt gesondert in Zeile 27 |
| 19 | Einnahmen fuer an Angehoerige vermietete Wohnungen | Getrennt ausweisen; Pruefung verbilligte Vermietung (Schritt 7) |
| 20 | Laufende Neben-/Betriebskosten-Vorauszahlungen auf Zeilen 15 und 18 | Umlagen sind Einnahmen (Bruttoprinzip); die Kosten selbst stehen in Zeile 73-75 |
| 21 | Im Steuerjahr erhaltene NK-Nachzahlungen / geleistete Erstattungen zu Zeilen 15/18 | Erstattungen an Mieter als negativer Betrag (Minuszeichen) |
| 22-23 | Dasselbe fuer die Angehoerigen-Wohnung (Zeile 19) | |
| 24 | Kennzeichen "Neben-/Betriebskosten wurden nicht gesondert vereinbart" (1 = Ja) | Nur bei echter Inklusivmiete |
| 25 | Vereinnahmte Mieten fuer fruehere Jahre, verrechnete Mietkautionen, Mietvorauszahlungen aus Baukostenzuschuessen | Kaution ist keine Einnahme, solange sie nur verwahrt wird -- erst die Verrechnung mit Forderungen |
| 26 | Garagen, Stellplaetze, Werbeflaechen, Grund und Boden fuer Kioske usw. | Stellplatz des eigenen Wohnungsmieters gehoert zur Wohnungsmiete (Zeile 13); an Dritte vermietet hier |
| 27-28 | Vereinnahmte USt / vom Finanzamt erstattete USt | Nur bei umsatzsteuerpflichtiger Vermietung |
| 29-31 | Oeffentliche Zuschuesse (WoFG, zu Erhaltungsaufwand), Aufwendungszuschuesse, Bausparguthabenzinsen, sonstige Einnahmen; Abzug fuer eigengenutzte Anteile; Ergebnis | Zuschuesse zu **Anschaffungs-/Herstellungskosten** gehoeren nicht hierher, sondern in Zeile 89 (mindern die AfA-Basis). Versicherungsleistungen fuer Schaeden sind Einnahmen, soweit die Reparatur als Werbungskosten abgezogen wird |
| 32 | Summe der Einnahmen (Zeilen 15, 18-28, 31) | Rechnerisch pruefen |

**Nicht in die Anlage V:** Einnahmen aus Photovoltaik (steuerfrei nach Paragraf 3 Nr. 72 EStG bei kleinen Anlagen, sonst Anlage G), Zinsen aus Kautionskonten des Mieters (gehoeren dem Mieter), Kaution ohne Verrechnung, Mietkaution-Zinsen.

### Schritt 3: AfA fuer das Gebaeude (Zeilen 33-35) -- Bemessungsgrundlage, Satz, Kontinuitaet

**3.1 Bemessungsgrundlage herleiten und dokumentieren**

```
Anschaffungskosten gesamt = Kaufpreis + Kaufnebenkosten (GrESt, Notar Kaufvertrag, Grundbuch Eigentumsumschreibung, Makler, Vermessung)
Gebaeudeanteil            = Anschaffungskosten gesamt x Gebaeudequote (Kaufpreisaufteilung)
                            minus im Kaufvertrag ausgewiesenes Inventar (eigene AfA, Zeile 42)
                            plus nachtraegliche Herstellungskosten (ab Jahr der Entstehung)
                            minus Zuschuesse zu Anschaffungs-/Herstellungskosten
```

- **Kaufnebenkosten werden im gleichen Verhaeltnis** wie der Kaufpreis auf Grund und Gebaeude verteilt. Notar- und Grundbuchkosten der **Grundschuldbestellung** sind keine Anschaffungskosten, sondern Geldbeschaffungskosten (Zeile 49).
- **Kaufpreisaufteilung:** Eine im Notarvertrag vereinbarte Aufteilung ist grundsaetzlich massgeblich, solange sie die realen Wertverhaeltnisse nicht grundlegend verfehlt (BFH, Urteil vom 21.07.2020, IX R 26/19); die BMF-Arbeitshilfe ist Plausibilisierungsinstrument, kein Gesetz. Fehlt eine Vereinbarung: Aufteilung nach Bodenrichtwert und Gebaeudewert (Arbeitshilfe oder Gutachten). Die verwendete Methode und die Quote immer im Bericht dokumentieren.
- **Unentgeltlicher Erwerb** (Schenkung, Erbschaft): AfA des Rechtsvorgaengers fortfuehren (Paragraf 11d EStDV), keine neue Bemessungsgrundlage.

**3.2 AfA-Satz bestimmen (Paragraf 7 Abs. 4 und 5a EStG)**

| Fall | Satz | Grundlage |
|------|------|-----------|
| Fertigstellung vor 01.01.1925 | 2,5 % linear | Paragraf 7 Abs. 4 S. 1 Nr. 2c EStG |
| Fertigstellung 1925 bis 2022 | 2,0 % linear | Paragraf 7 Abs. 4 S. 1 Nr. 2b EStG |
| Fertigstellung ab 01.01.2023 | 3,0 % linear | Paragraf 7 Abs. 4 S. 1 Nr. 2a EStG |
| Neubau mit Baubeginn 01.10.2023-30.09.2029 (Kauf: obligatorischer Vertrag in diesem Zeitraum und Erwerb bis Ende des Fertigstellungsjahres) | 5 % degressiv vom Restwert, Wechsel zu linear moeglich | Paragraf 7 Abs. 5a EStG (Wachstumschancengesetz) |
| Kuerzere tatsaechliche Nutzungsdauer nachgewiesen | 100 % / Restnutzungsdauer | Paragraf 7 Abs. 4 S. 2 EStG -- siehe Schritt 4 |
| Sonderabschreibung Mietwohnungsneubau | 5 % p.a. fuer 4 Jahre zusaetzlich (Zeilen 36-38), Baukosten- und Foerderobergrenzen, Effizienzstandard | Paragraf 7b EStG |
| Denkmal / Sanierungsgebiet | 8 x 9 % + 4 x 7 % auf bescheinigte Aufwendungen (Zeilen 39-41) | Paragrafen 7i, 7h EStG, Bescheinigung der Behoerde erforderlich |

- **Zeitanteilig** im Jahr des Uebergangs von Besitz/Nutzen/Lasten und im Verkaufsjahr (volle Monate; der Monat des Uebergangs zaehlt).
- **Kontinuitaet:** Zeile 33 verlangt Methode (1 = linear, 2 = degressiv), Prozentsatz und das Kennzeichen **"1 = wie Vorjahr" oder "2 = laut Erlaeuterung"**. Jede Aenderung gegenueber dem Vorjahr (neuer Satz, neue Bemessungsgrundlage, Gutachten, nachtraegliche HK) ist "laut Erlaeuterung" -- dann gehoert eine kurze Erlaeuterung mit Berechnung in die ergaenzenden Angaben der Erklaerung bzw. als Belegnachreichung.
- **Verhaeltnismaessige Zuordnung (Zeile 34):** Nur wenn Teile des Gebaeudes eigengenutzt oder unentgeltlich ueberlassen sind (Zeile 12). Dann Gesamtbetrag und abzugsfaehiger Anteil in % (Flaechenschluessel).

**3.3 AfA fuer Wirtschaftsgueter, die keine Gebaeude sind (Zeilen 42-45)**

- **Einbaukueche** ist ein einheitliches Wirtschaftsgut mit eigener AfA (BFH, Urteil vom 03.08.2016, IX R 14/15), Regel-Nutzungsdauer 10 Jahre; gebraucht mitgekauft: kuerzere Restnutzungsdauer begruendbar. Voraussetzung fuer die separate AfA beim Kauf: Ausweis im Kaufvertrag.
- **Geringwertige Wirtschaftsgueter** bis 800 EUR netto (Paragraf 6 Abs. 2 EStG): Sofortabzug im Anschaffungsjahr (dann in Zeile 80 als sonstige Kosten oder hier mit Nutzungsdauer "sofort" -- einheitlich handhaben).
- **Freistehende Garage** auf demselben Grundstueck: eigenes Wirtschaftsgut (Richtwert 20 Jahre); im Gebaeude integriert: Gebaeude-AfA.
- Einzelangaben sind Pflicht: Bezeichnung, Anschaffungskosten, Anschaffungsdatum, Nutzungsdauer.

### Schritt 4: Restnutzungsdauer-Gutachten steuerlich umsetzen

Das ist der groesste Hebel der Anlage V und zugleich der haeufigste Streitpunkt mit dem Finanzamt. Arbeite diesen Schritt vollstaendig ab, bevor du eine Zahl in Zeile 33 schreibst.

**4.1 Rechtslage fuer das Steuerjahr 2025 (Stand September 2026 -- vor Abgabe aktualisieren)**

- **Gesetz:** Paragraf 7 Abs. 4 S. 2 EStG erlaubt die AfA nach der tatsaechlichen Nutzungsdauer, wenn diese kuerzer ist als die typisierten 33/40/50 Jahre. Paragraf 11c Abs. 1 EStDV definiert sie als Zeitraum, in dem das Gebaeude voraussichtlich seiner Zweckbestimmung entsprechend genutzt werden kann. Ohne Nachweis unterstellt das Finanzamt immer die typisierte Dauer.
- **Rechtsprechung:** Der Steuerpflichtige darf sich **jeder Darlegungsmethode bedienen, die im Einzelfall zur Fuehrung des Nachweises geeignet erscheint**; erforderlich ist nur, dass die Nutzungsdauer mit hinreichender Sicherheit geschaetzt werden kann. Ein Bausubstanzgutachten ist keine Voraussetzung (BFH, Urteil vom 28.07.2021, IX R 25/19). Die modellhafte Ermittlung nach Paragraf 4 Abs. 3 ImmoWertV genuegt; die weitergehenden Anforderungen der Verwaltung liessen sich dem Gesetz nicht in Gaenze entnehmen (BFH, Urteil vom 23.01.2024, IX R 14/23). Mehrere Finanzgerichte haben modellhaft ermittelte Restnutzungsdauern anerkannt, teils ausdruecklich ohne Ortstermin und ohne oeffentliche Bestellung des Gutachters.
- **Verwaltung:** Das BMF-Schreiben vom 22.02.2023 (BStBl I S. 332), das den Nachweis auf Gutachten oeffentlich bestellter und vereidigter oder nach DIN EN ISO/IEC 17024 zertifizierter Sachverstaendiger beschraenkte, ist mit **BMF-Schreiben vom 01.12.2025 (GZ IV C 3 - S 2196/00040/006/008) aufgehoben**. Massgeblich sind seither Gesetzeswortlaut und BFH-Rechtsprechung.
- **Praktische Folge:** Die formalen Huerden sind gefallen, die Beweislast bleibt. Rechne trotzdem damit, dass einzelne Finanzaemter aeltere Pruefraster weiterverwenden -- ein gut qualifizierter Gutachter und ein sauber begruendetes Gutachten ersparen das Einspruchsverfahren, sind aber rechtlich nicht mehr zwingend.

**4.2 Gutachten-Check (vor dem Rechnen)**

| Pruefpunkt | Soll | Bei Abweichung |
|------------|------|----------------|
| Auftraggeber | Der Steuerpflichtige selbst ist Auftraggeber und Adressat des Gutachtens | Gutachten des Voreigentuemers oder eines Dritten wird regelmaessig verworfen -- neu beauftragen oder umschreiben lassen |
| Eigentuemerstellung zum Stichtag | Zum Stichtag war der Auftraggeber bereits AfA-berechtigt (ab Uebergang Besitz/Nutzen/Lasten) | Stichtag vor der eigenen AfA-Berechtigung ist ein klassischer Ablehnungsgrund |
| Stichtag | Moeglichst nah am Uebergang Besitz/Nutzen/Lasten; ein spaeterer Stichtag ist zulaessig, wenn der Zustand zum Stichtag beurteilt wird | Stichtag nach einer Sanierung macht eine kurze Restnutzungsdauer kaum noch begruendbar |
| Zeitpunkt gegenueber der Sanierung | **Gutachten vor Sanierungsbeginn**, spaetestens mit Stichtag vor der ersten Massnahme | Nach der Sanierung ist der Zustand ein anderer; das Finanzamt greift genau hier an |
| Determinanten | Technischer Verschleiss, wirtschaftliche Entwertung und rechtliche Nutzungsbeschraenkungen sind objektbezogen begruendet, nicht nur rechnerisch abgeleitet | Reines Alters-Rechenmodell ohne Objektbefund ist angreifbar -- Zustandsbeschreibung, Maengel, Modernisierungsgrad und Fotos nachfordern |
| Methode | Nachvollziehbar, z.B. modellhaft nach ImmoWertV mit Modernisierungspunkten; ein Verkehrswertgutachten mit ausgewiesener Restnutzungsdauer genuegt ebenfalls | Methode benennen lassen; ein Kurzgutachten der Bank oder eine selbst gerechnete Punktetabelle reicht nicht |
| Ortsbesichtigung | Vorhanden und dokumentiert | Nicht zwingend (mehrere FG-Entscheidungen), erhoeht aber die Durchsetzbarkeit deutlich -- ein reines Online-Gutachten ohne Begehung als Risiko ausweisen |
| Gutachterqualifikation | Oeffentlich bestellt und vereidigt fuer Grundstuecksbewertung oder nach DIN EN ISO/IEC 17024 zertifiziert (Zertifizierungsstelle idealerweise von der Deutschen Akkreditierungsstelle akkreditiert) | Seit Aufhebung des BMF-Schreibens keine Bedingung mehr; ohne diese Qualifikation aber hoeheres Streitrisiko -- Qualifikation im Bericht nennen |
| Zuordenbarkeit | Das Gutachten benennt eindeutig das bewertete Objekt (Gebaeude, bei Eigentumswohnungen zusaetzlich die Einheit) | Nicht zuordenbare Gutachten (MFH-Gutachten fuer eine ETW ohne Benennung) werden verworfen |
| Konsistenz zur Kaufpreisaufteilung | Restnutzungsdauer und Gebaeudeanteil passen zusammen; idealerweise bescheinigt derselbe Gutachter beides im selben Dokument | Sonst haeufigster Gegenangriff: kurze Restnutzungsdauer bedeute ein verbrauchtes Gebaeude, also niedrigerer Gebaeudeanteil (siehe 4.5) |
| Vollstaendigkeit der Angaben | Dem Gutachter wurden alle Sanierungen und Maengel offengelegt | Verschwiegene Modernisierungen machen das Gutachten angreifbar und den Auftraggeber angreifbar |

**Erfolgsaussicht einschaetzen:** Der Hebel lohnt sich vor allem bei Baujahren vor etwa 1960 bis 1970 und nicht durchsanierten Objekten. Bei jungen oder kernsanierten Gebaeuden liegt die ermittelte Restnutzungsdauer meist nahe der typisierten Dauer. Uebliche Ergebnisse liegen im Bereich von etwa 8 bis 30 Jahren. Der Grundsteuerwertbescheid enthaelt zwar eine Restnutzungsdauer, ist fuer die Einkommensteuer aber **nicht** verwendbar.

**4.3 Rechenlogik -- und der offene Streitpunkt**

```
AfA-Satz = 100 / festgestellte Restnutzungsdauer (Prozent, zwei Nachkommastellen)
```

Die Bemessungsgrundlage bleibt in jedem Fall auf den Gebaeudeanteil der Anschaffungskosten (inklusive anteiliger Nebenkosten) begrenzt. Ein Gutachten kann die Bemessungsgrundlage nie erhoehen, auch wenn es einen hoeheren Gebaeudewert ausweist.

Bei einem **Neuerwerb**, fuer den das Gutachten von Anfang an gilt, ist die Rechnung eindeutig: Gebaeudeanteil geteilt durch Restnutzungsdauer.

Bei einem **Bestandsobjekt mit nachtraeglichem Gutachten** ist die Behandlung umstritten. Rechne alle drei Varianten und lege sie dem Steuerberater vor:

| Variante | Rechnung | Vertreten von |
|----------|----------|---------------|
| A: neuer Satz auf urspruengliche Anschaffungskosten | Gebaeudeanteil x (100 / Restnutzungsdauer) | Beraterpraxis; hoechste AfA, Abschreibungsvolumen kann rechnerisch ueberschritten werden und endet dann frueher |
| B: Restwertmethode | (Gebaeudeanteil minus bisherige AfA) / Restnutzungsdauer ab Stichtag | Ebenfalls vertreten; sauberste Volumenlogik |
| C: Rueckrechnung auf den Anschaffungszeitpunkt | Finanzamt rechnet die Restnutzungsdauer auf den Kaufzeitpunkt zurueck und wendet den Satz ab Anschaffung an; Vorjahre bleiben unveraendert, ab dem ersten offenen Jahr gilt der zurueckgerechnete Satz | Typische Argumentation des Finanzamts |

Beispiel (Variante B): Gebaeudeanteil 300.000 EUR, seit 2020 linear 2 Prozent, bis Ende 2024 kumuliert 30.000 EUR, Restwert 270.000 EUR. Gutachten mit Stichtag 01.01.2025 und 30 Jahren Restnutzungsdauer: AfA 2025 = 270.000 / 30 = **9.000 EUR** (3,33 Prozent). Nach Variante A waeren es 300.000 / 30 = 10.000 EUR.

Weitere Regeln:
- **Kein Wahlrecht:** Entweder die typisierte Nutzungsdauer oder die nachgewiesene. Eine Zwischenzahl oder ein Verschieben von AfA-Volumen in Folgejahre gibt es nicht. Wer eine laengere Dauer will, braucht ein entsprechend lautendes Gutachten.
- **Laengeres Gutachtenergebnis:** Weist das Gutachten eine laengere Restnutzungsdauer aus als die verbleibende typisierte, bleibt es bei der bisherigen AfA. Ein solches Gutachten reicht man nicht ein.
- **Verkauf innerhalb der Zehnjahresfrist:** Die hoehere AfA erhoeht spaeter den steuerpflichtigen Veraeusserungsgewinn; der Vorteil ist dann eine Steuerstundung, kein endgueltiger Effekt. Bei steuerfreiem Verkauf nach zehn Jahren verfaellt nicht genutztes AfA-Volumen.
- **Erbbaurecht:** Kein Grund-und-Boden-Anteil, der volle Kaufpreis ist abschreibbar; ist die Restlaufzeit des Erbbaurechts kuerzer als die Nutzungsdauer, wird auf die Restlaufzeit abgeschrieben.
- **Schenkung oder Erbschaft:** Der Erwerber fuehrt die AfA des Rechtsvorgaengers fort (Paragraf 11d EStDV). Ein eigenes Gutachten begruendet dort keine neue Bemessungsgrundlage.
- **Jeder entgeltliche Erwerb startet neu:** Auch der Kauf zwischen Ehegatten oder der Verkauf an die eigene Gesellschaft eroeffnet eine neue AfA-Reihe und damit die Moeglichkeit eines neuen Gutachtens. Ein Gutachten wirkt nur fuer seinen Auftraggeber; der Erwerber braucht ein eigenes.

**4.4 Zeitliche Wirkung, Rueckwirkung und Verfahren**

- Das Gutachten wirkt fuer den **ersten noch offenen Veranlagungszeitraum** und dann fuer das ganze Jahr, nicht anteilig ab Erstellungsdatum. Ein spaet erstelltes Gutachten kann mehrere offene Jahre erfassen.
- **Offen** ist ein Jahr, fuer das noch keine Erklaerung abgegeben oder kein Bescheid ergangen ist, dessen Einspruchsfrist laeuft, fuer das ein Einspruch anhaengig ist oder dessen Bescheid unter dem Vorbehalt der Nachpruefung steht (Paragraf 164 AO). **Bestandskraeftige Jahre sind verloren** -- eine Aenderung nach Paragraf 173 AO scheidet aus, weil das nachtraegliche Bekanntwerden auf eigenem Verschulden beruht. Prueft immer zuerst, welche Jahre offen sind, bevor ein Gutachten beauftragt wird.
- **Erklaerung noch nicht veranlagt:** Geaenderte Anlage V nachreichen mit der Bitte um Beruecksichtigung, nicht nur das Gutachten schicken. Wer nur das Gutachten einreicht, verlagert die Rechenarbeit auf das Finanzamt und riskiert, dass sie unterbleibt.
- **Bescheid schon da:** Einspruch innerhalb eines Monats, Gutachten und Berechnung beifuegen. Einen Einspruch nie zuruecknehmen, solange die Rechtsfrage nicht geklaert ist -- mit der Ruecknahme wird das Jahr endgueltig zu.
- **Belege:** Es gilt die Belegvorhaltepflicht. Das Gutachten wird nicht automatisch mitgeschickt; das Finanzamt fordert es an. Bei einer Abweichung vom Vorjahr gehoert aber eine kurze Erlaeuterung mit der Berechnung in die Erklaerung, sonst kommt die Rueckfrage ohnehin. Eine verbindliche Auskunft nach Paragraf 89 AO ist hier nicht sinnvoll: Sie klaert Rechts-, nicht Tatsachenfragen, und lenkt die Aufmerksamkeit auf den Fall.
- **Kosten:** Restnutzungsdauer- und Zustandsgutachten fuer ein bereits erworbenes Objekt sind sofort abziehbare Werbungskosten im Zahlungsjahr (Zeile 80) und gehoeren nicht in die AfA-Bemessungsgrundlage und nicht in die 15-Prozent-Grenze. Ein **vor** dem Kauf zur Kaufpreisfindung beauftragtes Wertgutachten zaehlt dagegen zu den Anschaffungskosten -- deshalb das Gutachten erst als Eigentuemer beauftragen.

**4.5 Wechselwirkung mit der Kaufpreisaufteilung -- der eigentliche Angriffspunkt**

Der haeufigste Gegenangriff des Finanzamts lautet: Eine kurze Restnutzungsdauer bedeute ein wirtschaftlich verbrauchtes Gebaeude, also sei der im Kaufvertrag vereinbarte hohe Gebaeudeanteil unrealistisch und werde nach der BMF-Arbeitshilfe neu aufgeteilt. Der Effekt kann die Ersparnis aus dem Gutachten vollstaendig auffressen.

- **Gegenargument:** Nutzungsdauer und Wertverhaeltnis sind zwei verschiedene Fragen. Die Aufteilung darf nach der Rechtsprechung auch im Ertragswertverfahren erfolgen; schlechte Substanz mindert den Sachwert, nicht zwingend den Ertragswert.
- **Bester Schutz:** Denselben Gutachter im selben Dokument auch die Aufteilung in Grund und Boden und Gebaeude bescheinigen oder die vertragliche Aufteilung bestaetigen zu lassen. Dann widersprechen sich die Unterlagen nicht.
- **Reihenfolge:** Beides im ersten Jahr gemeinsam geltend machen. Ein getrenntes Einreichen bringt keinen Vorteil, weil das Finanzamt wegen der Jahresabschnittsbesteuerung ohnehin beides jederzeit pruefen kann.
- **Kaufpreisaufteilung ist korrigierbar:** Eine im Erstjahr ungeschickte Aufteilung kann in jedem noch offenen Jahr berichtigt werden; fuer bestandskraeftige Jahre bleibt sie bestehen.

**4.6 Nachtraegliche Herstellungskosten nach anerkanntem Gutachten**

- **Grundfall:** Nachtraegliche Anschaffungs- oder Herstellungskosten duerfen nach R 7.4 Abs. 9 S. 2 EStR mit dem bisher angewandten Prozentsatz abgeschrieben werden. Eine anerkannte kurze Restnutzungsdauer wirkt damit auch auf spaetere Sanierungen -- der eigentliche Grund, das Gutachten vor der Sanierung erstellen zu lassen.
- **Grenze 1, anderes Wirtschaftsgut:** Uebersteigt der Bauaufwand zuzueglich Eigenleistung den Verkehrswert des bisherigen Gebaeudes, kann von einem anderen Wirtschaftsgut ausgegangen werden; dann beginnt die AfA neu und das Gutachten wirkt nicht mehr (R 7.3 Abs. 5 S. 2, R 7.4 Abs. 9 S. 4 EStR).
- **Grenze 2, steuerlicher Neubau:** Werden tragende Teile (Fundamente, tragende Waende, Geschossdecken, Dachkonstruktion) ueberwiegend ersetzt, entsteht ein Neubau mit neuer Nutzungsdauer.
- Diese Abgrenzung nie selbst entscheiden -- als Steuerberater-Pruefpunkt kennzeichnen.

### Schritt 5: Schuldzinsen und Geldbeschaffungskosten (Zeilen 46-51)

- **Zeile 46-48 Schuldzinsen (ohne Tilgung):** Betrag laut Zinsbescheinigung der Bank fuer das Steuerjahr, je Darlehen mit Kreditinstitut. Tilgung ist nie Werbungskosten. Nur Darlehen, deren **Verwendungszweck** das Vermietungsobjekt ist (Kauf, Sanierung, Umschuldung solcher Darlehen) -- die Besicherung ist unerheblich. Gemischt verwendete Darlehen: Zinsen anteilig, Nachweis der Mittelverwendung anfordern.
- **Disagio/Damnum:** sofort abziehbar im Zahlungsjahr, soweit marktueblich (Verwaltungspraxis: bis 5 % bei mindestens fuenfjaehriger Zinsbindung); darueber hinaus Verteilung ueber die Zinsbindung. Einordnung im Bericht begruenden.
- **Zeile 49-51 Geldbeschaffungskosten:** Notar- und Grundbuchgebuehren fuer die Grundschuld, Bearbeitungs- und Schaetzgebuehren der Bank, Bereitstellungszinsen. Vorfaelligkeitsentschaedigung nur, wenn die Umschuldung der weiteren Vermietung dient; bei Verkauf grundsaetzlich nicht (Steuerberater-Frage).
- **Zeile 52-54 Renten, dauernde Lasten:** Nur der Zins-/Ertragsanteil bei Kauf gegen Rente.
- **Vor Vermietungsbeginn** (Leerstand nach Kauf, Bauphase): Zinsen sind vorweggenommene Werbungskosten, wenn die Vermietungsabsicht feststeht und dokumentiert ist.

### Schritt 6: Erhaltungsaufwand (Zeilen 55-72) -- klassifizieren, dann verteilen

**6.1 Klassifikation jeder Baumassnahme** (Vorarbeit idealerweise aus dem Beleg-Sortierer uebernehmen):

| Kategorie | Behandlung | Zeile |
|-----------|-----------|-------|
| Erhaltungsaufwand (Reparatur, Ersatz vorhandener Teile in zeitgemaesser Form) | Sofort im Zahlungsjahr oder Wahlrecht Verteilung 2-5 Jahre | 55/56 bzw. 57-60 |
| Herstellungskosten (Erweiterung, Substanzmehrung, Standardhebung bei 3 von 4 Kernmerkmalen Heizung/Sanitaer/Elektro/Fenster innerhalb von 5 Jahren) | Erhoehen die AfA-Bemessungsgrundlage | 33 (ueber AfA) |
| Anschaffungsnahe Herstellungskosten: Netto-Instandsetzungs-/Modernisierungskosten der ersten 3 Jahre nach Anschaffung uebersteigen 15 % der Gebaeude-Anschaffungskosten (Paragraf 6 Abs. 1 Nr. 1a EStG) | Alle erfassten Kosten rueckwirkend nur ueber AfA; Vorjahre werden geaendert | 33 (ueber AfA) |
| Vereinfachung: Einzelmassnahme bis 4.000 EUR netto | Auf Antrag Erhaltungsaufwand (R 21.1 Abs. 2 S. 2 EStR), zaehlt aber in die 15 % | 55 |
| Anschaffungskosten (Herstellung der Funktionstuechtigkeit, Kosten vor Nutzen-/Lastenuebergang) | AfA-Basis | 33 |

- **15 %-Tracker** fuehren, wenn das Objekt weniger als 3 Jahre im Bestand ist: Gebaeude-Anschaffungskosten (inkl. anteiliger Nebenkosten) x 15 % = Grenze netto; alle Netto-Massnahmen seit Uebergang Besitz/Nutzen/Lasten kumulieren; Entnahmen aus der WEG-Erhaltungsruecklage fuer Sanierungen und Bauabzugsteuer-/Reverse-Charge-Betraege zaehlen mit; Erweiterungen, jaehrlich uebliche Wartung und nach Erwerb durch Dritte verursachte Schaeden zaehlen nicht. Ampel im Bericht: gruen < 10 %, gelb 10-15 %, rot > 15 %.
- **Bauabzugsteuer (Paragraf 48 EStG):** Ab dem dritten vermieteten Objekt (Zwei-Wohnungen-Regel) ist der Vermieter Unternehmer im Sinne der Vorschrift; ohne Freistellungsbescheinigung des Bauunternehmers sind 15 % der Bauleistung einzubehalten (Freigrenzen 5.000 EUR bzw. 15.000 EUR bei ausschliesslich steuerfreier Vermietung). Fehlende Bescheinigungen als Risiko ausweisen.

**6.2 Eintragung**

| Zeile | Inhalt |
|-------|--------|
| 55 | Im Steuerjahr voll abzuziehende Erhaltungsaufwendungen einschliesslich **Entnahmen aus der Erhaltungsruecklage** (direkt zugeordnet) |
| 56 | Dasselbe verhaeltnismaessig (Gesamtbetrag, abzugsfaehiger Anteil %) |
| 57 | Auf bis zu 5 Jahre zu verteilende Erhaltungsaufwendungen (Paragrafen 11a, 11b EStG, Paragraf 82b EStDV): Gesamtaufwand des Steuerjahres und davon im Steuerjahr abzuziehender Anteil |
| 58-60 | Verteilter Betrag des Steuerjahres direkt / verhaeltnismaessig / abzugsfaehig |
| 61-63 | Im Steuerjahr zu beruecksichtigender Anteil aus **2021** |
| 64-66 | Anteil aus **2022** |
| 67-69 | Anteil aus **2023** |
| 70-72 | Anteil aus **2024** |

- **Paragraf 82b EStDV** gilt fuer groesseren Erhaltungsaufwand an Gebaeuden im Privatvermoegen, die ueberwiegend Wohnzwecken dienen: gleichmaessige Verteilung auf 2 bis 5 Jahre, Wahlrecht pro Massnahme. Sinnvoll, wenn der Sofortabzug das Einkommen unter die Progressionsspitze druecken wuerde oder Verluste sonst ungenutzt blieben. Der Skill rechnet beide Varianten vor (Sofortabzug vs. Verteilung) und legt die Entscheidung dem Nutzer/Steuerberater vor. Bei Verkauf oder Nutzungsaenderung wird der Restbetrag im letzten Jahr abgezogen.
- **Hausgeld zerlegen (ETW):** Zufuehrung zur Erhaltungsruecklage ist **nicht** abziehbar; erst die Verwendung durch die WEG laut Jahresabrechnung (Zeile 55). Betriebskostenanteil in Zeile 73, Verwalterverguetung in Zeile 76. Abrechnungsspitze (Nachzahlung/Guthaben) im Jahr des Zu-/Abflusses.
- **Zuschuesse zu Erhaltungsaufwand** (KfW, BAFA, Versicherung) sind Einnahmen (Zeile 29) oder kuerzen den Aufwand -- einheitlich handhaben und dokumentieren.

### Schritt 7: Laufende Kosten und sonstige Werbungskosten (Zeilen 73-82)

Das Formular unterscheidet nach **Kostenart**, nicht danach, ob der Vermieter die Kosten tatsaechlich umgelegt hat (Bruttoprinzip: Kosten voll als Werbungskosten, Umlagen voll als Einnahmen).

| Zeile | Kostenart | Typische Positionen | Hinweise |
|-------|-----------|---------------------|----------|
| 73-75 | Umgelegte Kosten (umlagefaehige Betriebskosten) | Grundsteuer (Bescheid 2025 der Reform), Strassenreinigung, Muellabfuhr, Wasser, Entwaesserung, Hausbeleuchtung/Allgemeinstrom, Heizung, Warmwasser, Schornsteinreinigung, Hausversicherungen (Gebaeude, Haftpflicht), Hauswart, Treppenhausreinigung, Fahrstuhl, Gartenpflege | Bei ETW der Betriebskostenanteil des Hausgelds; Zahlungsdatum entscheidet |
| 76-78 | Nicht umgelegte Kosten | Hausverwaltung/WEG-Verwalterverguetung, Kontofuehrung Mietkonto, Bankgebuehren, Mietausfall-/Rechtsschutzversicherung | Ohne Zufuehrung zur Erhaltungsruecklage |
| 79 | An das Finanzamt gezahlte USt | Nur bei umsatzsteuerpflichtiger Vermietung |
| 80-82 | Sonstige Kosten | Fahrtkosten, Telefon/Porto/Software (anteilig), Fortbildung mit Vermietungsbezug, Steuerberatungskosten (nur V+V-Anteil, z.B. Honorar fuer die Anlage V), Rechtsanwalt/Gericht/Raeumung, Inserate und Maklerkosten der Neuvermietung, Mitgliedsbeitrag Haus & Grund, Bonitaetsauskuenfte, Kosten fuer Restnutzungsdauer-/Zustandsgutachten, GWG-Sofortabzug, Homeoffice-Pauschale anteilig | Jede Position mit Einzelangabe |

Detailregeln fuer haeufige Streitpunkte:
- **Fahrtkosten:** Fahrten zum Objekt, zu Bank, Handwerkern, Baumarkt, Steuerberater und Eigentuemerversammlung sind mit den **tatsaechlichen Kilometerkosten fuer Hin- und Rueckweg** abziehbar (Paragraf 9 Abs. 1 S. 3 Nr. 4a EStG); die 0,30 EUR je Kilometer sind der Rueckfallwert ohne Kostennachweis. Mindestnachweis: Fahrtenliste mit Datum, Ziel, Anlass und Kilometern (Routenplaner), bei tatsaechlichen Kosten zusaetzlich Jahreskilometer und Kostenbelege. Wird das Objekt zur regelmaessigen Taetigkeitsstaette (Anhaltspunkt: deutlich mehr als 100 Fahrten im Jahr), gilt nur die Entfernungspauschale (BFH, Urteil vom 01.12.2015, IX R 18/15). **Dienstwagen mit 1-%-Regelung:** kein Abzug, weil keine eigenen Kosten entstehen. **Besichtigungsfahrten vor dem Kauf:** zum spaeter gekauften Objekt = Anschaffungsnebenkosten (AfA-Basis), zu nicht gekauften Objekten = vergebliche Werbungskosten (sofort). Verpflegungsmehraufwand (14/28 EUR bei mehr als 8 bzw. 24 Stunden Abwesenheit) ist auch bei Eigenrenovierung ansetzbar; die Eigenleistung selbst nie.
- **Steuerberatungskosten** sind nur abziehbar, soweit sie auf die Ermittlung der Vermietungseinkuenfte entfallen (Anlage V, Zuordnungsgrundsaetze im BMF-Schreiben vom 21.12.2007); der Rest sind nicht abziehbare Kosten der privaten Lebensfuehrung. Rechnungsaufteilung nach Leistung anfordern.
- **Arbeitszimmer / Homeoffice:** Ein Arbeitszimmer ist seit 2023 nur noch abziehbar, wenn es Mittelpunkt der gesamten Taetigkeit ist (typisch Vollzeit-Vermieter); sonst nur die Tagespauschale von 6 EUR, maximal 1.260 EUR im Jahr, insgesamt ueber alle Einkunftsarten -- bei V+V nur den anteiligen Tagesansatz, nie doppelt.
- **Telefon, Internet, Software, PC:** Nur der Vermietungsanteil; das Finanzamt akzeptiert bei gemischt genutzten Geraeten haeufig einen Privatanteil von etwa 30 %. Verwaltungssoftware, Analysetools und Portal-Abos mit Vermietungsbezug sind voll abziehbar.
- **Objektuebergreifende Kosten** (Software, Fortbildung, Buero, Fahrten zu mehreren Objekten): entweder nach Schluessel auf die Anlagen V verteilen oder gesammelt in einer Anlage V unter "Sonstige Kosten" als Block "allgemeine Kosten der Vermietung" mit Einzelaufstellung eintragen -- in der Praxis akzeptiert, Hauptsache nicht doppelt.
- **Fortbildung/Fachliteratur** mit konkretem Bezug zur Vermietungstaetigkeit ist abziehbar, auch als vorweggenommene Werbungskosten vor dem ersten Kauf. Typische Ablehnung des Finanzamts: private Lebensfuehrung oder Vermoegensbildung (Paragraf 12 Nr. 1 EStG) bzw. Umqualifizierung in Sonderausgaben. Investoren-Ausbildungen mit Objektbezug wurden von Finanzgerichten 2024 teils anerkannt, reine Steuergestaltungs-Kurse sieht die Verwaltung kritisch -- als "pruefen" markieren, Inhalt und Vermietungsbezug dokumentieren.
- **Gutachterkosten:** Restnutzungsdauer-, Zustands- und Wertgutachten fuer ein bereits vermietetes Objekt sind sofort abziehbar (Zeile 80); ein vor dem Kauf beauftragtes Wertgutachten zum gekauften Objekt gehoert zu den Anschaffungskosten. Versucht das Finanzamt, Gutachtenkosten fuer Bestandsobjekte in die AfA-Basis zu schieben, ist das ein Einspruchsgrund.
- **Versicherungsleistungen:** Ersatz fuer Mietausfall ist Einnahme; Ersatz fuer Reparaturkosten ist Einnahme, soweit die Reparatur als Werbungskosten abgezogen wird (ggf. in verschiedenen Jahren). Personenbezogene Versicherungen, die die Bank verlangt (Risikoleben, Berufsunfaehigkeit), sind keine Werbungskosten.
- **Hausgeld (ETW):** Alle Positionen der Jahresabrechnung sind Werbungskosten ausser der Zufuehrung zur Erhaltungsruecklage; Ruecklagenentnahmen und Sonderumlagen erst bei Verwendung durch die WEG. Kommt die Jahresabrechnung erst nach Abgabe, Aenderung des Bescheids nach Paragraf 173 Abs. 1 Nr. 2 AO beantragen. Kreditfinanzierte Grossmassnahmen der WEG werden dem Eigentuemer anteilig zugerechnet und zaehlen in die 15 %-Grenze.
- **Vorweggenommene und vergebliche Werbungskosten** (Besichtigungsfahrten zu nicht gekauften Objekten, Gutachten fuer gescheiterte Kaeufe, Fortbildung vor dem ersten Kauf) sind abziehbar, wenn die Einkuenfteerzielungsabsicht nachweisbar ist (Exposes, Termine, Finanzierungsanfragen); ohne Bestandsobjekt in einer eigenen Anlage V unter "Sonstige Kosten" mit Benennung des Objekts.
- **Bewirtung und Geschenke:** Bewirtung mit Vermietungsbezug (z.B. Handwerker-Abnahme) zu 70 %; Geschenke an Mieter/Handwerker bis 50 EUR je Empfaenger und Jahr (Grenze seit 2024). Bagatellpositionen mit Beleg und Anlass.
- **Kontofuehrung, Mitgliedsbeitraege** (Haus & Grund), Rechtsschutz- und Mietausfallversicherung: nicht umgelegte Kosten (Zeile 76) bzw. sonstige Kosten -- kleine Betraege, die regelmaessig vergessen werden.

### Schritt 8: Summen, Zurechnung, verbilligte Vermietung (Zeilen 83-89)

| Zeile | Inhalt | Pruefung |
|-------|--------|---------|
| 83 | Summe der Werbungskosten (Zeilen 35, 38, 41, 45, 48, 51, 54, 55, 56, 60, 63, 66, 69, 72, 75, 78, 79, 82) | Nachrechnen; jede Teilsumme muss aus Einzelposten belegbar sein |
| 84 | Darin enthaltene abziehbare Vorsteuer | Nur bei USt-Option |
| 85 | Ueberschuss = Zeile 32 minus Zeile 83; negativ mit Minuszeichen | Verluste sind bei AfA und Zinsen normal, kein Fehler |
| 86 | Zurechnung auf Person A / Person B | Nach Miteigentumsanteil (Grundbuch), bei Alleineigentum 100 % beim Eigentuemer |
| 87 | Kuerzung der Werbungskosten wegen verbilligter Vermietung in % | Nur wenn Miete < 50 % der ortsueblichen Warmmiete (siehe unten) |
| 88 | Betragsmaessige Kuerzung bei verbilligter Vermietung eines Teils des Objekts | Alternative zu Zeile 87 |
| 89 | Im Steuerjahr vereinnahmte oder bewilligte Zuschuesse aus oeffentlichen Mitteln zu Anschaffungs-/Herstellungskosten | Mindern AfA-Basis; gesonderte Aufstellung |

**Verbilligte Vermietung (Paragraf 21 Abs. 2 EStG), Massstab ortsuebliche Warmmiete (Kaltmiete plus umlagefaehige Kosten):**

| Vereinbarte Miete | Folge | Eintragung |
|-------------------|-------|-----------|
| Mindestens 66 % | Voll entgeltlich, Werbungskosten voll | Keine Kuerzung |
| 50 % bis unter 66 % | Totalueberschussprognose (30 Jahre) erforderlich; positiv: voll, negativ: anteilig | Prognose beilegen, ggf. Kuerzung |
| Unter 50 % | Aufteilung in entgeltlichen und unentgeltlichen Teil; Werbungskosten nur anteilig | Zeile 87 (Prozentsatz) oder 88 |

Ausnahme: Bei aufwendig gestalteten Objekten (Wohnflaeche ueber 250 m²) ist auch oberhalb 66 % eine Totalueberschussprognose noetig (BFH, Urteil vom 20.06.2023, IX R 17/21). Mietvertraege mit Angehoerigen muessen zivilrechtlich wirksam, fremdueblich gestaltet und tatsaechlich durchgefuehrt sein (Ueberweisung der Miete, NK-Abrechnung). Der Skill berechnet die Quote und weist bei Unterschreiten von 66 % auf die Anpassung der Miete zum naechsten Jahreswechsel hin.

### Schritt 9: Verluste, Einkunftserzielungsabsicht, Leerstand

- Bei auf Dauer angelegter Wohnungsvermietung wird die Einkunftserzielungsabsicht typisierend unterstellt; Verluste aus AfA und Zinsen sind ohne Prognose anzuerkennen (BMF-Schreiben vom 08.10.2004, BStBl I S. 933).
- Ausnahmen mit Pruefbedarf und Dokumentationspflicht: laengerer **Leerstand** (Vermietungsbemuehungen nachweisen: Inserate, Maklerauftrag, Preisanpassungen), **Sanierungsleerstand** (Zeitplan), **befristete Vermietung** oder konkrete Verkaufsabsicht innerhalb von fuenf Jahren, **Ferienwohnung** mit Selbstnutzung, **verbilligte Vermietung** unter 66 %, **Luxusobjekte**.
- Verluste aus V+V sind mit anderen Einkunftsarten verrechenbar; nicht ausgeglichene Verluste gehen in den Verlustvortrag. Der Skill weist die Summe aller Objekte aus, damit die Wirkung auf den Gesamtsteuerbetrag abschaetzbar ist.

### Schritt 10: Plausibilitaet, Belegpaket, Uebergabe

1. **Rechnerische Pruefung:** Alle Summenzeilen (15, 18, 31, 32, 35, 38, 41, 45, 48, 51, 54, 60, 63, 66, 69, 72, 75, 78, 82, 83, 85) neu addieren; Zeile 86 muss Zeile 85 ergeben.
2. **Vorjahresvergleich:** AfA (nur bei "laut Erlaeuterung" abweichend), Zinsen (Zinsbescheinigung), Grundsteuer (Reform-Bescheid), Verwaltung, Versicherungen; Abweichungen ueber 20 % kommentieren.
3. **Kennzahlen:** Werbungskosten ohne AfA und Zinsen im Verhaeltnis zu den Einnahmen; Erhaltungsaufwand im Verhaeltnis zur 15 %-Grenze; Miete je m² gegen ortsuebliche Miete; Leerstandsquote.
4. **Vollstaendigkeits-Check der Werbungskosten** (haeufig vergessen): Kontofuehrung, Fahrten, Telefon, Steuerberater-Anteil, Gutachten, Inserate, Mitgliedsbeitraege, Bearbeitungsgebuehren, GWG, Erhaltungsruecklagen-Entnahmen laut WEG-Abrechnung.
5. **Belegvorhaltung:** Seit 2017 werden Belege nur auf Anforderung eingereicht; sie muessen aber bis zur Bestandskraft vorgehalten werden. Empfehlung: Gutachten, AfA-Berechnung bei Aenderungen und Erlaeuterungen zu ungewoehnlichen Positionen proaktiv beifuegen (Belegnachreichung), Rechnungen von Handwerkern mindestens zwei Jahre aufbewahren (Paragraf 14b UStG), alles andere bis Bestandskraft plus Einspruchsfrist.
6. **Uebergabepaket:** Anlage-V-Ausfuellhilfe je Objekt, AfA-Rechnung, Erhaltungsaufwand-Klassifikation mit 15 %-Tracker, Erlaeuterungstext fuer das Finanzamt, Belegliste, Steuerberater-Fragenliste.

---

## Ausgabeformat

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext.

**Im Chat:** der unten gezeigte Markdown-Bericht.
**Als Datei:** je Objekt eine Uebertragungsliste `anlage-v_2025_<objekt>.csv` (Spalten: Zeile; Feld; Wert; Kennzahl; Herkunft/Beleg; Status) fuer die Eingabe in ELSTER oder die Uebergabe an die Kanzlei -- die Datei anbieten, nie als Rohdaten im Chat ausgeben.

### Zusammenfassung (Freitext)

3-5 Saetze: Anzahl Objekte, Gesamtueberschuss/-verlust, wichtigste Aenderung gegenueber dem Vorjahr (z.B. AfA nach Gutachten), Fristenstatus, Anzahl offener Steuerberater-Fragen.

### Bericht

```markdown
# Anlage V 2025: Musterstrasse 12, 40210 Duesseldorf (Objekt 1 von 2)

**Fristen:** Selbstabgabe 31.07.2026 (ueberschritten -- siehe Hinweis) | mit Steuerberater 01.03.2027
**Ergebnis Zeile 85:** -11.103 EUR | Zurechnung Zeile 86: Person A 50 % / Person B 50 % | Formular: Anlage V (keine V-FeWo)

## Stammdaten (Zeilen 4-12)

| Zeile | Feld | Wert | Herkunft | Status |
|-------|------|------|----------|--------|
| 4-5 | Lage | Musterstrasse 12, 40210 Duesseldorf | Kaufvertrag | 🟢 |
| 6 | AZ Grundsteuermessbescheid | 123/456/7890/001 | Bescheid vom 12.02.2025 | 🟢 |
| 7 | Kaufvertrag / Uebergang Nutzen-Lasten | 03.05.2020 / 01.07.2020 | Kaufvertrag | 🟢 |
| 10 | Ferienwohnung / kurzfristig / Angehoerige | Nein / Nein / Nein | Angabe Nutzer | 🟢 |
| 11 | Gesamtwohnflaeche | 412 m² | Teilungserklaerung | 🟢 |
| 12 | Eigengenutzt / Ferienwohnung | 0 m² / 0 m² | Angabe Nutzer | 🟢 |

## Einnahmen (Zeilen 13-32)

| Zeile | Feld | Wert | Herkunft | Status |
|-------|------|------|----------|--------|
| 13-15 | Kaltmieten Wohnungen (6 WE, Summe) | 38.400 EUR | Mietkonto 2025 | 🟢 |
| 20 | NK-Vorauszahlungen | 9.600 EUR | Mietkonto 2025 | 🟢 |
| 21 | NK-Nachzahlungen/-Erstattungen 2025 | -420 EUR | NK-Abrechnung 2024, gezahlt 15.09.2025 | 🟢 |
| 26 | Garagen an Dritte | 1.200 EUR | Mietkonto | 🟢 |
| 32 | Summe Einnahmen | 48.780 EUR | Berechnung | 🟢 |

## AfA (Zeilen 33-45)

| Position | Wert |
|----------|------|
| Anschaffungskosten gesamt (Kaufpreis 520.000 + Nebenkosten 46.800) | 566.800 EUR |
| Gebaeudeanteil laut Notarvertrag 78 % (Arbeitshilfe: 74 % -- Abweichung moderat) | 442.104 EUR |
| Bisherige AfA 2020-2024 (2 %, 2020 zeitanteilig 6/12) | 39.789 EUR |
| Restwert 01.01.2025 | 402.315 EUR |
| Restnutzungsdauer laut Gutachten (Stichtag 01.01.2025, Methode ImmoWertV, Ortstermin ja, Gutachter ISO 17024) | 32 Jahre |
| **AfA 2025 nach Variante B (Restwert / Restnutzungsdauer), Zeile 33: linear, 3,13 %, "2 = laut Erlaeuterung"** | **12.572 EUR** (Vorjahr 8.842 EUR) |
| Vergleich Variante A (urspruengliche AK / Restnutzungsdauer) | 13.816 EUR -- Entscheidung Steuerberater |
| Zeile 42: Einbaukueche WE 3 (AK 6.800 EUR, 10 J., ab 03/2025) | 567 EUR |

## Werbungskosten (Zeilen 46-83)

| Zeile | Feld | Wert | Herkunft | Status |
|-------|------|------|----------|--------|
| 46-48 | Schuldzinsen Sparkasse Nr. 123 / Nr. 456 | 11.240 EUR | Zinsbescheinigungen | 🟢 |
| 49-51 | Geldbeschaffung (Grundschuld-Nachtrag Notar) | 380 EUR | Rechnung 22.04.2025 | 🟢 |
| 55 | Erhaltungsaufwand sofort (5 Massnahmen) | 9.850 EUR | Belegliste | 🟢 |
| 57-60 | Dachsanierung 24.000 EUR, Verteilung auf 4 Jahre, 2025: 1/4 | 6.000 EUR | Rechnung 30.06.2025 | 🟡 Wahlrecht |
| 67-69 | Anteil Fenster 2023 (3 Jahre, Jahr 3 von 3) | 3.200 EUR | Anlage V 2023/2024 | 🟢 |
| 73-75 | Umgelegte Kosten (Grundsteuer 1.980, Versicherung 2.140, Muell/Wasser 4.310 ...) | 10.870 EUR | Bescheide/Rechnungen | 🟢 |
| 76-78 | Verwaltung, Kontofuehrung | 3.180 EUR | Verwalterrechnungen | 🟢 |
| 80-82 | Sonstige (Fahrten 412 km = 124 EUR, Gutachten 1.490 EUR, Steuerberater-Anteil 350 EUR, Telefon 60 EUR) | 2.024 EUR | Belege | 🟡 Steuerberater-Anteil aufteilen lassen |
| 83 | Summe Werbungskosten | 59.883 EUR | Berechnung | 🟢 |

## 15 %-Grenze und Standardhebung

| | |
|---|---|
| Frist | 01.07.2020 - 30.06.2023 (abgelaufen) |
| Netto-Massnahmen im Zeitraum | 41.200 EUR = 9,3 % der Gebaeude-AK -- 🟢 unter Grenze |
| Kernmerkmale seit 2020 (Heizung/Sanitaer/Elektro/Fenster) | Fenster 2023, Heizung 2025 = 2 von 4 -- 🟡 drittes Merkmal innerhalb 5 Jahren vermeiden |

## Plausibilitaetspruefung

| Pruefung | Ergebnis |
|----------|----------|
| Summen rechnerisch | 🟢 alle Summenzeilen stimmen |
| AfA vs. Vorjahr | 🟡 +42 % -- begruendet durch Gutachten, Erlaeuterung beigefuegt |
| Zinsen vs. Zinsbescheinigung | 🟢 identisch |
| Grundsteuer vs. Vorjahr | 🟡 +18 % (Reform 2025), Bescheid liegt vor |
| Vergessene Positionen | 🟡 Kontofuehrungsgebuehr Mietkonto fehlt -- nachreichen |
| Verbilligte Vermietung | 🟢 nicht einschlaegig |

## Erlaeuterung fuer das Finanzamt (Textvorschlag)

"Zu Zeile 33: Die AfA wurde ab 2025 gemaess Paragraf 7 Abs. 4 Satz 2 EStG nach der tatsaechlichen Restnutzungsdauer von 32 Jahren bemessen (Gutachten vom 14.02.2025, Stichtag 01.01.2025, anbei). Restwert zum 01.01.2025: 402.315 EUR; jaehrliche AfA: 12.572 EUR (3,13 %). Berechnung anbei."

## Offene Punkte fuer den Steuerberater

| # | Frage | Warum relevant |
|---|-------|----------------|
| 1 | Berechnungsvariante nach dem Gutachten: neuer Satz auf urspruengliche Anschaffungskosten oder auf den Restwert? | Differenz 1.244 EUR AfA im Jahr |
| 2 | Paragraf 82b: Dachsanierung auf 4 Jahre verteilen oder Sofortabzug? | Progression 2025 vs. 2026-2028 |
| 3 | Steuerberaterrechnung 1.400 EUR: welcher Anteil entfaellt auf Anlage V? | Nur V+V-Anteil abziehbar |
| 4 | Vorfaelligkeitsentschaedigung 2.100 EUR aus Umschuldung Darlehen 456 | Abzug nur bei fortgesetzter Vermietung |

## Dateien

Uebertragungsliste geschrieben: `anlage-v_2025_musterstrasse-12.csv` (89 Zeilen, ELSTER-Reihenfolge)
```

---

## Qualitaetspruefung

Vor der Ausgabe pruefen:

- [ ] Steuerjahr, Formularversion und Fristenstatus sind im Bericht genannt
- [ ] Pro Objekt (bzw. Eigentumswohnung) genau eine Anlage V; Ferienwohnung/kurzfristige Vermietung als V-FeWo geroutet; GbR als Feststellungsfall markiert
- [ ] Alle Einnahmen nach Zufluss im Steuerjahr, 10-Tage-Regel auf Jahreswechsel-Zahlungen angewendet
- [ ] Umlagen als Einnahmen (Zeile 20-23) und die Kosten als Werbungskosten (Zeile 73-75) -- kein Netting
- [ ] AfA-Bemessungsgrundlage hergeleitet (Kaufpreis, Nebenkosten, Aufteilung, Inventar, nachtraegliche HK, Zuschuesse) und Methode dokumentiert
- [ ] AfA-Satz passt zu Fertigstellungsjahr bzw. Gutachten; Kennzeichen "wie Vorjahr"/"laut Erlaeuterung" korrekt gesetzt; bei Aenderung Erlaeuterung erstellt
- [ ] Gutachten-Check vollstaendig (Auftraggeber, Eigentuemerstellung zum Stichtag, Stichtag vor Sanierung, Determinanten, Methode, Ortstermin, Qualifikation, Zuordenbarkeit, Konsistenz zur Kaufpreisaufteilung) und Risiken benannt
- [ ] Bei nachtraeglichem Gutachten: alle drei Berechnungsvarianten gerechnet und dem Steuerberater vorgelegt, nicht stillschweigend eine gewaehlt
- [ ] Geprueft, welche Veranlagungszeitraeume noch offen sind (keine Erklaerung, Einspruchsfrist, Vorbehalt der Nachpruefung) -- bestandskraeftige Jahre nicht eingerechnet
- [ ] Tilgung nirgends als Werbungskosten; Zinsen stimmen mit Zinsbescheinigungen ueberein
- [ ] Erhaltungsaufwand klassifiziert; 15 %-Grenze fuer Objekte unter 3 Jahren gerechnet; Paragraf-82b-Vorjahresanteile (2021-2024) in Zeilen 61-72 uebernommen
- [ ] Erhaltungsruecklage: nur Entnahmen abgezogen, Zufuehrung nicht
- [ ] Verbilligte Vermietung geprueft (66 %/50 % der ortsueblichen Warmmiete), Zeile 87/88 nur bei unter 50 %
- [ ] Zurechnung Zeile 86 entspricht den Eigentumsanteilen und ergibt Zeile 85
- [ ] Alle Summenzeilen nachgerechnet; jede Zahl hat eine Herkunft; keine geschaetzte Zahl ohne Kennzeichnung
- [ ] Strittige und gestaltbare Punkte stehen in der Steuerberater-Fragenliste, nicht stillschweigend entschieden
- [ ] Datei geschrieben und angeboten; keine Rohdaten im Chat

---

## Warnsignale

| Signal | Bedeutung | Aktion |
|--------|-----------|--------|
| Abgabefrist fuer Selbstabgeber ueberschritten | Verspaetungszuschlag ab 14 Monaten automatisch, vorher Ermessen | Sofort abgeben oder Steuerberater beauftragen; im Bericht rot markieren |
| Gutachten-Stichtag nach dem 01.01. des Umstellungsjahres | AfA-Erhoehung fuer das Jahr angreifbar | Stichtag klaeren, ggf. Nachtrag des Gutachters |
| Gutachten erst nach Sanierungsbeginn beauftragt | Kurze Restnutzungsdauer kaum noch begruendbar, spaetere Sanierungskosten verlieren den hohen AfA-Satz | Stichtag vor die erste Massnahme legen lassen, sonst Erwartung senken |
| Steuerpflichtiger ist nicht Auftraggeber des Gutachtens oder war zum Stichtag nicht Eigentuemer | Formaler Ablehnungsgrund | Gutachten umschreiben oder neu beauftragen lassen |
| Gutachten fuer ein MFH, geltend gemacht fuer eine einzelne Eigentumswohnung ohne deren Benennung | Nicht zuordenbar | Ergaenzung des Gutachters anfordern |
| Betroffene Jahre bereits bestandskraeftig | Gutachten wirkt fuer diese Jahre nicht mehr | Vor Beauftragung pruefen, welche Jahre offen sind |
| Restnutzungsdauer aus dem Grundsteuerwertbescheid uebernommen | Fuer die Einkommensteuer nicht verwendbar | Eigenes Gutachten oder typisierte AfA |
| Restnutzungsdauer sehr kurz bei hohem Gebaeudeanteil in der Kaufpreisaufteilung | Widerspruch, den das Finanzamt aufgreift | Konsistenz herstellen lassen, Steuerberater einbinden |
| Gutachten ohne Objektbezug (reines Baujahr-Modell) | Nachweis moeglicherweise nicht "geeignet" im Sinne der BFH-Rechtsprechung | Nachbesserung: Zustandsbeschreibung, Fotos, Modernisierungsgrad |
| AfA-Satz oder -Basis weicht vom Vorjahr ab, aber "1 = wie Vorjahr" gesetzt | Formfehler, Rueckfrage sicher | Kennzeichen 2 und Erlaeuterung |
| Objekt juenger als 3 Jahre und Netto-Sanierung ueber 10 % der Gebaeude-AK | 15 %-Grenze in Reichweite | Weitere Massnahmen vor Beauftragung mit Steuerberater abstimmen |
| 3 von 4 Kernmerkmalen (Heizung/Sanitaer/Elektro/Fenster) in 5 Jahren modernisiert | Standardhebung = Herstellungskosten statt Sofortabzug | Einordnung durch Steuerberater vor Abgabe |
| Hausgeld komplett als Werbungskosten | Ruecklagenzufuehrung faelschlich abgezogen | Jahresabrechnung zerlegen |
| Zinsen aus Darlehen ohne nachweisbaren Objektbezug | Abzug gefaehrdet | Verwendungsnachweis, ggf. Aufteilung |
| Vermietung an Angehoerige unter 66 % der ortsueblichen Warmmiete | Werbungskostenkuerzung bzw. Prognosepflicht | Miete pruefen, Prognose erstellen, Anpassung zum Jahreswechsel empfehlen |
| Leerstand ueber 12 Monate ohne dokumentierte Vermietungsbemuehungen | Einkunftserzielungsabsicht in Frage | Inserate, Maklerauftrag, Preisanpassungen sammeln |
| Kaution als Einnahme gebucht | Falsch, solange keine Verrechnung | Nur verrechnete Betraege in Zeile 25 |
| Grunderwerbsteuer oder Notar Kaufvertrag als sofortige Werbungskosten | Anschaffungskosten, nicht Werbungskosten | In AfA-Basis umbuchen |
| Photovoltaik-Einnahmen in der Anlage V | Falsche Einkunftsart | Paragraf 3 Nr. 72 EStG pruefen, sonst Anlage G |
| Verkauf im Steuerjahr | Zeile 8, AfA zeitanteilig, Paragraf-82b-Rest, Zinsen nach Verkauf, ggf. Paragraf 23 EStG | Sonderpruefung, Steuerberater-Frage |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Kaufpreisaufteilung fehlt | Aufteilung nach Bodenrichtwert vorschlagen, als Schaetzung kennzeichnen, Steuerberater-Frage |
| Vorjahres-AfA unbekannt | Aus Anschaffungsdaten rekonstruieren, mit Vorjahres-Bescheid abgleichen lassen |
| Zinsbescheinigung fehlt | Zinsen nicht schaetzen; Position offen lassen, Bescheinigung anfordern |
| Hausgeldabrechnung fehlt | Nur Vorauszahlungen ansetzen, Abrechnungsspitze als offen markieren; Ruecklagenzufuehrung anteilig herausrechnen nach Wirtschaftsplan |
| Zahlungsdatum eines Belegs unklar | Rechnungsdatum vorlaeufig, Position als "Zuordnung Steuerjahr pruefen" markieren |
| Ortsuebliche Miete fuer Angehoerigen-Vergleich fehlt | Mietspiegel/Mietdatenbank vorschlagen, Quote als vorlaeufig kennzeichnen |
| Gutachten-Stichtag oder -Methode fehlt | Gutachten-Check als unvollstaendig ausweisen, keine AfA-Umstellung ohne diese Angaben |
| Eigentumsanteile unklar | Grundbuchauszug anfordern; Zurechnung nicht raten |
| Belege ohne Objektbezug | In Klaerungsliste, nicht zuordnen |

---

## Konfidenz-Bewertung

| Stufe | Wert | Bedeutung |
|-------|------|-----------|
| Hoch | >= 0.90 | Alle Zahlen aus Bescheinigungen/Belegen, keine Schaetzung, keine strittige Einordnung |
| Mittel | 0.70 - 0.89 | Einzelne Positionen geschaetzt oder Wahlrecht offen, Kernzahlen belegt |
| Niedrig | 0.50 - 0.69 | AfA-Basis oder Klassifikation groesserer Massnahmen unsicher |
| Unsicher | < 0.50 | Wesentliche Grundlagen fehlen (Kaufvertrag, Zinsbescheinigung, Mietkonto) |

Faktoren, die den Score senken: fehlende Kaufpreisaufteilung (-0.15), Gutachten ohne Stichtag/Methode (-0.15), 15 %-Grenze nicht pruefbar bei Objekt unter 3 Jahren (-0.10), Hausgeld nicht zerlegbar (-0.10), Zahlungsdaten unklar (-0.05 je Position bis -0.20).

---

## Rechtsstand-Tabelle (Stand September 2026 -- vor jeder Nutzung gegen aktuelle Rechtslage pruefen)

| Thema | Regel | Grundlage |
|-------|-------|-----------|
| Zufluss/Abfluss, 10-Tage-Regel | Zahlungsjahr massgeblich; wiederkehrende Zahlungen um den Jahreswechsel dem Jahr der wirtschaftlichen Zugehoerigkeit | Paragraf 11 EStG |
| AfA-Saetze Gebaeude | 2 % / 2,5 % / 3 % nach Fertigstellung; 5 % degressiv fuer Neubau mit Baubeginn 10/2023-09/2029 | Paragraf 7 Abs. 4 S. 1, Abs. 5a EStG |
| Kuerzere Nutzungsdauer | Jede geeignete sachverstaendige Methode, auch modellhaft nach ImmoWertV; kein Bausubstanzgutachten noetig; BMF-Schreiben vom 22.02.2023 am 01.12.2025 aufgehoben | Paragraf 7 Abs. 4 S. 2 EStG; Paragraf 11c EStDV; BFH IX R 25/19 (28.07.2021), IX R 14/23 (23.01.2024); BMF IV C 3 - S 2196/00040/006/008 |
| Nachtraegliche HK nach anerkanntem Gutachten | Weiterhin bisheriger Prozentsatz zulaessig | R 7.4 Abs. 9 S. 2 EStR |
| Anderes Wirtschaftsgut / Neubau nach Sanierung | Neue AfA-Reihe, Gutachten wirkt nicht mehr | R 7.3 Abs. 5 S. 2, R 7.4 Abs. 9 S. 4 EStR; H 7.4 EStH |
| Aenderbarkeit von Bescheiden | Nur offene Jahre (keine Erklaerung, Einspruchsfrist, Vorbehalt der Nachpruefung); Paragraf 173 AO scheidet bei eigenem Verschulden aus | Paragrafen 164, 173 AO |
| Sonder-AfA Mietwohnungsneubau | 5 % p.a. fuer 4 Jahre, Bauantrag 2023-09/2029, Kostenobergrenzen | Paragraf 7b EStG |
| Denkmal | 8 x 9 %, 4 x 7 % | Paragraf 7i EStG |
| Anschaffungsnahe Herstellungskosten | 15 % der Gebaeude-AK netto in 3 Jahren nach Anschaffung | Paragraf 6 Abs. 1 Nr. 1a EStG |
| Vereinfachung Kleinmassnahmen | Bis 4.000 EUR netto auf Antrag Erhaltungsaufwand | R 21.1 Abs. 2 S. 2 EStR |
| Verteilung Erhaltungsaufwand | 2-5 Jahre gleichmaessig, Wohngebaeude im Privatvermoegen | Paragraf 82b EStDV |
| Unentgeltlicher Erwerb | AfA des Rechtsvorgaengers fortfuehren | Paragraf 11d EStDV |
| Einbaukueche | Einheitliches Wirtschaftsgut, 10 Jahre | BFH IX R 14/15 (03.08.2016) |
| GWG | Bis 800 EUR netto Sofortabzug | Paragraf 6 Abs. 2 EStG |
| Kaufpreisaufteilung | Vertragliche Aufteilung massgeblich, wenn nicht grundlegend unrealistisch | BFH IX R 26/19 (21.07.2020) |
| Verbilligte Vermietung | 66 % / 50 % der ortsueblichen Warmmiete | Paragraf 21 Abs. 2 EStG; BFH IX R 17/21 (Luxusobjekte) |
| Einkunftserzielungsabsicht | Typisierend bei dauerhafter Wohnraumvermietung | BMF-Schreiben vom 08.10.2004 |
| Fahrtkosten | 0,30 EUR/km bzw. tatsaechliche Kosten; Entfernungspauschale bei regelmaessiger Taetigkeitsstaette | Paragraf 9 EStG; BFH IX R 18/15 (01.12.2015) |
| Bauabzugsteuer | 15 % Einbehalt ohne Freistellungsbescheinigung; Zwei-Wohnungen-Regel; Freigrenzen 5.000/15.000 EUR | Paragrafen 48-48d EStG |
| Fristen 2025 | 31.07.2026 ohne / 01.03.2027 mit Beratung; Verspaetungszuschlag automatisch nach 14 Monaten | Paragrafen 149, 152 AO |
| Formulare | Anlage V, V-FeWo (Ferienwohnung/kurzfristig), V-Sonstige (Beteiligungen u.a.) seit VZ 2023 | Amtliche Vordrucke |

---

## Grenzen des Skills

Dieser Skill bereitet die Anlage V vor und macht sie pruefbar -- er ersetzt keine Steuerberatung. AfA-Umstellungen nach Gutachten, die Einordnung groesserer Baumassnahmen, Wahlrechte (Paragraf 82b, Disagio, Zuschuesse), verbilligte Vermietung und alle Faelle mit Verkauf, Gesellschaften oder Auslandsbezug muss ein Steuerberater final beurteilen. Zeilennummern gelten fuer den Vordruck 2025; Saetze, Grenzen und Verwaltungsauffassungen aendern sich.

---

## Verwandte Wissensdatenbanken

- `knowledge/anlage-v-formularstruktur.md` -- Zeilenstruktur der Anlage V 2025 und Rechtsstand-Tabelle zum Nachschlagen
- `knowledge/rechtsgrundlagen.md` -- Steuerliche Grundlagen, Grunderwerbsteuer, Mietrecht
- `knowledge/kalkulationsformeln.md` -- AfA-Berechnung, Denkmal-AfA, Cashflow nach Steuern
- `skills/beleg-sortierer/SKILL.md` -- Vorheriger Schritt: Belege klassifizieren, 15 %-Tracking, Standardhebung
- `skills/datev-vorbereitung/SKILL.md` -- Alternative Uebergabe an die Kanzlei als Buchungsstapel
- `skills/kaufvertrag-pruefung/SKILL.md` -- Kaufpreisaufteilung und Inventarausweis als AfA-Basis
- `skills/nebenkosten-pruefer/SKILL.md` -- Hausgeld- und Betriebskostenabrechnungen zerlegen
- `skills/dokument-klassifizierer/SKILL.md` -- Zinsbescheinigungen, Bescheide, Abrechnungen erkennen
