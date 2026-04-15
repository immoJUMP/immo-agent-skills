# Immo Agent Skills

**25+ KI-Skills fuer den deutschen Immobilienmarkt** -- von der Objektpruefung bis zur Anlage V.

Jeder Skill ist eine eigenstaendige Markdown-Datei. Kein Code, keine API-Keys, keine Abhaengigkeiten. Einfach in Claude, ChatGPT oder jedes andere LLM laden und loslegen.

---

## Was ist das?

Eine Sammlung strukturierter KI-Prompts (Skills), die den kompletten Immobilien-Investitionsprozess abdecken:

- **Ankauf** -- Deal-Screening, Marktanalyse, Bierdeckel-Kalkulation
- **Objektpruefung** -- Unterlagenanalyse, Risikoerkennung, Besichtigungsvorbereitung
- **Finanzierung** -- Bankenkonzept, Cashflow-Modellierung, Bankenpitch
- **Verwaltung** -- Wochen-Jour-Fixe, Mahn-Assistent, Nebenkostenpruefung
- **Vermietung** -- Mietspiegelanalyse, Mieterhoehungsstrategie, Inserat-Generator
- **Buchhaltung** -- Belegzuordnung, DATEV-Vorbereitung, Anlage-V-Assistent
- **Dokumente** -- Dokumentenklassifizierung, Mietlisten-Parser, Expose-Analyse

Jeder Skill wurde fuer den **deutschen Markt** entwickelt -- mit deutschen Rechtsbegriffen, Mietspiegellogik, BGB-Referenzen und praxiserprobten Workflows von Investoren mit 50-500+ Einheiten.

---

## Schnellstart

### Die einfachste Methode: Claude fragen

Oeffne Claude Code und tippe:

> **Installiere die Immobilien-Skills von https://github.com/immoJUMP/immo-agent-skills**

Das war's. Claude laedt alles herunter und richtet die Skills ein. Kein Git, kein Terminal-Wissen noetig.

---

### Alternative: Ein Befehl im Terminal

```bash
git clone https://github.com/immoJUMP/immo-agent-skills.git ~/.claude/skills/immo-agent-skills
```

---

### Danach: Skills nutzen

Starte eine neue Claude-Code-Session -- alle Skills sind sofort verfuegbar:

```
/deal-screener Kaufpreis 850.000, 8 Einheiten, Baujahr 1962, Koeln-Ehrenfeld
/mieterhoehung [Mietliste hochladen]
/unterlagen-analyst [100 Seiten Objektunterlagen hochladen]
/bierdeckel-kalkulation 650.000 EUR, 420 qm, 6 WE, 5.80 EUR/qm Ist-Miete
```

Oder stell einfach eine Frage -- Claude erkennt automatisch, welcher Skill passt.

### Wie die Skills funktionieren

**Du redest ganz normal mit Claude.** Kein JSON, keine technische Sprache, keine Formulare. Sag einfach was du brauchst:

> *"Ich habe ein MFH in Koeln-Ehrenfeld, 8 Einheiten, Kaufpreis 850.000. Kannst du mir eine Bankenpraesentation bauen?"*

Claude fragt dann im Gespraech alles ab, was er braucht -- Schritt fuer Schritt, auf Deutsch. Du kannst auch Dokumente hochladen (Mietliste, Expose, Objektunterlagen) und Claude extrahiert die Daten selbst.

Die JSON-Schemas in den Skill-Dateien sind die technische Referenz fuer Entwickler und Automatisierungen (z.B. wenn du Skills ueber eine API oder n8n ansteuerst). Als normaler Nutzer brauchst du die nie zu sehen.

> **Tipp:** Du brauchst nicht alle Skills. Kopiere nur die Ordner, die du brauchst (z.B. nur `skills/ankauf/` und `knowledge/`).

<details>
<summary><strong>Weitere Optionen: Claude Projects, ChatGPT, andere LLMs</strong></summary>

**Claude Projects / Cowork:**
1. Neues Project erstellen
2. Relevante Skill-Dateien als Knowledge hochladen
3. Knowledge-Dateien aus `knowledge/` dazu laden

**ChatGPT Custom GPT:**
1. Custom GPT erstellen
2. Skill-Inhalt in die Instructions kopieren
3. Knowledge-Dateien hochladen

**Direkt im Chat (jedes LLM):**
Skill-Datei oeffnen, Inhalt kopieren, in den Chat einfuegen, Daten dazu geben -- fertig.
</details>

---

## Verzeichnisstruktur

```
immo-agent-skills/
├── skills/
│   ├── ankauf/                    # Deal-Screening & Akquise
│   │   ├── deal-screener.md       # Schnellbewertung nach Ankaufskriterien
│   │   ├── marktanalyse.md        # Standort- und Marktbewertung
│   │   └── bierdeckel-kalkulation.md  # Sofort-Ampel: Deal oder kein Deal
│   │
│   ├── objektpruefung/            # Due Diligence & Unterlagenanalyse
│   │   ├── unterlagen-analyst.md  # 100-Seiten-Objektunterlagen analysieren
│   │   ├── risiko-scanner.md      # Hoch/Mittel/Niedrig Risikobewertung
│   │   ├── besichtigung-prep.md   # Besichtigungsfragen generieren
│   │   ├── energieausweis-check.md # Energieausweis auswerten
│   │   └── mietlisten-analyse.md  # Mietliste validieren & Potenzial erkennen
│   │
│   ├── finanzierung/              # Bankenkommunikation & Konzepte
│   │   ├── bankenkonzept.md       # Finanzierungskonzept erstellen
│   │   ├── cashflow-modell.md     # Cashflow-Projektion & Szenarien
│   │   └── bankenpitch.md         # Praesentation fuer den Banker
│   │
│   ├── verwaltung/                # Laufende Bestandsverwaltung
│   │   ├── wochen-jourfixe.md     # Woechentlicher Report aus E-Mail-Postfach
│   │   ├── mahn-assistent.md      # Mahnwesen & Zahlungsverfolgung
│   │   └── nebenkosten-pruefer.md # Nebenkostenabrechnung pruefen
│   │
│   ├── vermietung/                # Mietmanagement & Optimierung
│   │   ├── mieterhoehung.md       # Mieterhoehungsstrategie & Potenzialanalyse
│   │   ├── inserat-generator.md   # Vermietungsinserat erstellen
│   │   └── vermieterbescheinigung.md # Vermieterbescheinigung generieren
│   │
│   ├── buchhaltung/               # Belege, DATEV & Steuer
│   │   ├── beleg-sortierer.md     # Belege klassifizieren & zuordnen
│   │   ├── datev-vorbereitung.md  # DATEV-Export vorbereiten
│   │   └── anlage-v-assistent.md  # Anlage V fuer den Steuerberater
│   │
│   └── dokumente/                 # Dokumentenverarbeitung
│       ├── dokument-klassifizierer.md  # Dokumenttyp erkennen
│       ├── mietlisten-parser.md       # Mietlisten aus PDF extrahieren
│       └── expose-parser.md           # Expose-Daten strukturiert extrahieren
│
├── knowledge/                     # Wissensdatenbanken (Kontext fuer Skills)
│   ├── kalkulationsformeln.md     # Renditekennzahlen, Faktoren, Formeln
│   ├── risikobewertung.md         # Risiko-Scoring-Framework
│   ├── marktbenchmarks.md         # Benchmarks nach Baujahr, Lage, Zustand
│   ├── rechtsgrundlagen.md        # BGB-Mietrecht, WEG, Mietspiegel
│   └── checklisten.md             # Ankauf, Verwaltung, Vermietung
│
├── claude-code-plugins/           # Fertige Plugins fuer Claude Code
│   ├── ankauf-plugin/
│   ├── objektpruefung-plugin/
│   ├── verwaltung-plugin/
│   └── vermietung-plugin/
│
├── templates/                     # Beispiel-Eingabedaten
│   └── beispiel-inputs/
│       ├── beispiel-mietliste.csv
│       └── beispiel-objektdaten.json
│
├── LICENSE                        # Apache 2.0
├── DISCLAIMER.md                  # Haftungsausschluss
├── SECURITY.md                    # Sicherheitshinweise
├── CONTRIBUTING.md                # Mitmachen
├── CHANGELOG.md                   # Aenderungsprotokoll
└── README.md                      # Diese Datei
```

---

## Skills im Detail

### Ankauf

| Skill | Beschreibung | Typischer Input |
|-------|-------------|-----------------|
| **Deal-Screener** | Schnellbewertung: Passt das Objekt zu meinen Kriterien? | Inserat-Link oder Eckdaten |
| **Marktanalyse** | Standort, Mikrolage, Demografie, Mietentwicklung | Adresse oder PLZ |
| **Bierdeckel-Kalkulation** | Sofort-Ampel (Gruen/Gelb/Rot) mit wenigen Eingaben | Kaufpreis, Flaeche, Ist-Miete, Baujahr |

### Objektpruefung

| Skill | Beschreibung | Typischer Input |
|-------|-------------|-----------------|
| **Unterlagen-Analyst** | Analysiert 100+ Seiten Objektunterlagen in Minuten | PDF-Upload (Expose, Grundbuch, Vertraege) |
| **Risiko-Scanner** | Identifiziert Risiken: Hoch, Mittel, Niedrig | Objektunterlagen + Mietliste |
| **Besichtigung-Prep** | Generiert gezielte Fragen fuer die Besichtigung | Ergebnisse aus Unterlagen-Analyst |
| **Energieausweis-Check** | Wertet Energieausweis aus, erkennt Handlungsbedarf | Energieausweis-PDF |
| **Mietlisten-Analyse** | Validiert Mietliste, erkennt Potenziale und Risiken | Mietliste (CSV/PDF/Excel) |

### Finanzierung

| Skill | Beschreibung | Typischer Input |
|-------|-------------|-----------------|
| **Bankenkonzept** | Erstellt Finanzierungskonzept fuer die Bank | Objektdaten + Ankaufspreis + Strategie |
| **Cashflow-Modell** | 5-Jahres-Cashflow-Projektion mit Szenarien | Mietliste + Finanzierungskonditionen |
| **Bankenpitch** | Bankenpraesentation als strukturiertes Dokument | Ergebnisse aus Bankenkonzept |

### Verwaltung

| Skill | Beschreibung | Typischer Input |
|-------|-------------|-----------------|
| **Wochen-Jourfixe** | Automatischer Wochen-Report aus E-Mails | E-Mail-Postfach (via Konnektor) |
| **Mahn-Assistent** | Mahnwesen: Fristen, Eskalation, Schreiben | Zahlungseingaenge + Mietliste |
| **Nebenkosten-Pruefer** | Nebenkostenabrechnung auf Fehler pruefen | NK-Abrechnung PDF |

### Vermietung

| Skill | Beschreibung | Typischer Input |
|-------|-------------|-----------------|
| **Mieterhoehung** | Potenzialanalyse + Schreiben generieren | Mietliste + Mietspiegel-Daten |
| **Inserat-Generator** | Vermietungsinserat erstellen | Objektdaten + Fotos |
| **Vermieterbescheinigung** | Vermieterbescheinigung nach §19 BMG | Mieterdaten + Objektdaten |

### Buchhaltung

| Skill | Beschreibung | Typischer Input |
|-------|-------------|-----------------|
| **Beleg-Sortierer** | Belege nach Kategorie und Objekt zuordnen | Beleg-PDFs oder Scans |
| **DATEV-Vorbereitung** | Buchungssaetze fuer DATEV-Export aufbereiten | Sortierte Belege |
| **Anlage-V-Assistent** | Anlage V vorausfuellen fuer den Steuerberater | Jahresdaten pro Objekt |

### Dokumente

| Skill | Beschreibung | Typischer Input |
|-------|-------------|-----------------|
| **Dokument-Klassifizierer** | Erkennt Dokumenttyp automatisch | Beliebiges Dokument (PDF/Scan) |
| **Mietlisten-Parser** | Extrahiert strukturierte Daten aus Mietlisten-PDFs | Mietliste als PDF |
| **Expose-Parser** | Extrahiert Eckdaten aus Makler-Exposes | Expose-PDF |

---

## Knowledge-Dateien

Die Wissensdatenbanken liefern den Kontext, damit die Skills praeziese Ergebnisse liefern:

| Datei | Inhalt |
|-------|--------|
| **kalkulationsformeln.md** | Bruttomietrendite, Nettomietrendite, Kaufpreisfaktor, Cashflow-Berechnung, EK-Rueckfluss |
| **risikobewertung.md** | 10-Kategorien-Risiko-Framework fuer deutsche Wohnimmobilien |
| **marktbenchmarks.md** | Benchmarks nach Baujahr, Lage (A/B/C/D), Zustandsklasse |
| **rechtsgrundlagen.md** | BGB Mietrecht (§535ff), Kappungsgrenze, Mietpreisbremse, WEG, Modernisierungsumlage |
| **checklisten.md** | Pruef-Checklisten fuer Ankauf, Uebergabe, Vermietung, Verwaltung |

---

## Fuer wen ist das?

- **Immobilieninvestoren** mit 10-500+ Einheiten, die KI strukturiert einsetzen wollen
- **Hausverwaltungen**, die repetitive Prozesse automatisieren wollen
- **Teams**, die einheitliche Standards fuer Analyse und Entscheidung brauchen

**Nicht geeignet fuer:**
- Maklertaetigkeit (Fokus liegt auf Investoren und Bestandshalter)
- Gewerbeimmobilien (Fokus auf Wohnimmobilien / MFH)
- Internationale Maerkte (spezifisch fuer Deutschland)

---

## Wichtige Hinweise

- **Keine Rechts- oder Finanzberatung.** Siehe [DISCLAIMER.md](DISCLAIMER.md).
- **KI-Output immer pruefen.** KI ist stochastisch, nicht deterministisch. Ergebnisse validieren.
- **Marktdaten veralten.** Benchmarks und Mietspiegel regelmaessig aktualisieren.
- **Datenschutz beachten.** Keine personenbezogenen Mieterdaten in oeffentliche KI-Dienste hochladen, ohne Datenschutzkonformitaet sicherzustellen.

---

## Mitmachen

Beitraege sind willkommen! Siehe [CONTRIBUTING.md](CONTRIBUTING.md).

- Neue Skills vorschlagen oder bestehende verbessern
- Regionale Benchmarks ergaenzen (Mietspiegel, Sanierungskosten)
- Fehler melden

---

## Lizenz

Apache 2.0 -- siehe [LICENSE](LICENSE).

---

## Credits

Entwickelt von [immoJUMP](https://immojump.de).
