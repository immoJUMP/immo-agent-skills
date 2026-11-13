# Objekte und Einheiten

Eine Datei je Objekt: `<kennung>.md`. Hier stehen stabile Objektfakten, die mehrere Agenten brauchen. Mieter, Mieten, Zahlungen und Verträge führt MietJUMP; hier stehen davon höchstens Verweise.

## Kennungen

- Objektkennung wie im führenden System (MietJUMP). Gibt es dort keine, vergibt der Eigentümer eine kurze, stabile Kennung, zum Beispiel `OBJ1`.
- Einheiten: `<objekt>-WE<nn>` für Wohnungen, `-GE<nn>` für Gewerbe, `-ST<nn>` für Stellplätze, zum Beispiel `OBJ1-WE03`.
- Agenten nennen Mieter über die Einheitskennung, nicht über den Namen.

## Index

| Kennung | Adresse | Gesellschaft | Einheiten | Datei |
|---|---|---|---|---|

Neues Objekt: Datei und Zeile im selben Vorschlag. Keine Einträge ohne Beleg.

## Format einer Objektdatei

```markdown
---
thema: objekt-<kennung>
sources:
  - "<Beleg: Kaufvertrag, Teilungserklärung, Bestätigung im Raum mit Datum>"
status: draft
verantwortlich: <slug>
stale_after: JJJJ-MM
---

# <Kennung>: <Straße Nr>, <PLZ Ort>

## Eckdaten
| Feld | Wert | Quelle |
|---|---|---|
| Gesellschaft (Eigentümerin) | | |
| Einheiten (WE, GE, ST) | | |
| Heizung und Warmwasser | | |
| Umlageschlüssel Nebenkosten | | |
| Hausmeister, Notdienst | | |
| Versorger | | |

## Besonderheiten
## Offene Punkte
```

Felder ohne Beleg bleiben leer und stehen unter „Offene Punkte“.
