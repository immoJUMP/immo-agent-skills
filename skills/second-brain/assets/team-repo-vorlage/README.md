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

1. Schreib Kurt `freigeben #12` (bei einer Sprachnachricht fragt Kurt einmal schriftlich nach).
2. Nach spätestens etwa 2 Minuten schickt dir der Server einen sechsstelligen Code mit Titel und Dateien des PR, über den Doktor-Bot, falls eingerichtet, sonst über Kurts Bot. Prüfe, ob das wirklich der PR ist, den du willst.
3. Schreib Kurt `freigeben #12 Code 123456`. Der Code gilt 30 Minuten und nur für diesen Stand des PR. Ändert sich der PR, brauchst du einen neuen.
4. Der Doktor merged beim nächsten Abgleich, wenn du für alle Dateien berechtigt bist, und trägt die Änderung ins Änderungsprotokoll ein. Kurt meldet dir das Ergebnis.

Ablehnen: Schreib Kurt `ablehnen #12` und einen Satz, warum. Das braucht keinen Code, der Doktor schließt den PR.

### Auf GitHub

1. PR öffnen, Änderungen und Checkliste lesen.
2. Review mit „Approve“ auf dem aktuellen Stand. Der Doktor merged beim nächsten Abgleich, wenn du nach der Rechte-Matrix für alle Dateien berechtigt bist. Ein Approve auf einem älteren Stand zählt nicht. Das gilt nur für Vorschläge der Agenten (Label `von-<agent>`).
3. Läuft der Token des Servers auf dein Konto, bist du Autor der PRs und kannst sie auf GitHub nicht selbst genehmigen. Dann gibst du per Telegram frei.
4. Den Merge-Knopf auf GitHub kannst du nutzen, er umgeht aber Änderungsprotokoll und Testfragen. Lieber nicht.

### Nach der Übernahme

Die Testfragen der betroffenen Agenten laufen automatisch, spätestens nach 15 Minuten. Bericht: `betrieb/testfragen/<agent>.md`. Schlägt eine fehl, steht das im Logbuch. Zurückgenommen wird nichts automatisch.

### Was du vor der Freigabe prüfst

- Stimmt die Aussage fachlich?
- Steht der Fakt danach an genau einem Ort? (Checkliste im PR)
- Passt die Testfrage? Sie läuft erst nach der Übernahme.
- Steht eine `rechte.yaml` in der Dateiliste? Dann erweitert der PR, was ein Agent sehen oder vorschlagen darf. Genau hinsehen.
- Keine Mieternamen, keine IBAN, keine Kontaktdaten von Mietern?

## Wer gibt was frei

| Pfad | Wer gibt frei |
|---|---|
| `team/**` | laut Rechte-Matrix Fachverantwortliche/r oder du. Der Doktor lässt es derzeit nur dich freigeben |
| `geschaeftsfuehrung/**`, `.github/**`, `AGENTS.md` | nur du, nie per Agenten-Vorschlag |
| `betrieb/logbuch/**` | schreibt der Doktor direkt |
| alles ohne eigene Zeile (`README.md`, `INDEX.md`, `llms.txt`, `entscheidungen/`) | nur du |
| Dateien in einem Agentenordner | siehe [agenten/README.md](agenten/README.md) |

## Was nie hier hinein gehört

Das Repo liegt bei GitHub (USA). Darum nie hier hinein: Passwörter, Tokens, Zugangsdaten, Mieternamen, IBAN und andere Kontonummern, Telefonnummern und Mailadressen von Mietern, Gesundheits- oder Sozialdaten, Kopien von Mails oder Kontoauszügen. Mieter nur als Einheitsnummer (z. B. `OBJ1-WE03`). Das gilt auch für die Fallbücher, die der Doktor ohne Freigabe hierher spiegelt. Operative Daten bleiben in ihrem System: Mieter, Mieten und Zahlungen in MietJUMP, Mails in Gmail.

## Wenn du selbst etwas änderst

Du darfst alles. Geh trotzdem über einen PR mit der Vorlage und gib ihn per Telegram an Kurt frei (`freigeben #<nr>`, dann der Code). Nur dann laufen die Testfragen und das Änderungsprotokoll stimmt. Eine Regel, die du nur im Chat sagst, gilt dauerhaft erst, wenn sie hier steht.
