# Aenderungsprotokoll

Alle wesentlichen Aenderungen an diesem Projekt.

## [1.13.0](https://github.com/immoJUMP/immo-agent-skills/compare/v1.12.0...v1.13.0) (2026-10-22)


### Hinzugefuegt

* **immojump-cli:** immoJUMP per CLI als Agenten-Backend fuer Grossbestaende ([4ed0f6c](https://github.com/immoJUMP/immo-agent-skills/commit/4ed0f6c16a2d6ea18bf434f99b71e5970fb4a9e3))
* **second-brain:** Wissensbasis einrichten, pflegen und pruefen ([8b55e4b](https://github.com/immoJUMP/immo-agent-skills/commit/8b55e4b2b4b38fa51ab6e6e264632f017d694664))


### Behoben

* **cashflow-modell:** EK-Rendite und Cash-on-Cash trennen ([c7cc4f4](https://github.com/immoJUMP/immo-agent-skills/commit/c7cc4f41854d6a7f034ada35d4108d4dd0d4f21f))
* **grunderwerbsteuer:** Bremen 5,5 %, Sachsen 5,5 % und Thueringen-Aenderungsjahr korrigiert ([be996ae](https://github.com/immoJUMP/immo-agent-skills/commit/be996ae0e44d49dfdb02da29d4bc035f0b6d2f67))
* **immojump-cli:** Analyse-Block bricht bei Fehler ab, Neuvermietung nur bei bestaetigtem Leerstand ([9b099ce](https://github.com/immoJUMP/immo-agent-skills/commit/9b099ceff33ef2ce14d99af81de0f8019a6610c9))
* **immojump-cli:** Befunde aus dem Codex-Review ([769474e](https://github.com/immoJUMP/immo-agent-skills/commit/769474e1dda0b188b0e7b0593ec6466a6fdf7cad))
* **immojump-cli:** Befunde der zweiten Review-Runde (Claude und Codex) ([031841e](https://github.com/immoJUMP/immo-agent-skills/commit/031841ea304183e1c16c022ad5348249373be339))
* **immojump-cli:** dritte Review-Runde — IDs je Block, Analyse an freigegebene IDs gebunden, Leerstand-Markierung ([e64f0ce](https://github.com/immoJUMP/immo-agent-skills/commit/e64f0ce47d2344f4b324a69c6406c96b1caec289))
* **immojump-cli:** Feldwert-Beispiel legt jedes verwendete Feld vorher an ([cc7d796](https://github.com/immoJUMP/immo-agent-skills/commit/cc7d7965a5da41e7c3631c669c5c5fd189031f00))
* **immojump-cli:** Jahresmiete fuer den Faktor centgenau statt auf Euro gerundet ([3de5959](https://github.com/immoJUMP/immo-agent-skills/commit/3de59592fbe28507b6cf79382f4bb223701275e5))
* **immojump-cli:** Referenz neu, robust gegen verschluckte Fehler (zweite Review-Runde) ([6c952c9](https://github.com/immoJUMP/immo-agent-skills/commit/6c952c99ccb3ff31cad0048f9eae28078cd5afaa))
* **kalkulationsformeln:** EK-Rendite, Cash-on-Cash und Vermögensaufbau wie im Skill trennen ([b606b2c](https://github.com/immoJUMP/immo-agent-skills/commit/b606b2cde5c0d92e8f52186d8d77590de1956288))
* **kalkulationsformeln:** stimmiges Renditebeispiel, kein Produkt als Maßstab ([fce0bf4](https://github.com/immoJUMP/immo-agent-skills/commit/fce0bf434d957202e7446c34e390dc2961329f9e))
* **plugin:** Marketplace-Manifest, damit die Installation aus dem README klappt ([8d1cb15](https://github.com/immoJUMP/immo-agent-skills/commit/8d1cb15f9b4564a288b81f8f1e9e1ba245985fd0))
* **prozess-designer:** bestehende eigene Templates bleiben als Kettenziel erlaubt ([4651759](https://github.com/immoJUMP/immo-agent-skills/commit/4651759dbf60fe766fe8043fa11aa30afc2a43be))
* **prozess-designer:** IDs in Vorlagen nur aus der eigenen Organisation ([80bf242](https://github.com/immoJUMP/immo-agent-skills/commit/80bf242858154e23a61ea3db08d6a75a9b36ff0f))


### Dokumentation

* **immojump-cli:** Duplikat-Erkennung gilt organisationsweit ([63a77d1](https://github.com/immoJUMP/immo-agent-skills/commit/63a77d14a7fa1aedb1cb204c93f52c5fa66590b7))
* **second-brain:** Anwenderhandbuch mit Nutzen und Systemvergleich ([ac119b5](https://github.com/immoJUMP/immo-agent-skills/commit/ac119b5b4876cd79e0222c8ee3a99332bb6a7041))

## [1.12.0](https://github.com/immoJUMP/immo-agent-skills/compare/v1.11.0...v1.12.0) (2026-09-08)


### Hinzugefuegt

* Anlage-V-Assistent auf den amtlichen Vordruck 2025 heben ([6a63d24](https://github.com/immoJUMP/immo-agent-skills/commit/6a63d249434bba55f4ac793532f54055296a3fcd))
* **anlage-v:** Bericht als Markdown-Datei statt nur im Chat ([b9573d4](https://github.com/immoJUMP/immo-agent-skills/commit/b9573d4224e91a4bcc4df33048a40b75b2425224))
* **anlage-v:** Sanierung vor Nutzen-Lasten-Uebergang und Beweislast bei Standardhebung ([734026a](https://github.com/immoJUMP/immo-agent-skills/commit/734026a07db24461ac62fd032d15c874e413bdca))
* **anlage-v:** Zurechnung bei mehreren Eigentuemern praeziser fassen ([62804f0](https://github.com/immoJUMP/immo-agent-skills/commit/62804f03f398d55b31a14e969e2780b05bdb33f6))


### Behoben

* **anlage-v:** Auftraggeber-Anforderung beim Gutachten als strittig kennzeichnen ([91dd24f](https://github.com/immoJUMP/immo-agent-skills/commit/91dd24fa11851d5b9bd1150e5607a69d55479e65))
* **anlage-v:** Bauabzugsteuer knuepft an Wohnungen, nicht an Objekte ([e7e8399](https://github.com/immoJUMP/immo-agent-skills/commit/e7e83998b23975636f499f7f50c93fafab10f4b3))


### Dokumentation

* Ausgabekonvention um lange Berichte als Datei ergaenzen ([8dd0fec](https://github.com/immoJUMP/immo-agent-skills/commit/8dd0fec46c149354fb5f442a19a0a5f25b7d272d))


### Geaendert

* **anlage-v:** Berechnungsmethoden ausschreiben statt Variante A/B/C ([a2a3807](https://github.com/immoJUMP/immo-agent-skills/commit/a2a38072d3bc5af118790428a85f123551be6693))

## [1.11.0](https://github.com/immoJUMP/immo-agent-skills/compare/v1.10.0...v1.11.0) (2026-08-30)


### Hinzugefuegt

* **nebenkosten-pruefer:** erweitere Rechtspruefung ([8a9c184](https://github.com/immoJUMP/immo-agent-skills/commit/8a9c1849ef1feb6950872d0609a9dd2dab07a5b5))

## [1.10.0](https://github.com/immoJUMP/immo-agent-skills/compare/v1.9.0...v1.10.0) (2026-07-26)


### Hinzugefuegt

* immo-agent-skills v1.9.0 ([b87dd70](https://github.com/immoJUMP/immo-agent-skills/commit/b87dd703339c8cfd43968f0d50ee5aa4a523d34d))

## [1.9.0] (2026-07-26)

### Geaendert

* Lizenzumstellung auf die **immoJUMP Source Available License 1.0**. Die
  Nutzung im eigenen Unternehmen bleibt erlaubt, auch gewerblich und fuer
  Dienstleistungen an eigene Kunden. Erzeugte Arbeitsergebnisse gehoeren
  uneingeschraenkt dem Nutzer. Nicht mehr gestattet sind Weiterverbreitung,
  Weiterverkauf sowie der Einsatz in Schulungen und Produkten fuer Dritte.
* Beitragsmodell angepasst: Feedback und Fehlermeldungen laufen ueber Issues
  und E-Mail, inhaltliche Beitraege nach vorheriger Absprache.

### Enthalten

* 32 Skills fuer Ankauf, Finanzierung, Verwaltung, Vermietung, Buchhaltung,
  Dokumentenanalyse, Strategie und Prozessgestaltung
* 5 Wissensdatenbanken: Kalkulationsformeln, Risikobewertung,
  Marktbenchmarks, Rechtsgrundlagen, Checklisten
