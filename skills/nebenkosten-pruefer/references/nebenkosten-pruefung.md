# Nebenkosten-Pruefung: Rechtsanker und Regressionstests

**Stand:** 2026-08-29

**Geltungsbereich:** Wohnraummiete in Deutschland
**Zweck:** Referenz fuer den Nebenkosten-Pruefer; keine Rechtsberatung.

Diese Datei verbindet gesetzliche Primaerquellen mit Regressionstests fuer typische Fehlkonstellationen. Die Testfaelle strukturieren die Pruefung, ersetzen aber keine Rechtsquelle.

## Quellenhierarchie

1. Aktuelle Gesetzesfassung und einschlaegige hoechstrichterliche Rechtsprechung
2. Mietvertrag, Nachtraege, Abrechnung, Rechnungen und Messdaten des konkreten Falls
3. Verwalter- oder Messdienstunterlagen als Tatsachenquelle
4. Regressionstestfaelle als Such- und Risikosignal, niemals als alleinige Rechtsgrundlage

Bei Widerspruch gewinnt die hoehere Ebene. Unsichere Rechtsprechungsfragen werden als `RECHTLICH PRUEFEN` markiert, nicht erraten.

## Gate 1: Vertragsmodell bestimmen

| Modell | Jahresabrechnung | Nachforderung / Guthaben | Anpassung |
|---|---|---|---|
| Betriebskostenvorauszahlung | Ja, jaehrlich (§ 556 Abs. 3 BGB) | Nach korrekter, fristgerechter Abrechnung | Nach Abrechnung auf angemessene Hoehe (§ 560 Abs. 4 BGB) |
| Betriebskostenpauschale | Grundsaetzlich nein | Grundsaetzlich mit der Pauschale abgegolten | Erhoehung nur bei wirksamer Vertragsklausel; Senkung ist weiterzugeben (§ 560 Abs. 1-3 BGB) |
| Inklusiv- / Bruttowarmmiete | Keine separate kalte Betriebskostenabrechnung | Grundsaetzlich keine separate Nachforderung | Vertrags- und HeizkostenV-Pruefung erforderlich |
| Mischmodell | Nur fuer die als Vorauszahlung vereinbarten Positionen | Nur fuer abrechenbare Positionen | Je Kostenblock getrennt pruefen |
| Unklar | Kein belastbares Endurteil | Nicht berechnen | Mietvertrag und Nachtraege anfordern |

**Stop-Regel:** Der gesetzliche Flaechenschluessel nach § 556a BGB ersetzt keine fehlende Vereinbarung, dass der Mieter Betriebskosten ueberhaupt traegt. Erst Umlagepflicht, dann Umlageschluessel.[1][2]

## Gate 2: Formell, materiell oder nicht pruefbar

- **Formeller Mindestkern:** Gesamtkosten, angewandter Verteilerschluessel, Berechnung des Mieteranteils und Abzug der Vorauszahlungen muessen fuer den Mieter nachvollziehbar sein. Zweifel an der formellen Wirksamkeit als Rechtspruefung markieren.
- **Materieller Fehler:** Abrechnung ist nachvollziehbar, aber Kostenart, Betrag, Schluessel, Zeitraum oder Rechenweg ist falsch.
- **Nicht pruefbar:** Notwendiger Vertrag, Gesamtwert, Schluessel, Zaehlerstand, Rechnung oder Vorauszahlungsnachweis fehlt.

Nicht jeder falsche Betrag macht die gesamte Abrechnung formell unwirksam. Der Bericht muss die Fehlerklasse nennen und darf nicht pauschal `unwirksam` behaupten.

## Fristen und Verfahrensrechte

- Ueber Vorauszahlungen ist jaehrlich abzurechnen (§ 556 Abs. 3 BGB).[1]
- Die Abrechnung muss spaetestens bis zum Ablauf des zwoelften Monats nach Ende des Abrechnungszeitraums zugehen.[1]
- Nach Fristablauf ist eine Vermieternachforderung grundsaetzlich ausgeschlossen. Ausnahme: Der Vermieter hat die Verspaetung nicht zu vertreten. Diese Ausnahme nie automatisch verneinen oder bejahen.[1]
- Ein Guthaben des Mieters bleibt trotz verspaeteter Abrechnung zu beruecksichtigen.
- Mietereinwendungen sind grundsaetzlich innerhalb von zwoelf Monaten nach Zugang mitzuteilen; auch hier kennt das Gesetz eine Nichtvertretenmuessen-Ausnahme.[1]
- Der Mieter kann Belegeinsicht verlangen. Der Vermieter darf Belege elektronisch bereitstellen (§ 556 Abs. 4 BGB).[1]
- Der Grundsatz der Wirtschaftlichkeit ist Teil der Abrechnungspruefung (§ 556 Abs. 3 BGB).[1]

## Umlagefaehigkeit: Risikomatrix

Die BetrKV erfasst laufend entstehende Betriebskosten und grenzt insbesondere Verwaltung sowie Instandhaltung/Instandsetzung aus.[4]

| Position / Muster | Pruefregel |
|---|---|
| Grundsteuer | In § 2 Nr. 1 BetrKV genannt; zusaetzlich wirksame Umlagevereinbarung pruefen |
| Wasser / Entwaesserung | Verbrauch, Grundgebuehr, Miet- und Verwendungskosten von Wasserzaehlern trennen; Kauf oder Erneuerung nicht automatisch als laufende Kosten verteilen |
| Hauswart | Verguetung, Sozialbeitraege und geldwerte Leistungen nur fuer umlagefaehige Taetigkeiten; Verwaltung, Reparatur, Erneuerung und Instandhaltung herausrechnen; Doppelansatz mit Reinigung, Gartenpflege usw. verhindern |
| Wartung | Regelmaessige Betriebs- und Sicherheitspruefung kann umlagefaehig sein; stoerungsbedingte Reparatur und Teiletausch trennen |
| Abrechnungserstellung | Kosten der Berechnung und Aufteilung von Heizkosten koennen nach § 7 Abs. 2 HeizkostenV Betriebskosten sein; allgemeine Erstellung der Betriebskostenabrechnung ist Verwaltung und nicht umlagefaehig.[4][8] |
| Rauchwarnmelder | Mietkosten sind keine umlagefaehigen sonstigen Betriebskosten; Kauf und Wartung getrennt pruefen. Wartung nur mit belastbarer Vertrags- und Rechtsgrundlage freigeben.[20] |
| Kabel / Breitband | Seit 1. Juli 2024 sind Nutzungsentgelte und laufende Breitband-Grundgebuehren nicht mehr wie zuvor ueber § 2 Nr. 15 BetrKV umlagefaehig; nur die aktuell noch genannten Kostenbestandteile pruefen |
| Sonstige Betriebskosten | Muessen laufend im Sinn von § 1 BetrKV und im Mietvertrag konkret bezeichnet sein; Sammelbegriff allein reicht fuer neue Sonderpositionen nicht sicher aus |
| Leerstand | Vermieteranteil nicht auf belegte Einheiten verschieben |
| Verwaltung, Bank, Recht, Reparatur | Nicht als Betriebskosten umlegen (§ 1 Abs. 2 BetrKV bzw. kein Katalogtatbestand) |
| WEG-Ruecklage / Sonderumlage | Die WEG-Zahlungsposition selbst nicht uebernehmen; die zugrunde liegende Ausgabe separat gegen Vertrag und BetrKV pruefen |
| Eigenleistung Vermieter | Hoechstens Wert einer gleichwertigen Drittleistung, ohne fiktive Umsatzsteuer (§ 1 Abs. 1 BetrKV) |

## Umlageschluessel

1. Vertraglichen Schluessel je Position erfassen.
2. Spezialrecht und Verbrauchserfassung pruefen.
3. Nur wenn Betriebskosten wirksam uebertragen wurden und kein anderer Schluessel gilt, § 556a BGB anwenden.
4. Verbrauchs- oder verursachungsabhaengige Kosten nach erfasstem Verbrauch oder Verursachung verteilen.
5. Bei vermietetem Wohnungseigentum gilt ohne abweichende Vereinbarung grundsaetzlich der WEG-Verteilungsmassstab (§ 556a Abs. 3 BGB), sofern er billigem Ermessen entspricht.[2]
6. Leerstand im Nenner und Vermieteranteil korrekt behandeln; belegte Einheiten duerfen den Leerstand nicht finanzieren.

## Heiz- und Warmwasserkosten

### Anwendungsbereich und Ausnahmen

Die HeizkostenV geht Vertragsklauseln grundsaetzlich vor. Eine zentrale Ausnahme nennt § 2 HeizkostenV fuer Gebaeude mit hoechstens zwei Wohnungen, von denen der Vermieter eine selbst bewohnt.[5] Weitere Ausnahmen stehen in § 11 HeizkostenV und muessen im Einzelfall geprueft werden.[14]

### Waermecontracting und Waermepumpen-/PV-Strom

Bei einer Umstellung von Eigenversorgung auf gewerbliche Waermelieferung waehrend des Mietverhaeltnisses gilt ein eigenes Stop-Gate:

1. Der Mieter muss die Betriebskosten fuer Waerme oder Warmwasser tragen.
2. Die Waerme muss die Effizienzvoraussetzung des § 556c Abs. 1 BGB erfuellen.
3. Die Waermelieferkosten duerfen die bisherigen Eigenversorgungskosten nicht uebersteigen.
4. Die Umstellung muss spaetestens drei Monate vorher in Textform angekuendigt worden sein.[15]

Den Kostenvergleich nicht frei schaetzen. § 8 WaermeLV verlangt die Gegenueberstellung von bisheriger Eigenversorgung und hypothetischer Waermelieferung; § 9 WaermeLV stellt grundsaetzlich auf die letzten drei abgerechneten Abrechnungszeitraeume ab.[16][17]

Bei Waermepumpen gehoert der zur Waermeerzeugung verbrauchte Strom zu den in § 7 Abs. 2 HeizkostenV genannten Betriebskosten.[8] Deshalb:

- Waermepumpenstrom separat messen und von Allgemeinstrom trennen.
- Netzbezug, PV-Eigenstrom und Einspeisung nachvollziehbar abgrenzen.
- Fuer PV-Eigenstrom keinen fiktiven Stadtwerke-, Markt- oder Rabattpreis einsetzen. Fehlt eine belastbare Kosten- und Rechtsgrundlage, `RECHTLICH PRUEFEN`.
- Investition, Abschreibung, Finanzierung oder allgemeine Anlagenkosten nicht als Stromverbrauch tarnen.

### Verteilung

- Grundregel: 50 bis 70 Prozent nach erfasstem Verbrauch (§ 7 Abs. 1 HeizkostenV).[8]
- In dem in § 7 Abs. 1 Satz 2 beschriebenen Altbau-Fall mit Oel- oder Gasheizung sind 70 Prozent Verbrauchsanteil vorgeschrieben. Die Voraussetzungen einzeln pruefen; nicht nur auf das Baujahr schauen.
- Die restlichen Kosten werden nach Wohn- oder Nutzflaeche, umbautem Raum oder beheizter Flaeche verteilt, soweit die Verordnung dies zulaesst.

### Messung und Information

- Neu installierte Erfassungsgeraete muessen seit Dezember 2021 grundsaetzlich fernablesbar sein (§ 5 Abs. 2 HeizkostenV).[6]
- Nicht fernablesbare Bestandsgeraete muessen grundsaetzlich bis 31. Dezember 2026 nachgeruestet oder ersetzt werden; Haerte- und Technik-Ausnahme pruefen (§ 5 Abs. 3 HeizkostenV).[6]
- Bei fernablesbaren Geraeten sind monatliche Verbrauchsinformationen erforderlich (§ 6a HeizkostenV).[7]
- Fuer Waermepumpen lief die besondere Nachruestfrist zur Verbrauchserfassung am 30. September 2025 ab; § 12 Abs. 3 HeizkostenV fuer den konkreten Abrechnungszeitraum pruefen.

### Schaetzung bei Erfassungsausfall

§ 9a HeizkostenV erlaubt eine Ersatzermittlung nur bei Geraeteausfall oder anderen zwingenden Gruenden. Zulaessige Grundlagen sind:[18]

1. Verbrauch der betroffenen Raeume in vergleichbaren Zeitraeumen,
2. Verbrauch vergleichbarer anderer Raeume im selben Abrechnungszeitraum oder
3. Durchschnittsverbrauch des Gebaeudes oder der Nutzergruppe.

Schaetzgrund, Vergleichsdaten, betroffene Flaeche und Rechenweg muessen nachvollziehbar sein. Eine Simulationsrechnung, ein frei gewaehlter Pauschalwert oder die Behauptung `Messdienst hat geschaetzt` genuegt nicht als Pruefung. Ueberschreitet die betroffene massgebliche Flaeche 25 Prozent, ist die Sonderverteilung des § 9a Abs. 2 HeizkostenV anzuwenden.[18]

### Warmwasser bei verbundener Anlage

1. Warmwasser-Waermemenge grundsaetzlich mit Waermezaehler messen (§ 9 Abs. 2 HeizkostenV).[9]
2. Die Formel `Q = 2,5 x V x (tw - 10)` nur verwenden, wenn Messung nur mit unzumutbar hohem Aufwand moeglich ist.
3. Flaechenersatz `Q = 32 x AWohn` nur im gesetzlichen Ausnahmefall verwenden.
4. Brennstoff-, Fernwaerme- und Waermepumpen-Korrekturen aus der aktuellen Fassung anwenden.

### Kuerzungsrechte als Pruefsignal

- 15 Prozent bei entgegen der HeizkostenV nicht verbrauchsabhaengiger Abrechnung (§ 12 Abs. 1 HeizkostenV).[10]
- 3 Prozent bei pflichtwidrig fehlender Fernablesbarkeit oder fehlenden/unvollstaendigen Informationen nach § 6a HeizkostenV.[10]
- Weitere 3 Prozent koennen bei fehlender CO2-Kostenaufteilung oder fehlenden Pflichtangaben entstehen (§ 7 Abs. 4 CO2KostAufG).[12]

Kuerzungsrechte nicht blind addieren. Tatbestand, Bemessungsgrundlage, moegliche Ueberschneidung und Ausnahme zuerst pruefen; bei Streit als Rechtspruefung markieren.

## CO2-Kosten

Bei erfassten Brennstoffen oder Waermelieferungen im Anwendungsbereich des CO2KostAufG:

1. Spezifischen CO2-Ausstoss pro Quadratmeter und Jahr bestimmen.[11]
2. Gebaeude oder Wohnung in die gesetzliche Stufentabelle einordnen.
3. Vermieteranteil vor Verteilung auf den Mieter abziehen.[11][12]
4. Mieteranteil, Einstufung und Berechnungsgrundlagen in der Heizkostenabrechnung ausweisen.[12]
5. Selbstversorgung des Mieters und Nichtwohngebaeude als gesonderte Faelle behandeln.

## WEG und Eigentumswechsel

Eine WEG-Jahresabrechnung ist Rohmaterial, keine fertige Mieterabrechnung.

- WEG-Zahlungspositionen fuer Verwaltung, Ruecklage, Sonderumlage, Instandhaltung und Reparatur nicht ungeprueft uebernehmen; zugrunde liegende Ausgaben separat beurteilen.[2][4]
- Tatsaechlich angefallene Kosten und Gutschriften pruefen. Wirtschaftsplan, Hausgeldvorauszahlung oder eine vorlaeufige Simulationsrechnung ist kein endgueltiger Kostenbeleg.
- Mietvertraglichen oder gesetzlichen Mieterschluessel anwenden; nicht ungeprueft den WEG-Schluessel kopieren.
- Mieter-Vorauszahlungen statt WEG-Hausgeldzahlungen abziehen.
- Bei Eigentuemerwechsel Aussenverhaeltnis zum Mieter, Abrechnungszeitraum, Grundbuchumschreibung sowie kaufvertraglichen Nutzen-Lasten-Wechsel getrennt pruefen. Keine pauschale Zustaendigkeitsaussage ohne Daten und aktuelle Rechtsprechung.

## Unterjaehriger Mieterwechsel

- Eine einheitliche Abrechnung fuer den Nutzungszeitraum erstellen; keine kuenstliche Teilabrechnung nur wegen Mieterwechsel.
- Zeitabhaengige kalte Kosten sachgerecht zeitanteilig verteilen.
- Zwischenablesung der betroffenen Raeume ist der gesetzliche Regelfall (§ 9b Abs. 1 HeizkostenV).[19]
- Verbrauchskosten auf Grundlage der Zwischenablesung verteilen. Uebrige Heizkosten nach anerkannten Gradtagszahlen oder zeitanteilig, uebrige Warmwasserkosten zeitanteilig aufteilen (§ 9b Abs. 2 HeizkostenV).[19]
- Gradtagszahlen nicht anstelle vorhandener Verbrauchswerte fuer den Verbrauchsanteil verwenden.
- Ist Zwischenablesung technisch unmoeglich oder ungenau, Ersatzmassstab und Begruendung nach § 9b Abs. 3 HeizkostenV dokumentieren.

## Vorauszahlung oder Pauschale anpassen

### Vorauszahlung

`korrigierte umlagefaehige Jahreskosten / 12 = neue monatliche Basis`

Konkrete, bereits absehbare Aenderungen duerfen nachvollziehbar einbezogen werden. Ein pauschaler Sicherheitsaufschlag von 10 oder 15 Prozent ist keine belastbare Standardregel.[3][13]

### Pauschale

- Erhoehung nur, soweit der Mietvertrag dies vorsieht; Grund und Berechnung in Textform erlaeutern (§ 560 Abs. 1 BGB).[3]
- Kostensenkungen unverzueglich weitergeben (§ 560 Abs. 3 BGB).[3]
- Keine Abrechnung mit Nachforderung simulieren.
- HeizkostenV-Vorrang und Ausnahmen separat pruefen.

## Regressionstest-Matrix

| Fall | Erwartete Reaktion des Skills |
|---|---|
| Vertrag nennt `Pauschale`, Abrechnung fordert 900 EUR nach | Nachforderung blockieren und Vertrags-/Heizkosten-Sonderpruefung ausgeben |
| Vertrag fehlt, Abrechnung ist rechnerisch korrekt | Keine Umlagefaehigkeit unterstellen; Ergebnis `nicht abschliessend pruefbar` |
| ETW-Verwalterabrechnung wird 1:1 weitergereicht | Verwaltung, Ruecklage, Reparatur und falsche Vorauszahlungen erkennen |
| Hauswart macht Reinigung und Reparaturen | Taetigkeitsanteile und Doppelansatz verlangen; nicht gesamten Lohn freigeben |
| Wasserzaehler wurde gekauft | Nicht automatisch ueber Nutzungsdauer verteilen; aktuelle Rechtslage und Belegart pruefen |
| Allgemeine Kosten `Abrechnungserstellung` | Als Verwaltung entfernen; nur spezialgesetzlich erfasste Mess-/Heizkostenabrechnung getrennt pruefen |
| Rauchwarnmelder werden gemietet | Mietkosten nach BGH VIII ZR 379/20 entfernen; Wartungsanteil separat pruefen |
| Bestehende Versorgung wird auf Contracting umgestellt | § 556c BGB und WaermeLV als Stop-Gate anwenden |
| PV-Strom fuer Waermepumpe wird mit Orts- oder Rabattpreis angesetzt | Fiktiven Preis blockieren; Messung, Kostenbasis und Rechtsgrundlage anfordern |
| Messdienst schaetzt ohne Bezugsdaten | §-9a-Grund, Methode, Rechenweg und 25-Prozent-Schwelle anfordern |
| Mieterwechsel trotz Zwischenablesung nur nach Gradtagen | Verbrauchsanteil nach Zwischenablesung korrigieren; § 9b anwenden |
| Leerstand wird aus Gesamtflaeche entfernt | Vermieter-Leerstandsanteil wieder einsetzen |
| Abrechnung kommt nach Frist | Nachforderung grundsaetzlich ausschliessen, aber Nichtvertretenmuessen-Ausnahme abfragen |
| Fernablesbare Zaehler, keine Monatsinformation | Moegliches 3-Prozent-Kuerzungsrecht markieren |
| CO2-Kosten voll auf Mieter | Vermieteranteil und Pflichtangaben neu berechnen |
| Vorauszahlung plus pauschal 15 Prozent | Puffer entfernen; nur korrigierte Ist-Kosten und konkret belegte Aenderungen verwenden |
| Zweifamilienhaus, Vermieter wohnt in Einheit 1 | Ausnahme des § 2 HeizkostenV pruefen, nicht automatisch Standardsplit erzwingen |
| Mieter zieht im Oktober aus | Zwischenablesung und sachgerechte Zeit-/Verbrauchsabgrenzung verlangen |

## Primaerquellen

- § 556 BGB: https://www.gesetze-im-internet.de/bgb/__556.html
- § 556a BGB: https://www.gesetze-im-internet.de/bgb/__556a.html
- § 560 BGB: https://www.gesetze-im-internet.de/bgb/__560.html
- BetrKV: https://www.gesetze-im-internet.de/betrkv/BJNR234700003.html
- HeizkostenV: https://www.gesetze-im-internet.de/heizkostenv/
- CO2KostAufG: https://www.gesetze-im-internet.de/co2kostaufg/
- § 556c BGB: https://www.gesetze-im-internet.de/bgb/__556c.html
- WaermeLV §§ 8-9: https://www.gesetze-im-internet.de/w_rmelv/
- HeizkostenV §§ 9a-9b: https://www.gesetze-im-internet.de/heizkostenv/
- BGH, Urteil vom 28.09.2011, VIII ZR 294/10: Anpassung von Betriebskostenvorauszahlungen
- BGH, Urteil vom 11.05.2022, VIII ZR 379/20: Mietkosten fuer Rauchwarnmelder

Vor produktiver Nutzung den Versionsstand der Quellen pruefen. Gesetzeslinks sind kanonisch; abgeleitete Aussagen in dieser Datei bei Gesetzesaenderungen aktualisieren.

## Sources

[1] https://www.gesetze-im-internet.de/bgb/__556.html — § 556 BGB
[2] https://www.gesetze-im-internet.de/bgb/__556a.html — § 556a BGB
[3] https://www.gesetze-im-internet.de/bgb/__560.html — § 560 BGB
[4] https://www.gesetze-im-internet.de/betrkv/BJNR234700003.html — Betriebskostenverordnung
[5] https://www.gesetze-im-internet.de/heizkostenv/__2.html — § 2 HeizkostenV
[6] https://www.gesetze-im-internet.de/heizkostenv/__5.html — § 5 HeizkostenV
[7] https://www.gesetze-im-internet.de/heizkostenv/__6a.html — § 6a HeizkostenV
[8] https://www.gesetze-im-internet.de/heizkostenv/__7.html — § 7 HeizkostenV
[9] https://www.gesetze-im-internet.de/heizkostenv/__9.html — § 9 HeizkostenV
[10] https://www.gesetze-im-internet.de/heizkostenv/__12.html — § 12 HeizkostenV
[11] https://www.gesetze-im-internet.de/co2kostaufg/__5.html — § 5 CO2KostAufG
[12] https://www.gesetze-im-internet.de/co2kostaufg/__7.html — § 7 CO2KostAufG
[13] https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VIII_ZS/2010/VIII_ZR_294-10.pdf?__blob=publicationFile&v=1 — BGH VIII ZR 294/10
[14] https://www.gesetze-im-internet.de/heizkostenv/__11.html — § 11 HeizkostenV
[15] https://www.gesetze-im-internet.de/bgb/__556c.html — § 556c BGB
[16] https://www.gesetze-im-internet.de/w_rmelv/__8.html — § 8 WärmeLV
[17] https://www.gesetze-im-internet.de/w_rmelv/__9.html — § 9 WärmeLV
[18] https://www.gesetze-im-internet.de/heizkostenv/__9a.html — § 9a HeizkostenV
[19] https://www.gesetze-im-internet.de/heizkostenv/__9b.html — § 9b HeizkostenV
[20] https://www.bundesgerichtshof.de/SharedDocs/Entscheidungen/DE/Zivilsenate/VIII_ZS/2020/VIII_ZR_379-20.pdf?__blob=publicationFile&v=1 — BGH VIII ZR 379/20
