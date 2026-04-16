---
description: "Erkennt Dokumenttypen (Grundbuch, Mietvertrag, Energieausweis etc.), extrahiert Metadaten und schlaegt korrekte Ablage vor. Nutze diesen Skill wenn du unsortierte Dokumente hast, Uebergabe-Unterlagen bekommst oder Scans/Fotos digitalisierst."
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
   | `grundsteuerbescheid` | Finanzamt, Einheitswert/Grundsteuerwert, Hebesatz, Jahresbetrag |
   | `versicherungspolice` | Versicherungsgesellschaft, Versicherungsnummer, Deckungssumme, Praemie |
   | `rechnung` | Rechnungsnummer, Leistungsbeschreibung, Betrag, USt |
   | `handwerkerangebot` | Angebotsnummer, Leistungsbeschreibung, Positionen, Angebotssumme |

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

---

## Ausgabeformat

```json
{
  "document_classification": {
    "processing_date": "2025-11-15",
    "document_id": "DOK-2025-042",
    "document_type": "hausgeldabrechnung",
    "document_category": "verwaltungsunterlagen",
    "confidence": 0.95,
    "metadata": {
      "document_date": "2025-06-30",
      "title": "Hausgeldabrechnung 2024",
      "period": {
        "from": "2024-01-01",
        "to": "2024-12-31"
      },
      "parties": {
        "issuer": "ABC Hausverwaltung GmbH",
        "recipient": "Max Mustermann"
      },
      "property": {
        "address": "Musterstrasse 12, 40210 Duesseldorf",
        "unit": "WE 3",
        "mea_share": "85.32/1000"
      },
      "financial": {
        "total_hausgeld_paid": 3600.00,
        "total_costs_share": 3420.00,
        "balance": 180.00,
        "balance_type": "guthaben",
        "instandhaltungsruecklage": 720.00
      },
      "reference_numbers": {
        "file_number": "WEG-2024-MU12",
        "account_number": "IBAN DE89..."
      }
    },
    "property_assignment": {
      "property_id": "OBJ-001",
      "property_address": "Musterstrasse 12, 40210 Duesseldorf",
      "assignment_confidence": 0.98,
      "assignment_basis": "Adresse und Eigentuemername stimmen ueberein"
    },
    "suggested_filing": {
      "folder_path": "Musterstr12/Verwaltung/Hausgeldabrechnungen/",
      "filename": "2025-06-30_Hausgeldabrechnung_2024_3420EUR",
      "related_folder": "Musterstr12/Verwaltung/Wirtschaftsplaene/"
    },
    "completeness_check": {
      "all_pages_present": true,
      "signatures_present": false,
      "signatures_required": false,
      "document_current": true,
      "legibility": "gut",
      "missing_elements": [],
      "warnings": []
    },
    "actionable_items": [
      {
        "action": "Guthaben pruefen",
        "description": "180 EUR Guthaben -- Auszahlung oder Verrechnung mit naechstem Hausgeld",
        "deadline": null,
        "priority": "niedrig"
      },
      {
        "action": "Fuer Steuererklaerung vormerken",
        "description": "Hausgeldabrechnung 2024 fuer Anlage V 2024 relevant (Zeile 39-40, 46-48)",
        "deadline": "2025-07-31",
        "priority": "mittel"
      }
    ],
    "related_documents_needed": [
      {
        "type": "wirtschaftsplan",
        "year": 2025,
        "reason": "Vergleich Plan vs. Ist fuer Kostenplanung"
      },
      {
        "type": "protokoll_eigentuemerversammlung",
        "year": 2025,
        "reason": "Beschluesse zu Sonderumlagen oder Instandhaltungsmassnahmen pruefen"
      }
    ]
  }
}
```

---

## Qualitaetspruefung

Vor der Ausgabe pruefen:

- [ ] Dokumenttyp ist eindeutig bestimmt (nicht geraten)
- [ ] Alle erkennbaren Metadaten sind extrahiert
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
- `skills/beleg-sortierer/SKILL.md` -- Weiterverarbeitung von Rechnungen und Belegen
- `skills/mietlisten-parser/SKILL.md` -- Spezial-Skill fuer Mietlisten
- `skills/expose-parser/SKILL.md` -- Spezial-Skill fuer Exposes
- `skills/unterlagen-analyst/SKILL.md` -- Analyse von Ankaufsunterlagen
