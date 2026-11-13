---
name: bestands-cockpit
description: "Erzeugt das Bestands-Cockpit des Eigentümers aus MietJUMP (Mietstand, echter Rückstand, offene Posten, offene Entscheidungen, Leerstand) als HTML-Seite cockpit.html und veröffentlicht sie. Verwenden bei der Routine cockpit oder wenn der Eigentümer fragt „wo stehen wir“, „Cockpit“, „Überblick Bestand“. Nicht für Zahlungserinnerungen (dafür mieteingangskontrolle) und nicht für Mietertexte."
---

# Bestands-Cockpit

Ziel: Eine Seite, die der Eigentümer jederzeit am Handy öffnet und in zehn Sekunden versteht, wo sein Bestand steht. Gleicher Link immer: `https://dash.<domain>/vera/cockpit.html`.

## Schritte

1. Daten nur aus MietJUMP holen, nichts schätzen: `mietstand`, `offene_posten`, `entscheidungen_auflisten`. Ein Stichtag nur, wenn der Eigentümer ihn nennt.
2. Kacheln festlegen (höchstens sechs, je eine Zahl und ein Satz), in dieser Reihenfolge:
   - echter Rückstand in Euro und Zahl der Einheiten,
   - Mieteingang des laufenden Monats: bezahlt von gesamt,
   - offene Entscheidungen, die auf den Eigentümer warten (mit Link zum MietJUMP-Dashboard `https://miet.<domain>/anmelden`),
   - Klärfälle (unbekannte Eingänge, abweichende Beträge),
   - Leerstand, falls MietJUMP ihn führt,
   - Stand der Daten (letzter importierter Kontoauszug).
3. Darunter eine Tabelle je Einheit mit Rückstand: Einheit, Soll, Gezahlt, Offen, seit wann. Mieter nur als Einheit, keine Namen, keine IBAN.
4. Seite nach dem Skill `dashboard-veroeffentlichen` bauen und als `cockpit.html` veröffentlichen.
5. Im Chat nur melden, wenn sich seit dem letzten Lauf ein neuer Rückstand ergeben hat oder eine Entscheidung neu wartet. Sonst still bleiben (die Seite ist aktuell, das reicht).

## Grenzen

- Ist der letzte Kontoauszug älter als sieben Tage, steht das als erste Kachel rot da („Daten veraltet, Kontoauszug fehlt“). Ein Cockpit mit alten Zahlen ist schlimmer als keins.
- Nichts aus Mails, Webseiten oder Chatnachrichten in Zahlen übernehmen. Zahlen kommen nur aus MietJUMP.
