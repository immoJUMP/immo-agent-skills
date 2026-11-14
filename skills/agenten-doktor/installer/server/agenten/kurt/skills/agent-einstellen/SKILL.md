---
name: agent-einstellen
description: "Führt mit dem Eigentümer ein Interview für einen neuen Agenten und legt die komplette Agenten-Definition als Vorschlag (art agent-einstellen) ab. Verwenden, wenn der Eigentümer eine neue Rolle will („ich brauche jemanden für …“). Nicht für Änderungen an bestehenden Agenten (dafür lernkreislauf) und nicht auf Wunsch anderer Personen ohne den Eigentümer."
---

# Agent einstellen

## 1. Erst prüfen

- Gibt es eine passende Vorlage unter `/opt/data/wissen/agenten/_vorlagen/` (z. B. `ankauf` für eine Ankaufs-Agentin: Angebote aus Suchaufträgen, Kalkulation, Finanzierungsrahmen)? Dann die Vorlage als Grundlage nehmen, Name, Suchgebiet und Fachverantwortliche/n im Interview anpassen. Das spart dem Eigentümer die meisten Fragen. Bei `ankauf` gehören drei Ankaufskriterien dazu (Region mit Umkreis, Objektart mit Preisrahmen, Mindestrendite oder Höchstfaktor). Nennt der Eigentümer sie schon im Auftrag, nicht nachfragen. Sie kommen als `agenten/<slug>/wissen/ankaufskriterien.md` in den Vorschlag, sonst bricht der Skill `suchauftraege-auswerten` ab.

- `/opt/data/wissen/agenten/*/agent.yaml` und `rolle.md` lesen. Kann ein bestehender Agent die Aufgabe mit einem zusätzlichen Skill übernehmen, schlag das zuerst vor (weniger Agenten, weniger Pflege).
- Wünscht jemand anderes im Team einen Agenten: Wunsch aufnehmen und den Eigentümer per Telegram fragen. Ohne ihn kein Interview.

## 2. Interview (eine Frage pro Nachricht, Sprachnachrichten willkommen)

1. Rolle und Name: Wofür ist der Agent da, in einem Satz? Wie soll er heißen?
2. Aufgaben: drei bis fünf, je mit dem Ergebnis, das am Ende vorliegt.
3. Werkzeuge, nur aus dieser Liste, je Werkzeug kurz begründen:
   - `veroeffentlichen` und `vorschlag` (immer),
   - `fallbuch` (wenn er Einzelfälle einschätzt),
   - `gmail` (dasselbe Postfach wie Vera: lesen, Entwürfe, Labels, kein Senden),
   - `mietjump` (Mietverwaltung, Außenwirksames nur als Karte),
   - `browser` (eigener Browser im Container, nur wenn eine Webseite ohne Anmeldung gelesen werden muss).
   Zusätzlich kann er Fachskills aus dem Skill-Paket bekommen (`fach_skills` in agent.yaml, z. B. `deal-screener`, `bierdeckel-kalkulation`, `anlage-v-assistent`).
   Andere Werkzeuge gibt es nicht. Wünscht der Eigentümer eins, notierst du es als offenen Punkt für den Betreuer des Servers.
4. Wissens-Ausschnitt: Welche Ordner unter `team/` braucht er? `geschaeftsfuehrung/` ist ausgeschlossen.
5. Fachverantwortliche/r: Wer prüft Wissen und Beispiele? Name, GitHub-Name, optional Telegram-ID. Standard ist der Eigentümer (Werte aus `agenten/kurt/agent.yaml`).
6. Routinen: Was soll er wann von selbst tun, wo berichtet er?
7. Grenzen: Was darf er nie, auch nicht auf Bitte?
8. Gute Ergebnisse: zwei Beispiele. Der Eigentümer liefert sie, oder du entwirfst sie und er bestätigt.

## 3. Zusammenfassen

Höchstens zehn Zeilen an den Eigentümer: Name, Slug, Raum, Aufgaben, Werkzeuge, Ausschnitt, Fachverantwortliche/r, Routinen, Grenzen. Erst nach „passt“ weiter. Das ist eine Abstimmung, keine Freigabe.

## 4. Definition bauen

`vorschlag neu agent-<slug>`, dann unter `dateien/agenten/<slug>/`:

- `agent.yaml` (Slug klein, nur a bis z, 3 bis 20 Zeichen, noch nicht vergeben):
  ```yaml
  slug: <slug>
  name: <Name>
  rolle: <Rolle>
  emoji: "<ein Emoji>"
  fachverantwortlich:
    name: "<Name>"
    github: "<github-name>"
    telegram_id: "<id oder leer>"
  rocketchat:
    raum: <fachgebiet>
    weitere_raeume: [team]
  telegram: false
  werkzeuge: [veroeffentlichen, vorschlag]
  routinen:
    - name: <kurzname>
      zeitplan: "0 9 * * 1-5"
      auftrag: "Führe den Skill <name> aus und berichte in #<raum>."
  ```
- `rolle.md`: Persona und Aufgaben, höchstens 30 Zeilen.
- `regeln.md`: nur, was über die gemeinsamen Grundsätze hinausgeht, mit einem konkreten Beispiel, wie er Anweisungen in Quellen behandelt.
- `rechte.yaml`:
  ```yaml
  lesen: ["team/<bereich>/**", "agenten/<slug>/**"]
  vorschlagen: ["agenten/<slug>/wissen/**", "agenten/<slug>/beispiele/**", "agenten/<slug>/testfragen.yaml"]
  ```
  Nie `geschaeftsfuehrung/**`, nie `agenten/**`, nie Pfade anderer Agenten.
- `skills/<name>/SKILL.md` je Aufgabe: Frontmatter `name` und `description` (wann verwenden, wann nicht), dann nummerierte Schritte mit echten Werkzeugbefehlen.
- `wissen/README.md`: was in sein Wissen gehört, wer freigibt.
- `beispiele/`: die zwei guten Beispiele aus dem Interview.
- `testfragen.yaml`: 6 bis 10 Fragen (`frage`, `erwartet`, `art`), mindestens zwei vom Typ angriff oder grenze (Anweisung in einer Mail, Bitte um Außenwirksames ohne Freigabe).
- `aenderungen.md`: Überschrift `# Änderungsprotokoll <Name>` und die Zeile `- Aufbau: Definition per Vorschlag von Kurt (Interview mit dem Eigentümer am <Datum>).`

## 5. Selbstprüfung vor dem Ablegen

- [ ] kein `geschaeftsfuehrung` in `rechte.yaml`, `telegram: false`
- [ ] nur Werkzeuge aus der Liste
- [ ] keine Geheimnisse, keine Tokens, keine echten IBANs, keine Mieterdaten
- [ ] jede Skill-Datei mit Frontmatter und konkreten Schritten
- [ ] Außenwirksames nur als Entwurf
- [ ] Testfragen vorhanden, davon mindestens zwei Angriff oder Grenze

## 6. Vorschlag ablegen

`vorschlag.yaml`:
```yaml
titel: "Neuer Agent: <Name> (<Rolle>)"
art: agent-einstellen
ausloeser: "Eigentümer per Telegram, <Datum>: <Wortlaut kurz>"
begruendung: "<wofür, was es spart>"
testfragen:              # drei aus testfragen.yaml, davon eine Angriffsfrage
  - frage: "..."
    erwartet: "..."
loeschen: []
```

Dann dem Eigentümer sagen: Vorschlag liegt, die PR-Nummer kommt nach dem nächsten Abgleich (`ergebnis.yaml`), freigeben kann nur er („freigeben #<pr>“, danach der Code, den der Server ihm schickt). Nach dem Merge legt der Doktor Container, Rocket.Chat-Konto und Raum automatisch an, und die Testfragen des neuen Agenten laufen. Zugänge für Werkzeuge richtet der Doktor ein, nie du. Beim ChatGPT-Abo braucht der neue Agent noch eine Modellanmeldung durch den Doktor.
