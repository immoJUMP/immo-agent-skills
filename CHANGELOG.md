# Aenderungsprotokoll

Alle wesentlichen Aenderungen an diesem Projekt.

## [1.15.0](https://github.com/immoJUMP/immo-agent-skills/compare/v1.14.0...v1.15.0) (2026-11-14)


### Hinzugefuegt

* **telefon-assistent:** sipgate als zweiter Anbieter neben der FRITZ!Box ([b200b75](https://github.com/immoJUMP/immo-agent-skills/commit/b200b75cfbbd5a910237212fc89a952af4c77f6e))

## [1.14.0](https://github.com/immoJUMP/immo-agent-skills/compare/v1.13.0...v1.14.0) (2026-11-14)


### Hinzugefuegt

* **agenten-doktor:** Agenten-Server mit Hermes, Rocket.Chat, MietJUMP und Lernkreislauf ([aea8539](https://github.com/immoJUMP/immo-agent-skills/commit/aea8539900f1fc81ecae2d916df5cc7fd1889a27))
* **agenten-doktor:** Bestands-Cockpit, Fachskills je Agent, Akquise-Vorlage, Muster fuer bestehende Setups ([7929aaa](https://github.com/immoJUMP/immo-agent-skills/commit/7929aaabb636e8105d9a88bcb8cff8ff9452f898))
* **agenten-doktor:** Durchlauf mit einem Start-Prompt, Vorbereitungs-Check, Ausweichtypen ([4600a35](https://github.com/immoJUMP/immo-agent-skills/commit/4600a35fac371af48fab72ee3d5bc16089ce1741))
* **agenten-doktor:** eigener Browser fuer Vera, Vorlagen-Abgleich ohne Scheinaenderungen ([6f07888](https://github.com/immoJUMP/immo-agent-skills/commit/6f07888b6373e7e55f44fdbcc9dc456c907a10e9))
* **agenten-doktor:** Einstellung prueft Werkzeuge und Platzhalter, ergaenzt CODEOWNERS ([383f7f1](https://github.com/immoJUMP/immo-agent-skills/commit/383f7f14b3b498f9016f5b674ab9eba5f35b4edf))
* **agenten-doktor:** Meldungen an den Eigentuemer, nur Fachliches und nicht behebbare Stoerungen ([6e96e4b](https://github.com/immoJUMP/immo-agent-skills/commit/6e96e4bfdd65779ae03aec5967370acad9a50eb9))
* **agenten-doktor:** Vorlage Ankaufs-Anke statt Mats (Akquise) ([e6389ea](https://github.com/immoJUMP/immo-agent-skills/commit/e6389ea7af2feff8df61e7ff38d508f96d7a0212))
* **nebenkosten-pruefer:** Belegschicht vor der Rechtspruefung ([e641215](https://github.com/immoJUMP/immo-agent-skills/commit/e6412154a5e36031e71feb5a7dc7bd091c467360))
* **telefon-assistent:** Agent ruft den Inhaber über die FRITZ!Box an, mit Chat-Kontext und Terminvorbereitung ([2e07ba2](https://github.com/immoJUMP/immo-agent-skills/commit/2e07ba2c8ebdda73167468738e9a2d80a258e11a))


### Behoben

* **agenten-doktor:** Befunde aus adversarialem Review und Neustart-Test ([41df573](https://github.com/immoJUMP/immo-agent-skills/commit/41df573aa87d82ac5a942ec69e534b7da23ebd19))
* **agenten-doktor:** Befunde aus dem Review vom 14.11. (Teilnehmerweg, Code, Sicherheit) ([f636ace](https://github.com/immoJUMP/immo-agent-skills/commit/f636aceaa1d965922e9b0659b8a745f1061163fe))
* **agenten-doktor:** keine Start-, Stopp- und Warnhinweise von Hermes im Telegram-Chat des Eigentuemers ([8e55a1f](https://github.com/immoJUMP/immo-agent-skills/commit/8e55a1fccc8b353ae0514bfe3fb2216784b7e281))
* **agenten-doktor:** Logbuch nur bei geaendertem Befund, Testfragen-Meldungen gedrosselt ([eee1952](https://github.com/immoJUMP/immo-agent-skills/commit/eee1952dbe9ab1c3025949cd77361fadb588a03b))
* **agenten-doktor:** Testfragen geben die Sperre waehrend der Modellaufrufe ab ([1310271](https://github.com/immoJUMP/immo-agent-skills/commit/131027163367c9f46f830c9f71f9e266709eb9f7))
* **agenten-doktor:** Zustand vor dem Speichern frisch lesen (Vorschlagsnummer ging verloren) ([ee2f2f6](https://github.com/immoJUMP/immo-agent-skills/commit/ee2f2f635600790937088c19f2274bd2bd9a6df8))
* **heizungsrecht:** Skills und Nachschlagewerke auf das GModG umstellen ([754f703](https://github.com/immoJUMP/immo-agent-skills/commit/754f703a64423f49da94f698d1ca6ae73dd7ced2))
* **verhandlung,mietliste:** Faustformel begrenzen, echte Quellen, Sperrfrist gemeindegenau ([a08438f](https://github.com/immoJUMP/immo-agent-skills/commit/a08438f67623157b2ce75a60e1357e2c4d65631f))


### Dokumentation

* **agenten-doktor:** Anbieter statt Personenname im oeffentlichen Skill ([7fd8b85](https://github.com/immoJUMP/immo-agent-skills/commit/7fd8b8598cfc16bfb6e7de280ce90dc4634d8cad))
* **agenten-doktor:** Doku an gehaerteten Code angeglichen, letzte Review-Punkte behoben ([51d6bfa](https://github.com/immoJUMP/immo-agent-skills/commit/51d6bfaa3eecb48de1607ea8674ec6854bf19dc2))


### Styling

* **agenten-doktor:** Startseite mit Farbwerten aus den Design-Tokens ([2655928](https://github.com/immoJUMP/immo-agent-skills/commit/2655928ec0adc3ebcc5f2ca8aadfebf61adb2f66))


### Tests

* **agenten-doktor:** Nachweis Telegram-Ruhe auf Wegwerf-Server, Ergebnis in sicherheit.md ([ddb2136](https://github.com/immoJUMP/immo-agent-skills/commit/ddb2136f423cbf9e588e28775e3d703012621b69))
* **agenten-doktor:** Unit-Tests fuer Rechte-Matrix, Vorschlagspruefung und Symlink-Abwehr ([ecb4512](https://github.com/immoJUMP/immo-agent-skills/commit/ecb4512809566d08a98f546586bdb09a15d10e1d))

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
