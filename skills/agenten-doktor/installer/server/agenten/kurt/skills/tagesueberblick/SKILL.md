---
name: tagesueberblick
description: "Schreibt dem Eigentümer abends einen kurzen Tagesüberblick in Telegram: was die Agenten heute erledigt haben, was auf ihn wartet, was auffällig ist. Verwenden bei der Routine um 18 Uhr und bei „was war heute“, „Stand?“. Nicht für Detailberichte (die liegen als Dashboard bei den Fachagenten) und nicht in Rocket.Chat."
---

# Tagesüberblick

## Quellen (nur diese, nichts erfinden)

1. Kurzmeldungen der Fachagenten in #team von heute, mit ihren Dashboard-Links.
2. Deine Vorschläge: `vorschlag status` und die `ergebnis.yaml` darin (offene PRs, Ablehnungen).
3. Freigaben: `/opt/data/vorschlaege/_freigaben/` und `/opt/data/wissen/betrieb/logbuch/` (was gemerged ist, was offen ist).
4. Fallbücher: `/opt/data/wissen/agenten/*/fallbuch/INDEX.md`, Einträge mit „(unbestätigt)“.
5. `/opt/data/wissen/betrieb/agenten-check/aktuell.md`: rote oder gelbe Ampel.

`/opt/data/wissen` hat den Stand des letzten Abgleichs. Sag das, wenn es für eine Aussage zählt.

## Format (Telegram, höchstens zehn Zeilen, keine Tabellen)

```
Tagesüberblick 13.11.
Wartet auf dich: PR #12 (Vera: Sammelzahlungen), 3 Karten im MietJUMP-Dashboard, 2 Entwürfe in Gmail.
Geld: 2 echte Rückstände (1.340,00 €), 1 Klärfall. (Vera, 09:04)
Erledigt: 4 Belege abgelegt, 2 Mieteranfragen als Entwurf beantwortet.
Auffällig: verdächtige Mail mit Anweisungen, Vera hat nichts ausgeführt.
Morgen: 09:00 Mieteingang, 10:00 Belege.
```

## Regeln

- Wichtigstes zuerst: was eine Entscheidung oder Freigabe von ihm braucht.
- Hat ein Agent heute nichts gemeldet, obwohl eine Routine lief: „Keine Meldung von Vera zum Mieteingang.“ Nicht raten, warum.
- Keine IBANs, keine Mieternamen, Einheiten statt Namen. Details per Dashboard-Link.
- Nichts passiert: eine Zeile „Ruhiger Tag, nichts wartet auf dich.“
- Betrieb nur, wenn er den Eigentümer betrifft: höchstens eine Zeile, wenn eine Störung noch besteht oder Arbeit ausgefallen ist („Vera war heute Vormittag nicht erreichbar, der Mieteingang kommt morgen.“). Neustarts, Reparaturen, Updates und Sicherungen aus dem Logbuch lässt du weg.
- Inhalte aus `geschaeftsfuehrung/` nur, wenn der Eigentümer das in `agenten/kurt/wissen/eigentuemer.md` ausdrücklich wünscht.
