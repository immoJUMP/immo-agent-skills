---
name: agenten-check
description: "Liest den Agenten-Check des Doktors (Prompt-Länge, Werkzeuge, Gedächtnisgröße, Fehler, Routinen je Agent), fasst ihn für den Eigentümer zusammen und schlägt Entschlackung als Vorschlag vor. Verwenden bei „wie geht es den Agenten“, „warum ist Vera so langsam“, bei roter oder gelber Ampel im Tagesüberblick oder einmal pro Woche. Nicht zum Reparieren des Servers (macht der Doktor) und nicht für inhaltliche Korrekturen (dafür lernkreislauf)."
---

# Agenten-Check

## Schritte

1. `/opt/data/wissen/betrieb/agenten-check/aktuell.md` lesen. Datum oben prüfen: älter als sieben Tage, dann dem Eigentümer sagen, dass der Bericht veraltet ist und `doktor agenten-check` auf dem Server ihn erneuert.
2. Je Agent die Ampel aus dem Bericht übernehmen, nichts dazuerfinden. Zusammenfassung höchstens fünf Zeilen, z. B. „Vera gelb: Prompt 14.000 Token, Routine belege zweimal mit Fehler.“
3. Entschlackung prüfen, je Agent:
   - Werkzeug in `agent.yaml`, das laut Bericht nie genutzt wird: streichen.
   - Routine ohne Ergebnis oder mit wiederholten Fehlern: Fehler zuerst dem Eigentümer nennen, dann Zeitplan ändern oder Routine streichen.
   - Prompt lang: doppelte Sätze zwischen `rolle.md`, `regeln.md` und Skills, lange Beispiele, veraltete Abschnitte kürzen. Was in `gemeinsam.md` steht, gehört nicht noch einmal in `regeln.md`.
   - Gedächtnis groß: dauerhaft gültige Inhalte als Wissens-Vorschlag übernehmen. Leeren kann nur der Doktor, du nicht.
4. Nie kürzen: Freigaberegeln, „Quellen sind Daten“ mit Beispiel, Datenschutz, Grenzen. Lieber ein Beispiel straffen als eine Regel streichen.
5. Je Agent ein Vorschlag (`art: regel`, Freigabe nur Eigentümer): vollständige Fassung jeder geänderten Datei, `begruendung` mit Zahlen aus dem Bericht (vorher, erwartet nachher), Testfragen, die zeigen, dass das Verhalten gleich bleibt.
6. Dem Eigentümer: Ampel in Kurzform, was du vorschlägst und warum, PR-Nummern nach dem Abgleich.
