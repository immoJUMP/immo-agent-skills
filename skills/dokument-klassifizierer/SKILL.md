---
name: dokument-klassifizierer
description: "Erkennt Dokumenttypen (Grundbuch, Mietvertrag, Energieausweis, Steuerbescheide, Gutachten etc.), extrahiert Metadaten inkl. steuerlich relevanter Felder (Kaufpreisaufteilung, Nutzen-/Lastenwechsel, Ruecklagen) und schlaegt korrekte Ablage vor. Nutze diesen Skill wenn du unsortierte Dokumente hast, Uebergabe-Unterlagen bekommst oder Scans/Fotos digitalisierst."
---

# Dokument-Klassifizierer

> Beliebige Immobilien-Dokumente automatisch erkennen, klassifizieren und mit Metadaten anreichern -- vom Grundbuchauszug bis zur Handwerkerrechnung.

---

## Wann nutzen?

- Bei unsortierten Dokumentenstapeln: Typ jedes Dokuments automatisch erkennen
- Nach Objektkauf: Uebergabedokumente systematisch erfassen und ablegen
- Laufend: Neue Dokumente sofort richtig einordnen
- Bei der Digitalisierung: Scans und Fotos klassifizieren und benennen

---

## Inputs

Stelle folgende Informationen bereit:

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| `dokument` | Ja | Das zu klassifizierende Dokument (PDF, Scan, Foto) |
| `objekte` | Empfohlen | Liste der eigenen Objekte mit Adressen (fuer Zuordnung) |
| `kontext` | Optional | Zusaetzliche Informationen (z.B. "Dokumente aus Ankaufspruefung Musterstrasse 12") |

---

## Auftrag

Du bist ein erfahrener Dokumentenmanager fuer Immobilienportfolios. Analysiere das uebergebene Dokument, erkenne den Dokumenttyp, extrahiere alle relevanten Metadaten und schlage eine korrekte Ablage vor. Bei unleserlichen oder unvollstaendigen Dokumenten weise klar darauf hin.

---

## Strategie

1. **Dokumenttyp erkennen**

   Ordne das Dokument einer der folgenden Kategorien zu:

   **Eigentumsunterlagen:**
   | Typ | Typische Merkmale |
   |-----|-------------------|
   | `grundbuchauszug` | Amtsgericht, Abteilung I/II/III, Eigentuemer, Belastungen |
   | `teilungserklaerung` | Miteigentumsanteile (MEA), Sonder-/Gemeinschaftseigentum, Aufteilungsplan |
   | `kaufvertrag` | Notarurkunde, Kaufpreis, Vertragsparteien, Auflassung |
   | `baulastenverzeichnis` | Bauaufsichtsbehoerde, oeffentlich-rechtliche Verpflichtungen |

   **Objektunterlagen:**
   | Typ | Typische Merkmale |
   |-----|-------------------|
   | `energieausweis` | Energiekennwert kWh/(m2a), Effizienzklasse A+ bis H, Bedarfs-/Verbrauchsausweis |
   | `expose` | Maklerkopf, Kaufpreis, Wohnflaeche, Rendite, Objektfotos |
   | `grundriss` | Raumaufteilung, Massstab, Flaechenangaben |
   | `flurkarte` | Katasteramt, Flurstueck, Gemarkung |
   | `baugenehmigung` | Bauaufsichtsbehoerde, Genehmigungsbescheid |
   | `wertgutachten` | Sachverstaendiger, Verkehrswert, Bewertungsstichtag |
   | `restnutzungsdauer_gutachten` | Sachverstaendiger, wirtschaftliche Restnutzungsdauer in Jahren, Gebaeudezustand -- Gutachter-Qualifikation (oeffentlich bestellt/vereidigt oder DIN EN ISO/IEC 17024) miterfassen, entscheidet ueber Anerkennung beim Finanzamt |

   **Verwaltungsunterlagen:**
   | Typ | Typische Merkmale |
   |-----|-------------------|
   | `wirtschaftsplan` | WEG, Planjahr, Hausgeld, Instandhaltungsruecklage |
   | `hausgeldabrechnung` | WEG, Abrechnungszeitraum, Ist/Soll-Vergleich, Nachzahlung/Guthaben |
   | `nebenkostenabrechnung` | Abrechnungszeitraum, Verteilerschluessel, Nachzahlung/Guthaben, Mieter |
   | `protokoll_eigentuemerversammlung` | TOP, Beschluesse, Abstimmungsergebnisse, Versammlungsleiter |

   **Mietunterlagen:**
   | Typ | Typische Merkmale |
   |-----|-------------------|
   | `mietvertrag` | Vertragsparteien, Mietobjekt, Mietzins, Mietbeginn, Unterschriften |
   | `kuendigungsschreiben` | Kuendigungsfrist, Kuendigungsgrund, Auszugsdatum |
   | `mieterhoehungsschreiben` | Aktuelle Miete, neue Miete, Begruendung (Mietspiegel/Modernisierung) |
   | `vermieterbescheinigung` | §19 BMG, Ein-/Auszug, Meldebehoerde |
   | `uebergabeprotokoll` | Zaehlerstaende, Maengel, Schluesseluebergabe, Unterschriften |
   | `mietliste` | Tabellarische Uebersicht aller Mieter, Mieten, Flaechen |
   | `mahnung` | Zahlungserinnerung, Rueckstand, Fristsetzung |

   **Finanzunterlagen:**
   | Typ | Typische Merkmale |
   |-----|-------------------|
   | `zinsbescheinigung` | Bank, Darlehensnummer, Jahreszinsen, Tilgung |
   | `darlehensvertrag` | Bank, Darlehenssumme, Zinssatz, Zinsbindung, Disagio, Verwendungszweck |
   | `grundsteuerbescheid` | Finanzamt, Einheitswert/Grundsteuerwert, Hebesatz, Jahresbetrag |
   | `grunderwerbsteuerbescheid` | Finanzamt, Kaufvorgang, Bemessungsgrundlage, Steuersatz des Bundeslands |
   | `foerderbescheid` | KfW/BAFA/Landesbank, Foerderprogramm, Zuschusshoehe, gefoerderte Massnahme |
   | `versicherungspolice` | Versicherungsgesellschaft, Versicherungsnummer, Deckungssumme, Praemie |
   | `versicherungsabrechnung` | Schadennummer, Erstattungsbetrag, Schadenursache, Schadendatum |
   | `rechnung` | Rechnungsnummer, Leistungsbeschreibung, Betrag, USt |
   | `handwerkerangebot` | Angebotsnummer, Leistungsbeschreibung, Positionen, Angebotssumme |
   | `freistellungsbescheinigung_48b` | Finanzamt, Bauleistender, Gueltigkeitszeitraum (§48b EStG) |

   **Behoerdliche Unterlagen:**
   | Typ | Typische Merkmale |
   |-----|-------------------|
   | `wohnungsbindung` | Foerderbescheid, Bindungsfrist, Mietobergrenze |
   | `denkmalschutzbescheid` | Denkmalschutzbehoerde, Auflagen |
   | `baulast` | Bauaufsichtsbehoerde, eingetragene Baulast |

2. **Metadaten extrahieren**
   - Datum des Dokuments (Ausstellungsdatum, Gueltigkeitsdatum)
   - Beteiligte Parteien (Eigentuemer, Mieter, Verwalter, Behoerde, Handwerker)
   - Objekt-Bezug (Adresse, Flurstueck, Einheit)
   - Finanzielle Daten (Betrag, Miete, Kaufpreis, Praemie)
   - Fristen und Termine (Kuendigungsfrist, Gueltigkeitsdauer, Abrechnungszeitraum)
   - Referenznummern (Aktenzeichen, Rechnungsnummer, Vertragsnummer)
   - **Steuerlich relevante Felder** (wenn im Dokument enthalten):
     - Kaufvertrag: Datum Uebergang Besitz/Nutzen/Lasten (Startpunkt fuer AfA-Beginn,
       3-Jahres-Frist der 15%-Grenze und 10-Jahres-Frist), Kaufpreisaufteilung
       Grund/Gebaeude, separat ausgewiesenes Inventar (Einbaukueche, Moebel --
       nur mit Ausweis im Vertrag separat abschreibbar)
     - Hausgeldabrechnung: Zufuehrung zur UND Entnahme aus der Instandhaltungsruecklage
       getrennt erfassen (nur die Verwendung ist Werbungskosten; Entnahmen fuer
       Sanierungen zaehlen in die 15%-Grenze)
     - Zinsbescheinigung/Darlehensvertrag: Zins vs. Tilgung, Disagio, Verwendungszweck
     - Rechnung: Netto/USt/Brutto, Leistungsbeginn (fuer 15%-Grenzen-Fristlogik),
       Gewerk (Fenster/Elektro/Sanitaer/Heizung fuer Standardhebungs-Check)
     - Foerderbescheid/Versicherungsabrechnung: Zuordnung zur Massnahme (kuerzt Kosten
       und 15%-Volumen)
     - Protokoll Eigentuemerversammlung: Beschluesse zu Sonderumlagen und
       Sanierungsmassnahmen (steuerlich relevant fuer 15%-Grenze der Eigentuemer)

3. **Objekt-Zuordnung**
   - Adresse im Dokument mit Objektliste abgleichen
   - Bei WEG-Dokumenten: Miteigentumsanteil und Einheitennummer identifizieren
   - Bei unklarer Zuordnung: Moegliche Objekte vorschlagen

4. **Ablageort vorschlagen**
   - Ordnerstruktur: `{Objekt}/{Kategorie}/{Dokumenttyp}/`
   - Dateiname nach Konvention: `YYYY-MM-DD_Dokumenttyp_Details`
   - Beispiele:
     - `Musterstr12/Eigentumsunterlagen/Grundbuchauszug/2025-01-15_Grundbuchauszug.pdf`
     - `Musterstr12/Mietunterlagen/WE3/2024-06-01_Mietvertrag_Mueller.pdf`
     - `Musterstr12/Finanzen/Rechnungen/2025-03-15_Handwerkerrechnung_2450EUR.pdf`

5. **Vollstaendigkeitspruefung**
   - Sind alle Seiten vorhanden?
   - Sind Unterschriften vorhanden (wo erforderlich)?
   - Ist das Dokument aktuell oder veraltet?
   - Sind alle Pflichtangaben enthalten?
   - Ist der Scan lesbar (bei digitalisierten Dokumenten)?

6. **Steuerliche Relevanz kennzeichnen**

   Fuer Dokumente mit Steuerbezug einen Relevanz-Hinweis in den Bericht aufnehmen
   (Einordnung ist Vorbereitung, keine Steuerberatung -- mit Steuerberater validieren):

   | Dokumenttyp | Steuerlicher Hinweis |
   |-------------|----------------------|
   | `kaufvertrag` | Kaufpreisaufteilung und Inventarausweis pruefen -- Basis fuer AfA und 15%-Grenze; Nutzen-/Lastenwechsel startet die Fristen |
   | `rechnung` (Handwerker) | An beleg-sortierer uebergeben: Erhaltungsaufwand vs. Herstellungskosten, 15%-Grenzen-Tracking, betroffenes Ausstattungsmerkmal (Heizung/Sanitaer/Elektro/Fenster) fuer Standardhebungs-Check erfassen |
   | `grundsteuerbescheid` | Sofort abziehbare Werbungskosten (Anlage V) |
   | `grunderwerbsteuerbescheid` | Anschaffungskosten (AfA-Bemessung), NICHT sofort abziehbar |
   | `zinsbescheinigung` | Nur Zinsanteil ist Werbungskosten, Tilgung nie |
   | `hausgeldabrechnung` | Ruecklagen-Zufuehrung nicht abziehbar; Ruecklagen-Verwendung abziehbar und ggf. 15%-relevant |
   | `restnutzungsdauer_gutachten` | Kann AfA erhoehen; Anerkennung haengt an Gutachter-Qualifikation -- Steuerberater einbinden |
   | `foerderbescheid` | Zuschuss kuerzt Kosten/AfA-Basis und schafft Luft in der 15%-Grenze -- Behandlung mit Steuerberater klaeren |
   | `versicherungsabrechnung` | Erstattung gegen Aufwendungen rechnen; Schaeden durch Dritte nach Kauf ggf. nicht 15%-relevant |
   | `protokoll_eigentuemerversammlung` | Sonderumlagen-/Sanierungsbeschluesse fuer 15%-Grenze vormerken |
   | `freistellungsbescheinigung_48b` | Fehlt sie beim Bauleister, droht Bauabzugsteuer -- Gueltigkeit pruefen |

---

## Ausgabeformat

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext.

### Klassifizierungsbericht

```markdown
# Dokument-Klassifizierung: Hausgeldabrechnung 2024

**Dokumenttyp: Hausgeldabrechnung** (Kategorie: Verwaltungsunterlagen) | Konfidenz: Hoch (95%)

## Eckdaten des Dokuments

| | |
|---|---|
| Titel | Hausgeldabrechnung 2024 |
| Dokumentdatum | 30.06.2025 |
| Abrechnungszeitraum | 01.01.2024 - 31.12.2024 |
| Aussteller | ABC Hausverwaltung GmbH |
| Empfaenger | Max Mustermann |
| Objekt | Musterstrasse 12, 40210 Duesseldorf, WE 3 |
| Miteigentumsanteil | 85,32/1000 |
| Aktenzeichen | WEG-2024-MU12 |
| Bankverbindung | IBAN DE89... |

## Finanzielle Daten

| Position | Betrag |
|----------|--------|
| Gezahltes Hausgeld | 3.600,00 EUR |
| Kostenanteil laut Abrechnung | 3.420,00 EUR |
| **Saldo: Guthaben** | **180,00 EUR** |
| Zufuehrung Instandhaltungsruecklage | 720,00 EUR |

## Objekt-Zuordnung

Zugeordnet zu: **Musterstrasse 12, 40210 Duesseldorf** (Zuordnungs-Konfidenz: 98%)
Begruendung: Adresse und Eigentuemername stimmen ueberein.

## Ablage-Vorschlag

- Ordner: `Musterstr12/Verwaltung/Hausgeldabrechnungen/`
- Dateiname: `2025-06-30_Hausgeldabrechnung_2024_3420EUR`
- Verwandter Ordner: `Musterstr12/Verwaltung/Wirtschaftsplaene/`

## Vollstaendigkeitspruefung

| Pruefpunkt | Ergebnis |
|------------|----------|
| Alle Seiten vorhanden | 🟢 Ja |
| Unterschriften | Nicht erforderlich |
| Dokument aktuell | 🟢 Ja |
| Lesbarkeit | 🟢 Gut |
| Fehlende Elemente | Keine |
| Warnungen | Keine |

## Was zu tun ist

| Prioritaet | Aktion | Frist |
|-----------|--------|-------|
| Mittel | Fuer Steuererklaerung vormerken: Hausgeldabrechnung 2024 fuer Anlage V 2024 relevant (Zeile 39-40, 46-48) | 31.07.2025 |
| Niedrig | Guthaben pruefen: 180 EUR -- Auszahlung oder Verrechnung mit naechstem Hausgeld | -- |

## Verwandte Dokumente anfordern

- **Wirtschaftsplan 2025** -- Vergleich Plan vs. Ist fuer Kostenplanung
- **Protokoll Eigentuemerversammlung 2025** -- Beschluesse zu Sonderumlagen oder Instandhaltungsmassnahmen pruefen
```

### Strukturierte Daten fuer Folge-Skills (nur als Datei)

Falls die extrahierten Daten fuer einen Folge-Skill (z.B. `beleg-sortierer`, `unterlagen-analyst`, `mietlisten-parser`) oder eine sonstige Weiterverarbeitung gebraucht werden: Schreibe die strukturierten Daten als Datei neben das Quelldokument (z.B. JSON-Datei `2025-06-30_Hausgeldabrechnung_2024.json` im selben Ordner). Gib diese strukturierten Daten niemals im Chat aus -- im Chat erscheint ausschliesslich der lesbare Bericht. Erwaehne im Bericht kurz, wohin die Datei geschrieben wurde.

---

## Qualitaetspruefung

Vor der Ausgabe pruefen:

- [ ] Dokumenttyp ist eindeutig bestimmt (nicht geraten)
- [ ] Alle erkennbaren Metadaten sind extrahiert (inkl. steuerlich relevanter Felder wie Nutzen-/Lastenwechsel, Kaufpreisaufteilung, Ruecklagen-Positionen)
- [ ] Steuerliche Relevanz ist gekennzeichnet und traegt den Hinweis "mit Steuerberater validieren"
- [ ] Objekt-Zuordnung ist begruendet
- [ ] Dateiname folgt der Namenskonvention
- [ ] Vollstaendigkeitspruefung ist durchgefuehrt
- [ ] Handlungsempfehlungen sind praxisrelevant
- [ ] Verwandte Dokumente sind benannt

---

## Warnsignale

| Signal | Bedeutung | Aktion |
|--------|-----------|--------|
| Dokument nicht lesbar | Scan-Qualitaet zu niedrig | Neuen Scan anfordern |
| Seiten fehlen | Unvollstaendiges Dokument | Vollstaendiges Dokument anfordern |
| Dokument veraltet | Grundbuchauszug aelter als 3 Monate / Energieausweis abgelaufen | Aktuelles Dokument anfordern |
| Unterschrift fehlt | Vertrag/Protokoll nicht rechtsverbindlich | Unterschriebenes Exemplar anfordern |
| Adresse unbekannt | Kein Objekt im Portfolio mit dieser Adresse | Zuordnung manuell klaeren |
| Mehrere Dokumenttypen | Dokument enthaelt mehrere Dokumentarten | Einzeln aufteilen und klassifizieren |
| Manipulationsverdacht | Sichtbare Aenderungen, verschiedene Schriftarten | Original-Dokument anfordern |
| Fremdsprachig | Dokument nicht in Deutsch | Beglaubigte Uebersetzung anfordern |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Objektliste nicht vorhanden | Adresse aus Dokument extrahieren und Zuordnung als "unbestaetigt" markieren |
| Datum nicht erkennbar | Aus Kontext schaetzen (Poststempel, Bezugszeitraum), als "geschaetzt" markieren |
| Betrag nicht lesbar | Als "Betrag nicht lesbar" markieren, manuelle Pruefung anfordern |
| Dokumenttyp unklar | Die zwei wahrscheinlichsten Typen nennen mit jeweiliger Konfidenz |
| Mehrere Seiten, unterschiedliche Dokumente | Jede Seite/jeden Abschnitt separat klassifizieren |

---

## Konfidenz-Bewertung

| Stufe | Wert | Bedeutung |
|-------|------|-----------|
| Hoch | >= 0.90 | Dokumenttyp eindeutig, alle Metadaten lesbar |
| Mittel | 0.70 - 0.89 | Dokumenttyp wahrscheinlich korrekt, einzelne Felder unklar |
| Niedrig | 0.50 - 0.69 | Dokumenttyp unsicher, manuelle Bestaetigung empfohlen |
| Unsicher | < 0.50 | Dokument nicht klassifizierbar (unleserlich, unbekannter Typ) |

---

## Verwandte Wissensdatenbanken

- `knowledge/checklisten.md` -- Dokumenten-Checklisten fuer Ankauf, Verwaltung, Vermietung
- `knowledge/rechtsgrundlagen.md` -- Rechtliche Anforderungen an Dokumente
- `skills/beleg-sortierer/SKILL.md` -- Weiterverarbeitung von Rechnungen und Belegen (steuerliche Klassifizierung, 15%-Grenze)
- `skills/datev-vorbereitung/SKILL.md` -- Buchungssaetze aus klassifizierten Finanzdokumenten
- `skills/kaufvertrag-pruefung/SKILL.md` -- Tiefenpruefung von Kaufvertraegen (inkl. Kaufpreisaufteilung, Inventar)
- `skills/nebenkosten-pruefer/SKILL.md` -- Tiefenpruefung von Nebenkosten-/Hausgeldabrechnungen
- `skills/mietlisten-parser/SKILL.md` -- Spezial-Skill fuer Mietlisten
- `skills/expose-parser/SKILL.md` -- Spezial-Skill fuer Exposes
- `skills/unterlagen-analyst/SKILL.md` -- Analyse von Ankaufsunterlagen
