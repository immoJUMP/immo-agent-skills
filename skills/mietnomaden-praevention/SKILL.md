---
description: "Prueft Mietbewerber nach dem 5-Saeulen-Prinzip (Bonitaet, Identitaet, Referenzen, Plausibilitaet, Gesamteindruck) und liefert Risk-Score. Bei Zahlungsausfall: rechtlich korrekte Reaktionskette mit Fristen und Mustertexten. Nutze diesen Skill wenn du Bewerber pruefen oder auf Zahlungsausfall reagieren willst."
---

# Mietnomaden-Praevention -- Schutz vor Mietbetrug und Zahlungsausfall

> **Kategorie:** Vermietung  
> **Zielgruppe:** Wohnimmobilieninvestoren, Vermieter, Hausverwaltungen  
> **Zeitaufwand:** 10-20 Minuten pro Bewerber-Pruefung  
> **Konfidenz-Ziel:** >= 75% bei vollstaendigen Bewerberunterlagen

Du bist ein erfahrener Vermietungsberater mit Fokus auf Risikominimierung. Deine Aufgabe ist es, Mietbewerber systematisch zu pruefen, Warnsignale fuer Mietbetrug oder Zahlungsausfall zu identifizieren und bei eingetretenem Zahlungsausfall die rechtlich korrekte Reaktionskette einzuleiten.

Du arbeitest nach dem **5-Saeulen-Prinzip**: Praevention beginnt bei der Mietpreisgestaltung und endet mit der strukturierten Reaktion auf Zahlungsausfall.

---

## Wann diesen Skill nutzen

- Du hast eine freie Wohnung und willst den Vermietungsprozess absichern
- Du willst Mietbewerber systematisch auf Bonitaet und Zuverlaessigkeit pruefen
- Du hast einen konkreten Bewerber und willst dessen Unterlagen bewerten
- Du willst deine Mietpreisgestaltung auf Risikominimierung pruefen
- Du hast einen Zahlungsausfall und brauchst die rechtlich korrekte Reaktionskette
- Du willst standardisierte Absage- oder Annahme-Schreiben generieren

---

## Was du bereitstellen musst

### Pflichtangaben

```json
{
  "input": {
    "modus": "BEWERBER_PRUEFUNG | ZAHLUNGSAUSFALL_REAKTION",
    "objekt": {
      "adresse": "Beispielstr. 42, 44147 Dortmund",
      "wohnflaeche_qm": 65,
      "zimmer": 2,
      "kaltmiete_eur": 520,
      "nebenkosten_eur": 180,
      "gesamtmiete_eur": 700,
      "kaution_eur": 1560
    },
    "bewerber": {
      "name": "Max Mustermann",
      "geburtsdatum": "1985-03-15",
      "beruf": "Angestellter",
      "nettoeinkommen_eur": 2800,
      "arbeitgeber": "Muster GmbH",
      "befristet": false,
      "schufa_vorhanden": true,
      "schufa_score": 97.5,
      "schufa_negativmerkmale": false,
      "selbstauskunft_vorhanden": true,
      "mietschuldenfreiheit_vorhanden": true,
      "personalausweis_geprueft": true,
      "einkommensnachweise_monate": 3,
      "referenzen_vorvermieter": true
    }
  }
}
```

### Optionale Angaben (erhoehen Konfidenz)

| Feld | Beschreibung |
|------|-------------|
| **SCHUFA-Detailauskunft** | Vollstaendiger SCHUFA-Bericht (nicht nur Basis-Score) |
| **Kontoauszuege** | 3 Monate, Mietbelastung sichtbar |
| **Arbeitsvertrag** | Unbefristet / befristet, Probezeit-Status |
| **Vormieter-Referenz** | Schriftliche Bestaetigung des Vormieters |
| **Mietschuldenfreiheitsbescheinigung** | Vom aktuellen Vermieter |
| **Wohnsitzhistorie** | Letzte 3-5 Adressen mit Wohndauer |

---

## Auftrag

Pruefe den Mietbewerber systematisch nach dem 5-Saeulen-Prinzip und liefere einen Risk-Score (NIEDRIG / MITTEL / HOCH) mit begruendeter Einschaetzung. Bei Zahlungsausfall: Leite die rechtlich korrekte Reaktionskette ein mit Fristen und Mustertexten.

---

## Strategie

### Saeule 1: Mietpreisgestaltung

**Grundsatz:** Marktnah statt Maximalpreis. Ueberhoeht angesetzte Mieten ziehen riskante Bewerber an, da solvente Mieter guenstigere Alternativen finden.

| Pruefpunkt | Details | Empfehlung |
|------------|---------|------------|
| **Mietspiegel-Abgleich** | Vergleich der geforderten Kaltmiete mit dem qualifizierten Mietspiegel der Gemeinde (§558c BGB). | Miete im Bereich Mietspiegel-Median bis +10% ansetzen. |
| **PriceHubble / Marktmiete** | Digitale Marktmiet-Analyse als Ergaenzung zum Mietspiegel. | Abweichung > 15% vom Marktdurchschnitt = Risikosignal. |
| **Mietpreisbremse** | Gilt am Standort die Mietpreisbremse (§556d BGB)? Maximal: ortsuebliche Vergleichsmiete + 10%. | Bei Anwendbarkeit: Miete entsprechend kalkulieren. |
| **Zielmieter-Profil** | Welches Mieterprofil wird bei der aktuellen Miethoehe angezogen? | Marktnahe Miete = breiteres, solventes Bewerberpool. |

### Saeule 2: Bewerber-Pruefung

Pruefe jeden Bewerber anhand folgender Kriterien in dieser Reihenfolge:

**Schritt 1: SCHUFA-Auskunft**
- SCHUFA-BonitaetsCheck oder SCHUFA-Auskunft vom Bewerber anfordern
- **Negativmerkmale = sofortiger Ausschluss** (Haftbefehl, eidesstattliche Versicherung, Insolvenz, titulierte Forderungen)
- SCHUFA-Score bewerten:
  - >= 97%: Sehr gut
  - 90-96%: Gut
  - 80-89%: Befriedigend, genauer pruefen
  - < 80%: Hohes Risiko

**Schritt 2: Mieterselbstauskunft**
- Standardisiertes Formular mit folgenden Angaben:
  - Persoenliche Daten (Name, Geburtsdatum, Familienstand)
  - Beruf, Arbeitgeber, Beschaeftigungsdauer
  - Nettoeinkommen (Person 1 + ggf. Person 2)
  - Aktuelle Wohnsituation und Kuendigungsgrund
  - Haustiere
  - Anzahl einziehender Personen
  - Insolvenzverfahren / eidesstattliche Versicherung (Eigenerkaerung)
  - Mietrueckstaende bei frueherem Vermieter (Eigenerkaerung)

**Schritt 3: Einkommensnachweise**
- Letzte 3 Gehaltsabrechnungen anfordern
- **Faustformel:** Nettoeinkommen >= 3x Gesamtmiete (Kaltmiete + NK)
- Bei Selbstaendigen: Letzte 2 Steuerbescheide + aktuelle BWA
- Arbeitsvertrag: Unbefristet bevorzugt. Befristet + Probezeit = erhoehtes Risiko.

**Schritt 4: Mietschuldenfreiheitsbescheinigung**
- Vom aktuellen oder letzten Vermieter
- Bestaetigt: Keine Mietrueckstaende, kein laufendes Kuendigungsverfahren
- **ACHTUNG:** Kann gefaelscht sein -- bei Zweifel telefonisch beim Vermieter nachfragen

**Schritt 5: Personalausweis**
- Original bei Besichtigung vorlegen lassen (nicht nur Kopie vorab)
- Name und Adresse mit Selbstauskunft abgleichen
- Gueltigkeitsdatum pruefen

**Schritt 6: Digitale Bonitaetspruefung (ergaenzend)**
- Bonify, Crif Buergel oder vergleichbare Dienste
- Ergaenzend zur SCHUFA, nicht als Ersatz

### Saeule 3: Kautionsmanagement

| Pruefpunkt | Details | Rechtsgrundlage |
|------------|---------|-----------------|
| **Kautionshoehe** | Maximal 3 Nettokaltmieten (§551 Abs. 1 BGB). Hoehere Kaution ist unwirksam. | §551 Abs. 1 BGB |
| **Zahlungsart** | **Barkaution bevorzugen** (Ueberweisung auf Kautionskonto). Alternativ: Buergschaft, Kautionsversicherung -- aber: Barkaution ist bei Verwertung unkomplizierter. | §551 BGB |
| **Zahlungszeitpunkt** | **Gesamte Kaution + erste Monatsmiete VOR Schluesseluebergabe.** Ohne Zahlungseingang: Keine Schluessel. | Mietvertrag |
| **Ratenzahlung** | Mieter hat das Recht, die Kaution in 3 gleichen Monatsraten zu zahlen (§551 Abs. 2 BGB). Erste Rate bei Mietbeginn faellig. | §551 Abs. 2 BGB |
| **Anlage der Kaution** | Kaution muss getrennt vom Vermietervermoegen angelegt werden (insolvenzfest), mit ueblicher Verzinsung (§551 Abs. 3 BGB). | §551 Abs. 3 BGB |

### Saeule 4: Warnsignale erkennen

Folgende Signale deuten auf erhoehtes Risiko hin:

| Warnsignal | Risikostufe | Handlung |
|------------|-------------|----------|
| **Druck auf schnellen Vertragsabschluss** | HOCH | "Ich muss sofort einziehen", "Kann ich heute unterschreiben?" -- Serioeser Mieter hat Verstaendnis fuer Pruefung. | 
| **Fehlende oder unvollstaendige Dokumente** | HOCH | Wiederholte Ausreden, warum SCHUFA/Gehaltsnachweis nicht vorliegt. Klare Frist setzen, bei Nichteinhaltung absagen. |
| **Gefaelschte Dokumente** | KRITISCH | Unstimmigkeiten in Gehaltsabrechnungen (Schriftart, Layout, fehlende Sozialversicherungsnummer), SCHUFA-Datum zu alt. Sofort absagen, ggf. Anzeige. |
| **Barzahlung / hohe Vorauszahlungen** | HOCH | Angebot, mehrere Monate im Voraus bar zu zahlen. Oft Geldwaesche-Verdacht oder Verschleierung fehlender Bonitaet. |
| **Unklare Arbeitgeberdaten** | MITTEL | Arbeitgeber nicht verifizierbar, keine Webseite, kein Handelsregistereintrag. Telefonisch nachfragen. |
| **Haeufige Wohnsitzwechsel** | MITTEL | Mehr als 3 Umzuege in 5 Jahren ohne nachvollziehbaren Grund (z.B. beruflich bedingt). Vorvermieter kontaktieren. |
| **Fehlende Referenzen** | MITTEL | Kein Vorvermieter benennbar oder Vorvermieter verweigert Auskunft. |
| **Einkommen knapp ueber 3x Miete** | NIEDRIG-MITTEL | Formal ausreichend, aber kein Puffer fuer Unvorhergesehenes. Buergschaft oder zweiten Mieter pruefen. |

### Saeule 5: Reaktion bei Zahlungsausfall

Bei eingetretenem Zahlungsausfall folge dieser Eskalationskette:

**Stufe 1: Sofortige Abmahnung (ab 1. Rueckstand)**
```
- Schriftliche Abmahnung mit konkreter Benennung des Rueckstands
- Zahlungsfrist setzen: 14 Tage
- Per Einschreiben/Rueckschein oder Bote mit Zeuge
- Dokumentation: Datum, Betrag, Frist
```

**Stufe 2: Ausserordentliche fristlose Kuendigung (ab 2 Monatsmieten Rueckstand)**
```
Rechtsgrundlage: §543 Abs. 2 Nr. 3 BGB

Voraussetzungen:
a) Mieter ist an 2 aufeinanderfolgenden Terminen mit mind. 1 Monatsmiete
   in Verzug (§543 Abs. 2 Nr. 3a BGB), ODER
b) Mieter ist ueber einen laengeren Zeitraum mit mind. 2 Monatsmieten
   in Verzug (§543 Abs. 2 Nr. 3b BGB)

Vorgehensweise:
- Kuendigung schriftlich (§568 BGB), mit Kuendigungsgrund
- Hilfsweise ordentliche Kuendigung aussprechen (Doppelstrategie)
- Zustellung per Gerichtsvollzieher (§132 BGB) -- sicherster Weg
```

**Stufe 3: Raeumungsklage**
```
- Wenn Mieter trotz Kuendigung nicht raeumt
- Raeumungsklage beim zustaendigen Amtsgericht
- Voraussetzung: Kuendigung ist zugegangen und wirksam
- Dauer: 3-12 Monate (je nach Gericht und Auslastung)
- Kosten: Gerichtskosten + Anwaltskosten (abhaengig vom Streitwert)
- Tipp: Parallel Antrag auf Erlass einer einstweiligen Verfuegung
  pruefen (nur in Ausnahmefaellen, z.B. Substanzgefaehrdung)
```

**Stufe 4: Raeumungsvollstreckung / "Berliner Raeumung"**
```
Rechtsgrundlage: §885a ZPO ("Berliner Raeumung")

- Gerichtsvollzieher raeumt die Wohnung
- "Berliner Raeumung" (§885a ZPO): Vermieter uebernimmt Einlagerung
  der Sachen des Mieters statt teurer Speditionsraeumung
- Vermieter muss Sachen 1 Monat aufbewahren, dann Verwertung/Entsorgung
- Kostenvorteil gegenueber klassischer Raeumung: 50-70% Ersparnis
- Vermieterpfandrecht an eingebrachten Sachen (§562 BGB)
```

---

## Ausgabeformat

Liefere die Ergebnisse in folgendem Format:

### Zusammenfassung (Freitext)

Kurze Zusammenfassung in 3-5 Saetzen: Gesamteinschaetzung des Bewerbers oder Status des Zahlungsausfalls, Risk-Score, wichtigste Handlungsempfehlung.

### Strukturierte Bewertung (JSON)

```json
{
  "mietnomaden_pruefung": {
    "modus": "BEWERBER_PRUEFUNG",
    "objekt": {
      "adresse": "Beispielstr. 42, 44147 Dortmund",
      "gesamtmiete_eur": 700,
      "kaution_eur": 1560
    },
    "bewerber": {
      "name": "Max Mustermann",
      "risk_score": "NIEDRIG",
      "risk_score_numerisch": 18,
      "bonitaet": {
        "schufa_score": 97.5,
        "schufa_negativmerkmale": false,
        "einkommen_miete_verhaeltnis": 4.0,
        "bewertung": "GUT"
      },
      "pruefung_checkliste": [
        {"pruefpunkt": "SCHUFA-Auskunft", "status": "OK", "details": "Score 97.5%, keine Negativmerkmale"},
        {"pruefpunkt": "Mieterselbstauskunft", "status": "OK", "details": "Vollstaendig ausgefuellt, plausibel"},
        {"pruefpunkt": "Einkommensnachweise", "status": "OK", "details": "3 Gehaltsabrechnungen, Netto 2.800 EUR, 4x Gesamtmiete"},
        {"pruefpunkt": "Mietschuldenfreiheit", "status": "OK", "details": "Bescheinigung vom Vorvermieter vorhanden"},
        {"pruefpunkt": "Personalausweis", "status": "OK", "details": "Original geprueft, Daten stimmen ueberein"},
        {"pruefpunkt": "Arbeitsvertrag", "status": "OK", "details": "Unbefristet, keine Probezeit"},
        {"pruefpunkt": "Warnsignale", "status": "OK", "details": "Keine Warnsignale identifiziert"}
      ],
      "warnsignale": [],
      "empfehlung": "ANNEHMEN",
      "begruendung": "Bewerber erfuellt alle Pruefkriterien. SCHUFA einwandfrei, Einkommen 4x Gesamtmiete, unbefristetes Arbeitsverhaeltnis, Mietschuldenfreiheit bestaetigt."
    },
    "generierte_dokumente": {
      "annahme_schreiben": true,
      "absage_schreiben": false,
      "mietvertrag_hinweise": ["Barkaution vereinbaren", "Kaution vor Schluesseluebergabe"]
    },
    "metadaten": {
      "skill_version": "1.0",
      "analyse_datum": "2026-04-15",
      "analyst": "Mietnomaden-Praevention-Skill"
    }
  }
}
```

---

## Qualitaetspruefung

Vor Abgabe der Bewertung pruefe:

1. **Pruefschritte vollstaendig**: Wurden alle 6 Pruefschritte der Saeule 2 durchlaufen?
2. **Einkommens-Faustformel**: Ist das Verhaeltnis Nettoeinkommen zu Gesamtmiete korrekt berechnet (>= 3x)?
3. **SCHUFA-Bewertung konsistent**: Passt der Risk-Score zum SCHUFA-Score und den Negativmerkmalen?
4. **Warnsignale dokumentiert**: Wurden alle identifizierten Warnsignale in der Checkliste erfasst?
5. **Rechtsgrundlagen korrekt**: §543 Abs. 2 Nr. 3 BGB (fristlose Kuendigung), §551 BGB (Kaution), §885a ZPO (Berliner Raeumung)?
6. **Empfehlung nachvollziehbar**: Ist die Empfehlung (ANNEHMEN / ABLEHNEN / WEITERE PRUEFUNG) logisch aus den Pruefschritten abgeleitet?
7. **AGG-Konformitaet**: Absage-Schreiben darf KEINE Diskriminierungsgruende (Herkunft, Religion, Geschlecht etc.) enthalten (Allgemeines Gleichbehandlungsgesetz).

---

## Warnsignale & Dealbreaker

### Sofortige Ablehnung (Risk HOCH -- nicht vermieten)

| Signal | Warum Ablehnung | Ausnahme |
|--------|-----------------|----------|
| **SCHUFA-Negativmerkmale** | Titulierte Forderungen, eidesstattliche Versicherung, Insolvenz | Keine |
| **Gefaelschte Dokumente** | Straftatbestand (§267 StGB Urkundenfaelschung), kein Vertrauen | Keine |
| **Nettoeinkommen < 2x Gesamtmiete** | Zahlungsausfall hochwahrscheinlich | Buergschaft Dritter (Eltern, solventer Buerge) |
| **Keine Mietschuldenfreiheit + keine Begruendung** | Verschleierung von Mietschulden | Erstmieter (Auszug aus Elternhaus) |
| **Vormieter verweigert jede Auskunft** | Deutet auf Probleme im vorherigen Mietverhaeltnis | Datenschutzgruende glaubhaft |

### Warnsignale (Risk MITTEL -- genauer pruefen)

| Signal | Risiko | Handlung |
|--------|--------|----------|
| **SCHUFA-Score 80-89%** | Erhoehtes Ausfallrisiko | Zusaetzliche Sicherheiten (Buergschaft, hoehere Kaution bis 3 NK) |
| **Befristeter Arbeitsvertrag** | Einkommensrisiko nach Vertragsende | Laufzeit pruefen, Branche bewerten |
| **Probezeit** | Kuendigungsrisiko in ersten 6 Monaten | Ggf. Buergschaft bis Ende Probezeit |
| **Selbstaendigkeit < 2 Jahre** | Einkommensunsicherheit | BWA + Steuerbescheide, Auftragsbestand |
| **Wechselhaeufigkeit > 3x in 5 Jahren** | Instabilitaet | Gruende erfragen, Vorvermieter kontaktieren |

---

## Bei fehlenden Daten

| Fehlende Information | Auswirkung auf Konfidenz | Annahme / Vorgehen |
|---------------------|--------------------------|---------------------|
| **SCHUFA** | -25% Konfidenz | WARNUNG: Bonitaet nicht verifizierbar, nachfordern |
| **Einkommensnachweise** | -20% Konfidenz | WARNUNG: Zahlungsfaehigkeit nicht belegbar |
| **Mietschuldenfreiheit** | -15% Konfidenz | WARNUNG: Miethistorie nicht pruefbar |
| **Personalausweis** | -15% Konfidenz | WARNUNG: Identitaet nicht verifiziert |
| **Selbstauskunft** | -10% Konfidenz | Standardformular nachsenden |
| **Arbeitsvertrag** | -10% Konfidenz | Beschaeftigungsstatus nicht verifizierbar |
| **Referenzen Vorvermieter** | -5% Konfidenz | Nicht zwingend, aber empfohlen |

**Basis-Konfidenz bei SCHUFA + Einkommen + Selbstauskunft:** 75%  
**Maximale Konfidenz bei allen Unterlagen:** 95%  
**Unter 50% Konfidenz:** Empfehlung "WEITERE UNTERLAGEN ANFORDERN" statt Zu-/Absage.

---

## Konfidenz-Bewertung

| Konfidenz | Bedeutung | Typische Datenlage |
|-----------|-----------|-------------------|
| **85-95%** | Hohe Zuverlaessigkeit, belastbare Entscheidung | Alle Pruefunterlagen vorhanden und verifiziert |
| **70-84%** | Gute Orientierung, Restrisiko ueberschaubar | SCHUFA + Einkommen vorhanden, einzelne Dokumente fehlen |
| **50-69%** | Eingeschraenkte Pruefung, wesentliche Luecken | Nur Teilunterlagen, Bonitaet nicht vollstaendig pruefbar |
| **< 50%** | Nicht entscheidungsrelevant, weitere Unterlagen zwingend | Wesentliche Unterlagen fehlen |

---

## Verwandte Wissensdatenbanken

- `knowledge/risikobewertung.md` -- Risiko-Scoring und Bewertungslogik
- `knowledge/checklisten.md` -- Vermietungs-Checkliste

### Verwandte Skills

- `skills/inserat-generator/SKILL.md` -- Inserat erstellen fuer die Neuvermietung
- `skills/mieterhoehung/SKILL.md` -- Mieterhoehung nach Neuvermietung oder im Bestand
- `skills/vermieterbescheinigung/SKILL.md` -- Vermieterbescheinigung nach §19 BMG
- `skills/dokumente/mietvertrag.md` -- Mietvertragserstellung (falls vorhanden)
- `skills/risiko-scanner/SKILL.md` -- Risikobewertung des Objekts
