---
thema: firma
sources:
  - "Angaben des Eigentümers bei der Einrichtung, {{REPO_DATUM}}"
status: draft
verantwortlich: eigentuemer
---

# {{FIRMA}}

Stammdaten, die alle Agenten brauchen. Platzhalter füllt der Eigentümer; solange einer offen ist, nennen Agenten den Wert als unbekannt und raten nicht.

## Eckdaten

| Feld | Wert |
|---|---|
| Firma und Rechtsform | {{FIRMA}} {{RECHTSFORM}} |
| Sitz | {{SITZ}} |
| Eigentümerin der Objekte (Gesellschaften) | {{GESELLSCHAFTEN}} |
| Bestand | {{ANZAHL_OBJEKTE}} Objekte, {{ANZAHL_EINHEITEN}} Einheiten |
| Eigentümer und Entscheider | {{EIGENTUEMER_NAME}} |

Welches Objekt zu welcher Gesellschaft gehört, steht je Objekt in [objekte/](objekte/README.md).

## Erreichbarkeit

| Für | Wer und wie |
|---|---|
| Mieteranfragen, regulär | {{ERREICHBARKEIT}} |
| Notfälle (Wasser, Heizung, Strom, Schließanlage) | {{NOTFALL}} |

## Ansprache nach außen

- Anrede gegenüber Mietern und Dienstleistern: {{ANREDE_MIETER}}
- Signatur in Entwürfen: {{SIGNATUR}}
- Jeder Text nach außen ist ein Entwurf, bis ein Mensch ihn freigibt (`AGENTS.md`, Regel 2).

## Offene Punkte

Platzhalter, die noch `{{` enthalten, meldet `doktor check` als offen.
