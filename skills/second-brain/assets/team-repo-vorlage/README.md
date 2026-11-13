# Wissens-Repo von {{FIRMA}}

Das ist das gemeinsame Gedächtnis deines Agenten-Teams: wer deine Agenten sind, was sie wissen, was sie dürfen und warum. Das Repo ist privat. Jeder Agent liest nur seinen Ausschnitt und ändert nichts direkt. Jede Änderung kommt als Vorschlag (Pull Request), und du oder die/der zuständige Fachverantwortliche gibt frei.

Eingerichtet am {{REPO_DATUM}} vom Doktor für {{DOMAIN}}. Eigentümer: {{EIGENTUEMER_NAME}}.

## Was liegt wo

| Ordner | Inhalt |
|---|---|
| `team/` | Wissen für alle Agenten: Firma, Objekte |
| `agenten/` | ein Ordner je Agent: Rolle, Regeln, Rechte, Wissen, Testfragen, Fallbuch |
| `entscheidungen/` | deine Entscheidungen mit Begründung |
| `geschaeftsfuehrung/` | Strategie, Finanzierung, Ankauf und Verkauf. Liest nur Kurt |
| `betrieb/` | Adressen und Logbuch des Servers |

Suchen: [INDEX.md](INDEX.md). Regeln für die Agenten: [AGENTS.md](AGENTS.md).

## So lernt dein Team

1. Du korrigierst einen Agenten im Chat, zum Beispiel im Raum `#verwaltung`: „Sammelzahlungen für mehrere Wohnungen bitte aufteilen.“
2. Der Agent prüft: Einzelfall (dann Fallbuch) oder dauerhafte Regel (dann Vorschlag).
3. Für einen Vorschlag schreibt er die geänderte Seite und mindestens eine Testfrage. Der Doktor prüft die Rechte und macht daraus einen Pull Request.
4. Der Agent meldet dir: „Vorschlag liegt als PR 12 zur Freigabe.“
5. Du gibst frei. Erst dann gilt die Regel dauerhaft, und der Doktor trägt sie ins Änderungsprotokoll des Agenten ein.

Was ein Agent vorschlägt, gilt nie ohne Freigabe durch dich oder die/den zuständige/n Fachverantwortliche/n.

## So gibst du frei

### Per Telegram an Kurt

1. Schreib Kurt `freigeben #12` (auch als Sprachnachricht).
2. Kurt nennt dir Titel, betroffene Dateien und das Ergebnis der Testfragen und fragt einmal nach. Erst deine Bestätigung zählt.
3. Der Doktor merged, wenn du für alle Dateien berechtigt bist und alle Testfragen bestanden sind. Sonst bekommst du den Grund.

Ablehnen: Schreib Kurt `ablehnen #12` und einen Satz, warum. Der Doktor schließt den PR, der vorschlagende Agent kann neu vorschlagen.

### Auf GitHub

1. PR öffnen, Änderungen und Checkliste lesen.
2. „Approve“ klicken. Übernommen wird der PR mit `doktor freigeben 12 --von github:<dein-login>`; der Doktor prüft dabei deine Berechtigung für jede Datei.
3. Nicht über den Merge-Knopf auf GitHub mergen: Dann prüft niemand die Berechtigung, die Testfragen laufen nicht und das Änderungsprotokoll fehlt.

### Was du vor der Freigabe prüfst

- Stimmt die Aussage fachlich?
- Steht der Fakt danach an genau einem Ort? (Checkliste im PR)
- Passt die Testfrage, und ist sie bestanden?
- Beginnt der Titel mit `[Rechte]`? Dann erweitert der PR, was ein Agent sehen oder vorschlagen darf. Genau hinsehen.

## Wer gibt was frei

| Pfad | Wer gibt frei |
|---|---|
| `team/**` | Fachverantwortliche/r des vorschlagenden Agenten oder du |
| `geschaeftsfuehrung/**`, `.github/**`, `AGENTS.md` | nur du, nie per Agenten-Vorschlag |
| `betrieb/logbuch/**` | schreibt der Doktor direkt |
| alles ohne eigene Zeile (`README.md`, `INDEX.md`, `llms.txt`, `entscheidungen/`) | nur du |
| Dateien in einem Agentenordner | siehe [agenten/README.md](agenten/README.md) |

## Was nie hier hinein gehört

Passwörter, Tokens, Zugangsdaten, echte Kontonummern, Mieternamen ohne Notwendigkeit, Gesundheits- oder Sozialdaten, Kopien von Mails oder Kontoauszügen. Operative Daten bleiben in ihrem System: Mieten und Zahlungen in MietJUMP, Mails in Gmail.

## Wenn du selbst etwas änderst

Du darfst alles. Geh trotzdem über einen PR mit der Vorlage, damit die Testfragen laufen und das Änderungsprotokoll stimmt. Eine Regel, die du nur im Chat sagst, gilt dauerhaft erst, wenn sie hier steht.
