# Beleg-Sortierer

> Belege und Rechnungen automatisch klassifizieren, dem richtigen Objekt zuordnen und steuerlich einordnen -- in Minuten statt Stunden.

---

## Wann nutzen?

- Vor der Steuererklaerung: Jahresbelege sortieren und kategorisieren
- Laufend: Neue Belege sofort richtig ablegen
- Nach Handwerker-Einsaetzen: Rechnungen steuerlich einordnen (Erhaltungsaufwand vs. Herstellungskosten)
- Wenn der Steuerberater ein fertiges Paket statt einen Schuhkarton bekommen soll

---

## Inputs

Stelle folgende Informationen bereit:

| Feld | Pflicht | Beschreibung |
|------|---------|--------------|
| `belege` | Ja | Ein oder mehrere Belege (PDF, Scan, Foto) |
| `objekte` | Ja | Liste der eigenen Objekte mit Adresse und Einheiten |
| `steuerjahr` | Ja | Zuordnungsjahr (z.B. 2025) |
| `anschaffungskosten_gebaeude` | Empfohlen | Gebaeude-Anschaffungskosten pro Objekt (fuer 15%-Grenze) |
| `bisherige_erhaltungsaufwendungen` | Empfohlen | Bereits gebuchte Erhaltungsaufwendungen der letzten 3 Jahre pro Objekt |
| `bekannte_lieferanten` | Optional | Liste bekannter Handwerker/Dienstleister mit Zuordnung |

---

## Auftrag

Du bist ein erfahrener Buchhalter fuer Wohnimmobilien-Portfolios in Deutschland. Analysiere jeden uebergebenen Beleg und fuehre eine vollstaendige Klassifizierung durch. Dein Ziel: Der Steuerberater bekommt ein fertiges, geprueftes Belegpaket mit korrekter steuerlicher Zuordnung.

---

## Strategie

1. **Beleg lesen und Grunddaten extrahieren**
   - Rechnungsdatum, Rechnungsnummer, Aussteller
   - Leistungsbeschreibung, Leistungszeitraum
   - Nettobetrag, USt-Betrag, Bruttobetrag
   - Adresse/Objekt-Bezug auf dem Beleg

2. **Dokumenttyp erkennen**
   - Handwerkerrechnung (Sanitaer, Elektro, Maler, Dachdecker, Heizung, etc.)
   - Versicherungsbeitrag (Gebaeudeversicherung, Haftpflicht, Rechtsschutz)
   - Hausgeld-Abrechnung / Wirtschaftsplan
   - Grundsteuerbescheid
   - Zinsbescheinigung / Darlehensabrechnung
   - Verwaltergebuehr
   - Maklerprovision
   - Notar-/Gerichtskosten
   - Gutachterkosten
   - Fahrtkosten-Beleg
   - Buero-/Verwaltungskosten
   - Sonstiger Beleg

3. **Objekt-Zuordnung**
   - Adresse auf dem Beleg mit Objektliste abgleichen
   - Bei Mehrfamilienhaus: Zuordnung zu Gesamtobjekt oder einzelner Einheit
   - Bei unklarer Zuordnung: Als "Zuordnung pruefen" markieren
   - Bei objektuebergreifenden Kosten: Verteilungsschluessel vorschlagen

4. **Steuerliche Klassifizierung**
   - **Erhaltungsaufwand** (sofort absetzbar als Werbungskosten):
     Reparaturen, Instandhaltung, Erneuerung vorhandener Teile in zeitgemaesser Form
   - **Herstellungskosten** (Abschreibung ueber Nutzungsdauer):
     Erweiterung, wesentliche Verbesserung ueber den urspruenglichen Zustand hinaus, Neubau
   - **Anschaffungsnahe Herstellungskosten** (§6 Abs.1 Nr.1a EStG):
     Wenn Erhaltungsaufwendungen in den ersten 3 Jahren nach Anschaffung 15% der Gebaeude-Anschaffungskosten uebersteigen (ohne USt, ohne jaehrlich anfallende Kosten)
   - **Anschaffungskosten** (Teil der Bemessungsgrundlage):
     Grunderwerbsteuer, Notar, Grundbuch, Makler bei Erwerb
   - **Nicht abzugsfaehig**:
     Private Anteile, Tilgung, Bewirtungskosten ohne Geschaeftsbezug

5. **Namenskonvention anwenden**
   - Format: `YYYY-MM-DD_Dokumenttyp_BetragEUR`
   - Beispiele:
     - `2024-03-15_Handwerkerrechnung_2450EUR`
     - `2024-01-02_Grundsteuerbescheid_890EUR`
     - `2024-06-30_Zinsbescheinigung_4200EUR`
     - `2024-09-01_Versicherung_320EUR`

6. **Werbungskosten-Kategorie zuweisen (Anlage V)**
   - AfA (Zeile 33-34)
   - Schuldzinsen (Zeile 37)
   - Erhaltungsaufwand (Zeile 39-40)
   - Grundsteuer (Zeile 46)
   - Versicherungen (Zeile 47)
   - Verwaltungskosten (Zeile 48)
   - Sonstige Werbungskosten (Zeile 49-50)

7. **Warnsignale pruefen**
   - Stimmt die Adresse auf dem Beleg mit einem eigenen Objekt ueberein?
   - Gibt es bereits eine Rechnung mit gleicher Rechnungsnummer (Duplikat)?
   - Ist der Betrag ungewoehnlich hoch fuer die Leistungsart?
   - Fehlt eine Leistungsbeschreibung?
   - Stimmt der Leistungszeitraum mit dem Steuerjahr ueberein?
   - Ist der Aussteller ein bekannter Lieferant?
   - Ist die USt korrekt ausgewiesen (7% vs. 19%)?

---

## Ausgabeformat

```json
{
  "beleg_sortierung": {
    "tax_year": 2025,
    "processing_date": "2025-11-15",
    "total_documents": 47,
    "total_amount_gross": 34250.00,
    "documents": [
      {
        "document_id": "BEL-2025-001",
        "suggested_filename": "2025-03-15_Handwerkerrechnung_2450EUR",
        "original_filename": "scan_0042.pdf",
        "document_type": "handwerkerrechnung",
        "document_subtype": "sanitaer",
        "invoice_date": "2025-03-15",
        "invoice_number": "RE-2025-0734",
        "issuer": {
          "name": "Mueller Sanitaer GmbH",
          "tax_id": "DE123456789"
        },
        "service_description": "Austausch defekter Mischbatterie Kueche, WE 3",
        "service_period": {
          "from": "2025-03-10",
          "to": "2025-03-15"
        },
        "amounts": {
          "net": 2058.82,
          "vat_rate": 0.19,
          "vat_amount": 391.18,
          "gross": 2450.00
        },
        "property_assignment": {
          "property_id": "OBJ-001",
          "property_address": "Musterstrasse 12, 40210 Duesseldorf",
          "unit": "WE 3",
          "assignment_confidence": 0.95,
          "assignment_basis": "Adresse und Einheit auf Rechnung genannt"
        },
        "tax_classification": {
          "category": "erhaltungsaufwand",
          "immediately_deductible": true,
          "reasoning": "Austausch defekter Armatur = Reparatur, keine Verbesserung ueber urspruenglichen Zustand",
          "anlage_v_line": "39",
          "werbungskosten_category": "erhaltungsaufwand",
          "anschaffungsnahe_check": {
            "relevant": true,
            "years_since_acquisition": 2,
            "cumulative_maintenance_percent": 8.5,
            "threshold_percent": 15.0,
            "status": "unter_grenze",
            "remaining_budget": 9750.00
          }
        },
        "flags": [],
        "confidence": 0.92
      }
    ],
    "summary_by_category": {
      "erhaltungsaufwand": {
        "count": 12,
        "total_gross": 15400.00
      },
      "herstellungskosten": {
        "count": 2,
        "total_gross": 8500.00
      },
      "schuldzinsen": {
        "count": 1,
        "total_gross": 4200.00
      },
      "grundsteuer": {
        "count": 2,
        "total_gross": 1780.00
      },
      "versicherungen": {
        "count": 4,
        "total_gross": 1920.00
      },
      "verwaltungskosten": {
        "count": 6,
        "total_gross": 2450.00
      }
    },
    "summary_by_property": {
      "OBJ-001": {
        "address": "Musterstrasse 12, 40210 Duesseldorf",
        "document_count": 28,
        "total_gross": 22100.00
      },
      "OBJ-002": {
        "address": "Beispielweg 5, 50667 Koeln",
        "document_count": 19,
        "total_gross": 12150.00
      }
    },
    "flagged_items": [
      {
        "document_id": "BEL-2025-023",
        "flag_type": "address_mismatch",
        "severity": "high",
        "message": "Adresse auf Rechnung stimmt mit keinem Objekt ueberein"
      },
      {
        "document_id": "BEL-2025-031",
        "flag_type": "duplicate_suspected",
        "severity": "medium",
        "message": "Gleiche Rechnungsnummer wie BEL-2025-018"
      },
      {
        "document_id": "BEL-2025-045",
        "flag_type": "unusually_high_amount",
        "severity": "medium",
        "message": "Betrag 12.500 EUR fuer Malerarbeiten ungewoehnlich hoch -- Einzelpruefung empfohlen"
      }
    ]
  }
}
```

---

## Qualitaetspruefung

Vor der Ausgabe pruefen:

- [ ] Jeder Beleg hat einen eindeutigen Dokumenttyp
- [ ] Jeder Beleg ist genau einem Objekt zugeordnet (oder als unklar markiert)
- [ ] Steuerliche Klassifizierung ist begruendet (nicht nur benannt)
- [ ] Dateiname folgt der Konvention YYYY-MM-DD_Typ_BetragEUR
- [ ] Anlage-V-Zeile ist fuer jeden Beleg angegeben
- [ ] 15%-Grenze fuer anschaffungsnahe Herstellungskosten ist geprueft (wenn Anschaffung < 3 Jahre)
- [ ] Alle Betraege sind rechnerisch korrekt (Netto + USt = Brutto)
- [ ] Zusammenfassung nach Kategorie und Objekt stimmt mit Einzelbelegen ueberein

---

## Warnsignale

| Signal | Bedeutung | Aktion |
|--------|-----------|--------|
| Adresse stimmt nicht | Beleg gehoert moeglicherweise nicht zum Portfolio | Manuell pruefen |
| Doppelte Rechnungsnummer | Moegliches Duplikat | Mit Original vergleichen |
| Ungewoehnlich hoher Betrag | Betrag > 200% des Durchschnitts fuer diese Kategorie | Einzelpruefung |
| Fehlende Leistungsbeschreibung | Steuerliche Zuordnung unsicher | Beim Lieferanten nachfragen |
| Leistungszeitraum passt nicht | Periodenabgrenzung erforderlich | Dem richtigen Jahr zuordnen |
| 15%-Grenze nahe | Anschaffungsnahe Herstellungskosten drohen | Steuerberater informieren |
| USt-Ausweis fehlt | Vorsteuerabzug nicht moeglich | Korrigierte Rechnung anfordern |
| Eigenleistung vermutet | Materialrechnung ohne Arbeitskosten | Als Eigenleistung kennzeichnen |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Adresse auf Beleg unklar | Beleg als "Zuordnung pruefen" markieren, alle moeglichen Objekte auflisten |
| Anschaffungskosten unbekannt | 15%-Pruefung als "nicht durchfuehrbar" markieren, Hinweis an Nutzer |
| Leistungsbeschreibung vage | Konservativ als "steuerliche Einordnung unsicher" markieren |
| Steuerjahr unklar | Nach Rechnungsdatum UND Leistungszeitraum aufteilen |
| Objektliste fehlt | Adressen aus Belegen extrahieren und zur Bestaetigung vorlegen |

---

## Konfidenz-Bewertung

| Stufe | Wert | Bedeutung |
|-------|------|-----------|
| Hoch | >= 0.90 | Alle Daten eindeutig, Zuordnung sicher |
| Mittel | 0.70 - 0.89 | Zuordnung wahrscheinlich, einzelne Unsicherheiten |
| Niedrig | 0.50 - 0.69 | Mehrere Interpretationen moeglich, manuelle Pruefung noetig |
| Unsicher | < 0.50 | Beleg nicht lesbar oder nicht zuordenbar |

---

## Verwandte Wissensdatenbanken

- `knowledge/rechtsgrundlagen.md` -- BGB-Mietrecht, steuerliche Grundlagen
- `knowledge/checklisten.md` -- Belegpruefung, Jahresabschluss
- `skills/buchhaltung/datev-vorbereitung.md` -- Naechster Schritt: Buchungssaetze erstellen
- `skills/buchhaltung/anlage-v-assistent.md` -- Naechster Schritt: Anlage V vorausfuellen
- `skills/dokumente/dokument-klassifizierer.md` -- Dokumenttyp-Erkennung fuer unbekannte Belege
