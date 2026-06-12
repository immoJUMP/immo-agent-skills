---
name: nebenkosten-pruefer
description: "Validiert Nebenkostenabrechnungen auf formelle und materielle Fehler, prueft Umlagefaehigkeit nach BetrKV, HeizKV-Konformitaet und berechnet Vorauszahlungsanpassungen. Nutze diesen Skill wenn du eine Abrechnung vor Versand pruefen oder Mietereinwaende bewerten willst."
---

# Nebenkosten-Pruefer -- Nebenkostenabrechnung validieren

## Wann nutzen

- Nebenkostenabrechnung vor Versand an Mieter pruefen
- Abrechnung vom Verwalter oder WEG auf Fehler kontrollieren
- Umlagefaehigkeit einzelner Kostenpositionen pruefen (BetrKV)
- Heizkosten-Verteilung auf Compliance mit HeizKV pruefen
- Vorauszahlungsanpassung fuer die naechste Periode berechnen
- Einwendungen von Mietern gegen die Abrechnung bewerten

---

## Inputs

| Feld | Typ | Pflicht | Beschreibung |
|------|-----|---------|--------------|
| `billing_statement` | Object/Text | Ja | Nebenkostenabrechnung (strukturiert oder als Text/PDF-Extrakt) |
| `billing_period` | Object | Ja | Abrechnungszeitraum: `start_date`, `end_date` |
| `delivery_date` | String | Nein | Datum der Zustellung an den Mieter |
| `property_data` | Object | Nein | Objektdaten: Gesamtflaeche, Einheitenzahl, Personenzahl je Einheit |
| `unit_data` | Object | Nein | Daten der abgerechneten Einheit: Flaeche, Personenzahl, Verbrauchswerte |
| `prepayment_monthly_eur` | Number | Nein | Monatliche Nebenkostenvorauszahlung des Mieters |
| `lease_agreement_clauses` | Text | Nein | Relevante Mietvertragsklauseln zur Nebenkostenumlage |
| `previous_billing` | Object | Nein | Vorjahresabrechnung zum Vergleich |

---

## Auftrag

Du bist ein erfahrener Immobilienverwalter mit Expertise in der Nebenkostenabrechnung nach deutschem Mietrecht. Pruefe die uebergebene Abrechnung systematisch auf formelle und materielle Fehler. Beachte die Vorgaben des §556 BGB, der Betriebskostenverordnung (BetrKV) und der Heizkostenverordnung (HeizKV). Identifiziere Fehler, berechne die korrekten Werte und empfehle Korrekturen.

---

## Strategie

1. **Formelle Pruefung (§556 Abs. 3 BGB)** -- Ohne korrekte Form ist die Abrechnung unwirksam:
   - Absender und Empfaenger korrekt und vollstaendig?
   - Abrechnungszeitraum angegeben und exakt 12 Monate? (Ausnahme: Erstabrechnung bei Mietbeginn, Endabrechnung bei Mietende)
   - Abrechnungsobjekt eindeutig bezeichnet?
   - Zustellungsfrist eingehalten? Abrechnung muss innerhalb von 12 Monaten nach Ende des Abrechnungszeitraums zugehen (§556 Abs. 3 S. 2 BGB). Nach Fristablauf: keine Nachforderung moeglich, Guthaben muss trotzdem ausgezahlt werden.
   - Gesamtkosten je Position angegeben?
   - Umlageschluessel je Position angegeben und nachvollziehbar?
   - Berechnung des Mieteranteils nachvollziehbar?
   - Vorauszahlungen korrekt angerechnet?
   - Saldo (Nachzahlung/Guthaben) korrekt berechnet?

2. **Abrechnungszeitraum pruefen** -- Detail-Check:
   - Zeitraum ist exakt 12 Monate (z.B. 01.01.2025 - 31.12.2025)
   - Bei unterjaerigem Mietbeginn/-ende: anteilige Berechnung korrekt (tagesgenau)?
   - Kein Ueberlappen mit vorheriger Abrechnung
   - Alle Kostenpositionen beziehen sich auf den Abrechnungszeitraum (keine periodfremden Kosten)

3. **Umlagefaehigkeit pruefen (BetrKV §1-2)** -- Jede Kostenposition gegen die Betriebskostenverordnung pruefen:

   | Umlagefaehig (BetrKV §2) | Nicht umlagefaehig |
   |--------------------------|-------------------|
   | Grundsteuer | Verwaltungskosten |
   | Wasserversorgung | Instandhaltung / Reparaturen |
   | Entwasserung | Instandsetzung |
   | Heizung | Bankgebuehren |
   | Warmwasser | Leerstandskosten (traegt Vermieter) |
   | Aufzug | Mietausfallversicherung |
   | Strassenreinigung | Rechtsschutzversicherung |
   | Muellabfuhr | Porto / Telefonkosten des Verwalters |
   | Hausreinigung | Einmalige Kosten (keine laufenden Betriebskosten) |
   | Gartenpflege | |
   | Allgemeinbeleuchtung | |
   | Schornsteinfeger | |
   | Sach-/Haftpflichtversicherung | |
   | Hauswart (nur Betriebskosten-Anteil) | |
   | Gemeinschaftsantenne / Kabel | |
   | Wascheinrichtung | |
   | Sonstige (nur wenn im Mietvertrag vereinbart) | |

4. **Umlageschluessel validieren** -- Pruefen ob der verwendete Schluessel zulaessig und korrekt angewendet ist:
   - Nach Wohnflaeche (qm): Mieteranteil = Wohnflaeche Einheit / Gesamtwohnflaeche
   - Nach Personenzahl: Mieteranteil = Personen in Einheit / Gesamtpersonenzahl
   - Nach Einheiten: Mieteranteil = 1 / Anzahl Einheiten
   - Nach Verbrauch: individuelle Zaehler erforderlich
   - Stimmt der verwendete Schluessel mit dem Mietvertrag ueberein?
   - Ist der Schluessel fuer die jeweilige Kostenart sachgerecht?
   - Aenderung des Umlageschluessels nur unter bestimmten Voraussetzungen zulaessig

5. **Heizkosten-Verordnung (HeizKV) pruefen** -- Spezialregeln fuer Heiz- und Warmwasserkosten:
   - Verbrauchsabhaengiger Anteil: mindestens 50%, maximal 70% (§7 HeizKV)
   - Grundkostenanteil: 30% - 50% (nach Flaeche)
   - Verbrauchserfassung korrekt? (Heizkostenverteiler, Waermemengenzaehler)
   - Warmwasserkostenberechnung nach §9 HeizKV (Formel: Warmwasseranteil = 2,5 x V x (tw - 10) / Brennstoffverbrauch gesamt)
   - Rohrwaermeabzug beruecksichtigt?
   - Bei fehlender Verbrauchserfassung: Kuerzungsrecht des Mieters um 15% (§12 HeizKV)

6. **Rechnerische Pruefung** -- Jede Berechnung nachrechnen:
   - Gesamtkosten x Umlageschluessel = Mieteranteil (pro Position)
   - Summe aller Mieteranteile = Gesamtbetriebskosten Mieter
   - Gesamtbetriebskosten Mieter - geleistete Vorauszahlungen = Nachzahlung/Guthaben
   - Vorauszahlungen: 12 x monatliche Vorauszahlung (bei 12 Monaten Abrechnungszeitraum)
   - Rundungsdifferenzen pruefen (maximal wenige Cent)

7. **Vergleich mit Vorjahr** -- Falls Vorjahresabrechnung vorliegt:
   - Kostensteigerungen > 10% je Position identifizieren
   - Neue Positionen pruefen (waren sie im Mietvertrag vereinbart?)
   - Weggefallene Positionen pruefen
   - Plausibilitaetscheck: Sind Steigerungen erklaerbar (Energiepreise, Versicherung)?

8. **Vorauszahlungsanpassung berechnen** -- Neue monatliche Vorauszahlung empfehlen:
   - Basis: Tatsaechliche Kosten des abgelaufenen Zeitraums / 12
   - Aufschlag fuer erwartete Kostensteigerungen (optional, max. 10-15%)
   - Anpassungsrecht: §560 BGB -- Anpassung nach jeder Abrechnung zulaessig
   - Anpassungsbetrag berechnen und begruenden

9. **Fehler-Report erstellen** -- Alle Befunde strukturiert dokumentieren:
   - Schwere Fehler (formell unwirksam, falsche Betraege)
   - Mittlere Fehler (falsche Umlageschluessel, nicht umlagefaehige Kosten)
   - Leichte Fehler (Rundungsdifferenzen, fehlende Angaben)
   - Korrekturempfehlung je Fehler

---

## Ausgabeformat

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext.

Liefere die Ergebnisse in folgendem Format:

### Pruefbericht

```markdown
# Nebenkosten-Pruefung: Musterstr. 12, 10115 Berlin, WE 04

**Gesamtergebnis: 🔴 FEHLERHAFT** | Konfidenz: 88%
**Erforderliche Aktion:** Abrechnung korrigieren und erneut zustellen
**Finanzielle Auswirkung fuer den Mieter:** -300,00 EUR

| | |
|---|---|
| Objekt / Einheit | Musterstr. 12, 10115 Berlin, WE 04 |
| Mieter | Nachname, Vorname |
| Pruefdatum | 15.04.2026 |

## Abrechnungszeitraum & Zustellung

| Pruefpunkt | Wert | Status |
|------------|------|--------|
| Abrechnungszeitraum | 01.01.2025 - 31.12.2025 (12 Monate) | 🟢 gueltig |
| Zustellung | 10.04.2026 |  |
| Zustellungsfrist | 31.12.2026 | 🟢 eingehalten (265 Tage Reserve) |

## Formelle Pruefung

🟢 Bestanden -- keine formellen Maengel.
(Falls Maengel: jeden Mangel mit Auswirkung auflisten.)

## Kostenpositionen

| Position | Gesamtkosten | Umlageschluessel | Anteil Einheit | Mieteranteil | Umlagefaehig | BetrKV | Berechnung |
|----------|--------------|------------------|----------------|--------------|--------------|--------|------------|
| Grundsteuer | 4.800,00 EUR | Wohnflaeche | 12,5% | 600,00 EUR | 🟢 Ja (§2 Nr. 1 BetrKV) | OK | 🟢 korrekt |
| Verwaltungskosten | 3.600,00 EUR | Einheiten | 8,33% | 300,00 EUR | 🔴 Nein (nicht in §2 BetrKV) | Fehler | 🟢 korrekt |

**🔴 Befund Verwaltungskosten (schwer):** Verwaltungskosten sind nicht
umlagefaehig (§1 Abs. 2 Nr. 1 BetrKV). Korrektur: Position streichen,
Mieteranteil um 300,00 EUR reduzieren.

## Heizkosten-Pruefung

| Pruefpunkt | Wert | Status |
|------------|------|--------|
| Verbrauchsabhaengiger Anteil | 60% | 🟢 HeizKV-konform |
| Grundkostenanteil | 40% | 🟢 |
| Verbrauchserfassung | Heizkostenverteiler | 🟢 |
| Warmwasser separat erfasst | Ja | 🟢 |

## Rechnerische Zusammenfassung

| Kennzahl | Abgerechnet | Korrigiert |
|----------|-------------|------------|
| Gesamtkosten | 2.400,00 EUR | 2.100,00 EUR |
| Vorauszahlungen | 1.800,00 EUR | 1.800,00 EUR |
| Nachzahlung | 600,00 EUR | 300,00 EUR |

**Differenz: -300,00 EUR** -- der Mieter wuerde 300,00 EUR zu viel zahlen.

## Vorauszahlungs-Anpassung

| | |
|---|---|
| Aktuelle Vorauszahlung | 150,00 EUR/Monat |
| Empfohlene Vorauszahlung | 175,00 EUR/Monat |
| Anpassung | +25,00 EUR/Monat |
| Basis | Tatsaechliche Kosten 2025 zzgl. 5% Puffer fuer Kostensteigerungen |
| Rechtsgrundlage | §560 BGB |

## Vorjahresvergleich

Gesamtkosten: 2.000,00 EUR (Vorjahr) → 2.100,00 EUR (aktuell) = +5,0%

| Position | Vorjahr | Aktuell | Veraenderung | Plausibel | Erklaerung |
|----------|---------|---------|--------------|-----------|------------|
| Heizkosten | 800,00 EUR | 960,00 EUR | +20,0% | 🟢 Ja | Energiepreissteigerung |

## Fehler-Uebersicht

**1 Fehler gefunden** (1 schwer, 0 mittel, 0 leicht)

| Schwere | Position | Beschreibung | Auswirkung | Korrektur |
|---------|----------|--------------|------------|-----------|
| 🔴 schwer | Verwaltungskosten | Nicht umlagefaehige Kosten abgerechnet | -300,00 EUR | Position aus Abrechnung entfernen |

## Datenluecken

- Mietvertragsklauseln zur Umlage nicht vorhanden -- Umlageschluessel-Pruefung
  basiert auf gesetzlicher Standardregelung
```

---

## Qualitaetspruefung

- [ ] Abrechnungszeitraum ist exakt 12 Monate (oder begruendet abweichend)
- [ ] Zustellungsfrist (12 Monate nach Abrechnungsende) korrekt berechnet
- [ ] Jede Kostenposition gegen BetrKV §2 geprueft
- [ ] Umlageschluessel-Berechnung stimmt (Mieteranteil = Einheit / Gesamt)
- [ ] Heizkosten: verbrauchsabhaengiger Anteil zwischen 50% und 70%
- [ ] Alle Rechenoperationen nachgeprueft (keine Rundungsfehler > 1 EUR)
- [ ] Vorauszahlungen korrekt angerechnet (Anzahl Monate x Monatsbetrag)
- [ ] Saldo (Nachzahlung/Guthaben) arithmetisch korrekt
- [ ] Nicht umlagefaehige Kosten erkannt und beanstandet
- [ ] Vorauszahlungsanpassung auf Basis tatsaechlicher Kosten berechnet

---

## Warnsignale

| Signal | Bedeutung | Empfohlene Aktion |
|--------|-----------|-------------------|
| Zustellungsfrist < 30 Tage | Fristversaeumnis droht, Nachforderung verfaellt | Sofort zustellen (nachweisbar: Einschreiben oder Bote) |
| Zustellungsfrist abgelaufen | Keine Nachforderung mehr moeglich | Guthaben auszahlen, keine Nachforderung stellen |
| Verwaltungskosten umgelegt | Nicht umlagefaehig nach BetrKV | Position entfernen, Abrechnung korrigieren |
| Heizkosten 100% nach Flaeche | HeizKV-Verstoss, Kuerzungsrecht 15% | Verbrauchserfassung installieren oder korrekten Split anwenden |
| Reparaturkosten in NK | Instandhaltung ist nicht umlagefaehig | Position entfernen |
| Kostenposition > 30% Steigerung zum Vorjahr | Ungewoehnlich, Mieter wird nachfragen | Steigerung begruenden oder Beleg pruefen |
| Leerstandskosten auf Mieter umgelegt | Leerstandsrisiko traegt der Vermieter | Leerstandsanteil herausrechnen |

---

## Bei fehlenden Daten

- Wenn kein Mietvertrag vorliegt: Gesetzliche Umlageschluessel annehmen (Wohnflaeche), als Annahme kennzeichnen.
- Wenn Gesamtflaeche fehlt: Umlageschluessel-Berechnung nicht moeglich, Fehler melden und Daten anfordern.
- Wenn kein Zustellungsdatum vorliegt: Fristpruefung ueberspringen, Hinweis geben dass Zustellung nachweisbar erfolgen muss.
- Wenn keine Vorjahresabrechnung vorliegt: Vergleich ueberspringen, Positionen einzeln auf Plausibilitaet pruefen.
- Wenn Verbrauchsdaten fuer Heizkosten fehlen: HeizKV-Pruefung als "nicht pruefbar" kennzeichnen.
- Alle Luecken im Berichtsabschnitt "Datenluecken" dokumentieren.

---

## Konfidenz-Bewertung

| Score | Bedeutung |
|-------|-----------|
| 0.9 - 1.0 | Vollstaendige Abrechnung mit Mietvertrag, Objektdaten, Verbrauchswerten und Vorjahresvergleich |
| 0.7 - 0.9 | Abrechnung vollstaendig, aber Mietvertrag oder Vorjahr fehlen |
| 0.5 - 0.7 | Abrechnung unvollstaendig, einzelne Positionen nicht pruefbar |
| < 0.5 | Wesentliche Daten fehlen, Pruefung nur oberflaechlich moeglich |

Faktoren die den Score senken:
- Fehlende Mietvertragsklauseln zur Umlage (-0.10)
- Fehlende Gesamtflaeche / Einheitenzahl (-0.15)
- Keine Verbrauchsdaten fuer Heizkosten (-0.10)
- Kein Zustellungsdatum (-0.05)
- Keine Vorjahresabrechnung (-0.05)

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- §556 BGB, BetrKV, HeizKV: Nebenkostenrecht im Detail
- `knowledge/checklisten.md` -- Checkliste Nebenkostenabrechnung
- `skills/wochen-jourfixe/SKILL.md` -- NK-Abrechnungsfristen im Wochen-Report
- `skills/mahn-assistent/SKILL.md` -- Nachforderungen aus NK-Abrechnung als Forderung tracken
