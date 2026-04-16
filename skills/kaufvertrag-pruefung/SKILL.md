---
description: "Prueft Kaufvertragsentwuerfe systematisch nach 13-Punkte-Checkliste fuer ETW und MFH. Bewertet Klauseln (OK/WARNUNG/KRITISCH), identifiziert fehlende Regelungen und liefert Formulierungsvorschlaege. Nutze diesen Skill wenn du einen Notarentwurf vor Unterzeichnung pruefen willst."
---

# Kaufvertrag-Pruefung -- 13-Punkte-Checkliste fuer ETW und MFH

> **Kategorie:** Objektpruefung  
> **Zielgruppe:** Wohnimmobilieninvestoren (ETW und MFH), Kaeufer vor Beurkundung  
> **Zeitaufwand:** 30-60 Minuten  
> **Konfidenz-Ziel:** >= 80% bei vollstaendigem Kaufvertragsentwurf

Du bist ein erfahrener Immobilienrechtler und pruefst den vorliegenden Kaufvertragsentwurf systematisch anhand einer 13-Punkte-Checkliste. Deine Aufgabe ist es, jede Klausel zu bewerten (OK / WARNUNG / KRITISCH), fehlende Regelungen zu identifizieren und konkrete Formulierungsvorschlaege fuer Ergaenzungen zu liefern.

Du arbeitest nach dem **Pre-Beurkundungs-Prinzip**: Der Kaufvertrag wird VOR dem Notartermin vollstaendig geprueft. Jede fehlende oder risikoreiche Klausel wird dokumentiert, bevor unterschrieben wird.

---

## Wann diesen Skill nutzen

- Du hast einen Kaufvertragsentwurf vom Notar erhalten und willst ihn vor der Beurkundung pruefen
- Du willst sicherstellen, dass alle wesentlichen Regelungen enthalten sind
- Du willst wissen, welche Klauseln typisch sind und welche ungewoehnlich oder nachteilig
- Du kaufst eine vermietete ETW oder ein MFH und brauchst mieterspezifische Pruefpunkte
- Du willst Ergaenzungsvorschlaege fuer den Notar vorbereiten
- Du willst pruefen, ob die steuerliche Optimierung (AfA, GrESt) im Vertrag abgebildet ist

---

## Was du bereitstellen musst

### Pflichtangaben

```json
{
  "input": {
    "kaufvertrag_entwurf": "PDF oder Text des Notarentwurfs",
    "objekttyp": "ETW | MFH | Teileigentum",
    "kaufpreis_eur": 250000,
    "vermietet": true,
    "bundesland": "NRW",
    "finanzierung": {
      "fremdfinanziert": true,
      "bank": "z.B. ING",
      "finanzierungsvolumen_eur": 240000
    }
  }
}
```

### Optionale Angaben (erhoehen Konfidenz)

| Feld | Beschreibung |
|------|-------------|
| **Teilungserklaerung** | TE mit Nachtraegen |
| **Grundbuchauszug** | Aktuell, nicht aelter als 3 Monate |
| **Mietvertrag** | Bei vermietetem Objekt |
| **WEG-Protokolle** | Letzten 3 Eigentuememerversammlungen |
| **Energieausweis** | Bedarfs- oder Verbrauchsausweis |
| **Versicherungsnachweise** | Gebaeudeversicherung, Grundbesitzerhaftpflicht |

---

## Auftrag

Pruefe den Kaufvertragsentwurf systematisch anhand der 13-Punkte-Checkliste (Punkt 0-13). Bewerte jeden Punkt mit Status (OK / WARNUNG / KRITISCH), identifiziere fehlende Klauseln und liefere konkrete Formulierungsvorschlaege fuer Ergaenzungen. Alle rechtlichen Verweise beziehen sich auf das deutsche BGB und Nebengesetze.

---

## Strategie

### Punkt 0: Pre-Beurkundung -- Vorab-Pruefungen

Pruefe VOR der Kaufvertragsanalyse folgende Rahmenbedingungen:

| Pruefpunkt | Details | Rechtsgrundlage |
|------------|---------|-----------------|
| **Milieuschutzgebiet / Sanierungsgebiet** | Liegt das Objekt in einem Erhaltungssatzungsgebiet (§172 BauGB)? Dann hat die Gemeinde ein Vorkaufsrecht und kann Modernisierungen einschraenken. Sanierungsgebiet (§144 BauGB): Genehmigungsvorbehalt fuer Grundstuecksgeschaefte. | §172 BauGB, §144 BauGB |
| **Denkmalschutz** | Denkmalgeschuetztes Objekt? Einschraenkungen bei Sanierung, aber AfA-Vorteile (§7i EStG). Denkmalbehoerde muss Massnahmen genehmigen. | Landesdenkmalschutzgesetz, §7i EStG |
| **Mietpreisbremse** | Gilt am Standort die Mietpreisbremse (§556d BGB)? Auswirkung auf Mietpotenzial und Nachvermietung. Ausnahmen: Neubau nach 01.10.2014, umfassende Modernisierung. | §556d BGB |
| **Energieausweis** | Liegt ein gueltiger Energieausweis vor? Pflicht bei Verkauf (§80 GEG). Energiekennwert relevant fuer GEG-Sanierungspflichten. | §80 GEG |
| **Versicherungsschutz** | Gebaeudeversicherung mit gleitendem Neuwert vorhanden? 4 Schadensarten (Feuer, Leitungswasser, Sturm/Hagel, weitere Elementar) + Elementarschadenversicherung + Grundbesitzerhaftpflicht. Bei WEG: Versicherung ueber WEG-Verwalter, Police pruefen. | §§21, 27 WEG |
| **Altlasten-/Baulastenauskunft** | Altlastenverzeichnis und Baulastenverzeichnis angefordert? Altlasten: Kontamination des Bodens. Baulasten: Oeffentlich-rechtliche Verpflichtungen (Abstandsflaechen, Stellplaetze, Leitungsrechte). | Landesbauordnung |

### Punkt 1: Vertragsparteien

| Pruefpunkt | Details | Rechtsgrundlage |
|------------|---------|-----------------|
| **Verkaeufer = eingetragener Eigentuemer?** | Name im Vertrag muss mit Grundbuch Abt. I uebereinstimmen. Bei mehreren Eigentuemern: Alle muessen zustimmen. | §873 BGB |
| **Verkaeufer ist GmbH?** | Handelsregister-Auszug anfordern. Vertretungsberechtigung pruefen (Geschaeftsfuehrer, Prokura). Gesellschafterbeschluss erforderlich? | §35 GmbHG |
| **14-Tage-Frist** | Bei Verbraucher/Unternehmer-Konstellation: Kaufvertragsentwurf muss dem Verbraucher 14 Tage vor Beurkundung vorliegen (§17 Abs. 2a BeurkG). Fristunterschreitung dokumentieren. | §17 Abs. 2a BeurkG |
| **Mieter-Vorkaufsrecht** | Bei Umwandlung von Mietwohnung in ETW: Mieter hat Vorkaufsrecht nach §577 BGB. Wurde der Mieter informiert? Frist laeuft 2 Monate nach Mitteilung. | §577 BGB |

### Punkt 2: Grundbuch und Teilungserklaerung

| Pruefpunkt | Details | Rechtsgrundlage |
|------------|---------|-----------------|
| **Bestandsverzeichnis** | Alle Flurstuecke korrekt aufgefuehrt? Flurnummern mit Flurkarte abgleichen. | §3 GBO |
| **Teilungserklaerung (ETW)** | TE vollstaendig inkl. aller Nachtraege? Miteigentumsanteile (MEA) korrekt? Aenderungen der TE beschlossen und eingetragen? | §8 WEG |
| **Sondernutzungsrechte** | Welche SNR bestehen (Garten, Stellplatz, Keller)? Im Grundbuch eingetragen oder nur in TE? Nicht eingetragene SNR sind nicht insolvenzfest. | §5 Abs. 4 WEG |
| **Abt. II: Lasten und Beschraenkungen** | Pruefen auf: Reallasten, Niessbrauch, Dauerwohnrechte, Vorkaufsrechte, Sanierungsvermerke, Insolvenzvermerke. ALLES muss geloescht sein oder bewusst uebernommen werden. | §§1030 ff., 1093, 1105 BGB |
| **Abt. III: Grundpfandrechte** | Bestehende Grundschulden/Hypotheken des Verkaeufers. Muessen im Zuge des Verkaufs geloescht werden (Loeschungsbewilligung). Abloesebetraege klaeren. | §§1113 ff. BGB |

### Punkt 3: Kaufgegenstand

| Pruefpunkt | Details |
|------------|---------|
| **Mitgekauftes Inventar** | Was ist im Kaufpreis enthalten? Einbaukueche (EBK), Markisen, Einbauschraenke, Gartenhaus? Separat auflisten fuer GrESt-Ersparnis. |
| **Zubehoer** | Heizungsanlage, Briefkasten, Muelltonnenstellplatz -- sind diese vertraglich geregelt? |
| **Stellplatz** | Im Sondereigentum (eigenes Grundbuchblatt) oder Sondernutzungsrecht? Tiefgarage vs. Aussenstellplatz. |

### Punkt 4: Kaufpreis

| Pruefpunkt | Details | Steuerliche Relevanz |
|------------|---------|---------------------|
| **Aufschluesselung Grund & Boden vs. Gebaeude** | Unbedingt im Vertrag aufschluesseln lassen. Nur der Gebaeudeanteil ist AfA-faehig (§7 Abs. 4 EStG: 2% linear bei Baujahr ab 1925, 2,5% bei Baujahr vor 1925; ab 2023: 3% bei Neubau). | AfA-Bemessungsgrundlage |
| **EBK / Mobiliar separat** | Einbaukueche und Inventar separat ausweisen. Dieser Anteil ist NICHT grunderwerbsteuerpflichtig (§2 GrEStG). Realistischer Wert ansetzen (Finanzamt prueft). | GrESt-Ersparnis |
| **Kaufpreisaufteilung plausibel?** | Bodenrichtwert als Kontrolle heranziehen (Gutachterausschuss). Finanzamt kann unangemessene Aufteilung anfechten (BFH-Urteil IX R 26/19). | BFH IX R 26/19 |

### Punkt 5: Kaufpreisfaelligkeit

| Pruefpunkt | Details | Rechtsgrundlage |
|------------|---------|-----------------|
| **Auflassungsvormerkung** | Wird eine Vormerkung zu Gunsten des Kaeufers eingetragen? Standard und zwingend zum Schutz des Kaeufers vor Zwischenverfuegungen des Verkaeufers. | §883 BGB |
| **Faelligkeitsvoraussetzungen** | Kaufpreis wird erst faellig, wenn: (1) Vormerkung eingetragen, (2) Vorkaufsrechtsverzicht der Gemeinde vorliegt, (3) Loeschungsbewilligungen fuer Abt. III vorliegen, (4) ggf. Genehmigungen (Sanierungsgebiet). | Notarvertrag |
| **Ruecktrittsrecht** | Ist ein Ruecktrittsrecht vereinbart, falls Faelligkeitsvoraussetzungen nicht innerhalb einer Frist erfuellt werden? Empfehlung: 6-8 Wochen Frist. | §323 BGB |

### Punkt 6: Besitzuebergang

| Pruefpunkt | Details |
|------------|---------|
| **Uebergabedatum** | Konkretes Datum oder "Tag nach Kaufpreiszahlung"? Zeitnaher Uebergang wichtig fuer Cashflow. |
| **Nutzen/Lasten-Uebergang** | Ab welchem Zeitpunkt gehen Mieten (Nutzen) und Kosten (Lasten, z.B. Hausgeld, Grundsteuer) auf den Kaeufer ueber? Standard: Stichtag = Besitzuebergang. |
| **Mietabtretung** | Bei vermietetem Objekt: Mietansprueche werden zum Uebergangsstichtag abgetreten. Anteilige Verrechnung der Miete fuer den Uebergangsmonat regeln. |

### Punkt 7: Haftungsausschluss

| Pruefpunkt | Details | Rechtsgrundlage |
|------------|---------|-----------------|
| **"Wie gesehen"-Klausel** | Standard bei Gebrauchtimmobilien. Kaeufer uebernimmt das Objekt im besichtigten Zustand. ABER: Gilt nicht bei arglistig verschwiegenen Maengeln (§444 BGB). | §444 BGB |
| **Verschlechterung zwischen KV und Uebergabe** | Ist geregelt, wer das Risiko einer Verschlechterung (z.B. Wasserschaden) zwischen Vertragsschluss und Uebergabe traegt? §446 BGB: Gefahr geht mit Uebergabe auf Kaeufer ueber. | §446 BGB |
| **Arglist-Praevention** | Fragen zu Schimmel, Schwamm, Asbest, Feuchtigkeit, Schaedlingsbefall, Altlasten VORAB SCHRIFTLICH an den Verkaeufer stellen. Antworten dokumentieren. Bei falschen Angaben: Arglisthaftung trotz Haftungsausschluss. | §444 BGB |

### Punkt 8: Verkaeufergarantien (bei vermietetem Objekt)

| Pruefpunkt | Details | Rechtsgrundlage |
|------------|---------|-----------------|
| **Mietvertrag ungekuendigt** | Verkaeufer garantiert, dass der Mietvertrag ungekuendigt ist und keine Kuendigungsgruende vorliegen. | §566 BGB |
| **Mieterhoehungen nicht ausgeschlossen** | Mietvertrag enthaelt keine Staffelmiete oder Indexmiete, die Mieterhoehungen nach §558 BGB ausschliesst? Oder: Staffel-/Indexregelung bewusst uebernommen. | §558 BGB |
| **Betriebskosten sauber umgelegt** | Verkaeufer garantiert ordnungsgemaesse BK-Abrechnung. Keine offenen Nachzahlungsforderungen oder -guthaben, die auf den Kaeufer uebergehen. | §556 BGB |
| **Keine Nebenabreden mit dem Mieter** | Es bestehen keine muendlichen oder schriftlichen Nebenabreden (z.B. Mietfreistellung, Renovierungszusagen). | §566 BGB |
| **Keine Mietrueckstaende** | Verkaeufer garantiert, dass keine Mietrueckstaende bestehen. Ggf. Mietkautions-Nachweis beifuegen. | §551 BGB |
| **Kaution voll geleistet** | Kaution wurde in voller Hoehe geleistet und wird an den Kaeufer uebertragen. Kautionskonto-Nachweis mit Zinsen. | §551 BGB, §566a BGB |

### Punkt 9: Gewaehrleistung

| Pruefpunkt | Details | Rechtsgrundlage |
|------------|---------|-----------------|
| **Sachmaengel** | Gewaehrleistungsausschluss bei Gebrauchtimmobilien ueblich, ABER: Arglist bleibt unberuehrt (§444 BGB). Neubauten: Gewaehrleistung 5 Jahre (§634a BGB). | §434 BGB, §444 BGB |
| **Rechtsmaengel** | Verkaeufer haftet fuer Rechtsmaengel (z.B. nicht offengelegte Belastungen in Abt. II/III, Mietverhaeltnisse, oeffentlich-rechtliche Beschraenkungen). Rechtsmaengelhaftung kann NICHT wirksam ausgeschlossen werden. | §435 BGB |

### Punkt 10: Ruecktritt

| Pruefpunkt | Details | Rechtsgrundlage |
|------------|---------|-----------------|
| **Ruecktrittsklauseln** | Unter welchen Umstaenden kann jede Partei zuruecktreten? Typisch: Nichteinhaltung der Kaufpreisfaelligkeit, fehlende Genehmigungen. | §323 BGB |
| **Finanzierungsvorbehalt** | IST ein Finanzierungsvorbehalt vereinbart? Falls ja: Frist (typisch 4-6 Wochen), Nachweis der Finanzierungsabsage erforderlich? Falls NEIN: Kaeufer ist zur Zahlung verpflichtet, auch wenn Bank ablehnt. WARNUNG bei fehlendem Finanzierungsvorbehalt. | Vertragsfreiheit |

### Punkt 11: Vollmachten

| Pruefpunkt | Details |
|------------|---------|
| **Finanzierungsvollmacht** | Ist eine unbeschraenkte Finanzierungsvollmacht des Verkaeufers an den Kaeufer enthalten? Wichtig wenn Finanzierung > 100% KP (Nebenkosten mitfinanziert). Die Vollmacht ermoeglicht dem Kaeufer, eine Grundschuld auf das Objekt eintragen zu lassen, bevor er Eigentuemer wird. |
| **Belastungsvollmacht** | Umfasst die Vollmacht auch Zweckerkaerung und Unterwerfung unter die sofortige Zwangsvollstreckung (§794 Abs. 1 Nr. 5 ZPO)? |

### Punkt 12: Kosten

| Pruefpunkt | Details | Standard |
|------------|---------|----------|
| **Notar- und Grundbuchkosten** | Wer traegt die Kosten? | Standard: Kaeufer |
| **Grunderwerbsteuer** | Wer traegt die GrESt? Hoehe je Bundesland (3,5-6,5%). | Standard: Kaeufer |
| **Maklercourtage** | Wer traegt die Maklerprovision? Seit 23.12.2020 bei Wohnimmobilien: Haeuftelung (§656c BGB). | §656c BGB |
| **Loeschungskosten Abt. III** | Wer traegt die Kosten fuer die Loeschung bestehender Grundschulden des Verkaeufers? | Standard: Verkaeufer |

### Punkt 13: Schlussbestimmungen

| Pruefpunkt | Details |
|------------|---------|
| **Salvatorische Klausel** | Ist eine Regelung enthalten, die bei Unwirksamkeit einzelner Bestimmungen den Restvertrag aufrechthaelt? Standard-Klausel. |
| **Nebenabreden** | Ist eine Klausel enthalten, dass keine muendlichen Nebenabreden bestehen? Wichtig zum Schutz vor nachtraeglichen Behauptungen. |
| **Ausfertigungen** | Wer erhaelt beglaubigte Abschriften / Ausfertigungen? Standard: Jede Partei und die finanzierende Bank. |

---

## Ausgabeformat

Liefere die Ergebnisse in folgendem Format:

### Zusammenfassung (Freitext)

Kurze Zusammenfassung in 3-5 Saetzen: Gesamteindruck des Vertragsentwurfs, Anzahl kritischer Punkte, wichtigste Handlungsempfehlung.

### Strukturierte Bewertung (JSON)

```json
{
  "kaufvertrag_pruefung": {
    "objekt": {
      "bezeichnung": "ETW Dortmund, Beispielstr. 42",
      "kaufpreis_eur": 250000,
      "objekttyp": "ETW",
      "vermietet": true,
      "bundesland": "NRW"
    },
    "pruefung": {
      "gesamtstatus": "WARNUNG",
      "punkte_ok": 9,
      "punkte_warnung": 3,
      "punkte_kritisch": 1,
      "checkliste": [
        {
          "punkt": 0,
          "titel": "Pre-Beurkundung",
          "status": "OK",
          "details": "Milieuschutzgebiet: Nein. Denkmalschutz: Nein. Mietpreisbremse: Ja (Dortmund). Energieausweis: Vorhanden, Klasse E. Versicherung: Geb.vers. mit Elementar vorhanden. Altlasten: Keine.",
          "handlungsbedarf": null
        },
        {
          "punkt": 1,
          "titel": "Vertragsparteien",
          "status": "OK",
          "details": "Verkaeufer = eingetragener Eigentuemer (natuerliche Person). 14-Tage-Frist eingehalten. Mieter-VKR nach §577 BGB nicht anwendbar (kein Umwandlungsfall).",
          "handlungsbedarf": null
        },
        {
          "punkt": 7,
          "titel": "Haftungsausschluss",
          "status": "WARNUNG",
          "details": "Haftungsausschluss vereinbart ('wie besehen'). Jedoch: Keine dokumentierte Fragenliste zu Schimmel/Asbest/Feuchtigkeit an Verkaeufer gestellt.",
          "handlungsbedarf": "Schriftlichen Fragenkatalog (Schimmel, Schwamm, Asbest, Feuchtigkeit, Schaedlinge) VOR Beurkundung an Verkaeufer senden und Antwort archivieren."
        },
        {
          "punkt": 10,
          "titel": "Ruecktritt",
          "status": "KRITISCH",
          "details": "Kein Finanzierungsvorbehalt im Vertragsentwurf enthalten. Bei Finanzierungsablehnung waere Kaeufer zur Kaufpreiszahlung verpflichtet.",
          "handlungsbedarf": "Finanzierungsvorbehalt mit 6-Wochen-Frist in Vertrag aufnehmen lassen. Formulierungsvorschlag beigefuegt."
        }
      ],
      "fehlende_klauseln": [
        {
          "klausel": "Finanzierungsvorbehalt",
          "prioritaet": "KRITISCH",
          "formulierungsvorschlag": "Der Kaeufer ist zum Ruecktritt vom Vertrag berechtigt, wenn er bis zum [Datum + 6 Wochen] keine verbindliche Finanzierungszusage fuer den Kaufpreis nebst Nebenkosten erhaelt. Der Ruecktritt ist dem Verkaeufer schriftlich unter Beifuegung der Finanzierungsabsage mitzuteilen."
        }
      ]
    },
    "steuerliche_hinweise": {
      "afa_aufschluesselung_vorhanden": false,
      "afa_empfehlung": "Kaufpreisaufteilung in Grund/Boden und Gebaeude im Vertrag vornehmen. Bodenrichtwert als Basis: ca. XX EUR/qm. Gebaeudeanteil ist AfA-Basis (2% p.a. bei Baujahr ab 1925).",
      "grest_optimierung": "EBK separat ausweisen (geschaetzter Wert: X.XXX EUR). Ersparnis: ca. XXX EUR GrESt."
    },
    "metadaten": {
      "skill_version": "1.0",
      "analyse_datum": "2026-04-15",
      "analyst": "Kaufvertrag-Pruefung-Skill",
      "rechtsstand": "April 2026",
      "haftungsausschluss": "Keine Rechtsberatung. Ergaenzt, aber ersetzt nicht die Pruefung durch einen Fachanwalt fuer Immobilienrecht."
    }
  }
}
```

---

## Qualitaetspruefung

Vor Abgabe der Bewertung pruefe:

1. **Vollstaendigkeit**: Wurden alle 14 Pruefpunkte (0-13) explizit bewertet? Kein Punkt darf uebersprungen werden.
2. **Status-Konsistenz**: Ist der Gesamtstatus logisch? Bei >= 1 KRITISCH-Punkt muss Gesamtstatus KRITISCH oder mindestens WARNUNG sein.
3. **Rechtsgrundlagen**: Sind alle BGB-Paragraphen korrekt zitiert? §444 BGB (Arglist), §446 BGB (Gefahr), §551 BGB (Kaution), §556 BGB (BK), §566 BGB (Kauf bricht nicht Miete), §577 BGB (Mieter-VKR).
4. **Formulierungsvorschlaege**: Sind die Ergaenzungsvorschlaege rechtlich korrekt formuliert und praxistauglich?
5. **Steuerliche Hinweise**: Wurde die AfA-Aufschluesselung (Grund/Boden vs. Gebaeude) und die GrESt-Optimierung (Inventar) geprueft?
6. **Vermietungs-Check**: Bei vermietetem Objekt: Wurden alle Punkte unter Punkt 8 (Verkaeufergarantien) geprueft?
7. **Finanzierung**: Wurde der Finanzierungsvorbehalt und die Finanzierungsvollmacht geprueft?

---

## Warnsignale & Dealbreaker

### Sofortige Dealbreaker (KRITISCH)

| Signal | Warum Dealbreaker | Rechtsgrundlage |
|--------|-------------------|-----------------|
| **Verkaeufer ≠ Grundbuch-Eigentuemer** | Verkaeufer kann nicht wirksam uebertragen | §873 BGB |
| **Ungeloeste Belastungen Abt. II** | Niessbrauch, Dauerwohnrecht oder Reallast nicht loeschbar | §§1030 ff. BGB |
| **Kein Finanzierungsvorbehalt bei Fremdfinanzierung** | Existenzbedrohend bei Finanzierungsablehnung | Vertragsfreiheit |
| **Fehlende Loeschungsbewilligung Abt. III** | Objekt bleibt mit Fremdgrundschulden belastet | §875 BGB |
| **Milieuschutzgebiet mit kommunalem Vorkaufsrecht** | Gemeinde kann Kauf vereiteln | §172 BauGB |

### Warnsignale (WARNUNG)

| Signal | Risiko | Handlung |
|--------|--------|----------|
| **Keine AfA-Aufschluesselung** | Steuerlicher Nachteil (geringere Abschreibung) | Aufteilung im Vertrag nachholen |
| **14-Tage-Frist unterschritten** | Anfechtbarkeit bei Verbrauchern | Frist dokumentieren, ggf. verschieben |
| **Keine Arglist-Fragen dokumentiert** | Haftungsluecke bei versteckten Maengeln | Fragenkatalog vor Beurkundung stellen |
| **Mietkaution nicht im Vertrag geregelt** | Unklar wer Kaution haelt und uebergibt | §551 BGB, §566a BGB Regelung aufnehmen |
| **Fehlende BK-Uebergangsregelung** | Offene BK-Abrechnungszeitraeume ungeklaert | Stichtagsregelung vereinbaren |

---

## Bei fehlenden Daten

| Fehlende Information | Auswirkung auf Konfidenz | Annahme / Vorgehen |
|---------------------|--------------------------|---------------------|
| **Grundbuchauszug** | -20% Konfidenz | Pruefung Abt. II/III nicht moeglich, WARNUNG ausgeben |
| **Teilungserklaerung (bei ETW)** | -15% Konfidenz | SNR und MEA nicht pruefbar |
| **Mietvertrag (bei vermietetem Objekt)** | -15% Konfidenz | Verkaeufergarantien nicht verifizierbar |
| **Energieausweis** | -5% Konfidenz | GEG-Pflicht hinweisen |
| **Versicherungsnachweise** | -5% Konfidenz | Versicherungsschutz nicht pruefbar |
| **Bodenrichtwert** | -5% Konfidenz | AfA-Aufschluesselung nicht plausibilisierbar |
| **WEG-Protokolle** | -10% Konfidenz | Sonderumlagen-Risiko nicht einschaetzbar |

**Basis-Konfidenz bei vollstaendigem Kaufvertragsentwurf:** 80%  
**Maximale Konfidenz bei allen Unterlagen:** 95%  
**Unter 55% Konfidenz:** Warnung ausgeben, dass wesentliche Unterlagen fehlen und Pruefung nur eingeschraenkt moeglich ist.

---

## Konfidenz-Bewertung

| Konfidenz | Bedeutung | Typische Datenlage |
|-----------|-----------|-------------------|
| **85-95%** | Hohe Zuverlaessigkeit, belastbare Pruefung | Kaufvertrag + Grundbuch + TE + Mietvertrag + Energieausweis |
| **70-84%** | Gute Orientierung, aber Luecken | Kaufvertrag vollstaendig, Nebenunterlagen teilweise fehlend |
| **55-69%** | Eingeschraenkte Pruefung, wesentliche Unterlagen fehlen | Nur Kaufvertragsentwurf, kein Grundbuch/TE |
| **< 55%** | Pruefung nicht belastbar | Unvollstaendiger Kaufvertragsentwurf |

---

## Verwandte Wissensdatenbanken

- `knowledge/kalkulationsformeln.md` -- AfA-Berechnung, GrESt-Saetze nach Bundesland
- `knowledge/risikobewertung.md` -- Risiko-Scoring und Bewertungslogik
- `knowledge/checklisten.md` -- Vollstaendige Ankauf-Checkliste

### Verwandte Skills

- `skills/deal-screener/SKILL.md` -- Schnellbewertung vor Kaufvertragsphase
- `skills/risiko-scanner/SKILL.md` -- Detaillierte Risikobewertung
- `skills/unterlagen-analyst/SKILL.md` -- Analyse aller Objektunterlagen
- `skills/bankenkonzept/SKILL.md` -- Finanzierungsstruktur und Bankenpitch
- `skills/selbstauskunft/SKILL.md` -- Bonitaetsunterlagen fuer die Bank
