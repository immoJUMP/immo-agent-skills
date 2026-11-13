<!-- Für PRs, die Menschen anlegen. PRs der Agenten schreibt der Doktor selbst aus vorschlag.yaml. -->

## Auslöser

<!-- Wer hat was wann und wo korrigiert oder entschieden? Raum, Telegram oder Fall mit Datum. Eine Mail allein ist kein Auslöser. -->

- Vorschlagender Agent:
- Art: korrektur | wissen | agent-einstellen | regel
- Auslöser:
- Begründung:

## Betroffene Seiten

<!-- Je Datei: Pfad, was sich ändert, welche Aussage ersetzt wird. -->

| Datei | Änderung | ersetzt |
|---|---|---|
| | | |

## Ein-Fakt-Check

- [ ] Gesucht in `INDEX.md`, Unterindex, Volltext und offenen PRs.
- [ ] Der Fakt steht danach an genau einem Ort; andere Stellen verweisen nur.
- [ ] Kein zweites `thema`; ersetzte Aussagen sind entfernt, nicht daneben gestellt.
- [ ] Indexzeile ergänzt oder angepasst.

## Testfragen und Ergebnis

| Frage | erwartet | Ergebnis |
|---|---|---|
| | | |

- [ ] Mindestens eine neue Testfrage, auch in `agenten/<slug>/testfragen.yaml`.
- Die Testfragen laufen erst nach der Übernahme durch den Doktor (Bericht `betrieb/testfragen/<agent>.md`).

## Rechte-Check

- [ ] Alle Dateien liegen in `vorschlagen` des Agenten.
- [ ] Keine Datei aus `geschaeftsfuehrung/`, `.github/`, `AGENTS.md`, `betrieb/`, keine fremden Fallbücher.
- [ ] Ändert eine `rechte.yaml`: Titel beginnt mit `[Rechte]`, Erweiterung hier alt → neu.
- [ ] Keine Geheimnisse, keine IBAN oder Kontonummern, keine Mieternamen oder Kontaktdaten von Mietern (das Repo liegt bei GitHub).
- Freigabe durch: Fachverantwortliche/r oder Eigentümer | nur Eigentümer

## Übernahme

Eigentümer per Telegram: Kurt `freigeben #<nr>` schreiben, dann den Code vom Server als `freigeben #<nr> Code <code>`. Ein Approve auf GitHub reicht nur bei Vorschlägen der Agenten. Nicht über den Merge-Knopf: dann fehlen Änderungsprotokoll und Testfragen.
