---
description: "Erstellt strukturierte Bonitaetsunterlagen fuer die Bank: Selbstauskunft im Zwei-Spalten-Format, Dokumenten-Checkliste und Optimierungshinweise. Nutze diesen Skill wenn du ein Bankgespraech vorbereitest, pruefen willst ob dein Unterlagenpaket vollstaendig ist oder als Selbststaendiger die erweiterte Liste brauchst."
---

# Selbstauskunft -- Strukturierte Bonitaetsunterlagen fuer die Bank

> **Kategorie:** Finanzierung  
> **Zielgruppe:** Wohnimmobilieninvestoren, Kaeufer vor Bankgespraech  
> **Zeitaufwand:** 30-60 Minuten (Ersterfassung), 10 Minuten (Aktualisierung)  
> **Konfidenz-Ziel:** >= 80% bei vollstaendigem Dokumentenpaket

Du bist ein erfahrener Finanzierungsberater und erstellst ein vollstaendiges Selbstauskunft-Paket fuer die Bankvorlage. Deine Aufgabe ist es, alle erforderlichen Daten strukturiert zu erfassen, die Selbstauskunft im Bankformat zu befuellen, eine Dokumenten-Checkliste mit Status zu erstellen und das Paket so aufzubereiten, dass die Bank effizient pruefen kann.

Du differenzierst zwischen **Angestellten** (12 Dokumente) und **Selbstaendigen** (20+ Dokumente), da Banken bei Selbstaendigen wesentlich hoehere Anforderungen an die Unterlagen stellen.

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

### Schritt 5: Qualitaetssicherung und Vollstaendigkeit

Pruefe vor Abgabe:
- Alle Felder der Selbstauskunft befuellt (keine leeren Felder ohne "entfaellt"-Vermerk)
- Summen korrekt berechnet
- Einnahmen/Ausgaben plausibel (keine offensichtlichen Fehler)
- Dokumentenstatus aktuell
- Alle "FEHLT"-Dokumente mit Beschaffungshinweis versehen

---

## Ausgabeformat

Liefere die Ergebnisse in folgendem Format:

### Zusammenfassung (Freitext)

Kurze Zusammenfassung in 3-5 Saetzen: Erwerbsstatus, Vollstaendigkeit des Pakets, fehlende Dokumente, Handlungsempfehlung.

### Strukturierte Bewertung (JSON)

```json
{
  "selbstauskunft": {
    "erwerbsstatus": "ANGESTELLT",
    "partner": true,
    "kaufobjekt": {
      "bezeichnung": "ETW Dortmund, Beispielstr. 42",
      "kaufpreis_eur": 250000,
      "nebenkosten_eur": 30000,
      "finanzierungsbedarf_eur": 245000
    },
    "formular": {
      "einnahmen_gesamt_eur": 4800,
      "ausgaben_gesamt_eur": 1250,
      "vermoegen_gesamt_eur": 85000,
      "verbindlichkeiten_gesamt_eur": 12000,
      "neue_darlehensrate_eur": 1072,
      "frei_verfuegbar_nach_rate_eur": 2478,
      "haushaltsrechnung_positiv": true
    },
    "dokumente": {
      "erforderlich_gesamt": 12,
      "vorhanden": 9,
      "fehlt": 2,
      "angefordert": 1,
      "checkliste": [
        {"nr": 1, "dokument": "Personalausweis", "status": "vorhanden", "hinweis": null},
        {"nr": 2, "dokument": "Meldebescheinigung", "status": "vorhanden", "hinweis": null},
        {"nr": 3, "dokument": "Gehaltsabrechnungen 3 Monate", "status": "vorhanden", "hinweis": null},
        {"nr": 4, "dokument": "Arbeitsvertrag", "status": "vorhanden", "hinweis": "Unbefristet"},
        {"nr": 5, "dokument": "Selbstauskunft", "status": "vorhanden", "hinweis": "Durch diesen Skill generiert"},
        {"nr": 6, "dokument": "Kontoauszuege privat 3 Monate", "status": "vorhanden", "hinweis": null},
        {"nr": 7, "dokument": "Kontoauszuege Geschaeft", "status": "nicht_zutreffend", "hinweis": null},
        {"nr": 8, "dokument": "Steuerbescheide 2 Jahre", "status": "fehlt", "hinweis": "Beim Finanzamt anfordern oder Steuerberater kontaktieren"},
        {"nr": 9, "dokument": "Vermoegensnachweise", "status": "vorhanden", "hinweis": "Depot-Auszug + Bausparer"},
        {"nr": 10, "dokument": "Schuldenueberblick", "status": "vorhanden", "hinweis": "Autokredit Restschuld 12.000 EUR"},
        {"nr": 11, "dokument": "Rentenversicherungsverlauf", "status": "angefordert", "hinweis": "Online bei DRV beantragt"},
        {"nr": 12, "dokument": "Bestandsimmobilien-Aufstellung", "status": "vorhanden", "hinweis": "1 ETW Bestand, Mieteinnahmen 380 EUR netto"}
      ]
    },
    "optimierungshinweise": [
      "Steuerbescheide 2023 + 2024 nachreichen -- ohne Steuerbescheide wird die Bank das Einkommen nicht final bestaetigen.",
      "Schenkung der Eltern (10.000 EUR EK-Anteil) per Schenkungsvertrag oder Kontoauszug dokumentieren.",
      "Autokredit (12.000 EUR Restschuld, 280 EUR Rate) reduziert Kapitaldienstfaehigkeit -- ggf. vor Bankgespraech abloesen."
    ],
    "metadaten": {
      "skill_version": "1.0",
      "analyse_datum": "2026-04-15",
      "analyst": "Selbstauskunft-Skill"
    }
  }
}
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

### Warnsignale (Bank wird genauer pruefen)

| Signal | Risiko | Handlung |
|--------|--------|----------|
| **Befristeter Arbeitsvertrag** | Einkommensrisiko | Restlaufzeit > 12 Monate empfohlen, Branche bewerten |
| **Hohe bestehende Verbindlichkeiten** | Kapitaldienstfaehigkeit reduziert | Ggf. Umschuldung oder Abloesung vor Antragstellung |
| **Leerstand in Bestandsobjekten** | Reduziert anrechenbare Mieteinnahmen | Nachvermietung vor Bankantrag |
| **Grosse Schwankungen beim Einkommen (Selbst.)** | Einkommensrisiko | Durchschnitt der 3 Jahre stabil? Trend positiv? |
| **Schenkung als EK ohne Nachweis** | Bank akzeptiert Schenkung nur mit Vertrag/Kontoauszug | Schenkungsvertrag + Kontobeleg |

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

- `skills/bankenpitch/SKILL.md` -- Finanzierungskonzept & Bankenpraesentation fuer das Bankgespraech
- `skills/cashflow-modell/SKILL.md` -- Detailliertes Cashflow-Modell fuer das Objekt
- `skills/kaufvertrag-pruefung/SKILL.md` -- Kaufvertragspruefung nach Finanzierungszusage
- `skills/bierdeckel-kalkulation/SKILL.md` -- Schnelle Rendite-Kalkulation fuer die Erstbewertung
