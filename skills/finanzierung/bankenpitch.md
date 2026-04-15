# Bankenpitch -- Vollstaendige 13-Sektionen-Bankenpraesentation fuer Wohnimmobilien-Investoren

Erstellt eine vollstaendige, professionelle Bankenpraesentation in 13 Sektionen, die auf der Analyse von 4 realen Praesentationsformaten basiert (Gamma PDF, 2 interaktive HTML-Praesentationen, 2 PDF-Projektvorstellungen). Das Ergebnis ist ein bankenfertiges Dokument, das der Firmenkundenberater ohne Rueckfragen intern an Marktfolge und Kreditausschuss weiterreichen kann.

> **Praxis-Insight:** Ein Investor hat mit einer strukturierten Bankenpraesentation zwei 1-Mio-Euro-Deals mit NULL Eigenkapital finanziert bekommen. Der Banker sagte: "Er hat sich wirklich Gedanken gemacht." Die Praesentation zeigte klar den Pfad: Ist-Mieten -> organische Mieterhoehung -> Modernisierung -> tilgungsfrei Jahr 1 -> Cashflow-positiv ab Jahr 2. Die Bank konnte das Konzept intern ohne Rueckfragen vorlegen. Der Schluessel: Die Eigenleistungen des Investors (Neuvermietung, Mietverhandlungen, Projektmanagement Sanierung, Foerderkoordination) wurden marktueblich bewertet und als EK-Ersatz dargestellt -- Block 1 (Barmittel fuer KNK) plus Block 2 (bewertete Eigenleistungen) ergaben eine EK-Quote von ueber 15%, obwohl kein einziger Euro in Cash eingebracht wurde.

> **Ausgabeformate:** Das Ergebnis kann verwendet werden als: (a) Markdown-Dokument zur direkten Nutzung, (b) Input fuer Gamma.app zur Erzeugung einer designten PDF-Praesentation, (c) Input fuer Claude Code zur Erzeugung einer interaktiven HTML-Praesentation mit Slidern und DSCR-Matrix.

---

## Wann diesen Skill nutzen

- Du hast das Bankenkonzept und Cashflow-Modell bereits erstellt und willst ein vollstaendiges Praesentationsdokument fuer den Banktermin
- Du bereitest einen Ersttermin oder Zweitgespraech mit dem Firmenkundenberater vor
- Du willst dem Banker ein Dokument geben, das er intern (Marktfolge, Kreditausschuss) ohne Rueckfragen weiterreichen kann
- Du willst dich mit einer professionellen 13-Sektionen-Praesentation von anderen Finanzierungsanfragen abheben
- Du argumentierst eine 100%-Finanzierung oder ueberdurchschnittlichen Beleihungsauslauf mit Eigenleistungen als EK-Ersatz
- Du brauchst eine Praesentation, die DSCR-Bedienbarkeit in JEDER Phase nachweist

---

## Was du bereitstellen musst

```json
{
  "investor": {
    "name": "Max Mustermann",
    "company": "Mustermann Immobilien GmbH",
    "role": "Geschaeftsfuehrer",
    "description": "Bestandshalter mit Fokus auf Value-Add-Wohnimmobilien in Ostdeutschland",
    "contact": {
      "phone": "+49 170 1234567",
      "email": "max@mustermann-immo.de",
      "address": "Musterstrasse 1, 03046 Cottbus"
    },
    "portfolio_kpis": {
      "units_total": 42,
      "experience_years": 6,
      "bestandsrendite_pct": 8.2,
      "leerstand_pct": 2.1
    },
    "werdegang_timeline": [
      { "year": 2019, "milestone": "Erste ETW als Kapitalanlage erworben" },
      { "year": 2020, "milestone": "Erstes MFH (6 WE) -- Cottbus" },
      { "year": 2021, "milestone": "Gruendung Mustermann Immobilien GmbH" },
      { "year": 2022, "milestone": "Zwei MFH-Paketkaeufe (18 WE) -- 100% finanziert" },
      { "year": 2023, "milestone": "Portfolio auf 35 WE ausgebaut" },
      { "year": 2024, "milestone": "42 WE, erste KfW-Sanierung abgeschlossen" }
    ],
    "trackrecord_highlight": {
      "property_name": "KM 59/60, Cottbus",
      "jnkm_increase_pct": 95,
      "dscr": 3.20,
      "ltv_pct": 51.7,
      "leerstand_pct": 0
    },
    "stille_reserven": {
      "freie_grundschulden_eur": 120000,
      "description": "Freie Grundschulden aus getilgten Bestandsdarlehen, nachrangig beleihbar"
    }
  },
  "property": {
    "address": "Beispielstrasse 10-12, 03046 Cottbus",
    "city": "Cottbus",
    "bundesland": "Brandenburg",
    "type": "Mehrfamilienhaus / Wohn- und Geschaeftshaus",
    "year_built": 1936,
    "energy_class": "H",
    "units_residential": 10,
    "units_commercial": 2,
    "total_sqm": 904,
    "plot_size_sqm": 1250,
    "parking_spaces": 6,
    "heating_type": "Gas-Zentralheizung",
    "basement": true,
    "grundbuch_clean": true,
    "photos": ["front_view.jpg", "rear_view.jpg"],
    "strategy": "Value-Add: Leerstandsabbau + Mieterhoehung + selektive Modernisierung"
  },
  "darlehensnehmer": {
    "gesellschaft": "Mustermann Immobilien GmbH",
    "gesellschafter": "Max Mustermann (100%)",
    "geschaeftsfuehrer": "Max Mustermann",
    "sitz": "Cottbus"
  },
  "rent_roll": {
    "market_rent_per_sqm": 7.50,
    "units": [
      {
        "unit_id": "WE 01",
        "type": "Wohnung",
        "sqm": 65.0,
        "rent_ist_monthly": 325.00,
        "rent_soll_monthly": 455.00,
        "tenant": "Mueller, A.",
        "lease_start": "2018-03-01"
      },
      {
        "unit_id": "WE 02",
        "type": "Wohnung",
        "sqm": 78.0,
        "rent_ist_monthly": 390.00,
        "rent_soll_monthly": 546.00,
        "tenant": "Schmidt, B.",
        "lease_start": "2020-07-01"
      },
      {
        "unit_id": "GE 01",
        "type": "Gewerbe",
        "sqm": 120.0,
        "rent_ist_monthly": 600.00,
        "rent_soll_monthly": 840.00,
        "tenant": "Leer",
        "lease_start": null
      }
    ],
    "buildings": [
      {
        "name": "Haus 10",
        "units_residential": 5,
        "units_commercial": 1,
        "rent_ist_monthly": 2100,
        "rent_sofort_monthly": 2520,
        "rent_soll1_monthly": 3150,
        "rent_soll2_monthly": 3400,
        "rent_soll3_monthly": 3600
      },
      {
        "name": "Haus 12",
        "units_residential": 5,
        "units_commercial": 1,
        "rent_ist_monthly": 1900,
        "rent_sofort_monthly": 2280,
        "rent_soll1_monthly": 2850,
        "rent_soll2_monthly": 3100,
        "rent_soll3_monthly": 3300
      }
    ],
    "summary": {
      "jnkm_ist": 48000,
      "jnkm_sofort": 57600,
      "jnkm_soll1": 72000,
      "jnkm_soll2": 78000,
      "jnkm_soll3": 82800,
      "avg_ist_per_sqm": 4.42,
      "avg_soll1_per_sqm": 6.64
    }
  },
  "investment_strategy": {
    "development_path": [
      {
        "stage": "IST",
        "jnkm": 48000,
        "delta": null,
        "rendite_pct": 5.8,
        "dscr": 1.15,
        "description": "Aktuelle Situation bei Uebernahme"
      },
      {
        "stage": "SOFORT",
        "jnkm": 57600,
        "delta": "+9.600",
        "rendite_pct": 7.0,
        "dscr": 1.38,
        "description": "Leerstand beseitigen, Neuvermietung zu Marktniveau"
      },
      {
        "stage": "SOLL 1",
        "jnkm": 72000,
        "delta": "+14.400",
        "rendite_pct": 8.7,
        "dscr": 1.50,
        "description": "Mieterhoehung Bestand (Sec. 558 + Sec. 559 BGB)"
      },
      {
        "stage": "SOLL 2",
        "jnkm": 78000,
        "delta": "+6.000",
        "rendite_pct": 9.5,
        "dscr": 1.63,
        "description": "Gewerbe-Neuvermietung + weitere Mietanpassung"
      },
      {
        "stage": "SOLL 3",
        "jnkm": 82800,
        "delta": "+4.800",
        "rendite_pct": 10.0,
        "dscr": 1.72,
        "description": "Vollstabilisierung nach Sanierung"
      }
    ],
    "sanierungsaufstellung": [
      { "massnahme": "Fenstertausch (10 WE)", "kosten": 35000, "programm": "KfW 261/262" },
      { "massnahme": "Heizungsoptimierung", "kosten": 12000, "programm": "BAFA BEG EM" },
      { "massnahme": "Treppenhaussanierung", "kosten": 8000, "programm": null },
      { "massnahme": "Badsanierung (3 WE bei MW)", "kosten": 15000, "programm": null },
      { "massnahme": "Elektrik-Ertuechtigung", "kosten": 10000, "programm": null },
      { "massnahme": "Fassade (Teilbereich)", "kosten": 20000, "programm": "KfW 261" }
    ],
    "sanierung_total": 100000,
    "kfw_tilgungszuschuss": 15000,
    "zeitstrahl": [
      { "zeitpunkt": "Sofort (Monat 1-3)", "meilenstein": "Leerstandsabbau + Neuvermietung", "wirkung": "JNKM +9.600 EUR, DSCR steigt auf 1,38" },
      { "zeitpunkt": "Monat 4-12", "meilenstein": "Organische Mieterhoehung (Sec. 558 BGB)", "wirkung": "Bestandsmieten +15-20% bei Mietspiegelberechtigung" },
      { "zeitpunkt": "Jahr 2", "meilenstein": "Modernisierung + Sec. 559 Umlage", "wirkung": "JNKM auf 72.000 EUR, DSCR 1,50" },
      { "zeitpunkt": "Jahr 3-4", "meilenstein": "Gewerbe-Neuvermietung + Stabilisierung", "wirkung": "JNKM auf 78.000 EUR" },
      { "zeitpunkt": "Jahr 5+", "meilenstein": "Vollstabilisierung", "wirkung": "JNKM 82.800 EUR, DSCR 1,72, Option Nachbeleihung" },
      { "zeitpunkt": "Jahr 6+", "meilenstein": "Exit-Optionen pruefen", "wirkung": "WEG-Aufteilung oder Portfolioverkauf moeglich" }
    ],
    "investitionslogik": "Erwerb eines unterbewerteten Wohn- und Geschaeftshauses mit 20% Leerstand und 35% Mietanpassungspotenzial. Die Strategie kombiniert sofortige Leerstandsbeseitigung (DSCR-Sprung auf 1,38), organische Mieterhoehung im Bestand und selektive KfW-foerderfaehige Modernisierung. Der Kapitaldienst wird in JEDER Phase aus dem Objekt bedient. Die tilgungsfreie Anlaufphase von 24 Monaten ermoeglicht die Umsetzung ohne zusaetzlichen Liquiditaetsbedarf."
  },
  "financing": {
    "purchase_price": 520000,
    "knk": {
      "grest_pct": 6.5,
      "grest_eur": 33800,
      "notar_gericht_pct": 2.0,
      "notar_gericht_eur": 10400,
      "makler_pct": 3.57,
      "makler_eur": 18564
    },
    "knk_total": 62764,
    "sanierung_total": 100000,
    "eigenleistungen_value": 45000,
    "gik_total": 727764,
    "bank_loan": {
      "amount": 620000,
      "interest_rate_pct": 3.90,
      "repayment_rate_pct": 2.00,
      "tilgungsfrei_months": 24,
      "fixed_rate_years": 10,
      "sondertilgung_pct": 5
    },
    "kfw": {
      "program": "KfW 261",
      "amount": 60000,
      "interest_rate_pct": 1.25,
      "repayment_start_month": 36,
      "tilgungszuschuss_eur": 15000
    },
    "eigenkapital": {
      "barmittel_knk": 47764,
      "eigenleistungen_block2": 45000,
      "eigenleistungen_detail": [
        { "leistung": "Neuvermietung Leerstand (3 WE)", "marktpreis_eur": 8000 },
        { "leistung": "Mieterhoehungsgespraeche + Durchsetzung", "marktpreis_eur": 6000 },
        { "leistung": "Gewerbe-Akquise + Verhandlung", "marktpreis_eur": 5000 },
        { "leistung": "Projektmanagement Sanierung", "marktpreis_eur": 12000 },
        { "leistung": "Objektueberwachung + Baubegleitung", "marktpreis_eur": 6000 },
        { "leistung": "KfW-/BAFA-Foerderkoordination", "marktpreis_eur": 4000 },
        { "leistung": "WEG-Aufteilungsvorbereitung", "marktpreis_eur": 4000 }
      ],
      "ek_quote_pct": 12.7
    }
  },
  "ertragswert_ltv": {
    "jnkm_soll_basis": 72000,
    "factors": [15, 16, 17, 18],
    "beleihungswert_pct": 70,
    "results": [
      { "factor": 15, "ertragswert": 1080000, "bw_70pct": 756000, "ltv_bank_pct": 82.0 },
      { "factor": 16, "ertragswert": 1152000, "bw_70pct": 806400, "ltv_bank_pct": 76.9 },
      { "factor": 17, "ertragswert": 1224000, "bw_70pct": 856800, "ltv_bank_pct": 72.4 },
      { "factor": 18, "ertragswert": 1296000, "bw_70pct": 907200, "ltv_bank_pct": 68.3 }
    ]
  },
  "cashflow_interactive": {
    "slider_defaults": {
      "avg_rent_per_sqm": { "default": 6.64, "min": 4.00, "max": 9.00 },
      "leerstand_pct": { "default": 5, "min": 0, "max": 20 },
      "bewirtschaftung_pct": { "default": 25, "min": 15, "max": 35 },
      "zinssatz_pct": { "default": 3.90, "min": 2.00, "max": 8.00 },
      "tilgung_pct": { "default": 2.00, "min": 0, "max": 5.00 }
    }
  },
  "phasen_cashflow": [
    {
      "phase": 1,
      "name": "IST (tilgungsfrei)",
      "zeitraum": "Monat 1-24",
      "jnkm": 57600,
      "kd_monthly": 2015,
      "dscr": 2.38,
      "cf_monthly": 795
    },
    {
      "phase": 2,
      "name": "Sec. 559 + Bank tilgt",
      "zeitraum": "Monat 25-36",
      "jnkm": 72000,
      "kd_monthly": 4664,
      "dscr": 1.29,
      "cf_monthly": 1336
    },
    {
      "phase": 3,
      "name": "Sec. 558 + KfW tilgt",
      "zeitraum": "Monat 37-48",
      "jnkm": 72000,
      "kd_monthly": 4726,
      "dscr": 1.27,
      "cf_monthly": 1274
    },
    {
      "phase": 4,
      "name": "SOLL 2",
      "zeitraum": "Monat 49-72",
      "jnkm": 78000,
      "kd_monthly": 4726,
      "dscr": 1.38,
      "cf_monthly": 1774
    },
    {
      "phase": 5,
      "name": "SOLL 3 (stabilisiert)",
      "zeitraum": "Ab Monat 73",
      "jnkm": 82800,
      "kd_monthly": 4726,
      "dscr": 1.46,
      "cf_monthly": 2174
    }
  ],
  "sensitivity": {
    "rent_steps_per_sqm": [4.00, 4.50, 5.00, 5.50, 6.00, 6.50, 7.00, 7.50],
    "interest_rate_steps_pct": [3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0],
    "ist_rent_per_sqm": 4.42,
    "dscr_matrix_note": "Gruen >= 1,20 (komfortabel) | Gelb 1,00-1,20 (bedienbar) | Rot < 1,00 (unterdeckt)"
  },
  "scenarios": {
    "conservative": {
      "label": "Konservativ",
      "avg_rent_per_sqm": 5.50,
      "leerstand_pct": 10,
      "bewirtschaftung_pct": 30,
      "brutto_pa": 59664,
      "netto_pa": 37688,
      "kd_pa": 55968,
      "cf_vst": -18280,
      "dscr": 0.67,
      "rendite_gk_pct": 5.54
    },
    "basis": {
      "label": "Basis (empfohlen)",
      "avg_rent_per_sqm": 6.64,
      "leerstand_pct": 5,
      "bewirtschaftung_pct": 25,
      "brutto_pa": 72000,
      "netto_pa": 51300,
      "kd_pa": 55968,
      "cf_vst": -4668,
      "dscr": 0.92,
      "rendite_gk_pct": 7.55
    },
    "optimistic": {
      "label": "Optimistisch",
      "avg_rent_per_sqm": 7.50,
      "leerstand_pct": 3,
      "bewirtschaftung_pct": 22,
      "brutto_pa": 81360,
      "netto_pa": 60869,
      "kd_pa": 55968,
      "cf_vst": 4901,
      "dscr": 1.09,
      "rendite_gk_pct": 8.96
    }
  },
  "risks_and_exit": {
    "risk_matrix": [
      {
        "risk": "Mieterhoehungen nicht durchsetzbar",
        "probability": "Niedrig",
        "mitigation": "Mietspiegel-gestuetzte Begruendung, konservatives Szenario zeigt Bedienbarkeit auch bei 60% der geplanten Erhoehungen"
      },
      {
        "risk": "Leerstand steigt dauerhaft ueber 10%",
        "probability": "Niedrig",
        "mitigation": "Marktleerstand unter 4%, attraktive Mikrolage, Mietausfallversicherung vorhanden"
      },
      {
        "risk": "Sanierungskosten uebersteigen Budget",
        "probability": "Mittel",
        "mitigation": "20% Puffer eingeplant, Handwerkerangebote fuer Hauptpositionen vorliegend, KfW-Foerderung als zusaetzlicher Puffer"
      },
      {
        "risk": "Zinsanstieg nach Zinsbindung",
        "probability": "Mittel",
        "mitigation": "10 Jahre Zinsbindung, Sondertilgungen reduzieren Restschuld, DSCR-Matrix zeigt Bedienbarkeit bis 6% Zins"
      },
      {
        "risk": "Regulatorische Aenderungen",
        "probability": "Niedrig",
        "mitigation": "Konservative Kalkulation ohne Ausreizung der Mietgrenzen, energetische Massnahmen im Sanierungsplan"
      }
    ],
    "exit_options": [
      {
        "option": "Bestandshaltung",
        "zeitpunkt": "Dauerhaft",
        "wirkung": "DSCR 1,72 bei SOLL 3, CF +2.174 EUR/Mo, kontinuierlicher Vermoegensaufbau durch Tilgung"
      },
      {
        "option": "Nachbeleihung / Kapitalrotation",
        "zeitpunkt": "Ab Jahr 5",
        "wirkung": "Ertragswert 1,3 Mio EUR -> freier Beleihungsraum ca. 200.000 EUR fuer naechsten Deal"
      },
      {
        "option": "Grundstuecksentwicklung (Hinterland)",
        "zeitpunkt": "Ab Jahr 3",
        "wirkung": "1.250 qm Grundstueck, 800 qm bebaut -> 450 qm Bauerwartungsland, Potenzial fuer 4-6 Stellplaetze oder Tiny-Houses"
      },
      {
        "option": "WEG-Aufteilung + Einzelverkauf",
        "zeitpunkt": "Ab Jahr 5",
        "wirkung": "12 Einheiten x Ø 85.000 EUR = 1.020.000 EUR Erloes vs. 520.000 EUR Kaufpreis -> Potenzial ca. 500.000 EUR stille Reserve"
      },
      {
        "option": "Portfolioverkauf (en bloc)",
        "zeitpunkt": "Ab Jahr 5",
        "wirkung": "Faktor 17-18 auf JNKM SOLL 3 (82.800 EUR) = 1,4 - 1,5 Mio EUR Verkaufserloes"
      }
    ],
    "stille_reserven_text": "Neben den freien Grundschulden aus dem Bestandsportfolio (120.000 EUR) bietet das Grundstueck mit 450 qm unbebautem Hinterland zusaetzliches Entwicklungspotenzial. Bei konservativer Bewertung (Faktor 17 auf JNKM SOLL 1) ergibt sich ein Ertragswert von 1,22 Mio EUR -- der Kaufpreis inklusive Sanierung liegt bei 620.000 EUR. Die stille Reserve betraegt somit ca. 600.000 EUR."
  },
  "bank_decision": {
    "wir_bieten": [
      "EK-Quote 12,7% (Barmittel + bewertete Eigenleistungen)",
      "Grundschuld 1. Rang auf das Objekt",
      "DSCR >= 1,27 in ALLEN Phasen (kein kritisches Fenster)",
      "LTV Bank unter 80% ab Faktor 16",
      "Voll vermietetes Objekt nach Leerstandsabbau (Monat 3)",
      "Nachgewiesener Trackrecord mit vergleichbarem Objekt (JNKM +95%)"
    ],
    "wir_wuenschen": {
      "darlehensart": "Annuitaetendarlehen mit tilgungsfreier Anlaufphase",
      "bankdarlehen": {
        "betrag": 620000,
        "zins_pct": 3.90,
        "tilgung_pct": 2.00,
        "laufzeit_jahre": 10,
        "tilgungsfrei_monate": 24
      },
      "kfw": {
        "programm": "KfW 261",
        "betrag": 60000,
        "zins_pct": 1.25,
        "tilgungszuschuss": 15000
      },
      "sondertilgung": "Bis 5% p.a. ohne Vorfaelligkeitsentschaedigung",
      "sicherheit": "Grundschuld 1. Rang auf Kaufobjekt, ggf. nachrangige Grundschuld auf Bestandsobjekt",
      "auszahlungsvoraussetzung": "Kaufvertrag, Grundschuldbestellung, Eigentumsumschreibung",
      "anschlussfinanzierung": "Praeferred Partner bei gleicher Bank nach Zinsbindungsende"
    },
    "zusammenfassung": "Wir bieten der Bank ein durchgerechnetes Value-Add-Projekt mit nachgewiesenem Trackrecord, Cashflow-Bedienbarkeit in jeder Phase und konservativer LTV-Abdeckung. Der Investor bringt Eigenleistungen im Wert von 45.000 EUR ein, die marktueblich bewertet sind und den Projekterfolg sicherstellen. Die Kombination aus sofortiger Leerstandsbeseitigung, organischer Mieterhoehung und KfW-gefoerderter Modernisierung schafft einen klaren, nachvollziehbaren Pfad zur Vollstabilisierung."
  },
  "reference_properties": [
    {
      "address": "KM 59/60, Cottbus",
      "type": "MFH",
      "units": 8,
      "purchase_price_eur": 380000,
      "current_jnkm": 45600,
      "jnkm_increase_pct": 95,
      "dscr": 3.20,
      "ltv_pct": 51.7,
      "leerstand_pct": 0,
      "note": "Vergleichsobjekt im Eigenbestand -- Strategie identisch, bereits erfolgreich umgesetzt"
    }
  ],
  "documents_available": [
    "Maklerexpose",
    "Mieterliste (aktuell)",
    "Lageplan / Katasterauszug",
    "Bestandsuebersicht Portfolio",
    "Trackrecord Vergleichsobjekt",
    "Selbstauskunft Investor",
    "Grundbuchauszug"
  ]
}
```

---

## Auftrag

Erstelle eine vollstaendige Bankenpraesentation in 13 Sektionen, die:

1. **In der Executive Summary das Projekt auf einen Blick zusammenfasst** -- mit 5 KPI-Boxen, Kern-Argumenten und Investitionslogik
2. **Den Investor als erfahrenen, systematischen Bestandshalter positioniert** -- mit Portfolio-KPIs, Trackrecord und stillen Reserven
3. **Das Objekt mit allen technischen und wirtschaftlichen Parametern vorstellt** -- inkl. Darlehensnehmer-Struktur
4. **Die Investmentstrategie als 5-Stufen-Entwicklungspfad visualisiert** -- IST -> SOFORT -> SOLL 1 -> SOLL 2 -> SOLL 3 mit DSCR-Trajektorie
5. **Den Wohnungsmix und die Mietentwicklung pro Einheit und Gebaeude detailliert** -- mit Marktvergleich
6. **Die Finanzierungsstruktur mit Eigenleistungen als EK-Ersatz darstellt** -- Block 1 + Block 2 Konzept
7. **Einen interaktiven Cashflow-Rechner mit 5 Stellschrauben bietet** -- mit Live-Berechnung
8. **Die Phasen-Cashflows mit DSCR pro Phase nachweist** -- "Kein kritisches Fenster"
9. **Eine DSCR-Sensitivitaetsmatrix mit Farbcodierung liefert** -- Gruen/Gelb/Rot
10. **Drei Szenarien nebeneinander vergleicht** -- Konservativ, Basis, Optimistisch
11. **Risiken proaktiv adressiert und Exit-Optionen mit Zahlen belegt** -- inkl. stille Reserven
12. **Eine klare Bankenentscheidungsvorlage formuliert** -- "Wir bieten / Wir wuenschen"
13. **Alle Anlagen und Download-Optionen auflistet** -- mit PDF-Export-Hinweis

---

## Strategie

### Schritt 1: Executive Summary (Sektion 1)

- **Hero-Sektion** mit Platzhalter fuer Objektfoto
- **5 KPI-Boxen** am oberen Rand:
  - Kreditbetrag (Bankdarlehen + KfW gesamt)
  - DSCR (SOFORT) -- nach Leerstandsabbau
  - DSCR (ab Monat X) -- nach Mieterhoehung/Modernisierung
  - LTV Bankdarlehen (auf Beleihungswert)
  - EK-Quote (inkl. Eigenleistungen)
- **"Projekt auf einen Blick"** Tabelle: Objekt, Standort, Typ, Einheiten, Flaeche, Grundstueck, Strategie, Finanzierungswunsch
- **"Kern-Argumente fuer die Bank"** -- genau 5 Bullet Points mit Checkmarks, die die STAERKSTEN Argumente fuer den Deal zusammenfassen (z.B. "DSCR >= 1,27 in ALLEN Phasen", "Trackrecord: JNKM +95% bei Vergleichsobjekt", "LTV unter 77% ab Faktor 16")
- **Footer-KPIs:** JNKM IST -> SOFORT -> SOLL 1 mit jeweiliger Rendite in %
- **Investitionslogik** als praegnanter Absatz (der "Elevator Pitch" fuer den Deal)

### Schritt 2: Unternehmensprofil (Sektion 2)

- **Investor-Card:** Avatar-Platzhalter, Name, Beschreibung ("Bestandshalter mit Fokus auf..."), Kontaktdaten
- **4 Portfolio-KPIs** als Boxen: Einheiten gesamt, Erfahrung (Jahre), Bestandsrendite (%), Leerstand (%)
- **Werdegang als Timeline:** Jahreszahl + Meilenstein (z.B. "2019: Erste ETW | 2020: Erstes MFH | 2021: GmbH-Gruendung | ...")
- **Trackrecord-Highlight:** Das beste Vergleichsobjekt als Beweis hervorheben -- mit JNKM-Steigerung, DSCR, LTV und Leerstand (z.B. "KM 59/60 Cottbus -- JNKM +95%, DSCR 3,20, LTV 51,7%, Leerstand 0")
- **Stille Reserven & Sicherheiten:** Freie Grundschulden aus dem Bestandsportfolio, nachrangig beleihbar

### Schritt 3: Projektuebersicht (Sektion 3)

- **Darlehensnehmer-Tabelle:** Gesellschaft, Gesellschafter (mit Anteil), Geschaeftsfuehrer, Sitz
- **Objektfotos:** 2 Fotos nebeneinander (Platzhalter mit Hinweis "Foto 1: Frontansicht | Foto 2: Rueckansicht/Hofseite")
- **Objektparameter-Tabelle** mit mindestens 15 Zeilen: Adresse, Objektart, Baujahr, Energieeffizienz, Wohneinheiten, Gewerbeeinheiten, Stellplaetze, Wohnflaeche gesamt, Grundstueck, Heizungsart, Keller, Kaufpreis, Kaufpreis/qm, IST-Miete/qm, Verhaeltnis zu Marktniveau
- **Kompakte KPI-Badges** am unteren Rand (z.B. "10 WE | 2 GE | Bj. 1936 | 904 m2 | Effizienz H")

### Schritt 4: Investmentstrategie (Sektion 4)

- **Entwicklungspfad IST -> SOLL** als visuelles Flussdiagramm mit 5 Stufen: IST -> SOFORT -> SOLL 1 -> SOLL 2 -> SOLL 3, jeweils mit JNKM-Betrag, Delta zum Vorgaenger und Rendite in %
- **DSCR-Trajektorie** unterhalb des Flussdiagramms (zeigt Anstieg ueber die Phasen)
- **Sanierungsaufstellung** als Tabelle: Massnahme | Kosten (EUR) | Programm/Hinweis -- mit Gesamtsumme und KfW-Tilgungszuschuss
- **Zeitstrahl Meilensteine** als Tabelle: Zeitpunkt | Meilenstein | Bedeutung/Wirkung -- von "Sofort" bis "Jahr 6+"
- **Investitionslogik** als erklaerenden Absatz: Warum funktioniert diese Strategie?

### Schritt 5: Wohnungsmix & Miete (Sektion 5)

- **3 Header-KPIs:** durchschnittliche IST-Miete (EUR/qm), durchschnittliche SOLL 1 (EUR/qm), Marktniveau (EUR/qm)
- **Vollstaendige Mieterliste** pro Einheit: Einheit | Typ | Flaeche (qm) | IST/Mo (EUR) | SOLL/Mo (EUR) | Mieter | Mietbeginn
- **Bei mehreren Gebaeuden:** Aufschluesselung nach Gebaeude: Gebaeude | WE | GE | IST/Mo | SOFORT/Mo | SOLL 1/Mo | SOLL 2/Mo | SOLL 3/Mo
- **Summenzeile** mit Totals ueber alle Einheiten/Gebaeude

### Schritt 6: Finanzierung (Sektion 6)

- **Split-Layout:** Gesamtinvestitionskosten (links) | Finanzierungsstruktur (rechts)
- **GIK-Aufstellung:** Kaufpreis + KNK-Breakdown (GrESt nach Bundesland-Satz + Notar/Gericht + Makler) + Sanierung + Eigenleistungen (bewertet)
- **Finanzierungsstruktur:** Bankdarlehen + KfW (falls vorhanden) + EK (aufgeteilt in Barmittel + Eigenleistungen)
- **Konditionen-Detail:** Zinsen, Tilgung (mit tilgungsfreier Phase in Monaten), KfW-Details (Programm, Zins, Tilgungszuschuss), Sondertilgung
- **Eigenleistungen als EK-Ersatz** -- das kritische Konzept:
  - **Block 1 (Barmittel):** Cash fuer Kaufnebenkosten (oder Teilfinanzierung)
  - **Block 2 (marktueblich bewertete Eigenleistungen):** Jede Leistung einzeln mit Marktpreis: Neuvermietung (X EUR), Mieterhoehungsgespraeche (X EUR), Gewerbeoptimierung (X EUR), PM Sanierung (X EUR), Objektueberwachung (X EUR), Foerderkoordination (X EUR), WEG-Vorbereitung (X EUR)
  - **Ergebnis:** Block 1 + Block 2 = EK-Quote Y%, obwohl kein oder wenig Cash eingebracht wird
- **Footer-KPIs:** GIK gesamt, Gesamtkredit (Bank + KfW), KfW-Tilgungszuschuss, EK-Quote
- **Ertragswert & LTV-Herleitung** als Tabelle: Faktor (15/16/17/18) x JNKM SOLL = Ertragswert -> Beleihungswert (70%) -> LTV Bank (%). Diese Tabelle zeigt der Bank, dass ihr Sicherheitenwert (Beleihungswert bei 70% des Ertragswerts) solide Abdeckung bietet.

### Schritt 7: Cashflow-Rechner -- Interaktiv (Sektion 7)

- **5 Eingabeparameter mit Slider-Bereichen:**
  - durchschnittliche Miete EUR/qm (min-max)
  - Leerstand % (0-20)
  - Bewirtschaftung % (15-35)
  - Zinssatz % (2-8)
  - Tilgung % (0-5)
- **3 live-berechnete Ausgabe-KPIs:** CF v.St. p.a. (EUR), DSCR, Rendite auf Gesamtkredit (%)
- **Berechnungsdetail-Breakdown:** Mieteinnahmen brutto -> Abzug Leerstand -> Abzug Bewirtschaftung -> Netto -> Abzug Zinsen Bank -> Abzug Zinsen KfW -> Abzug Tilgung -> CF v.St.
- **Farbcodierung:** Positiver CF = gruen, Negativer CF = rot

### Schritt 8: Phasen-Cashflow (Sektion 8)

- **Phase-Cards am oberen Rand:** Je Phase eine Karte mit CF/Monat (z.B. "Phase 1: +795 EUR/Mo | Phase 2: +1.336 EUR/Mo | ...")
- **Phasen-Uebersicht als Tabelle:** Phase | Zeitraum | JNKM (EUR) | KD/Mo (EUR) | DSCR | CF/Mo (EUR)
- **Typischerweise 5 Phasen:** IST (tilgungsfrei) -> Sec.559 + Bank tilgt -> Sec.558 + KfW tilgt -> SOLL 2 -> SOLL 3
- **Erlaeuterungstext:** "Kein kritisches Fenster. In jeder Phase uebersteigen die Mieteinnahmen den Kapitaldienst. Der DSCR faellt zu keinem Zeitpunkt unter 1,27."
- Der Phasen-Cashflow ist das Herzstück der Praesentation -- er beweist, dass der Deal in JEDER Phase bedienbar ist, nicht nur im Endzustand.

### Schritt 9: Sensitivitaetsanalyse (Sektion 9)

- **DSCR-Matrix** als Tabelle: Zeilen = Mietentwicklung (EUR/qm in Stufen), Spalten = Zinssatz (in Stufen)
- **Farbcodierung:** Gruen >= 1,20 (komfortabel), Gelb 1,00-1,20 (bedienbar), Rot < 1,00 (unterdeckt)
- **IST-Miete-Zeile hervorgehoben** (z.B. fett oder mit Markierung)
- **Lesehinweis:** Erlaeuterung der Matrix fuer den Bankberater ("Bei der aktuellen IST-Miete von X EUR/qm und einem Zinssatz von Y% betraegt der DSCR Z. Selbst bei einem Zinsanstieg auf W% bleibt der DSCR ueber 1,0.")

### Schritt 10: Szenarienvergleich (Sektion 10)

- **3 Spalten nebeneinander:** Konservativ | Basis (empfohlen) | Optimistisch
- **Jedes Szenario enthaelt:** Kurzbeschreibung, durchschnittliche Miete (EUR/qm), Leerstand (%), Bewirtschaftung (%), dann berechnet: Brutto p.a., Netto p.a., KD p.a., CF v.St. (EUR), DSCR, Rendite auf GK (%)
- **Basis-Szenario visuell hervorgehoben** (empfohlen)
- **Erlaeuterungstext** mit Kontext: Warum ist das Basis-Szenario konservativ genug? Welche Annahmen stecken im Worst Case?

### Schritt 11: Risiken & Exit (Sektion 11)

- **Risikomatrix als Tabelle:** Risiko | Eintrittswahrscheinlichkeit | Absicherung/Mitigation
- **Exit-Optionen & stille Reserven als Tabelle:** Option | Zeitpunkt | Wirkung (mit konkreten Zahlen: Ertragswert, Faktor, Erloespot enzial)
- **Optionen umfassen:** Bestandshaltung, Nachbeleihung/Kapitalrotation, Grundstuecksentwicklung (falls zutreffend), WEG-Aufteilung + Einzelverkauf, Portfolioverkauf (en bloc)
- **Stille Reserven als Absatz:** Beschreibung der stillen Reserven (z.B. Bauerwartungsland, freie Grundschulden, Differenz Kaufpreis zu Ertragswert)

### Schritt 12: Bankenentscheidung (Sektion 12)

- **"Wir bieten"-Box** mit 5-6 Checkmark-Items: EK-Quote, Grundschuld 1. Rang, DSCR >= X in allen Phasen, LTV unter Y%, voll vermietetes Objekt, Trackrecord
- **"Wir wuenschen"-Tabelle:** Art des Darlehens, Bankdarlehen (Betrag/Zins/Tilgung/Laufzeit/tilgungsfrei), KfW (falls zutreffend, mit Programm/Betrag/Zins/TZ), Sondertilgung, Sicherheit, Auszahlungsvoraussetzung, Anschlussfinanzierung
- **4 Footer-KPIs:** DSCR (Minimum ueber alle Phasen), LTV (Bank), JNKM SOLL (Zielwert), EK-Quote
- **Zusammenfassung** als abschliessendes Argument (der "Closing Pitch")

### Schritt 13: Downloads / Anlagen (Sektion 13)

- **PDF-Export-Hinweis:** "Diese Praesentation kann als PDF exportiert oder in Gamma.app als designte Praesentation aufbereitet werden."
- **Anlagen-Liste** mit allen beigefuegten/nachzureichenden Dokumenten: Maklerexpose, Mieterliste, Lageplan, Bestandsuebersicht Portfolio, Trackrecord Vergleichsobjekt, Selbstauskunft, Grundbuchauszug

---

## Ausgabeformat

```markdown
# Finanzierungsantrag: [Objektbezeichnung]
## [Adresse] | [Stadt], [Bundesland]
## Erstellt: [Datum] | Investor: [Name] | [Firma]

---

## 1. Executive Summary

![Objektfoto](foto_platzhalter.jpg)

### KPI-Boxen

| Kreditbetrag | DSCR (SOFORT) | DSCR (ab Mo 25) | LTV Bankdarlehen | EK-Quote |
|:---:|:---:|:---:|:---:|:---:|
| 680.000 EUR | 1,38 | 1,29 | 76,9% (F16) | 12,7% |

### Projekt auf einen Blick

| Parameter | Wert |
|-----------|------|
| Objekt | Mehrfamilienhaus / Wohn- und Geschaeftshaus |
| Standort | Cottbus, Brandenburg |
| Typ | Bestandsobjekt, Value-Add |
| Einheiten | 10 WE + 2 GE |
| Flaeche | 904 m2 |
| Grundstueck | 1.250 m2 |
| Strategie | Leerstandsabbau + Mieterhoehung + KfW-Modernisierung |
| Finanzierungswunsch | 680.000 EUR (Bank 620.000 + KfW 60.000) |

### Kern-Argumente fuer die Bank

- [x] DSCR >= 1,27 in ALLEN Phasen -- kein kritisches Fenster, Kapitaldienst jederzeit gesichert
- [x] Trackrecord: Vergleichsobjekt KM 59/60 Cottbus mit JNKM +95%, DSCR 3,20, Leerstand 0%
- [x] LTV unter 77% bei konservativem Faktor 16 auf JNKM SOLL 1
- [x] Sofortiger DSCR-Sprung auf 1,38 durch Leerstandsabbau in Monat 1-3
- [x] KfW-Foerderung sichert 15.000 EUR Tilgungszuschuss und reduziert effektiven Kapitaldienst

### Mietentwicklung & Rendite

| | JNKM IST | JNKM SOFORT | JNKM SOLL 1 |
|---|:---:|:---:|:---:|
| Betrag | 48.000 EUR | 57.600 EUR | 72.000 EUR |
| Rendite | 5,8% | 7,0% | 8,7% |

### Investitionslogik

Erwerb eines unterbewerteten Wohn- und Geschaeftshauses mit 20% Leerstand und 35% Mietanpassungspotenzial. Die Strategie kombiniert sofortige Leerstandsbeseitigung (DSCR-Sprung auf 1,38), organische Mieterhoehung im Bestand und selektive KfW-foerderfaehige Modernisierung. Der Kapitaldienst wird in JEDER Phase aus dem Objekt bedient. Die tilgungsfreie Anlaufphase von 24 Monaten ermoeglicht die Umsetzung ohne zusaetzlichen Liquiditaetsbedarf.

---

## 2. Unternehmensprofil

### Investor

| | |
|---|---|
| **[Avatar]** | **Max Mustermann** |
| | Geschaeftsfuehrer, Mustermann Immobilien GmbH |
| | Bestandshalter mit Fokus auf Value-Add-Wohnimmobilien in Ostdeutschland |
| Telefon | +49 170 1234567 |
| E-Mail | max@mustermann-immo.de |
| Adresse | Musterstrasse 1, 03046 Cottbus |

### Portfolio-KPIs

| Einheiten | Erfahrung | Bestandsrendite | Leerstand |
|:---:|:---:|:---:|:---:|
| 42 WE | 6 Jahre | 8,2% | 2,1% |

### Werdegang

| Jahr | Meilenstein |
|------|------------|
| 2019 | Erste ETW als Kapitalanlage erworben |
| 2020 | Erstes MFH (6 WE) -- Cottbus |
| 2021 | Gruendung Mustermann Immobilien GmbH |
| 2022 | Zwei MFH-Paketkaeufe (18 WE) -- 100% finanziert |
| 2023 | Portfolio auf 35 WE ausgebaut |
| 2024 | 42 WE, erste KfW-Sanierung abgeschlossen |

### Trackrecord-Highlight

> **KM 59/60, Cottbus** -- JNKM +95% | DSCR 3,20 | LTV 51,7% | Leerstand 0%
>
> Vergleichsobjekt im Eigenbestand. Identische Strategie (Leerstandsabbau + Mieterhoehung + Modernisierung) bereits erfolgreich umgesetzt. Nachweis, dass der Investor die hier geplante Strategie beherrscht.

### Stille Reserven & Sicherheiten

Freie Grundschulden aus dem Bestandsportfolio in Hoehe von 120.000 EUR, nachrangig beleihbar. Zusaetzlich stille Reserven im Bestandsportfolio durch Wertsteigerungen der letzten 5 Jahre.

---

## 3. Projektuebersicht

### Darlehensnehmer

| Parameter | Wert |
|-----------|------|
| Gesellschaft | Mustermann Immobilien GmbH |
| Gesellschafter | Max Mustermann (100%) |
| Geschaeftsfuehrer | Max Mustermann |
| Sitz | Cottbus |

### Objektfotos

| Foto 1: Frontansicht | Foto 2: Hofseite |
|:---:|:---:|
| ![Front](foto1_platzhalter.jpg) | ![Hof](foto2_platzhalter.jpg) |

### Objektparameter

| Parameter | Wert |
|-----------|------|
| Adresse | Beispielstrasse 10-12, 03046 Cottbus |
| Objektart | Mehrfamilienhaus / Wohn- und Geschaeftshaus |
| Baujahr | 1936 |
| Energieeffizienzklasse | H |
| Wohneinheiten | 10 |
| Gewerbeeinheiten | 2 |
| Stellplaetze | 6 |
| Wohnflaeche gesamt | 904 m2 |
| Grundstueck | 1.250 m2 |
| Heizungsart | Gas-Zentralheizung |
| Keller | Ja |
| Kaufpreis | 520.000 EUR |
| Kaufpreis/m2 | 575 EUR/m2 |
| IST-Miete (Ø) | 4,42 EUR/m2 |
| Marktniveau | 7,50 EUR/m2 |
| Grundbuch | Lastenfrei |

### KPI-Badges

`10 WE` | `2 GE` | `Bj. 1936` | `904 m2` | `1.250 m2 Grundstueck` | `Effizienz H` | `575 EUR/m2`

---

## 4. Investmentstrategie

### Entwicklungspfad IST -> SOLL

```
IST ---------> SOFORT -------> SOLL 1 -------> SOLL 2 -------> SOLL 3
48.000 EUR      57.600 EUR      72.000 EUR      78.000 EUR      82.800 EUR
                +9.600          +14.400         +6.000          +4.800
Rendite 5,8%    Rendite 7,0%    Rendite 8,7%    Rendite 9,5%    Rendite 10,0%
DSCR 1,15       DSCR 1,38       DSCR 1,50       DSCR 1,63       DSCR 1,72
```

### Sanierungsaufstellung

| Massnahme | Kosten (EUR) | Programm / Hinweis |
|-----------|:---:|---|
| Fenstertausch (10 WE) | 35.000 | KfW 261/262 |
| Heizungsoptimierung | 12.000 | BAFA BEG EM |
| Treppenhaussanierung | 8.000 | -- |
| Badsanierung (3 WE bei Mieterwechsel) | 15.000 | -- |
| Elektrik-Ertuechtigung | 10.000 | -- |
| Fassade (Teilbereich) | 20.000 | KfW 261 |
| **Gesamt** | **100.000** | |
| **KfW-Tilgungszuschuss** | **-15.000** | KfW 261 |
| **Effektive Sanierungskosten** | **85.000** | |

### Zeitstrahl Meilensteine

| Zeitpunkt | Meilenstein | Bedeutung / Wirkung |
|-----------|------------|---------------------|
| Sofort (Monat 1-3) | Leerstandsabbau + Neuvermietung | JNKM +9.600 EUR, DSCR steigt auf 1,38 |
| Monat 4-12 | Organische Mieterhoehung (Sec. 558 BGB) | Bestandsmieten +15-20% bei Mietspiegelberechtigung |
| Jahr 2 | Modernisierung + Sec. 559 Umlage | JNKM auf 72.000 EUR, DSCR 1,50 |
| Jahr 3-4 | Gewerbe-Neuvermietung + Stabilisierung | JNKM auf 78.000 EUR |
| Jahr 5+ | Vollstabilisierung | JNKM 82.800 EUR, DSCR 1,72, Option Nachbeleihung |
| Jahr 6+ | Exit-Optionen pruefen | WEG-Aufteilung oder Portfolioverkauf moeglich |

### Investitionslogik

Erwerb eines unterbewerteten Wohn- und Geschaeftshauses mit 20% Leerstand und 35% Mietanpassungspotenzial. Die Strategie kombiniert sofortige Leerstandsbeseitigung (DSCR-Sprung auf 1,38), organische Mieterhoehung im Bestand und selektive KfW-foerderfaehige Modernisierung. Der Kapitaldienst wird in JEDER Phase aus dem Objekt bedient. Die tilgungsfreie Anlaufphase von 24 Monaten ermoeglicht die Umsetzung ohne zusaetzlichen Liquiditaetsbedarf.

---

## 5. Wohnungsmix & Miete

### KPI-Header

| Ø IST-Miete | Ø SOLL 1 | Marktniveau |
|:---:|:---:|:---:|
| 4,42 EUR/m2 | 6,64 EUR/m2 | 7,50 EUR/m2 |

### Mieterliste

| Einheit | Typ | Flaeche (m2) | IST/Mo (EUR) | SOLL/Mo (EUR) | Mieter | Mietbeginn |
|---------|-----|:---:|:---:|:---:|--------|------------|
| WE 01 | Wohnung | 65,0 | 325,00 | 455,00 | Mueller, A. | 03/2018 |
| WE 02 | Wohnung | 78,0 | 390,00 | 546,00 | Schmidt, B. | 07/2020 |
| WE 03 | Wohnung | 55,0 | 275,00 | 385,00 | Weber, C. | 01/2019 |
| WE 04 | Wohnung | 90,0 | 450,00 | 630,00 | Fischer, D. | 11/2017 |
| WE 05 | Wohnung | 72,0 | 360,00 | 504,00 | Wagner, E. | 04/2021 |
| WE 06 | Wohnung | 68,0 | 340,00 | 476,00 | Becker, F. | 09/2019 |
| WE 07 | Wohnung | 82,0 | 410,00 | 574,00 | Schulz, G. | 02/2022 |
| WE 08 | Wohnung | 58,0 | 0,00 | 406,00 | **Leer** | -- |
| WE 09 | Wohnung | 76,0 | 380,00 | 532,00 | Hoffmann, H. | 06/2020 |
| WE 10 | Wohnung | 60,0 | 0,00 | 420,00 | **Leer** | -- |
| GE 01 | Gewerbe | 120,0 | 600,00 | 840,00 | **Leer** | -- |
| GE 02 | Gewerbe | 80,0 | 470,00 | 640,00 | Salon Iris | 01/2023 |
| **Gesamt** | | **904,0** | **4.000,00** | **6.408,00** | | |

### Aufschluesselung nach Gebaeude

| Gebaeude | WE | GE | IST/Mo | SOFORT/Mo | SOLL 1/Mo | SOLL 2/Mo | SOLL 3/Mo |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Haus 10 | 5 | 1 | 2.100 | 2.520 | 3.150 | 3.400 | 3.600 |
| Haus 12 | 5 | 1 | 1.900 | 2.280 | 2.850 | 3.100 | 3.300 |
| **Gesamt** | **10** | **2** | **4.000** | **4.800** | **6.000** | **6.500** | **6.900** |

---

## 6. Finanzierung

### Gesamtinvestitionskosten (GIK)

| Position | Betrag (EUR) |
|----------|:---:|
| Kaufpreis | 520.000 |
| GrESt (6,5% -- Brandenburg) | 33.800 |
| Notar + Grundbuch (2,0%) | 10.400 |
| Makler (3,57%) | 18.564 |
| **KNK gesamt** | **62.764** |
| Sanierung | 100.000 |
| Eigenleistungen (bewertet) | 45.000 |
| **GIK gesamt** | **727.764** |

### Finanzierungsstruktur

| Quelle | Betrag (EUR) | Anteil |
|--------|:---:|:---:|
| Bankdarlehen | 620.000 | 85,2% |
| KfW 261 | 60.000 | 8,2% |
| EK Barmittel (Block 1) | 47.764 | 6,6% |
| EK Eigenleistungen (Block 2) | 45.000 | -- (nicht-monetaer) |
| **Gesamt** | **727.764** | **100%** |

### Konditionen

| Parameter | Bankdarlehen | KfW 261 |
|-----------|:---:|:---:|
| Betrag | 620.000 EUR | 60.000 EUR |
| Zinssatz | 3,90% p.a. | 1,25% p.a. |
| Tilgung | 2,00% p.a. | nach Karenzzeit |
| Tilgungsfrei | 24 Monate | 36 Monate |
| Zinsbindung | 10 Jahre | Programmlaufzeit |
| Sondertilgung | 5% p.a. | -- |
| Tilgungszuschuss | -- | 15.000 EUR |

### Eigenleistungen als EK-Ersatz

**Block 1 -- Barmittel:**

| Position | Betrag (EUR) |
|----------|:---:|
| Barmittel fuer KNK (anteilig) | 47.764 |

**Block 2 -- Marktueblich bewertete Eigenleistungen:**

| Leistung | Marktpreis (EUR) |
|----------|:---:|
| Neuvermietung Leerstand (3 WE) | 8.000 |
| Mieterhoehungsgespraeche + Durchsetzung | 6.000 |
| Gewerbe-Akquise + Verhandlung | 5.000 |
| Projektmanagement Sanierung | 12.000 |
| Objektueberwachung + Baubegleitung | 6.000 |
| KfW-/BAFA-Foerderkoordination | 4.000 |
| WEG-Aufteilungsvorbereitung | 4.000 |
| **Block 2 gesamt** | **45.000** |

**EK-Quote:** Block 1 (47.764 EUR) + Block 2 (45.000 EUR) = 92.764 EUR = **12,7% der GIK**

> **Hinweis:** Die Eigenleistungen werden nicht als Cash eingebracht, sondern als vom Investor persoenlich erbrachte Leistungen, die bei Beauftragung eines Dritten den angegebenen Marktpreis kosten wuerden. Die Bank erhaelt damit den Nachweis, dass der Investor "Skin in the Game" hat -- durch Arbeitseinsatz statt durch Kapital.

### Footer-KPIs

| GIK | Gesamtkredit | KfW TZ | EK-Quote |
|:---:|:---:|:---:|:---:|
| 727.764 EUR | 680.000 EUR | 15.000 EUR | 12,7% |

### Ertragswert & LTV-Herleitung

| Faktor | x JNKM SOLL 1 | = Ertragswert | BW (70%) | LTV Bank |
|:---:|:---:|:---:|:---:|:---:|
| 15 | x 72.000 | 1.080.000 | 756.000 | 82,0% |
| **16** | **x 72.000** | **1.152.000** | **806.400** | **76,9%** |
| 17 | x 72.000 | 1.224.000 | 856.800 | 72,4% |
| 18 | x 72.000 | 1.296.000 | 907.200 | 68,3% |

> Bereits ab Faktor 16 liegt der LTV des Bankdarlehens (620.000 EUR) unter 77%. Der Beleihungswert bei Faktor 17 (856.800 EUR) uebersteigt den Gesamtkredit (680.000 EUR) um 176.800 EUR -- die Bank ist solide abgesichert.

---

## 7. Cashflow-Rechner (Interaktiv)

### Eingabeparameter (Slider)

| Parameter | Default | Min | Max | Schrittweite |
|-----------|:---:|:---:|:---:|:---:|
| Ø Miete (EUR/m2) | 6,64 | 4,00 | 9,00 | 0,25 |
| Leerstand (%) | 5 | 0 | 20 | 1 |
| Bewirtschaftung (%) | 25 | 15 | 35 | 1 |
| Zinssatz (%) | 3,90 | 2,00 | 8,00 | 0,10 |
| Tilgung (%) | 2,00 | 0 | 5,00 | 0,25 |

### Ausgabe-KPIs (live berechnet)

| CF v.St. p.a. | DSCR | Rendite auf GK |
|:---:|:---:|:---:|
| [berechnet] EUR | [berechnet] | [berechnet] % |

### Berechnungsdetail

| Position | Betrag (EUR/Jahr) |
|----------|:---:|
| Mieteinnahmen brutto (904 m2 x 6,64 EUR x 12) | 72.000 |
| - Leerstand (5%) | -3.600 |
| - Bewirtschaftung (25%) | -18.000 |
| **= Nettomieteinnahmen** | **50.400** |
| - Zinsen Bankdarlehen (620.000 x 3,90%) | -24.180 |
| - Zinsen KfW (60.000 x 1,25%) | -750 |
| - Tilgung Bank (620.000 x 2,00%) | -12.400 |
| **= CF v.St. p.a.** | **13.070** |

> Farbcodierung: **Positiver CF = GRUEN** | **Negativer CF = ROT**

---

## 8. Phasen-Cashflow

### Phase-Cards

| Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 |
|:---:|:---:|:---:|:---:|:---:|
| +795 EUR/Mo | +1.336 EUR/Mo | +1.274 EUR/Mo | +1.774 EUR/Mo | +2.174 EUR/Mo |
| IST (tilgungsfrei) | Sec.559+Bank tilgt | Sec.558+KfW tilgt | SOLL 2 | SOLL 3 |

### Phasen-Uebersicht

| Phase | Zeitraum | JNKM (EUR) | KD/Mo (EUR) | DSCR | CF/Mo (EUR) |
|:---:|---------|:---:|:---:|:---:|:---:|
| 1 | Mo 1-24 (tilgungsfrei) | 57.600 | 2.015 | **2,38** | +795 |
| 2 | Mo 25-36 (Sec.559 + Bank tilgt) | 72.000 | 4.664 | **1,29** | +1.336 |
| 3 | Mo 37-48 (Sec.558 + KfW tilgt) | 72.000 | 4.726 | **1,27** | +1.274 |
| 4 | Mo 49-72 (SOLL 2) | 78.000 | 4.726 | **1,38** | +1.774 |
| 5 | Ab Mo 73 (SOLL 3 stabilisiert) | 82.800 | 4.726 | **1,46** | +2.174 |

### Erlaeuterung

**Kein kritisches Fenster.** In jeder Phase uebersteigen die Mieteinnahmen den Kapitaldienst. Der DSCR faellt zu keinem Zeitpunkt unter 1,27 -- auch nicht beim Uebergang von der tilgungsfreien Phase zur Volltilgung. Die tilgungsfreie Anlaufphase (Phase 1) wird gezielt genutzt, um den Leerstand abzubauen und die Mietbasis auf 57.600 EUR JNKM zu heben, bevor die Tilgung einsetzt. Ab Phase 2 traegt die Modernisierungsumlage (Sec. 559 BGB) die hoehere Annuitaet. In Phase 5 (Vollstabilisierung) betraegt der freie Cashflow +2.174 EUR/Monat bei einem DSCR von 1,46.

---

## 9. Sensitivitaetsanalyse

### DSCR-Matrix

| Miete (EUR/m2) | 3,0% Zins | 3,5% Zins | 4,0% Zins | 4,5% Zins | 5,0% Zins | 5,5% Zins | 6,0% Zins |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 4,00 | 1,02 | 0,95 | 0,89 | 0,83 | 0,78 | 0,73 | 0,69 |
| **4,42 (IST)** | **1,13** | **1,05** | **0,98** | **0,92** | **0,86** | **0,81** | **0,76** |
| 4,50 | 1,15 | 1,07 | 1,00 | 0,94 | 0,88 | 0,83 | 0,78 |
| 5,00 | 1,27 | 1,19 | 1,11 | 1,04 | 0,98 | 0,92 | 0,86 |
| 5,50 | 1,40 | 1,31 | 1,22 | 1,15 | 1,08 | 1,01 | 0,95 |
| 6,00 | 1,53 | 1,43 | 1,33 | 1,25 | 1,17 | 1,10 | 1,04 |
| 6,50 | 1,66 | 1,55 | 1,45 | 1,36 | 1,27 | 1,19 | 1,12 |
| 7,00 | 1,79 | 1,67 | 1,56 | 1,46 | 1,37 | 1,29 | 1,21 |
| 7,50 | 1,91 | 1,78 | 1,67 | 1,57 | 1,47 | 1,38 | 1,30 |

> **Farbcodierung:** Gruen >= 1,20 (komfortabel) | Gelb 1,00-1,20 (bedienbar) | Rot < 1,00 (unterdeckt)

### Lesehinweis

Bei der aktuellen IST-Miete von 4,42 EUR/m2 und einem Zinssatz von 4,0% betraegt der DSCR 0,98 -- knapp unter 1,0. **Deshalb ist die sofortige Leerstandsbeseitigung und Mieterhoehung essenziell.** Bereits bei 5,50 EUR/m2 (realistisch nach Sec. 558 BGB) liegt der DSCR bei 1,22 auch bei 4,0% Zins -- komfortabel. Bei der SOLL 1-Miete von 6,64 EUR/m2 bleibt der DSCR selbst bei einem Zinsanstieg auf 5,5% ueber 1,19 (bedienbar). Erst bei einem extremen Szenario (IST-Miete + 6% Zins) wuerde der DSCR kritisch -- ein Szenario, das durch die Mieterhoehungsstrategie ausgeschlossen wird.

---

## 10. Szenarienvergleich

| Parameter | Konservativ | **Basis (empfohlen)** | Optimistisch |
|-----------|:---:|:---:|:---:|
| Beschreibung | Keine Mieterhoehung, hoher Leerstand | Geplante Strategie mit Puffer | Volle Marktmiete, geringer Leerstand |
| Ø Miete (EUR/m2) | 5,50 | **6,64** | 7,50 |
| Leerstand (%) | 10 | **5** | 3 |
| Bewirtschaftung (%) | 30 | **25** | 22 |
| **Brutto p.a.** | 59.664 | **72.000** | 81.360 |
| **Netto p.a.** | 37.688 | **51.300** | 60.869 |
| **KD p.a.** | 55.968 | **55.968** | 55.968 |
| **CF v.St. (EUR)** | -18.280 | **-4.668** | +4.901 |
| **DSCR** | 0,67 | **0,92** | 1,09 |
| **Rendite auf GK (%)** | 5,54 | **7,55** | 8,96 |

### Erlaeuterung

Das Basis-Szenario unterstellt die geplante Mieterhoehung auf 6,64 EUR/m2 (SOLL 1) -- deutlich unter dem Marktniveau von 7,50 EUR/m2. Der Leerstandspuffer von 5% ist konservativ fuer einen Standort mit unter 4% Marktleerstand. Selbst im konservativen Szenario ohne Mieterhoehung (5,50 EUR/m2) zeigt der Phasen-Cashflow (Sektion 8), dass der Kapitaldienst in der tilgungsfreien Phase vollstaendig bedient wird. Die Szenarien beziehen sich auf den stabilisierten Zustand mit voller Tilgung -- in der tilgungsfreien Anlaufphase liegt der DSCR deutlich hoeher.

---

## 11. Risiken & Exit

### Risikomatrix

| Risiko | Eintrittswahrscheinlichkeit | Absicherung / Mitigation |
|--------|:---:|--------------------------|
| Mieterhoehungen nicht durchsetzbar | Niedrig | Mietspiegel-gestuetzte Begruendung, konservatives Szenario zeigt Bedienbarkeit auch bei 60% der geplanten Erhoehungen |
| Leerstand steigt dauerhaft ueber 10% | Niedrig | Marktleerstand unter 4%, attraktive Mikrolage, Mietausfallversicherung vorhanden |
| Sanierungskosten uebersteigen Budget | Mittel | 20% Puffer eingeplant, Handwerkerangebote fuer Hauptpositionen vorliegend, KfW-Foerderung als zusaetzlicher Puffer |
| Zinsanstieg nach Zinsbindung | Mittel | 10 Jahre Zinsbindung, Sondertilgungen reduzieren Restschuld, DSCR-Matrix zeigt Bedienbarkeit bis 6% Zins |
| Regulatorische Aenderungen | Niedrig | Konservative Kalkulation ohne Ausreizung der Mietgrenzen, energetische Massnahmen im Sanierungsplan |

### Exit-Optionen & stille Reserven

| Option | Zeitpunkt | Wirkung |
|--------|-----------|---------|
| Bestandshaltung | Dauerhaft | DSCR 1,72 bei SOLL 3, CF +2.174 EUR/Mo, kontinuierlicher Vermoegensaufbau durch Tilgung |
| Nachbeleihung / Kapitalrotation | Ab Jahr 5 | Ertragswert 1,3 Mio EUR -> freier Beleihungsraum ca. 200.000 EUR fuer naechsten Deal |
| Grundstuecksentwicklung (Hinterland) | Ab Jahr 3 | 1.250 m2 Grundstueck, 800 m2 bebaut -> 450 m2 Bauerwartungsland, Potenzial fuer 4-6 Stellplaetze oder Tiny-Houses |
| WEG-Aufteilung + Einzelverkauf | Ab Jahr 5 | 12 Einheiten x Ø 85.000 EUR = 1.020.000 EUR Erloes vs. 520.000 EUR Kaufpreis -> ca. 500.000 EUR stille Reserve |
| Portfolioverkauf (en bloc) | Ab Jahr 5 | Faktor 17-18 auf JNKM SOLL 3 (82.800 EUR) = 1,4-1,5 Mio EUR Verkaufserloes |

### Stille Reserven

Neben den freien Grundschulden aus dem Bestandsportfolio (120.000 EUR) bietet das Grundstueck mit 450 m2 unbebautem Hinterland zusaetzliches Entwicklungspotenzial. Bei konservativer Bewertung (Faktor 17 auf JNKM SOLL 1) ergibt sich ein Ertragswert von 1,22 Mio EUR -- der Kaufpreis inklusive Sanierung liegt bei 620.000 EUR. Die stille Reserve betraegt somit ca. 600.000 EUR.

---

## 12. Bankenentscheidung

### Wir bieten

- [x] EK-Quote 12,7% (Barmittel + bewertete Eigenleistungen)
- [x] Grundschuld 1. Rang auf das Kaufobjekt
- [x] DSCR >= 1,27 in ALLEN Phasen -- kein kritisches Fenster
- [x] LTV unter 77% bei konservativem Faktor 16 auf JNKM SOLL 1
- [x] Voll vermietetes Objekt nach Leerstandsabbau (Monat 3)
- [x] Nachgewiesener Trackrecord: KM 59/60 Cottbus -- JNKM +95%, DSCR 3,20, Leerstand 0%

### Wir wuenschen

| Parameter | Details |
|-----------|---------|
| Art des Darlehens | Annuitaetendarlehen mit tilgungsfreier Anlaufphase |
| Bankdarlehen | 620.000 EUR, 3,90% Zins, 2,00% Tilgung, 10 Jahre Zinsbindung, 24 Monate tilgungsfrei |
| KfW 261 | 60.000 EUR, 1,25% Zins, 15.000 EUR Tilgungszuschuss, Tilgungsbeginn Monat 37 |
| Sondertilgung | Bis 5% p.a. ohne Vorfaelligkeitsentschaedigung |
| Sicherheit | Grundschuld 1. Rang auf Kaufobjekt, ggf. nachrangige Grundschuld auf Bestandsobjekt |
| Auszahlungsvoraussetzung | Kaufvertrag, Grundschuldbestellung, Eigentumsumschreibung |
| Anschlussfinanzierung | Preferred Partner bei gleicher Bank nach Zinsbindungsende |

### Footer-KPIs

| DSCR (min. alle Phasen) | LTV Bank | JNKM SOLL 1 | EK-Quote |
|:---:|:---:|:---:|:---:|
| 1,27 | 76,9% (F16) | 72.000 EUR | 12,7% |

### Zusammenfassung

Wir bieten der Bank ein durchgerechnetes Value-Add-Projekt mit nachgewiesenem Trackrecord, Cashflow-Bedienbarkeit in jeder Phase und konservativer LTV-Abdeckung. Der Investor bringt Eigenleistungen im Wert von 45.000 EUR ein, die marktueblich bewertet sind und den Projekterfolg sicherstellen. Die Kombination aus sofortiger Leerstandsbeseitigung, organischer Mieterhoehung und KfW-gefoerderter Modernisierung schafft einen klaren, nachvollziehbaren Pfad zur Vollstabilisierung. Die Bank finanziert ein Objekt, das ab Monat 3 voll vermietet ist, in jeder Phase einen DSCR >= 1,27 aufweist und bei konservativer Bewertung (Faktor 16) einen LTV von unter 77% bietet.

---

## 13. Downloads / Anlagen

### PDF-Export

Diese Praesentation kann als PDF exportiert oder in Gamma.app als designte Praesentation aufbereitet werden. Alternativ kann Claude Code daraus eine interaktive HTML-Praesentation mit Slidern (Cashflow-Rechner) und farbcodierter DSCR-Matrix generieren.

### Anlagen

| Nr. | Dokument | Status |
|:---:|---------|:---:|
| 1 | Maklerexpose | Beigefuegt |
| 2 | Mieterliste (aktuell) | Beigefuegt |
| 3 | Lageplan / Katasterauszug | Beigefuegt |
| 4 | Bestandsuebersicht Portfolio | Beigefuegt |
| 5 | Trackrecord Vergleichsobjekt (KM 59/60 Cottbus) | Beigefuegt |
| 6 | Selbstauskunft Investor | Beigefuegt |
| 7 | Grundbuchauszug | Beigefuegt |
```

---

## Qualitaetspruefung

Pruefe die Praesentation gegen diese Kriterien:

- [ ] **13 Sektionen vollstaendig:** Alle 13 Sektionen sind vorhanden und in der richtigen Reihenfolge
- [ ] **Executive Summary mit 5 KPI-Boxen:** Kreditbetrag, DSCR (SOFORT), DSCR (ab Mo X), LTV, EK-Quote
- [ ] **Kern-Argumente sind die STAERKSTEN 5 Punkte:** Nicht generisch, sondern deal-spezifisch
- [ ] **Entwicklungspfad hat 5 Stufen:** IST -> SOFORT -> SOLL 1 -> SOLL 2 -> SOLL 3 mit JNKM + Delta + Rendite
- [ ] **Phasen-Cashflow beweist Bedienbarkeit in JEDER Phase:** DSCR nie unter 1,0 (idealerweise nie unter 1,20)
- [ ] **Eigenleistungen korrekt aufgeschluesselt:** Block 1 (Barmittel) + Block 2 (bewertete Eigenleistungen) = EK-Quote
- [ ] **Ertragswert-Tabelle mit 4 Faktoren:** Zeigt der Bank, dass LTV unter 80% liegt
- [ ] **DSCR-Matrix mit Farbcodierung:** Gruen/Gelb/Rot klar erkennbar
- [ ] **Szenarienvergleich hat 3 Spalten:** Konservativ | Basis | Optimistisch
- [ ] **Exit-Optionen mit konkreten Zahlen:** Ertragswert, Erloesp., stille Reserven
- [ ] **"Wir bieten / Wir wuenschen" ist klar formuliert:** Bank kann direkt entscheiden
- [ ] **Zahlen konsistent ueber alle 13 Sektionen:** JNKM, DSCR, LTV, EK-Quote stimmen ueberall ueberein
- [ ] **Sprache professionell:** Sachlich, praezise, keine Uebertreibungen
- [ ] **Trackrecord als Beweis:** Vergleichsobjekt mit konkreten Zahlen (nicht nur "Erfahrung vorhanden")

---

## Warnsignale & Dealbreaker

| Warnsignal | Bewertung | Handlungsempfehlung |
|------------|:---------:|---------------------|
| DSCR < 1,0 in einer Phase des Phasen-Cashflows | KRITISCH | Tilgungsfreie Phase verlaengern, Sanierungsreihenfolge anpassen, oder Deal ueberarbeiten |
| Kein Trackrecord und kein Vergleichsobjekt | HOCH | Erfahrung anders belegen: Co-Investor, Ausbildungen, Hausverwaltungserfahrung |
| Eigenleistungen nicht plausibel bewertet | HOCH | Marktpreise fuer jede Leistung mit Vergleichsangeboten belegen |
| LTV > 100% auch bei hohem Faktor | KRITISCH | Zusatzsicherheiten einbringen oder Eigenkapitalanteil erhoehen |
| Keine Liquiditaetsreserve und kein laufendes Einkommen | KRITISCH | Bank wird ohne Sicherheitsnetz nicht finanzieren |
| Grundbuch belastet (Vormerkungen, Wegerechte, Altlasten) | HOCH | Klaeren vor Banktermin, ggf. im Kaufvertrag regeln |
| DSCR-Matrix zeigt grosse rote Flaeche | MITTEL | Mieterhoehungsstrategie ueberpruefen, Zinsbindung verlaengern |
| Sanierungskosten > 30% des Kaufpreises ohne KfW-Foerderung | HOCH | KfW-Foerderfaehigkeit pruefen, Sanierung in Phasen aufteilen |
| Mietzins ueber ortsueblicher Vergleichsmiete geplant | HOCH | Keine Mieten ueber Mietspiegel-Obergrenze planen, Glaubwuerdigkeit bewahren |
| Praesentation enthaelt Widersprueche oder Rechenfehler | KRITISCH | Alle Zahlen gegenprufen, insbesondere JNKM/DSCR/LTV-Konsistenz ueber alle 13 Sektionen |

---

## Bei fehlenden Daten

| Fehlende Information | Vorgehen |
|---------------------|----------|
| Investor-Trackrecord (erster Deal) | Berufliche Qualifikation hervorheben, Netzwerk benennen (Hausverwaltung, Steuerberater, Handwerker), Weiterbildungen erwaehnen, ggf. Co-Investor mit Trackrecord einbinden |
| Detaillierte Mieterliste | Mindestens Summen pro Gebaeude und Gesamt-JNKM. Hinweis "Vollstaendige Mieterliste als Anlage" |
| Eigenleistungen-Bewertung | Marktpreise aus Vergleichsangeboten (Hausverwaltung, Makler, Bauleiter) ableiten. Transparent als "marktueblich bewertet" kennzeichnen |
| KfW-Konditionen | Aktuelle Konditionen von kfw.de uebernehmen, als "Stand [Datum], vorbehaltlich Zusage" kennzeichnen |
| Fotos | Darauf hinweisen, dass Fotos nachgeliefert werden. Alternativ: Google Street View fuer Aussenansicht |
| Grundbuchauszug | Als "wird nachgereicht" markieren, aber keine Finanzierung ohne Grundbucheinsicht moeglich |
| Standortdaten / Mietspiegel | Statistisches Landesamt, kommunale Statistik, ImmoScout24-Mietpreisspiegel nutzen |
| Sanierungskosten | Markt-Benchmarks verwenden (siehe `knowledge/marktbenchmarks.md`), transparent als "Schaetzung ohne Handwerkerangebot" kennzeichnen |
| Referenzobjekte | ImmoScout24, Immowelt, lokale Makler fuer Vergleichspreise nutzen |
| Ertragswert-Faktor fuer Standort | Konservativen Faktor (15-16) fuer B-/C-Standorte, hoeheren Faktor (17-20) fuer A-Standorte ansetzen |

> **Tipp:** Lieber eine Luecke transparent benennen als mit unsicheren Daten die Glaubwuerdigkeit des gesamten Dokuments zu gefaehrden. Eine ehrliche Praesentation mit "wird nachgereicht" ist besser als eine vollstaendige Praesentation mit falschen Zahlen.

---

## Konfidenz-Bewertung

| Konfidenz | Kriterien |
|-----------|-----------|
| **HOCH** (90%+) | Alle 13 Sektionen mit vollstaendigen Daten befuellt. Trackrecord mit Vergleichsobjekt vorhanden. Mieterliste pro Einheit vollstaendig. DSCR > 1,20 in allen Phasen. Ertragswert-Tabelle zeigt LTV < 80%. Eigenleistungen marktueblich bewertet und belegt. Handwerkerangebote fuer Sanierung vorliegend. Grundbuchauszug eingesehen. |
| **MITTEL** (70-89%) | Kern-Sektionen (1, 4, 6, 8, 12) vollstaendig, aber Trackrecord duenn oder Mieterliste nur summarisch. Sanierungskosten geschaetzt. Eigenleistungen plausibel aber nicht mit Vergleichsangeboten belegt. DSCR > 1,0 in allen Phasen. |
| **NIEDRIG** (< 70%) | Wesentliche Sektionen unvollstaendig. Kein Trackrecord. DSCR in mindestens einer Phase < 1,0. Eigenleistungen nicht bewertet. Keine Ertragswert-Herleitung. Finanzierungskonditionen nicht abgestimmt. |

---

## Verwandte Wissensdatenbanken

- `skills/finanzierung/bankenkonzept.md` -- Erstellt das zugrundeliegende Finanzierungskonzept (Basis fuer Sektion 6: Finanzierung)
- `skills/finanzierung/cashflow-modell.md` -- Erstellt die detaillierte Cashflow-Projektion (Basis fuer Sektionen 7, 8, 9, 10)
- `skills/ankauf/marktanalyse.md` -- Standortanalyse und Marktdaten (ergaenzend zu Sektion 3)
- `skills/ankauf/bierdeckel-kalkulation.md` -- Schnellkalkulation fuer erste Einschaetzung vor der vollstaendigen Praesentation
- `skills/objektpruefung/unterlagen-analyst.md` -- Analysiert Objektunterlagen fuer Sektion 3 (Projektuebersicht)
- `skills/objektpruefung/risiko-scanner.md` -- Identifiziert Risiken fuer Sektion 11 (Risiken & Exit)
- `skills/objektpruefung/mietlisten-analyse.md` -- Analysiert Mieterlisten fuer Sektion 5 (Wohnungsmix & Miete)
- `skills/dokumente/expose-parser.md` -- Parsed Maklerexposes fuer Objektdaten
- `skills/dokumente/mietlisten-parser.md` -- Parsed Mieterlisten in strukturiertes Format
- `skills/vermietung/mieterhoehung.md` -- Berechnet Mieterhoehungspotenzial (Sec. 558/559 BGB) fuer die Investmentstrategie
- `knowledge/kalkulationsformeln.md` -- Renditekennzahlen, DSCR-Berechnung, Ertragswertverfahren
- `knowledge/rechtsgrundlagen.md` -- BGB-Referenzen fuer Mieterhoehung und Modernisierungsumlage
- `knowledge/marktbenchmarks.md` -- Benchmarks fuer Sanierungskosten, Bewirtschaftung, Mietvergleiche
- `knowledge/risikobewertung.md` -- Risiko-Framework fuer systematische Risikoanalyse
- `knowledge/checklisten.md` -- Checklisten fuer Banktermin-Vorbereitung und Dokumentenvollstaendigkeit
