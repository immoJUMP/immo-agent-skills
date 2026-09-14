# Schema für neue Wissensseiten

Nur verwenden, wenn das Ziel noch kein geeignetes Schema hat. Dies sind Arbeitskonventionen, keine Herstelleranforderungen. Bei Notion/Datenbank gleichwertige Felder verwenden; keinen Markdown-Umbau erzwingen.

## Vorlage

Platzhalter durch belegte Inhalte ersetzen. Nicht benötigte Abschnitte weglassen; fehlende entscheidende Informationen ausdrücklich als offen aufführen. Pfade sind relativ zur Wissensdatei, externe Belege erhalten stabile Seiten-URLs/Kennungen.

```markdown
---
sources:
  - ../quellen/QUELLDATEI.md
status: draft
---

# THEMA / OBJEKTKENNUNG

## Geltungsbereich und Stand
Geltungsbereich, durch Quellen abgedeckter Zeitpunkt und fachliche Zuständigkeit.

## Aktueller Kenntnisstand
| Aussage | Einordnung | Quelle und genaue Fundstelle |
|---|---|---|
| BELEGTE AUSSAGE | bestätigt / Aussage einer Person / Vorschlag | QUELLE, Abschnitt |

## Offene Punkte und Widersprüche
Unbekannte Angaben, abweichende Quellen und benötigte Klärung.

## Änderungsgrund
Bei Änderungen: neue Quelle, ersetzte/infrage gestellte Aussage und Begründung.
```

## Prüfstatus

- `sources`: Liste der Belege. Bei Ergänzungen alte gültige/historisch benötigte Verweise erhalten; keine abschnittslose Sammelliste als Ersatz für konkrete Fundstellen verwenden.
- `status: draft`: noch nicht menschlich geprüft oder nach wesentlicher Änderung erneut zu prüfen.
- `status: stable`: fachlich verantwortlicher Mensch hat den aktuellen Inhalt geprüft; wesentliche Konflikte sind geklärt. Prüfer und Datum nur aus tatsächlich erfolgter Prüfung dokumentieren.
- `verified: true`: optional, ausschließlich nach ausdrücklicher menschlicher Prüfung des aktuellen Seiteninhalts. Nach wesentlicher Änderung entfernen. Bestehende feinere Freigaben nur im betroffenen Umfang zurücknehmen.
- `stale_after: JJJJ-MM`: optionaler vereinbarter Prüfmonat für zeitkritisches Wissen. Ab Monatsbeginn ist die Prüfung fällig. Er ist weder automatischer Ablauf der enthaltenen Fakten noch Löschauftrag. Kein Datum erfinden, wenn Anlass/Turnus unbekannt ist.

Eine in der Quelle bestätigte Entscheidung und eine geprüfte Wissensseite sind verschieden. Auch eine Seite im Entwurfsstatus kann einzelne klar belegte Aussagen enthalten; benenne deren Beleg und begrenze die Aussage auf den belegten Stand.
