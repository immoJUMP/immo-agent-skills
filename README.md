# Immo Agent Skills

**25+ KI-Skills fuer den deutschen Immobilienmarkt** -- von der Objektpruefung bis zur Anlage V.

Jeder Skill ist eine eigenstaendige Markdown-Datei mit YAML-Frontmatter. Kein Code, keine API-Keys, keine Abhaengigkeiten. Als **Claude Code Plugin** installieren -- alle Skills werden automatisch als Slash-Commands erkannt und auto-triggered.

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

### Option 1: Plugin aus GitHub installieren (empfohlen)

Oeffne Claude Code (CLI, Desktop-App oder Web) und fuehre diese zwei Befehle aus:

```
/plugin marketplace add immoJUMP/immo-agent-skills
/plugin install immo-agent-skills@immoJUMP-immo-agent-skills
```

Fertig. Alle Skills sind sofort als Slash-Commands verfuegbar. Kein Git, kein Terminal noetig.

> **Wichtig:** Nach der Installation Claude Code einmal neu starten oder `/reload-plugins` ausfuehren.

---

### Option 2: Manuell klonen und als Plugin laden

```bash
# 1. Repo klonen (wohin ist egal -- z.B. ins Home-Verzeichnis)
git clone https://github.com/immoJUMP/immo-agent-skills.git ~/immo-agent-skills

# 2. Claude Code mit dem Plugin starten
claude --plugin-dir ~/immo-agent-skills
```

Wenn du das Plugin **dauerhaft** verfuegbar haben willst (ohne jedes Mal `--plugin-dir` anzugeben), trage es in deine Claude-Code-Settings ein:

**Datei:** `~/.claude/settings.json`
```json
{
  "plugins": [
    {
      "path": "~/immo-agent-skills"
    }
  ]
}
```

---

### Option 3: Einzelne Skills ohne Plugin kopieren

Falls du nur bestimmte Skills brauchst und kein Plugin installieren willst:

```bash
# Repo klonen
git clone https://github.com/immoJUMP/immo-agent-skills.git /tmp/immo-agent-skills

# Einzelne Skills in den Skills-Ordner kopieren
cp -r /tmp/immo-agent-skills/skills/deal-screener ~/.claude/skills/deal-screener
cp -r /tmp/immo-agent-skills/skills/bierdeckel-kalkulation ~/.claude/skills/bierdeckel-kalkulation
# ... weitere Skills nach Bedarf
```

> **Achtung:** Bei dieser Methode fehlt der Plugin-Namespace. Die Skills sind dann als `/deal-screener` statt `/immo-agent-skills:deal-screener` verfuegbar.

---

### Haeufiger Fehler: Ganzes Repo nach `~/.claude/skills/` klonen

```bash
# FALSCH -- so funktioniert es NICHT:
git clone https://github.com/immoJUMP/immo-agent-skills.git ~/.claude/skills/immo-agent-skills
```

Das fuehrt dazu, dass die SKILL.md-Dateien unter `~/.claude/skills/immo-agent-skills/skills/deal-screener/SKILL.md` landen -- eine Ebene zu tief. Claude Code findet nur `~/.claude/skills/*/SKILL.md` (eine Verzeichnisebene). Nutze stattdessen die Plugin-Installation (Option 1 oder 2).

---

### Skills nutzen

Nach der Installation sind alle Skills als Slash-Commands verfuegbar:

```
/immo-agent-skills:deal-screener Kaufpreis 850.000, 8 Einheiten, Baujahr 1962, Koeln-Ehrenfeld
/immo-agent-skills:mieterhoehung [Mietliste hochladen]
/immo-agent-skills:unterlagen-analyst [100 Seiten Objektunterlagen hochladen]
/immo-agent-skills:bierdeckel-kalkulation 650.000 EUR, 420 qm, 6 WE, 5.80 EUR/qm Ist-Miete
```

Oder stell einfach eine Frage -- Claude erkennt automatisch, welcher Skill passt.

### Wie die Skills funktionieren

**Du redest ganz normal mit Claude.** Kein JSON, keine technische Sprache, keine Formulare. Sag einfach was du brauchst:

> *"Ich habe ein MFH in Koeln-Ehrenfeld, 8 Einheiten, Kaufpreis 850.000. Kannst du mir eine Bankenpraesentation bauen?"*

Claude fragt dann im Gespraech alles ab, was er braucht -- Schritt fuer Schritt, auf Deutsch. Du kannst auch Dokumente hochladen (Mietliste, Expose, Objektunterlagen) und Claude extrahiert die Daten selbst.

**Die Antwort ist immer ein lesbarer Bericht** -- Tabellen, Ampeln (🟢🟡🔴), druckfertige Schreiben. Kein JSON, kein technisches Format. Das ist eine feste Design-Regel dieses Repos: Jede Ausgabeformat-Sektion der Skills verbietet rohe Maschinenformate in der Antwort. Wo strukturierte Daten fuer die Weiterverarbeitung gebraucht werden (z.B. Expose-Parser → Deal-Screener, DATEV-Buchungsstapel fuer den Steuerberater), schreibt der Skill sie in eine **Datei** (JSON/CSV) -- im Chat erscheint nur der Bericht. JSON-Bloecke in den Skill-Dateien selbst sind reine *Eingabe*-Spezifikationen fuer Entwickler und Automatisierungen (API, n8n).

---

## Skills in claude.ai importieren (ohne Claude Code)

Du kannst jeden Skill auch direkt in claude.ai (Web-App) hochladen -- dann steht er dir in jedem Chat zur Verfuegung:

1. **Skill-ZIP besorgen:** Entweder das fertige ZIP aus dem letzten [build-skills-Workflow-Lauf](../../actions/workflows/build-skills.yml) herunterladen (Artifact `skill-zips`), oder selbst zippen -- wichtig: die `SKILL.md` muss in einem Ordner mit dem Skill-Namen liegen (z.B. `deal-screener/SKILL.md`).
2. **claude.ai oeffnen** → Profil-Menue unten links → **Einstellungen** → **Funktionen** (Capabilities).
3. Im Abschnitt **Skills** auf **Skill hochladen** klicken und das ZIP auswaehlen.
4. Fertig -- der Skill wird in neuen Chats automatisch getriggert, wenn deine Frage passt. Du kannst ihn auch direkt ansprechen ("Nutze den Deal-Screener fuer ...").

**Tipp fuer Claude Projects:** Alternativ ein Project anlegen, die SKILL.md als Project-Knowledge hochladen und die passenden Dateien aus `knowledge/` dazu laden -- dann gilt der Skill fuer alle Chats im Project.

> Screenshots der einzelnen Schritte folgen in `docs/screenshots/`.

---

## Skills in ChatGPT importieren (Custom GPT)

ChatGPT kennt kein Skill-Format -- dort wird der Skill-Inhalt zu den Instructions eines Custom GPT:

1. **chatgpt.com** oeffnen → Seitenleiste **GPTs erkunden** → oben rechts **+ Erstellen**.
2. In den Tab **Konfigurieren** wechseln (nicht den Chat-Assistenten "Erstellen" nutzen -- der verwaessert die Anweisungen).
3. **Name** und **Beschreibung** vergeben (z.B. "Deal-Screener -- Schnellbewertung MFH").
4. Den kompletten Inhalt der `SKILL.md` (ohne YAML-Frontmatter) in das Feld **Hinweise** (Instructions) einfuegen.
5. Unter **Wissen** (Knowledge) die passenden Dateien aus `knowledge/` hochladen (z.B. `kalkulationsformeln.md`, `marktbenchmarks.md`).
6. Oben rechts **Erstellen** → Sichtbarkeit waehlen ("Nur ich" reicht fuer den Eigenbedarf).

> **Hinweis:** Die Instructions-Felder von Custom GPTs sind auf 8.000 Zeichen begrenzt. Bei langen Skills den Skill-Inhalt stattdessen als Knowledge-Datei hochladen und in die Instructions nur schreiben: "Befolge exakt die Anweisungen aus SKILL.md."
>
> Screenshots der einzelnen Schritte folgen in `docs/screenshots/`.

**Direkt im Chat (jedes LLM):**
Skill-Datei oeffnen, Inhalt kopieren, in den Chat einfuegen, Daten dazu geben -- fertig.

---

## Verzeichnisstruktur

```
immo-agent-skills/
├── .claude-plugin/
│   └── plugin.json                # Plugin-Manifest (Name, Version, Beschreibung)
│
├── skills/                        # Jeder Skill = ein Ordner mit SKILL.md
│   ├── deal-screener/SKILL.md     # Schnellbewertung nach Ankaufskriterien
│   ├── marktanalyse/SKILL.md      # Standort- und Marktbewertung
│   ├── bierdeckel-kalkulation/SKILL.md  # Sofort-Ampel: Deal oder kein Deal
│   ├── akquise-agent/SKILL.md     # Parametrisierter Deal-Such-Agent
│   ├── unterlagen-analyst/SKILL.md # 100-Seiten-Objektunterlagen analysieren
│   ├── risiko-scanner/SKILL.md    # Hoch/Mittel/Niedrig Risikobewertung
│   ├── besichtigung-prep/SKILL.md # Besichtigungsfragen generieren
│   ├── energieausweis-check/SKILL.md # Energieausweis auswerten
│   ├── mietlisten-analyse/SKILL.md # Mietliste validieren & Potenzial
│   ├── kaufvertrag-pruefung/SKILL.md # 13-Punkte Kaufvertragspruefung
│   ├── bankenkonzept/SKILL.md     # Finanzierungskonzept erstellen
│   ├── cashflow-modell/SKILL.md   # 5-Jahres-Cashflow mit Szenarien
│   ├── bankenpitch/SKILL.md       # 13-Sektionen-Bankenpraesentation
│   ├── selbstauskunft/SKILL.md    # Bonitaetsunterlagen fuer die Bank
│   ├── wochen-jourfixe/SKILL.md   # Automatischer Wochenreport
│   ├── mahn-assistent/SKILL.md    # Mahnwesen & Zahlungsverfolgung
│   ├── nebenkosten-pruefer/SKILL.md # Nebenkostenabrechnung pruefen
│   ├── mieterhoehung/SKILL.md     # Potenzialanalyse & Schreiben
│   ├── inserat-generator/SKILL.md # Vermietungsinserat erstellen
│   ├── vermieterbescheinigung/SKILL.md # §19 BMG Bescheinigung
│   ├── mietnomaden-praevention/SKILL.md # 5-Saeulen Bewerber-Check
│   ├── beleg-sortierer/SKILL.md   # Belege klassifizieren & zuordnen
│   ├── datev-vorbereitung/SKILL.md # DATEV-Export vorbereiten
│   ├── anlage-v-assistent/SKILL.md # Anlage V fuer Steuerberater
│   ├── dokument-klassifizierer/SKILL.md # Dokumenttyp erkennen
│   ├── ordner-architekt/SKILL.md  # Ablage aufbauen & restrukturieren
│   ├── mietlisten-parser/SKILL.md # Mietlisten aus PDF extrahieren
│   ├── expose-parser/SKILL.md     # Expose-Daten strukturiert extrahieren
│   ├── akquise-netzwerk/SKILL.md  # Off-Market Akquiseplan
│   ├── bankgespraech-coach/SKILL.md # Banktermin-Vorbereitung
│   ├── makler-coach/SKILL.md      # Maklerbeziehungen aufbauen
│   └── verhandlungs-assistent/SKILL.md # Preisverhandlung & Strategie
│
├── knowledge/                     # Wissensdatenbanken (Kontext fuer Skills)
│   ├── kalkulationsformeln.md     # Renditekennzahlen, Faktoren, Formeln
│   ├── risikobewertung.md         # Risiko-Scoring-Framework
│   ├── marktbenchmarks.md         # Benchmarks nach Baujahr, Lage, Zustand
│   ├── rechtsgrundlagen.md        # BGB-Mietrecht, WEG, Mietspiegel
│   └── checklisten.md             # Ankauf, Verwaltung, Vermietung
│
├── templates/                     # Beispiel-Eingabedaten & HTML-Templates
│   └── bankenpitch-template.html  # Interaktives Bankenpitch-Template
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

### Organisation & Ablage

| Skill | Beschreibung | Typischer Input |
|-------|-------------|-----------------|
| **Ordner-Architekt** | Baut/ordnet die Portfolio-Ablage als Grundlage fuer alle Folge-Skills -- im gefuehrten Gespraech mit Ist-Inventar, Bewertung & bestaetigungspflichtigem Umzugsplan | Zugriff auf Drive/Dropbox/lokalen Ordner |

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
