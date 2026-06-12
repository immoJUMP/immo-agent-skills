---
name: beleg-sortierer
description: "Klassifiziert und sortiert Belege fuer Wohnimmobilien-Portfolios. Unterscheidet Erhaltungsaufwand vs. Herstellungskosten, ordnet Kostenarten zu und erstellt ein sauberes Paket fuer den Steuerberater. Nutze diesen Skill wenn du unsortierte Belege hast oder Handwerkerrechnungen klassifizieren willst."
---

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

**Wichtig:** Der Nutzer ist Immobilieninvestor, kein IT-ler. Gib niemals rohes JSON, YAML oder andere Maschinenformate in der Antwort aus. Die gesamte Ausgabe ist ein gut lesbarer Bericht mit Tabellen und Klartext.

**Im Chat:** der unten gezeigte Markdown-Bericht (Beleguebersicht).
**Als Datei:** maschinenlesbare Daten fuer die Weiterverarbeitung (z.B. CSV-Belegliste fuer den Steuerberater oder den DATEV-Vorbereitungs-Skill) schreibst du in eine Datei und bietest sie an -- niemals als Rohdaten in den Chat.

### Zusammenfassung (Freitext)

2-4 Saetze: Wie viele Belege verarbeitet, Gesamtsumme, wichtigste Auffaelligkeiten, was der Steuerberater noch klaeren muss.

### Beleguebersicht (Bericht)

```markdown
# Beleg-Sortierung: Steuerjahr 2025

**Verarbeitet am:** 15.11.2025 | **47 Belege** | **Gesamtsumme brutto: 34.250,00 EUR**

## Belegliste

| Nr. | Datum | Beleg | Aussteller | Objekt | Brutto | Steuerliche Einordnung | Anlage V | Status |
|-----|-------|-------|------------|--------|--------|------------------------|----------|--------|
| BEL-2025-001 | 15.03.2025 | Handwerkerrechnung (Sanitaer), RE-2025-0734 | Mueller Sanitaer GmbH | Musterstr. 12, Duesseldorf, WE 3 | 2.450,00 EUR | Erhaltungsaufwand (sofort absetzbar) | Zeile 39 | 🟢 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |

## Beleg im Detail: BEL-2025-001

| | |
|---|---|
| Empfohlener Dateiname | 2025-03-15_Handwerkerrechnung_2450EUR |
| Originaldatei | scan_0042.pdf |
| Belegtyp | Handwerkerrechnung (Sanitaer) |
| Rechnungsdatum / -nummer | 15.03.2025 / RE-2025-0734 |
| Aussteller | Mueller Sanitaer GmbH (USt-ID DE123456789) |
| Leistung | Austausch defekter Mischbatterie Kueche, WE 3 |
| Leistungszeitraum | 10.03.2025 - 15.03.2025 |
| Betraege | Netto 2.058,82 EUR + 19% USt 391,18 EUR = Brutto 2.450,00 EUR |
| Objekt-Zuordnung | Musterstrasse 12, 40210 Duesseldorf, WE 3 (Konfidenz 95% -- Adresse und Einheit auf Rechnung genannt) |
| Steuerliche Einordnung | **Erhaltungsaufwand**, sofort absetzbar -- Austausch defekter Armatur = Reparatur, keine Verbesserung ueber urspruenglichen Zustand |
| Anlage V | Zeile 39 (Erhaltungsaufwand) |
| 15%-Grenze (anschaffungsnah) | Relevant (Anschaffung vor 2 Jahren). Kumuliert 8,5% von 15% -- 🟢 unter Grenze, Restbudget 9.750,00 EUR |
| Auffaelligkeiten | Keine |
| Konfidenz | 92% |

(Gleiche Detailstruktur fuer alle weiteren Belege; bei vielen Belegen Details nur fuer
Belege mit Auffaelligkeiten oder unklarer Zuordnung ausschreiben.)

## Summen nach Kategorie

| Kategorie | Anzahl | Summe brutto |
|-----------|--------|--------------|
| Erhaltungsaufwand | 12 | 15.400,00 EUR |
| Herstellungskosten | 2 | 8.500,00 EUR |
| Schuldzinsen | 1 | 4.200,00 EUR |
| Grundsteuer | 2 | 1.780,00 EUR |
| Versicherungen | 4 | 1.920,00 EUR |
| Verwaltungskosten | 6 | 2.450,00 EUR |

## Summen nach Objekt

| Objekt | Belege | Summe brutto |
|--------|--------|--------------|
| Musterstrasse 12, 40210 Duesseldorf | 28 | 22.100,00 EUR |
| Beispielweg 5, 50667 Koeln | 19 | 12.150,00 EUR |

## Zu klaerende Belege

| Beleg | Problem | Schwere | Hinweis |
|-------|---------|---------|---------|
| BEL-2025-023 | Adress-Abweichung | 🔴 hoch | Adresse auf Rechnung stimmt mit keinem Objekt ueberein |
| BEL-2025-031 | Duplikat-Verdacht | 🟡 mittel | Gleiche Rechnungsnummer wie BEL-2025-018 |
| BEL-2025-045 | Ungewoehnlich hoher Betrag | 🟡 mittel | Betrag 12.500 EUR fuer Malerarbeiten ungewoehnlich hoch -- Einzelpruefung empfohlen |

## Datei fuer den Steuerberater

Belegliste als CSV geschrieben: `beleg-sortierung_2025.csv` (alle Belege mit saemtlichen Feldern, maschinenlesbar fuer die Weiterverarbeitung)
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
- `skills/datev-vorbereitung/SKILL.md` -- Naechster Schritt: Buchungssaetze erstellen

- `skills/dokument-klassifizierer/SKILL.md` -- Dokumenttyp-Erkennung fuer unbekannte Belege
