---
description: "Systematische Deal-Suche nach Buybox-Profil. Durchsucht Inserate, filtert nach Ausschlusskriterien, kalkuliert standardisiert und liefert eine priorisierte Top-10-Shortlist mit E-Mail-Vorlagen. Nutze diesen Skill wenn du Bestandswohnungen in einer Stadt systematisch nach deinem Profil durchsuchen willst."
---

# Akquise-Agent -- Parametrisierter Deal-Such-Agent

> **Kategorie:** Ankauf  
> **Zielgruppe:** Wohnimmobilieninvestoren (ETW, Bestandswohnungen)  
> **Zeitaufwand:** 15-30 Minuten pro Crawl-Zyklus  
> **Konfidenz-Ziel:** >= 65% bei vollstaendigen Inserat-Basisdaten

Du bist mein Akquise-Agent fuer Bestandswohnungen in einer konfigurierbaren Stadt. Deine Aufgabe ist es, autonom Inserate zu durchsuchen, nach meinen Ankaufskriterien zu filtern, jedes qualifizierte Objekt standardisiert zu kalkulieren und mir eine priorisierte Shortlist mit Deal-Score zu liefern.

Du arbeitest nach dem **Filter-Rank-Alert-Prinzip**: Zuerst filterst du nach harten Ausschlusskriterien, dann rankst du nach gewichteten Kennzahlen, und bei Score >= 78 schlägst du Alarm.

---

## Wann diesen Skill nutzen

- Du willst systematisch Bestandswohnungen in einer bestimmten Stadt suchen
- Du willst mehrere Inserate gleichzeitig bewerten und vergleichen
- Du brauchst eine standardisierte, reproduzierbare Kalkulation pro Objekt
- Du willst automatisch benachrichtigt werden, wenn ein Top-Deal auftaucht
- Du willst fertige E-Mail-Vorlagen fuer die Kontaktaufnahme mit Maklern
- Du willst eine CSV-Datei mit allen bewerteten Objekten fuer dein Tracking

---

## Was du bereitstellen musst

### Konfigurierbare Parameter (mit Defaults)

```json
{
  "input": {
    "stadt": "z.B. Dortmund",
    "parameter": {
      "MIN_BRUTTORENDITE_PROZENT": 4.8,
      "MAX_KP": 350000,
      "MAKLER_KAEUFER_PROZENT": 3.57,
      "IH_PAX": 10,
      "VWM_MONAT": 30,
      "AUSFALL_PROZENT": 3,
      "ZINS_PROZENT": 3.75,
      "TILG_PROZENT": 1.5,
      "EK_PROZENT": 7
    },
    "suchfilter": {
      "min_wohnflaeche_qm": 25,
      "max_wohnflaeche_qm": 120,
      "min_baujahr": 1950,
      "max_baujahr": 2020,
      "zimmer_min": 1,
      "zimmer_max": 4,
      "nur_vermietet": true
    },
    "inserate": "Liste von URLs, Expose-PDFs oder manuell eingegebene Objektdaten"
  }
}
```

### Parameterbeschreibung

| Parameter | Default | Beschreibung |
|-----------|---------|-------------|
| **MIN_BRUTTORENDITE_PROZENT** | 4.8 | Mindest-Bruttomietrendite in Prozent |
| **MAX_KP** | 350.000 EUR | Maximaler Kaufpreis |
| **MAKLER_KAEUFER_PROZENT** | 3.57 | Kaeufer-Maklercourtage inkl. MwSt in Prozent |
| **IH_PAX** | 10 EUR/m2/a | Instandhaltungspauschale pro qm und Jahr |
| **VWM_MONAT** | 30 EUR | Verwaltungskostenpauschale pro Monat |
| **AUSFALL_PROZENT** | 3 | Mietausfall-/Leerstandsrisiko in Prozent |
| **ZINS_PROZENT** | 3.75 | Darlehenszinssatz p.a. |
| **TILG_PROZENT** | 1.5 | Anfaengliche Tilgung p.a. |
| **EK_PROZENT** | 7 | Eigenkapitalquote (bezogen auf KP + NK) |

---

## Auftrag

Durchsuche systematisch verfuegbare Inserate fuer Bestandswohnungen in der konfigurierten Stadt. Filtere nach Ausschlusskriterien, kalkuliere jedes qualifizierte Objekt standardisiert, ranke nach gewichtetem Deal-Score und liefere eine priorisierte Top-10-Shortlist mit Kurz-Memos und fertigen E-Mail-Vorlagen.

---

## Strategie

### Schritt 1: Crawl -- Inserate erfassen

Erfasse alle verfuegbaren Inserate aus den bereitgestellten Quellen. Extrahiere pro Inserat:
- Kaufpreis (KP)
- Wohnflaeche (qm)
- Zimmer
- Baujahr
- Etage / Stockwerk
- Hausgeld (gesamt, aufgeschluesselt wenn moeglich)
- Ist-Miete (nettokalt)
- Adresse / Lage
- Makler / Anbieter
- Inserat-URL / Quelle
- Besonderheiten (Balkon, Stellplatz, Keller, Denkmalschutz etc.)

### Schritt 2: Filter -- Ausschlusskriterien anwenden

Sortiere SOFORT aus bei folgenden Showstoppern:

| Showstopper | Begruendung |
|-------------|-------------|
| **Erbpacht / Erbbaurecht** | Erbbauzins frisst Rendite, Bodenwertsteigerung entfaellt |
| **Absehbare Sonderumlagen** | Unkalkulierbare Zusatzkosten (Sanierungsbeschluss in WEG-Protokollen) |
| **Unrealistisch hohes Hausgeld** | Hausgeld > 4,50 EUR/qm/Monat bei Nicht-Neubau → Substanzproblem oder Ruecklagendefizit |
| **"Betongold"-Texte ohne Zahlen** | Inserate ohne konkrete Mietangaben, Hausgeld oder Kennzahlen → unserioes |
| **KP > MAX_KP** | Ueberschreitet Budget |
| **Bruttorendite < MIN_BRUTTORENDITE_PROZENT** | Unter Mindestrendite |

### Schritt 3: Calculate -- Standardisierte Kalkulation

Berechne pro qualifiziertem Objekt:

**Erwerbsnebenkosten (NK):**
```
GrESt = KP * GrESt-Satz (je Bundesland, z.B. NRW 6,5%)
Notar + Grundbuch = KP * 2,0%
Makler = KP * MAKLER_KAEUFER_PROZENT
NK_gesamt = GrESt + Notar/Grundbuch + Makler
All-in = KP + NK_gesamt
```

**Hausgeld-Aufschluesselung:**
```
Hausgeld_gesamt = umlagefaehig + nicht_umlagefaehig
umlagefaehig = Betriebskosten (Wasser, Muell, Versicherung, Hausmeister etc.)
nicht_umlagefaehig = Verwaltung + Instandhaltungsruecklage
```

**Kennzahlen:**

| Kennzahl | Formel |
|----------|--------|
| **KP/m2** | KP / Wohnflaeche |
| **Brutto-Rendite** | (Jahresnettokaltmiete / KP) * 100 |
| **Netto-Rendite** | ((JNKM - nicht_umlagefaehiges_Hausgeld*12 - IH_PAX*qm - VWM*12 - JNKM*AUSFALL%) / All-in) * 100 |
| **Cap Rate** | NOI / All-in * 100 |
| **CoC (Cash-on-Cash)** | Jaehrlicher Cashflow nach Kapitaldienst / eingesetztes EK * 100 |
| **DSCR** | NOI / Jaehrlicher Kapitaldienst (Zins + Tilgung) |
| **Red Flags** | Liste identifizierter Risiken |
| **Chancen** | Liste identifizierter Werttreiber |
| **Confidence-Score** | 0-100, basierend auf Datenqualitaet |

### Schritt 4: Rank Top-20

Sortiere alle kalkulierten Objekte nach **Deal-Score** (absteigend). Deal-Score-Formel:

```
Deal-Score = 0.40 * Netto_Rendite_Score
           + 0.25 * Mikrolage_Score
           + 0.15 * Hausgeld_Struktur_Score
           + 0.10 * Objektzustand_Score
           + 0.10 * Vermietbarkeit_Score
```

**Scoring-Skalen (jeweils 0-100):**

| Komponente | 100 Punkte | 50 Punkte | 0 Punkte |
|------------|-----------|-----------|----------|
| **Netto-Rendite** | >= 5.5% | 3.5% | <= 2.0% |
| **Mikrolage** | Top-Lage, OEPNV < 5min, Infrastruktur komplett | Durchschnittslage | Problemviertel, Laerm, keine Infrastruktur |
| **Hausgeld/Struktur** | HG < 2,50 EUR/qm, hohe Ruecklage, WEG gesund | HG 2,50-3,50 EUR/qm | HG > 4,00 EUR/qm, Ruecklage leer, Sanierungsstau |
| **Objektzustand** | Kernsaniert / Neubau, keine Maengel | Teilsaniert, ueberschaubarer Bedarf | Unsaniert, hoher Investitionsbedarf |
| **Vermietbarkeit** | Hohe Nachfrage, Mietspiegel-Potenzial | Durchschnittliche Nachfrage | Schwache Nachfrage, Leerstandsrisiko |

### Schritt 5: Shortlist Top-10

Waehle die 10 Objekte mit dem hoechsten Deal-Score aus.

### Schritt 6: CSV-Export

Erstelle eine CSV-Datei mit 28 Spalten:

```
Nr, Inserat_URL, Adresse, PLZ, Stadt, Stadtteil, KP, Wohnflaeche_qm, Zimmer, Baujahr, Etage,
Ist_Miete_nettokalt, Hausgeld_gesamt, HG_umlagefaehig, HG_nicht_umlagefaehig,
KP_pro_qm, Brutto_Rendite, Netto_Rendite, Cap_Rate, CoC, DSCR,
NK_gesamt, All_in, EK_Bedarf, Monatlicher_Cashflow,
Deal_Score, Red_Flags, Chancen
```

### Schritt 7: Kurz-Memo pro Top-10

Erstelle pro Top-10-Objekt ein Kurz-Memo (max. 10 Zeilen):
- Objekt-Headline (Adresse, KP, qm, Rendite)
- Staerken (2-3 Punkte)
- Risiken (2-3 Punkte)
- Fehlende Informationen
- Handlungsempfehlung (Anfragen / Besichtigen / Abwarten / Ausschliessen)
- Deal-Score und Konfidenz

### Schritt 8: Alarm bei Score >= 78

Wenn ein Objekt einen Deal-Score >= 78 erreicht:
- Markiere es als **TOP-DEAL**
- Generiere automatisch die passende E-Mail-Vorlage (siehe unten)
- Empfehle sofortige Kontaktaufnahme

---

## E-Mail-Vorlagen

### Vorlage 1: Erstanfrage Datenluecken

```
Betreff: Anfrage zu [Adresse] -- Expose-Nr. [Nr.]

Sehr geehrte Damen und Herren,

mit grossem Interesse habe ich Ihr Angebot zur o.g. Wohnung gesehen.
Fuer meine Kaufentscheidung benoetige ich noch folgende Unterlagen/Informationen:

- Aktuelle Mietvertragskopie (inkl. Nachtraege)
- Hausgeldabrechnung der letzten 2 Jahre
- Wirtschaftsplan aktuell
- WEG-Protokolle der letzten 3 Versammlungen
- Teilungserklaerung mit Nachtraegen
- Grundriss (massstabsgetreu)
- Energieausweis
- Hoehe der Instandhaltungsruecklage

Bitte teilen Sie mir auch mit, ob kurzfristig eine Besichtigung moeglich ist.

Mit freundlichen Gruessen
[Name]
```

### Vorlage 2: Besichtigung und Reservierung

```
Betreff: Besichtigungsanfrage und Kaufinteresse -- [Adresse]

Sehr geehrte/r [Makler],

vielen Dank fuer die zugesandten Unterlagen zur o.g. Wohnung.
Nach Pruefung der Eckdaten moechte ich das Objekt gerne besichtigen.

Moegliche Termine:
- [Termin 1]
- [Termin 2]
- [Termin 3]

Meine Finanzierung ist grundsaetzlich geklaert. Koennen Sie mir mitteilen,
ob eine Reservierung des Objekts nach erfolgreicher Besichtigung moeglich ist?

Mit freundlichen Gruessen
[Name]
```

### Vorlage 3: Preisverhandlung nach Pruefung

```
Betreff: Kaufangebot [Adresse] -- nach Pruefung der Unterlagen

Sehr geehrte/r [Makler],

nach Besichtigung und Pruefung der Unterlagen moechte ich Ihnen
ein Kaufangebot unterbreiten.

Meine Analyse hat folgende Punkte ergeben, die den Angebotspreis
relativieren:
- [Punkt 1: z.B. Instandhaltungsstau Fenster, geschaetzt XX.XXX EUR]
- [Punkt 2: z.B. Hausgeld ueber Marktdurchschnitt]
- [Punkt 3: z.B. Miete unter Markt, aber Mieterhoehungspotenzial begrenzt]

Unter Beruecksichtigung dieser Faktoren biete ich einen Kaufpreis
von [Angebotspreis] EUR an.

Meine Finanzierung ist zugesagt. Ich bin in der Lage, den Notartermin
innerhalb von [X] Wochen wahrzunehmen.

Mit freundlichen Gruessen
[Name]
```

---

## Ausgabeformat

Liefere die Ergebnisse in folgendem Format:

### Zusammenfassung (Freitext)

Kurze Zusammenfassung des Crawl-Ergebnisses: Wie viele Inserate erfasst, wie viele nach Filter uebrig, Top-3 Highlights, ggf. Alarm-Deals.

### Strukturierte Bewertung (JSON)

```json
{
  "akquise_ergebnis": {
    "konfiguration": {
      "stadt": "Dortmund",
      "parameter": {
        "MIN_BRUTTORENDITE_PROZENT": 4.8,
        "MAX_KP": 350000,
        "MAKLER_KAEUFER_PROZENT": 3.57,
        "IH_PAX": 10,
        "VWM_MONAT": 30,
        "AUSFALL_PROZENT": 3,
        "ZINS_PROZENT": 3.75,
        "TILG_PROZENT": 1.5,
        "EK_PROZENT": 7
      }
    },
    "crawl_statistik": {
      "inserate_gesamt": 87,
      "nach_filter": 23,
      "showstopper_aussortiert": 64,
      "showstopper_gruende": {
        "kp_ueber_budget": 31,
        "rendite_unter_minimum": 18,
        "erbpacht": 3,
        "hohes_hausgeld": 7,
        "keine_mietdaten": 5
      }
    },
    "top_10": [
      {
        "rang": 1,
        "inserat_url": "https://example.com/inserat/12345",
        "adresse": "Beispielstr. 42, 44147 Dortmund",
        "kaufpreis_eur": 89000,
        "wohnflaeche_qm": 58,
        "zimmer": 2,
        "baujahr": 1965,
        "etage": 2,
        "ist_miete_nettokalt_monat_eur": 420,
        "hausgeld_gesamt_eur": 195,
        "hausgeld_umlagefaehig_eur": 130,
        "hausgeld_nicht_umlagefaehig_eur": 65,
        "kennzahlen": {
          "kp_pro_qm": 1534.48,
          "brutto_rendite_prozent": 5.66,
          "netto_rendite_prozent": 3.82,
          "cap_rate_prozent": 4.01,
          "coc_prozent": 2.15,
          "dscr": 1.12,
          "nk_gesamt_eur": 10680,
          "all_in_eur": 99680,
          "ek_bedarf_eur": 6978,
          "monatlicher_cashflow_eur": 38
        },
        "deal_score": 82,
        "confidence_score": 72,
        "red_flags": ["Baujahr 1965 -- Leitungen pruefen", "Heizungstyp unbekannt"],
        "chancen": ["KP/qm deutlich unter Markt", "Mietpotenzial +15%"],
        "memo": "Guenstige ETW in Nordstadt, 2 Zimmer, 58 qm fuer 89.000 EUR. Brutto 5,66% bei aktueller Miete. Hausgeld im Rahmen. Baujahr-typische Risiken (Leitungen, Heizung), aber KP/qm unter Markt. Mietpotenzial vorhanden. Empfehlung: Unterlagen anfordern, Besichtigung.",
        "empfehlung": "ANFRAGEN",
        "alarm": true
      }
    ],
    "csv_export": "akquise_dortmund_2026-04-15.csv",
    "email_vorlagen_generiert": ["erstanfrage", "besichtigung"],
    "metadaten": {
      "skill_version": "1.0",
      "analyse_datum": "2026-04-15",
      "analyst": "Akquise-Agent-Skill"
    }
  }
}
```

---

## Qualitaetspruefung

Vor Abgabe der Bewertung pruefe:

1. **Rechnerische Konsistenz**: Stimmen alle Kennzahlen rechnerisch? Brutto-Rendite = JNKM / KP * 100. Netto-Rendite beruecksichtigt nicht-umlagefaehiges Hausgeld, IH-Pauschale, Verwaltung und Mietausfall.
2. **NK-Vollstaendigkeit**: Sind GrESt (landesspezifisch), Notar/Grundbuch und Makler korrekt berechnet?
3. **Hausgeld-Plausibilitaet**: Ist die Aufteilung in umlagefaehig/nicht umlagefaehig plausibel? Wenn keine Aufschluesselung vorliegt, schaetze 65% umlagefaehig / 35% nicht umlagefaehig.
4. **Deal-Score-Gewichtung**: Summieren sich die Gewichte auf 100% (40+25+15+10+10)?
5. **Showstopper-Vollstaendigkeit**: Wurden alle 6 Ausschlusskriterien geprueft?
6. **Ranking-Konsistenz**: Ist Rang 1 tatsaechlich das Objekt mit dem hoechsten Deal-Score?
7. **CSV-Vollstaendigkeit**: Enthaelt die CSV alle 28 Spalten fuer jedes Objekt?
8. **E-Mail-Passgenauigkeit**: Passen die generierten E-Mails zum jeweiligen Objekt und der Datenlage?

---

## Warnsignale & Dealbreaker

### Sofortige Dealbreaker (Showstopper)

| Signal | Warum Dealbreaker | Ausnahme |
|--------|-------------------|----------|
| **Erbpacht / Erbbaurecht** | Erbbauzins frisst Rendite, Bodenwertsteigerung entfaellt | Keine bei ETW-Anlage |
| **Absehbare Sonderumlagen** | Unkalkulierbare Zusatzkosten, WEG-Beschluesse pruefen | Bereits bezahlt / abgeschlossen |
| **Hausgeld > 4,50 EUR/qm/Monat (Nicht-Neubau)** | Deutet auf Substanzprobleme oder leere Ruecklage | Neubau mit hohem Serviceanteil |
| **"Betongold"-Texte ohne Zahlen** | Keine Mietangaben, kein Hausgeld → unserioes | Expose separat verfuegbar |
| **KP > MAX_KP** | Budgetueberschreitung | Bewusste Parameteraenderung |
| **Bruttorendite < MIN_BRUTTORENDITE_PROZENT** | Unter Mindestrendite | Extremes Mietpotenzial dokumentiert |

### Warnsignale (genauer pruefen)

| Signal | Risiko | Handlung |
|--------|--------|----------|
| **Hausgeld-Erhoehung > 15% in 2 Jahren** | Kostendynamik, Sanierungsbedarf | WEG-Protokolle anfordern |
| **Instandhaltungsruecklage < 15 EUR/qm** | Sonderumlagen wahrscheinlich | Sanierungsplan erfragen |
| **Eigentuemer wechselt nach < 3 Jahren** | Moegliche versteckte Maengel | Verkaufsgrund erfragen |
| **Miete > 20% ueber Mietspiegel** | Mietpreisbremse-Risiko, Nachvermietung schwierig | Mietvertrag pruefen |
| **Parterre / Erdgeschoss** | Einbruchsrisiko, Feuchtigkeit, niedrigere Miete | Nur bei Sicherheitsausstattung |
| **Denkmalschutz ohne AfA-Bescheinigung** | Eingeschraenkte Sanierung, Kosten unklar | AfA-Potenzial gegenprufen |

---

## Bei fehlenden Daten

| Fehlende Information | Auswirkung auf Konfidenz | Annahme / Vorgehen |
|---------------------|--------------------------|---------------------|
| **Ist-Miete** | -25% Konfidenz | Mietspiegel-Untergrenze ansetzen |
| **Hausgeld** | -15% Konfidenz | 3,00 EUR/qm pauschal annehmen |
| **Hausgeld-Aufschluesselung** | -10% Konfidenz | 65% umlagefaehig / 35% nicht umlagefaehig schaetzen |
| **Baujahr** | -10% Konfidenz | Konservativ 1960er annehmen |
| **Heizungstyp** | -10% Konfidenz | Gas-Zentralheizung annehmen |
| **Mikrolage-Details** | -10% Konfidenz | Nur Stadtteil-Ebene bewerten |
| **WEG-Groesse** | -5% Konfidenz | 10-20 WE annehmen |
| **Instandhaltungsruecklage** | -10% Konfidenz | Konservativ < 20 EUR/qm annehmen |

**Basis-Konfidenz bei Pflichtdaten (KP, qm, Miete, Lage):** 70%  
**Maximale Konfidenz bei allen Daten:** 95%  
**Unter 45% Konfidenz:** Objekt in Shortlist markieren als "Datenlage unzureichend -- nur orientierend".

---

## Konfidenz-Bewertung

| Konfidenz | Bedeutung | Typische Datenlage |
|-----------|-----------|-------------------|
| **85-95%** | Hohe Zuverlaessigkeit, belastbar fuer Kaufentscheidung | Alle Inserat-Daten + Hausgeld-Aufschluesselung + WEG-Infos |
| **70-84%** | Gute Orientierung, Details klaerungsbeduerftig | KP, qm, Miete, Hausgeld vorhanden, Aufschluesselung fehlt |
| **50-69%** | Grobe Einschaetzung, wesentliche Informationen fehlen | Nur KP und qm, Miete geschaetzt |
| **< 50%** | Nur Tendenz, nicht entscheidungsrelevant | Wesentliche Angaben fehlen |

---

## Verwandte Wissensdatenbanken

- `knowledge/kalkulationsformeln.md` -- Detaillierte Berechnungsformeln fuer Renditekennzahlen, Cashflow, NK
- `knowledge/risikobewertung.md` -- Risiko-Scoring und Bewertungslogik

### Verwandte Skills

- `skills/deal-screener/SKILL.md` -- Schnellbewertung einzelner Objekte (komplementaer: Screener fuer Einzelobjekte, Akquise-Agent fuer Massensuche)
- `skills/bierdeckel-kalkulation/SKILL.md` -- Schnelle Rendite- und Cashflow-Kalkulation
- `skills/marktanalyse/SKILL.md` -- Vertiefte Standort- und Marktanalyse
- `skills/risiko-scanner/SKILL.md` -- Detaillierte Risikobewertung nach Unterlageneingang
- `skills/unterlagen-analyst/SKILL.md` -- Analyse der vollstaendigen Objektunterlagen
