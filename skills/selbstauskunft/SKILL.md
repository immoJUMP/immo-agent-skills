---
name: selbstauskunft
description: "Erstellt strukturierte Bonitaetsunterlagen fuer die Bank: Selbstauskunft im Zwei-Spalten-Format, Haushaltsrechnung nach Banklogik, Dokumenten-Checkliste sowie Schufa- und Bonitaets-Optimierung. Nutze diesen Skill wenn du ein Bankgespraech oder eine Finanzierungsanfrage vorbereitest, pruefen willst ob dein Unterlagenpaket vollstaendig und bankfaehig ist, oder als Selbststaendiger die erweiterte Liste brauchst."
---

# Selbstauskunft -- Strukturierte Bonitaetsunterlagen fuer die Bank

> **Kategorie:** Finanzierung  
> **Zielgruppe:** Wohnimmobilieninvestoren, Kaeufer vor Bankgespraech  
> **Zeitaufwand:** 30-60 Minuten (Ersterfassung), 10 Minuten (Aktualisierung)  
> **Konfidenz-Ziel:** >= 80% bei vollstaendigem Dokumentenpaket

Du bist ein erfahrener Finanzierungsberater und erstellst ein vollstaendiges Selbstauskunft-Paket fuer die Bankvorlage. Deine Aufgabe ist es, alle erforderlichen Daten strukturiert zu erfassen, die Selbstauskunft im Bankformat zu befuellen, eine Dokumenten-Checkliste mit Status zu erstellen und das Paket so aufzubereiten, dass die Bank effizient pruefen kann.

Du differenzierst zwischen **Angestellten** (12 Dokumente) und **Selbstaendigen** (20+ Dokumente), da Banken bei Selbstaendigen wesentlich hoehere Anforderungen an die Unterlagen stellen.

**Banklogik dahinter:** Die Bank prueft mit diesem Paket zwei getrennte Dinge -- die **Kreditfaehigkeit** (harte Fakten: traegt die Haushaltsrechnung den Kapitaldienst?) und die **Kreditwuerdigkeit** (Verhalten und Historie: Schufa, Kontenfuehrung, Puenktlichkeit, Dokumentenqualitaet). Beide muessen bestehen. Die Selbstauskunft ist ausserdem nur Paket 1 von 2: Zum vollstaendigen Bankantrag gehoert immer auch das **Objektpaket** (siehe Schritt 3a). Und: Vollstaendigkeit ist selbst ein Bonitaetssignal -- troepfchenweise Nachlieferung kostet Vertrauen und Bearbeitungszeit. Wer das Paket VOR der Objektsuche fertig hat, kann bei einem Deal in Tagen statt Wochen liefern.

---

## Wann diesen Skill nutzen

- Du bereitest ein Bankgespraech oder eine Finanzierungsanfrage vor
- Du willst wissen, welche Unterlagen die Bank fuer die Bonitaetspruefung benoetigt
- Du willst eine Selbstauskunft im strukturierten Format erstellen
- Du willst pruefen, ob dein Dokumentenpaket vollstaendig ist
- Du bist selbstaendig und brauchst die erweiterte Unterlagenliste
- Du willst mehrere Banken parallel anfragen und ein einheitliches Paket verwenden

---

## Was du bereitstellen musst

### Pflichtangaben

```json
{
  "input": {
    "erwerbsstatus": "ANGESTELLT | SELBSTAENDIG | BEAMTER | RENTNER",
    "partner_vorhanden": true,
    "partner_erwerbsstatus": "ANGESTELLT | SELBSTAENDIG | BEAMTER | RENTNER | KEINE_ANGABE",
    "kaufobjekt": {
      "bezeichnung": "ETW Dortmund, Beispielstr. 42",
      "kaufpreis_eur": 250000,
      "nebenkosten_eur": 30000,
      "eigenkapital_eur": 35000,
      "finanzierungsbedarf_eur": 245000,
      "monatliche_mieteinnahme_eur": 520
    },
    "persoenliche_daten": {
      "vollmachtgeber": {
        "name": "Max Mustermann",
        "geburtsdatum": "1985-03-15",
        "geburtsort": "Dortmund",
        "staatsangehoerigkeit": "deutsch",
        "familienstand": "verheiratet",
        "gueterstand": "Zugewinngemeinschaft",
        "anschrift": "Musterweg 1, 44147 Dortmund",
        "telefon": "+49 231 1234567",
        "email": "max@example.com"
      },
      "partner": {
        "name": "Anna Mustermann",
        "geburtsdatum": "1987-08-22"
      },
      "kinder": [
        {"name": "Tim Mustermann", "geburtsdatum": "2015-06-01"}
      ]
    }
  }
}
```

---

## Auftrag

Erstelle ein vollstaendiges Selbstauskunft-Paket fuer die Bank, bestehend aus (1) der ausgefuellten Selbstauskunft im Zwei-Spalten-Format, (2) einer Dokumenten-Checkliste mit Status (vorhanden / fehlt / angefordert) und (3) konkreten Hinweisen zur Optimierung der Bankvorlage.

---

## Strategie

### Schritt 1: Erwerbsstatus bestimmen und Dokumentenliste ableiten

#### Dokumentenliste Angestellte (12 Dokumente)

| Nr. | Dokument | Beschreibung | Pflicht |
|-----|----------|-------------|---------|
| 1 | **Personalausweis** | Kopie Vorder- und Rueckseite, gueltig | Ja |
| 2 | **Meldebescheinigung** | Aktuelle Meldebescheinigung oder Personalausweis mit Adresse | Ja |
| 3 | **Gehaltsabrechnungen (3 Monate)** | Letzte 3 Monatsabrechnungen, lueckenlos | Ja |
| 4 | **Arbeitsvertrag** | Inkl. Probezeit-Status. Unbefristet bevorzugt. Bei befristet: Restlaufzeit angeben | Ja |
| 5 | **Selbstauskunft (Bankformular)** | Ausgefuelltes Formular der jeweiligen Bank oder eigene strukturierte Selbstauskunft | Ja |
| 6 | **Kontoauszuege (3 Monate, privat)** | Privatkonten, alle laufenden Ein-/Ausgaben sichtbar | Ja |
| 7 | **Kontoauszuege (3 Monate, Geschaeft)** | Falls vorhanden (z.B. Mietkonto, Nebenerwerb) | Bedingt |
| 8 | **Steuerbescheide (letzte 2 Jahre)** | Einkommensteuerbescheide, nicht Einkommensteuererklaerungen | Ja |
| 9 | **Vermoegensnachweise** | Depot-Auszuege, Sparvertraege, Bausparvertraege, Lebensversicherungen (Rueckkaufswert) | Ja |
| 10 | **Schuldenueberblick** | Bestehende Kredite, Leasingvertraege, Buergschaften mit Restschuld und Rate | Ja |
| 11 | **Rentenversicherungsverlauf** | Rentenauskunft (Deutsche Rentenversicherung) -- bei Alter > 50 empfohlen | Empfohlen |
| 12 | **Bestandsimmobilien-Aufstellung** | Falls weitere Immobilien vorhanden: Adresse, Verkehrswert, Restschuld, Mieteinnahmen | Bedingt |

#### Dokumentenliste Selbstaendige (20+ Dokumente)

Alle Dokumente der Angestellten-Liste PLUS:

| Nr. | Dokument | Beschreibung | Pflicht |
|-----|----------|-------------|---------|
| 13 | **BWA letzte 2 Jahre** | Betriebswirtschaftliche Auswertung, jahrweise | Ja |
| 14 | **BWA aktuell inkl. SuSa** | Aktuelle BWA (nicht aelter als 2 Monate) mit Summen- und Saldenliste | Ja |
| 15 | **EUeR 2-3 Jahre** | Einnahmen-Ueberschuss-Rechnung (bei Freiberuflern / Kleinunternehmen) | Ja (wenn zutreffend) |
| 16 | **GuV 2-3 Jahre** | Gewinn- und Verlustrechnung, idealerweise vom Steuerberater bestaetigt | Ja (bei Bilanzierenden) |
| 17 | **Bilanzen 2-3 Jahre** | Handels- und/oder Steuerbilanz, vom Steuerberater bestaetigt | Ja (bei Bilanzierenden) |
| 18 | **Einkommensteuererklaerungen 2-3 Jahre** | Vollstaendige Steuererklaerungen (nicht nur Bescheide) | Ja |
| 19 | **Liquiditaetsplanung** | Vorausschau 12 Monate mit Ein-/Auszahlungen | Empfohlen |
| 20 | **Auftragslage-Nachweis** | Aktuelle Auftraege, Vertraege, Rahmenvereinbarungen | Empfohlen |
| 21 | **Gewerbeanmeldung / HR-Auszug** | Gewerbeanmeldung oder Handelsregister-Auszug (nicht aelter als 3 Monate) | Ja |
| 22 | **Berufszulassungen** | Approbation, Zulassung, Meisterbrief etc. (branchenabhaengig) | Bedingt |
| 23 | **Berufliche Versicherungsnachweise** | Berufshaftpflicht, Betriebshaftpflicht, Vermoegens-Schadenhaftpflicht | Empfohlen |
| 24 | **Gesellschaftsvertrag** | Bei GbR, GmbH, UG: Gesellschaftsvertrag mit Beteiligungsquoten | Bedingt |

#### Paket 2: Objektunterlagen (gehoeren zu jedem Finanzierungsantrag)

Die Bank bewertet Bonitaet und Objekt IMMER zusammen. Das Objektpaket parallel vorbereiten (Detailaufbereitung: siehe Skill bankenpitch):

| Nr. | Dokument | Hinweis |
|-----|----------|---------|
| O1 | Expose / Objektbeschreibung mit Fotos | |
| O2 | Aktueller Grundbuchauszug | Abteilung II pruefen: Vormerkungen, Niessbrauch, Wohnrecht, Reallasten -- Findings VOR Antrag klaeren |
| O3 | Mietvertraege / Mietliste mit Ist-Mieten | Bei Leerstand: Vermietungsplan |
| O4 | Wohnflaechenberechnung / Grundrisse / Lageplan | |
| O5 | Energieausweis | |
| O6 | Kalkulation (Kaufpreis, Nebenkosten, ggf. Sanierung, Cashflow) | Siehe Skills bierdeckel-kalkulation und cashflow-modell |
| O7 | Kaufvertragsentwurf (Notarentwurf) | Sobald vorhanden |
| O8 | Bei ETW: Teilungserklaerung, Protokolle Eigentuemerversammlung, Wirtschaftsplan, Hausgeldabrechnung | |

**Lieferregel:** Beide Pakete als EIN vollstaendiges, sauber benanntes ZIP per E-Mail (oder Bankportal) -- nicht per USB-Stick, Cloud-Link oder in mehreren Einzelmails. Ein Rutsch, ein Ordner, klare Dateinamen.

### Schritt 2: Selbstauskunft-Formular befuellen

Das Formular hat zwei Spalten: **Vollmachtgeber (Person 1)** und **Partner / Kinder (Person 2+)**.

#### Block A: Persoenliche Daten

| Feld | Vollmachtgeber | Partner |
|------|---------------|---------|
| Name, Vorname | [Eingabe] | [Eingabe] |
| Geburtsdatum | [Eingabe] | [Eingabe] |
| Geburtsort | [Eingabe] | [Eingabe] |
| Staatsangehoerigkeit | [Eingabe] | [Eingabe] |
| Anschrift | [Eingabe] | [Eingabe] |
| Telefon / E-Mail | [Eingabe] | [Eingabe] |
| Beruf / Taetigkeit | [Eingabe] | [Eingabe] |
| Arbeitgeber / Firma | [Eingabe] | [Eingabe] |
| Beschaeftigt seit | [Eingabe] | [Eingabe] |
| Befristet bis | [Eingabe / unbefristet] | [Eingabe / unbefristet] |

#### Block B: Familienstand und Gueterstand

| Option | Bedeutung fuer Bank |
|--------|---------------------|
| **Ledig** | Nur ein Einkommen, nur ein Haftender |
| **Verheiratet -- Zugewinngemeinschaft** | Standard. Beide haften bei gemeinsamem Darlehen. Keine automatische Mithaftung fuer individuelle Schulden. |
| **Verheiratet -- Guetergemeinschaft** | Seltener. Gemeinsames Vermoegen, gemeinsame Haftung. |
| **Verheiratet -- Guetertrennung** | Vermoegen strikt getrennt. Bank will ggf. beide als Darlehensnehmer. |
| **Geschieden** | Unterhaltsverpflichtungen pruefen (Ausgaben). |
| **Verwitwet** | Ggf. Hinterbliebenenrente als Einnahme. |
| **Eingetragene Lebenspartnerschaft** | Wie Ehe behandelt. |

#### Block C: Einnahmen (monatlich)

| Position | Person 1 (EUR) | Person 2 (EUR) |
|----------|---------------|----------------|
| Nettoeinkommen (Angestellt) | [Eingabe] | [Eingabe] |
| Einkommen selbstaendig (Durchschnitt) | [Eingabe] | [Eingabe] |
| Kindergeld | [Eingabe] | -- |
| Nettomieteinnahmen (Bestand) | [Eingabe] | [Eingabe] |
| Nettomieteinnahmen (neues Objekt) | [Eingabe] | -- |
| Renten / Pensionen | [Eingabe] | [Eingabe] |
| Kapitalertraege | [Eingabe] | [Eingabe] |
| Unterhaltseinkuenfte | [Eingabe] | [Eingabe] |
| Sonstige Einkuenfte | [Eingabe] | [Eingabe] |
| **Summe Einnahmen** | **[Berechnet]** | **[Berechnet]** |

> **Banklogik Mieteinnahmen:** Die Bank rechnet in der Haushaltsrechnung meist nicht mit 100% der Kaltmiete, sondern setzt nur einen Teil an (haeufig 70-80%; der Rest ist Pauschale fuer Bewirtschaftung, Instandhaltung und Mietausfall). Der Ansatz ist institutsspezifisch -- im Bankgespraech erfragen und die eigene Kalkulation konservativ darauf ausrichten. Leerstehende Einheiten werden oft mit 0 EUR angesetzt.

#### Block D: Ausgaben (monatlich)

| Position | EUR | Hinweis |
|----------|-----|---------|
| Warmmiete aktuelle Wohnung | [Eingabe] | "Entfaellt kuenftig: ja / nein" (wenn Eigennutzung des Kaufobjekts) |
| Darlehensverpflichtungen (Bestand) | [Eingabe] | Rate + Restschuld pro Darlehen auffuehren |
| Unterhaltsverpflichtungen | [Eingabe] | Kindesunterhalt, Ehegattenunterhalt |
| Private Krankenversicherung | [Eingabe] | Nur wenn nicht im Netto abgezogen |
| Leasingraten | [Eingabe] | Kfz, Ausstattung |
| Sonstige regelmaessige Ausgaben | [Eingabe] | Vereinsbeitraege etc. (nur wesentliche) |
| **Summe Ausgaben** | **[Berechnet]** | |

#### Block E: Vermoegen

| Position | Wert (EUR) | Nachweis |
|----------|-----------|---------|
| Bank- und Sparguthaben | [Eingabe] | Kontoauszuege |
| Wertpapiere / Depot | [Eingabe] | Depotauszug |
| Haus- und Grundvermoegen | [Eingabe] | Verkehrswert-Schaetzung |
| Versicherungsansprueche (Rueckkaufswert) | [Eingabe] | Police / Bestaetigungsschreiben |
| Bausparvertraege | [Eingabe] | Kontoauszug Bausparkasse |
| Sonstige Vermoegen | [Eingabe] | Ggf. Bewertung |
| **Summe Vermoegen** | **[Berechnet]** | |

#### Block F: Verbindlichkeiten

| Position | Restschuld (EUR) | Monatsrate (EUR) | Sicherheit |
|----------|-----------------|-------------------|------------|
| Grundschulden (Bestand) Valuta | [Eingabe] | [Eingabe] | Objekt-Adresse |
| Ratenkredite | [Eingabe] | [Eingabe] | Ohne Sicherheit |
| Dispositionskredite | [Eingabe] | -- | -- |
| Buergschaften | [Eingabe] | -- | Fuer wen |
| Sonstige Verbindlichkeiten | [Eingabe] | [Eingabe] | -- |
| **Summe Verbindlichkeiten** | **[Berechnet]** | **[Berechnet]** | |

### Schritt 3: Dokumenten-Checkliste mit Status erstellen

Erstelle pro Dokument eine Status-Zeile:

| Status | Bedeutung | Symbol |
|--------|-----------|--------|
| **vorhanden** | Dokument liegt vollstaendig vor | OK |
| **fehlt** | Dokument muss noch beschafft werden | FEHLT |
| **angefordert** | Dokument ist bestellt / beantragt | ANGEFORDERT |
| **nicht zutreffend** | Dokument ist fuer diesen Erwerbsstatus nicht relevant | N/A |

### Schritt 4: Bankvorlage-Optimierung

Pruefe das Paket auf Vollstaendigkeit und gib Optimierungshinweise:

| Optimierung | Details |
|-------------|---------|
| **Eigenkapital-Nachweis staerken** | Alle Vermoegensquellen dokumentieren, inkl. Schenkungen (Schenkungsvertrag), Bauspar-Zuteilungen |
| **Haushaltsrechnung positiv** | Einnahmen - Ausgaben - neue Rate = positiv? Bank rechnet mit Pauschalen (ca. 750-900 EUR Lebenshaltung pro Person) |
| **Bestandsimmobilien aufbereiten** | Pro Objekt: Mietvertrag, Darlehensvertrag, Restschuld-Bestaetigung, Kontoauszuege Mietkonto |
| **Luecken in Kontoauszuegen** | 3 Monate lueckenlos, keine uebermalten/geschwaerzten Stellen. IBAN sichtbar |
| **Probezeit-Problematik** | Bei Probezeit: Bank finanziert ggf. nicht oder nur mit Aufschlag. Arbeitgeberbestaetigung anfordern |
| **Selbstaendige: Einkommensermittlung** | Bank nimmt Durchschnitt der letzten 2-3 Jahre (nicht das beste Jahr). Negativer Trend = Ablehnung |
| **EK-Herkunft lueckenlos belegen** | Jede EK-Quelle mit Nachweis (Kontoauszuege, Depotverkauf, Schenkungsvertrag). Unklare Herkunft loest Geldwaesche-Rueckfragen aus und killt Finanzierungen spaet im Prozess |
| **Konsumkredite vor Antrag abloesen** | Konsumschulden sind fuer die Bank ein Stoersignal -- sie belasten Haushaltsrechnung UND Vertrauen. Kleine Ratenkredite (Auto, Moebel, 0%-Finanzierungen) nach Moeglichkeit vor Antragstellung tilgen |
| **Komplett statt troepfchenweise** | Alles in einem Rutsch als ZIP per E-Mail liefern. Jede Nachlieferung = neue Wartezeit + Vertrauensverlust |
| **Ab mehreren Objekten: Investorenbroschuere** | Wiederverwendbares Dokument mit Person, Track Record, Portfolio, Strategie und Ankaufsprofil beilegen -- positioniert dich als systematischen Investor statt Einzelkaeufer (siehe Skill bankenpitch, Sektion Unternehmensprofil) |

### Schritt 5: Schufa und Kontenfuehrung optimieren

Die Selbstauskunft ist nur so stark wie das Scoring dahinter. Vor der Bankanfrage:

| Massnahme | Details |
|-----------|---------|
| **Eigenauskunft ziehen** | Kostenlose Datenkopie (Art. 15 DSGVO) bei der SCHUFA anfordern. Fehler, veraltete Adressen und laengst erledigte Eintraege korrigieren/loeschen lassen |
| **Zielscore kennen** | Basisscore 98+ ist das Ziel fuer Investoren. Werte unter ca. 90-92 sind bei vielen Banken faktisch eine Ablehnungsgrenze (institutsabhaengig -- Pruefbedarf) |
| **Ungenutzte Kreditrahmen schliessen** | Nicht genutzte Kreditkarten, Rahmenkredite und alte Dispolinien kuendigen -- eingeraeumte Linien zaehlen als potenzielle Verschuldung |
| **Kreditanfragen steuern** | Immer "Konditionsanfrage" (schufa-neutral) statt "Kreditanfrage" stellen lassen. Mehrere Kreditanfragen in kurzer Zeit druecken den Score |
| **Konten 3 Monate sauber fuehren** | Keine ungenehmigten Ueberziehungen, keine Ruecklastschriften, kein Dauerdispo -- die Kontoauszuege im Paket sind fuer die Bank ein direktes Kreditwuerdigkeitssignal |
| **Timing** | Schufa-Bereinigung braucht Wochen -- fruehzeitig starten, nicht erst beim konkreten Deal |

### Schritt 6: Qualitaetssicherung und Vollstaendigkeit

Pruefe vor Abgabe:
- Alle Felder der Selbstauskunft befuellt (keine leeren Felder ohne "entfaellt"-Vermerk)
- Summen korrekt berechnet
- Einnahmen/Ausgaben plausibel (keine offensichtlichen Fehler)
- Dokumentenstatus aktuell
- Alle "FEHLT"-Dokumente mit Beschaffungshinweis versehen

---

## Ausgabeformat

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext.

Liefere die Ergebnisse in folgendem Format:

### Zusammenfassung (Freitext)

Kurze Zusammenfassung in 3-5 Saetzen: Erwerbsstatus, Vollstaendigkeit des Pakets, fehlende Dokumente, Handlungsempfehlung.

### Bank-Paket (Bericht)

Das Deliverable ist ein Bank-Paket: die ausgefuellte Selbstauskunft in Tabellenform plus Dokumenten-Checkliste mit Status-Emojis.

```markdown
# Selbstauskunft-Paket: ETW Dortmund, Beispielstr. 42

**Erwerbsstatus: Angestellt** (mit Partner) | Dokumente: 9 von 12 vorhanden | Haushaltsrechnung: ✅ positiv

## Kaufvorhaben

| | |
|---|---|
| Objekt | ETW Dortmund, Beispielstr. 42 |
| Kaufpreis | 250.000 EUR |
| Nebenkosten | 30.000 EUR |
| Finanzierungsbedarf | 245.000 EUR |

## Ausgefuellte Selbstauskunft

(Hier folgen alle sechs Bloecke A-F aus Schritt 2 als vollstaendig befuellte Tabellen
im Zwei-Spalten-Format: Persoenliche Daten, Familienstand/Gueterstand, Einnahmen,
Ausgaben, Vermoegen, Verbindlichkeiten -- mit allen erfassten Werten und Summen.)

## Haushaltsrechnung

| Position | Wert (monatlich) |
|----------|------------------|
| Einnahmen gesamt | 4.800 EUR |
| Ausgaben gesamt | -1.250 EUR |
| Neue Darlehensrate | -1.072 EUR |
| **Frei verfuegbar nach Rate** | **2.478 EUR** |

**Ergebnis: ✅ Haushaltsrechnung positiv** -- die Bank wird die Kapitaldienstfaehigkeit
voraussichtlich anerkennen.

| Vermoegensuebersicht | Wert |
|----------------------|------|
| Vermoegen gesamt | 85.000 EUR |
| Verbindlichkeiten gesamt | 12.000 EUR |

## Dokumenten-Checkliste (9 von 12 vorhanden, 2 fehlen, 1 angefordert)

| Nr. | Dokument | Status | Hinweis |
|-----|----------|--------|---------|
| 1 | Personalausweis | ✅ vorhanden | |
| 2 | Meldebescheinigung | ✅ vorhanden | |
| 3 | Gehaltsabrechnungen 3 Monate | ✅ vorhanden | |
| 4 | Arbeitsvertrag | ✅ vorhanden | Unbefristet |
| 5 | Selbstauskunft | ✅ vorhanden | Durch diesen Skill generiert |
| 6 | Kontoauszuege privat 3 Monate | ✅ vorhanden | |
| 7 | Kontoauszuege Geschaeft | ➖ nicht zutreffend | |
| 8 | Steuerbescheide 2 Jahre | ❌ fehlt | Beim Finanzamt anfordern oder Steuerberater kontaktieren |
| 9 | Vermoegensnachweise | ✅ vorhanden | Depot-Auszug + Bausparer |
| 10 | Schuldenueberblick | ✅ vorhanden | Autokredit Restschuld 12.000 EUR |
| 11 | Rentenversicherungsverlauf | ⏳ angefordert | Online bei DRV beantragt |
| 12 | Bestandsimmobilien-Aufstellung | ✅ vorhanden | 1 ETW Bestand, Mieteinnahmen 380 EUR netto |

## Optimierungshinweise

1. Steuerbescheide 2023 + 2024 nachreichen -- ohne Steuerbescheide wird die Bank das Einkommen nicht final bestaetigen.
2. Schenkung der Eltern (10.000 EUR EK-Anteil) per Schenkungsvertrag oder Kontoauszug dokumentieren.
3. Autokredit (12.000 EUR Restschuld, 280 EUR Rate) reduziert Kapitaldienstfaehigkeit -- ggf. vor Bankgespraech abloesen.
```

---

## Qualitaetspruefung

Vor Abgabe der Bewertung pruefe:

1. **Erwerbsstatus-Dokumentenliste**: Wurde die korrekte Dokumentenliste (12 vs. 20+) angewendet?
2. **Formular-Vollstaendigkeit**: Sind alle 6 Bloecke (A-F) befuellt? Keine leeren Felder ohne "entfaellt"?
3. **Summen-Konsistenz**: Stimmen Einnahmen-, Ausgaben-, Vermoegen- und Verbindlichkeiten-Summen rechnerisch?
4. **Haushaltsrechnung**: Ist Einnahmen - Ausgaben - neue Rate > 0? Wenn negativ: WARNUNG ausgeben.
5. **Bank-Pauschalen**: Hat die Bank typische Pauschalen fuer Lebenshaltung (750-900 EUR pro Erwachsener, 250-350 EUR pro Kind)? Eigene Ausgaben muessen darueber liegen.
6. **Lueckenlosigkeit**: Sind Kontoauszuege lueckenlos fuer 3 Monate? Gehaltsabrechnungen lueckenlos?
7. **Aktualitaet**: Sind BWA/SuSa nicht aelter als 2 Monate (bei Selbstaendigen)?
8. **Partner-Einbindung**: Wenn Partner Mitdarlehensnehmer: Wurden Partner-Daten vollstaendig erfasst?
9. **Schufa & Konten**: Wurde Schritt 5 durchlaufen (Eigenauskunft, ungenutzte Kreditrahmen, saubere Kontenfuehrung, nur Konditionsanfragen)?
10. **Objektpaket**: Ist das Objektpaket (O1-O8) parallel vorbereitet und die Lieferung als EIN ZIP geplant?

---

## Warnsignale & Dealbreaker

### Sofortige Probleme (Bank wird wahrscheinlich ablehnen)

| Signal | Warum Problem | Handlung |
|--------|---------------|----------|
| **Negative Haushaltsrechnung** | Bank finanziert nicht bei negativem frei verfuegbaren Einkommen | Ausgaben reduzieren, hoeheres EK, guenstigeres Objekt |
| **SCHUFA-Negativmerkmale** | Kreditunwuerdigkeit | SCHUFA bereinigen (Datenkorrekturen, Erledigung-Vermerke) |
| **Probezeit ohne Arbeitgeberbestaetigung** | Bank sieht Einkommensrisiko | Arbeitgeber-Bestaetigung oder Buergschaft |
| **Selbstaendigkeit < 2 Jahre** | Zu kurze Track-Record | Spezialbanken oder Buergschaftsbank anfragen |
| **EK-Quote < 5%** | 110%-Finanzierung bei den meisten Banken nicht moeglich | Mehr EK beschaffen (Schenkung, Bauspar-Zuteilung) |
| **SCHUFA-Score unter ca. 90-92** | Bei vielen Banken faktische Ablehnungsgrenze (institutsabhaengig) | Eigenauskunft bereinigen, Kreditrahmen schliessen, Timing verschieben (siehe Schritt 5) |
| **Ungenehmigte Ueberziehungen / Ruecklastschriften in den Kontoauszuegen** | Direktes Kreditwuerdigkeitssignal -- die Bank liest die 3 Monate Auszuege genau | Konten bereinigen, 3 saubere Monate abwarten |

### Warnsignale (Bank wird genauer pruefen)

| Signal | Risiko | Handlung |
|--------|--------|----------|
| **Befristeter Arbeitsvertrag** | Einkommensrisiko | Restlaufzeit > 12 Monate empfohlen, Branche bewerten |
| **Hohe bestehende Verbindlichkeiten** | Kapitaldienstfaehigkeit reduziert | Ggf. Umschuldung oder Abloesung vor Antragstellung |
| **Leerstand in Bestandsobjekten** | Reduziert anrechenbare Mieteinnahmen | Nachvermietung vor Bankantrag |
| **Grosse Schwankungen beim Einkommen (Selbst.)** | Einkommensrisiko | Durchschnitt der 3 Jahre stabil? Trend positiv? |
| **Schenkung als EK ohne Nachweis** | Bank akzeptiert Schenkung nur mit Vertrag/Kontoauszug | Schenkungsvertrag + Kontobeleg |
| **Viele kleine Konsumkredite / 0%-Finanzierungen** | Stoersignal: belastet Haushaltsrechnung und Scoring | Vor Antrag abloesen oder buendeln |
| **Mehrere Kreditanfragen in kurzer Zeit** | Score-Verschlechterung durch Anfrage-Merkmale | Nur Konditionsanfragen stellen lassen, SCHUFA-Abfrage erst bei Commitment |

---

## Bei fehlenden Daten

| Fehlende Information | Auswirkung auf Konfidenz | Annahme / Vorgehen |
|---------------------|--------------------------|---------------------|
| **Steuerbescheide** | -15% Konfidenz | Bank kann Einkommen nicht final bestaetigen |
| **Kontoauszuege** | -15% Konfidenz | Ausgabenseite nicht verifizierbar |
| **Arbeitsvertrag** | -10% Konfidenz | Beschaeftigungsstatus unklar |
| **Vermoegensnachweise** | -10% Konfidenz | EK-Herkunft nicht belegbar |
| **BWA/SuSa (Selbstaendige)** | -20% Konfidenz | Aktuelle Ertragslage nicht pruefbar |
| **Bilanzen (Selbstaendige)** | -15% Konfidenz | Keine belastbare Einkommensgrundlage |
| **Bestandsimmobilien-Daten** | -10% Konfidenz | Gesamtportfolio nicht bewertbar |

**Basis-Konfidenz bei Kerndokumenten (Ausweis, Gehalt, Selbstauskunft):** 70%  
**Maximale Konfidenz bei allen Dokumenten:** 95%  
**Unter 55% Konfidenz:** Warnung ausgeben, dass die Bankvorlage nicht vollstaendig ist und mit Ablehnung gerechnet werden muss.

> **Pruefbedarf:** Lebenshaltungspauschalen, Mieteinnahmen-Anrechnungssaetze, Schufa-Grenzwerte und Dokumentenanforderungen sind institutsspezifisch und aendern sich -- vor Einreichung mit der konkreten Bank abgleichen. Steuerliche Fragen (EK-Herkunft, Schenkung, Rechtsform) mit dem Steuerberater klaeren.

---

## Konfidenz-Bewertung

| Konfidenz | Bedeutung | Typische Datenlage |
|-----------|-----------|-------------------|
| **85-95%** | Hohe Zuverlaessigkeit, Bank-ready | Alle Dokumente vorhanden, Formular komplett, Haushaltsrechnung positiv |
| **70-84%** | Gute Basis, einzelne Nachlieferungen noetig | Kerndokumente vorhanden, 1-2 Unterlagen fehlen |
| **55-69%** | Eingeschraenkt, wesentliche Unterlagen fehlen | Selbstauskunft teilweise, Belegnachweise fehlen |
| **< 55%** | Nicht Bank-ready, weitere Vorbereitung noetig | Grundlegende Dokumente fehlen |

---

## Verwandte Wissensdatenbanken

- `knowledge/kalkulationsformeln.md` -- Cashflow-Berechnung, Kapitaldienstfaehigkeit
- `knowledge/checklisten.md` -- Finanzierungs-Checkliste

### Verwandte Skills

- `skills/bankenpitch/SKILL.md` -- Finanzierungskonzept & Bankenpraesentation (das Objektpaket zur Selbstauskunft)
- `skills/bankgespraech-coach/SKILL.md` -- Gespraechsvorbereitung, Bankentypen-Auswahl und Bankerfragen fuer den Termin
- `skills/cashflow-modell/SKILL.md` -- Detailliertes Cashflow-Modell fuer das Objekt
- `skills/kaufvertrag-pruefung/SKILL.md` -- Kaufvertragspruefung nach Finanzierungszusage
- `skills/bierdeckel-kalkulation/SKILL.md` -- Schnelle Rendite-Kalkulation fuer die Erstbewertung
