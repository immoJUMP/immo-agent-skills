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

## Entscheidungen

Für datierte Entscheidungen eine eigene Datei je Entscheidung: `entscheidungen/JJJJ-MM-TT-slug.md`, dazu eine Zeile im Index des Ordners. Die Entscheidung erklärt das Warum. Die Regel, die daraus folgt, steht an ihrem zuständigen Ort und verweist auf die Entscheidung; sie wird nicht in die Entscheidung kopiert.

```markdown
# ENTSCHEIDUNG ALS SATZ

**Datum:** JJJJ-MM-TT
**Status:** vorgeschlagen | entschieden | ersetzt durch JJJJ-MM-TT-slug.md
**Entschieden von:** ROLLE
**Gilt für:** FIRMA / OBJEKT / BEREICH

## Entscheidung
Was gilt ab wann.

## Warum
Begründung und Belege mit Fundstelle.

## Alternativen
Verworfene Optionen und Grund.

## Folgen
Was sich ändert, wo die daraus folgende Regel steht, Risiken, nächste Schritte.

## Neu bewerten wenn
Konkrete Auslöser: Zahl, Datum, Ereignis.

## Referenzen
- QUELLE
```

- `Status` nur aus tatsächlicher Entscheidung setzen. Ein Vorschlag bleibt `vorgeschlagen`, bis die zuständige Person entschieden hat.
- Überholte Entscheidungen nicht löschen und nicht umschreiben: Status `ersetzt durch` mit Verweis auf die neue Datei.
- Leere Abschnitte weglassen; fehlende entscheidende Angaben als offen nennen.
- Die Datei `assets/team-repo-vorlage/entscheidungen/_vorlage.md` folgt dieser Vorlage. Bei einer Änderung hier auch dort anpassen.
