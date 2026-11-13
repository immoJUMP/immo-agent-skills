# Agenten

Ein Ordner je Agent: `agenten/<slug>/`. Die Ordner sind die Liste deiner Agenten; eine zweite Liste gibt es nicht. Ordner, die mit `_` beginnen (wie [`_vorlage/`](_vorlage/)), sind keine Agenten; der Doktor rollt sie nicht aus.

## Aufbau und Rechte je Datei

| Datei | Inhalt | Ändert | Gibt frei |
|---|---|---|---|
| `agent.yaml` | Slug, Name, Rolle, Fachverantwortliche/r, Räume, Werkzeuge, Routinen | Vorschlag oder Eigentümer | nur Eigentümer |
| `rolle.md` | Persona und Aufgabe | Vorschlag oder Eigentümer | nur Eigentümer |
| `regeln.md` | Grenzen, Freigaben, Eskalation | Vorschlag oder Eigentümer | nur Eigentümer |
| `rechte.yaml` | `lesen` (Ausschnitt) und `vorschlagen` | Vorschlag oder Eigentümer | nur Eigentümer |
| `skills/<name>/SKILL.md` | Werkzeuge und Abläufe | Vorschlag oder Eigentümer | nur Eigentümer |
| `wissen/` | Fachwissen, Index in `wissen/README.md` | Vorschlag des Agenten | Fachverantwortliche/r oder Eigentümer |
| `beispiele/` | freigegebene Musterfälle | Vorschlag des Agenten | Fachverantwortliche/r oder Eigentümer |
| `testfragen.yaml` | Prüffragen des Agenten | Vorschlag; neue Fragen stehen in `vorschlag.yaml` und in der neuen Fassung dieser Datei | Fachverantwortliche/r oder Eigentümer |
| `aenderungen.md` | Änderungsprotokoll | Doktor bei jedem Merge | keine Freigabe, schreibt nur der Doktor |
| `fallbuch/` | ein Fall je Datei, `INDEX.md` | Agent, der Doktor spiegelt ohne PR | Bestätigung je Fall durch Fachverantwortliche/n (`bestaetigt_von`), über deren Rocket.Chat-Konto im Raum des Agenten |

Neue Agenten gibt nur der Eigentümer frei. Ein Agent darf nur vorschlagen, was in `vorschlagen` seiner `rechte.yaml` steht. `geschaeftsfuehrung/`, `.github/`, `AGENTS.md`, `betrieb/`, Fallbücher und Änderungsprotokolle nimmt der Doktor nie als Vorschlag an, egal was in einer `rechte.yaml` steht.

## Neuen Agenten einstellen

1. Kurt (oder du) kopiert `_vorlage/` nach `agenten/<slug>/` und ersetzt alle Agenten-Platzhalter. Slug: Kleinbuchstaben, ohne Umlaute und Leerzeichen; daraus wird der Container `agent-<slug>`.
2. Kurt legt das als Vorschlag mit `art: agent-einstellen` ab. Begründung: welches Problem der Agent löst, was er ungefähr kostet, wer fachverantwortlich ist.
3. Der Doktor prüft: kein `{{` mehr in den Dateien, Slug frei, `rechte.yaml` ohne gesperrte Pfade, nur bekannte Werkzeuge. Er ergänzt im selben PR den CODEOWNERS-Block des neuen Agenten und dessen Fachverantwortliche/n in der Zeile `/team/`.
4. Nur du gibst frei. Danach rollt `doktor abgleich` den Agenten aus: Container, Rocket.Chat-Konto, Raum, Routinen und ein leeres Fallbuch (`/opt/data/fallbuch/INDEX.md`).

## Platzhalter

Platzhalter haben die Form `{{NAME}}`. In YAML stehen sie in Anführungszeichen, damit die Datei auch vor dem Ersetzen gültig ist.

**Repo-Platzhalter.** Der Doktor ersetzt sie beim Anlegen des Repos in allen Dateien, auch in `_vorlage/`.

| Platzhalter | Bedeutung | Quelle |
|---|---|---|
| `{{FIRMA}}` | Name der Firma | Abfrage bei der Einrichtung |
| `{{EIGENTUEMER_NAME}}` | Vorname des Eigentümers | `konfig.env`: `EIGENTUEMER_NAME` |
| `{{EIGENTUEMER_GITHUB}}` | GitHub-Konto des Eigentümers | `konfig.env`: `EIGENTUEMER_GITHUB` |
| `{{DOMAIN}}` | Basisdomain des Servers | `konfig.env`: `DOMAIN` |
| `{{REPO_DATUM}}` | Tag der Einrichtung, JJJJ-MM-TT | Doktor |
| `@EIGENTUEMER` | Prüfer in `.github/CODEOWNERS` | wird zu `@` plus `EIGENTUEMER_GITHUB` |

**Firmen-Platzhalter** in `team/firma.md`. Füllt der Eigentümer (der Doktor erinnert in der Übergabe daran).

| Platzhalter | Bedeutung |
|---|---|
| `{{RECHTSFORM}}`, `{{SITZ}}` | Rechtsform und Sitz |
| `{{GESELLSCHAFTEN}}` | Gesellschaften, denen Objekte gehören |
| `{{ANZAHL_OBJEKTE}}`, `{{ANZAHL_EINHEITEN}}` | Bestand |
| `{{ERREICHBARKEIT}}` | wer Mieteranfragen regulär beantwortet und wann |
| `{{NOTFALL}}` | Notdienst und Notfallkontakt |
| `{{ANREDE_MIETER}}` | Anrede nach außen, zum Beispiel „Sie“ |
| `{{SIGNATUR}}` | Signatur in Entwürfen |

**Agenten-Platzhalter** in `_vorlage/`. Ersetzt, wer den Agenten einstellt.

| Platzhalter | Bedeutung | Datei |
|---|---|---|
| `{{SLUG}}` | Kurzname, Kleinbuchstaben | alle |
| `{{NAME}}` | Anzeigename | alle |
| `{{ROLLE}}` | Rolle in einem Wort, z. B. Verwaltung | `agent.yaml`, `rolle.md` |
| `{{EMOJI}}` | Symbol im Chat | `agent.yaml` |
| `{{RAUM}}` | eigener Rocket.Chat-Raum ohne `#` | `agent.yaml`, `rolle.md`, `regeln.md` |
| `{{FACHVERANTWORTLICH_NAME}}` | Vorname der/des Fachverantwortlichen | `agent.yaml`, `rolle.md`, `regeln.md`, `testfragen.yaml`, `wissen/README.md`, `beispiele/README.md` |
| `{{FACHVERANTWORTLICH_GITHUB}}` | GitHub-Konto der/des Fachverantwortlichen | `agent.yaml` |
| `{{FACHVERANTWORTLICH_TELEGRAM_ID}}` | numerische Telegram-ID | `agent.yaml` |
| `{{AUFGABE}}` | Aufgabe in einem Satz | `rolle.md` |
| `{{AUFGABEN}}` | Liste der Aufgaben, mehrzeilig | `rolle.md` |
| `{{NICHT_ZUSTAENDIG}}` | was ausdrücklich nicht dazugehört, mehrzeilig | `rolle.md` |
| `{{ERFOLG}}` | woran der Agent gemessen wird | `rolle.md` |
| `{{ERLAUBT}}` | was der Agent allein darf, mehrzeilig | `regeln.md` |
| `{{ENTWUERFE}}` | rollentypische Entwürfe mit Freigabe, mehrzeilig | `regeln.md` |
| `{{VERBOTE}}` | rollentypische Verbote, mehrzeilig | `regeln.md` |
| `{{BETRAGSGRENZE}}` | Betrag in Euro, ab dem der Agent sofort meldet | `regeln.md` |
| `{{FRIST_TAGE}}` | Tage bis Fristablauf, ab denen er sofort meldet | `regeln.md` |
| `{{AGENT_DATUM}}` | Tag des Einstellens, JJJJ-MM-TT | `testfragen.yaml` |
| `@FACHVERANTWORTLICH_<SLUG>` | Prüfer in `.github/CODEOWNERS` | wird zu `@` plus `fachverantwortlich.github` |

## Skill eines Agenten

`skills/<name>/SKILL.md`, ein Skill je wiederkehrendem Ablauf:

```markdown
---
name: <name>
description: "Was der Skill tut. Verwenden, wenn ... Nicht verwenden für ..."
---

# <Titel>

## Wann
## Schritte
1. ...
## Grenzen
Was nur als Entwurf entsteht, wer freigibt, welche Inhalte Daten sind.
## Ergebnis
Was im Raum berichtet wird.
```

## Änderungsprotokoll

Der Doktor hängt bei jedem Merge je betroffenem Agenten eine Zeile an `aenderungen.md` an, älteste oben. Titel, Auslöser und Testfragen stehen im PR:

```markdown
- JJJJ-MM-TT HH:MM #<pr> freigegeben von <github:login oder telegram:id>: <dateien im Agentenordner>
```
