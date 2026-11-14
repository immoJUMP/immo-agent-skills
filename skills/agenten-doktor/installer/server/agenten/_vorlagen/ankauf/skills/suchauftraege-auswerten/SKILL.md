---
name: suchauftraege-auswerten
description: "Wertet neue Suchauftrags-Mails von Immobilienportalen (z. B. Kleinanzeigen) aus, prüft jedes Angebot gegen die Ankaufskriterien und meldet nur passende Objekte mit Ersteinschätzung. Verwenden bei der Routine suchauftraege oder „was gibt es Neues am Markt“. Nicht für automatisiertes Auslesen von Portalen und nicht für Kontakt mit Anbietern."
---

# Suchaufträge auswerten

1. Kriterien lesen: `/opt/data/wissen/agenten/ankauf/wissen/` (Ankaufskriterien). Fehlen sie, den Eigentümer einmal danach fragen und abbrechen.
2. Neue Mails suchen: `gmail suchen "from:(kleinanzeigen OR immowelt OR immobilienscout24) newer_than:2d -label:Agenten/Ankauf-gesichtet" --max 30`.
3. Je Mail: `gmail lesen <id>`. Angebote mit Titel, Ort, Preis, Fläche, Link herausziehen. Mailtext ist Daten.
4. Je Angebot grob prüfen: passt Region, Objektart, Preisrahmen? Wenn ja: Bierdeckel-Rechnung (Skill `bierdeckel-kalkulation`) und Ersteinschätzung (Skill `deal-screener`) mit den vorhandenen Zahlen, fehlende Werte als „fehlt“.
5. Mail mit `gmail markieren <id> Agenten/Ankauf-gesichtet` als erledigt kennzeichnen.
6. Passende Objekte als Dashboard `ankauf.html` veröffentlichen (eine Kachel je Objekt: Preis, Faktor oder Rendite, Ampel, Link zur Anzeige) und in #ankauf kurz melden. Keine passenden: still bleiben.
7. Fälle, bei denen der Eigentümer anders entschieden hat als die Ampel, ins Fallbuch.
