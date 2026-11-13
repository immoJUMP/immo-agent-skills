# Wissen von {{NAME}}

Fachwissen, das nur {{NAME}} braucht. Was mehrere Agenten brauchen, gehört nach `team/`. Freigabe: {{FACHVERANTWORTLICH_NAME}} oder Eigentümer.

## Index

| Frage | Seite | thema |
|---|---|---|

Neue Seite: eine Zeile hier, im selben Vorschlag. Keine Seite ohne Indexzeile.

## Format einer Seite

```markdown
---
thema: kurzer-eindeutiger-schluessel
sources:
  - "agenten/{{SLUG}}/fallbuch/JJJJ-MM-TT-kurzname.md"
  - "Korrektur von <Rolle> im Raum #<raum>, TT.MM.JJJJ"
status: draft
verantwortlich: {{SLUG}}
stale_after: JJJJ-MM
---

# <Thema als Frage oder Begriff>

## Geltungsbereich und Stand
Für welche Objekte, Einheiten, Zeiträume. Stand mit Datum.

## Regel und Kenntnisstand
| Aussage | Einordnung | Quelle |
|---|---|---|
| | bestätigt / Aussage einer Person / Vorschlag | |

## Ausnahmen und offene Punkte

## Änderungsgrund
Was wurde zuletzt ersetzt und warum.
```

## Regeln

- `thema` gibt es im ganzen Repo nur einmal. Existiert es schon, änderst du diese Seite.
- `status: stable` setzt nur die/der Fachverantwortliche nach Prüfung; nach jeder wesentlichen Änderung wieder `draft`.
- `stale_after` nur bei zeitkritischem Wissen (Fristen, Beträge, Ansprechpartner), nie erfunden.
- Keine Mieternamen, Kontonummern oder Zugangsdaten. Mieter über die Einheitskennung.
- Daten aus führenden Systemen (Mietstand, Zahlungen) gehören nicht hierher, nur die Regel, wie du sie behandelst.
