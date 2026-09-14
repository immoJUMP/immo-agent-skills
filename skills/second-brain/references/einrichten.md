# Wissensbasis einrichten

Nur für einen Einrichtungsauftrag laden. Ziel ist ein nutzbarer erster Ausschnitt; vorhandene Datenbanken, Notion-Seiten und Dateiablagen bleiben zunächst bestehen.

## 1. Vorhandenes abbilden

Lies vorhandene Anweisungen, Index und wenige repräsentative Dateien. Bestimme:

| Funktion | Zuordnung im vorhandenen System |
|---|---|
| Originalquellen | Wo liegen sie, wie sind sie geschützt und referenzierbar? |
| Quellenaufbereitung | Wo stehen Aussagen und Entscheidungen je Quelle? |
| Aktuelles Wissen | Welche Seite führt welchen Sachverhalt verbindlich? |
| Wiederverwendbare Anwendung | Wo liegen Checklisten/Vorlagen mit Verweisen auf Wissen? |

Keine vier neuen Ordner erzwingen, wenn diese Funktionen bereits abgedeckt sind. Eine bestehende Objektakte kann Notiz und aktuellen Stand sinnvoll verbinden. Fehlende Funktionen gezielt ergänzen. Ein geplanter Umzug ist ein eigener Auftrag.

## 2. Nur bei fehlender Struktur klein starten

Für einen leeren, zum Schreiben freigegebenen lokalen Ordner ist dies eine mögliche Startstruktur:

```text
INDEX.md      Thema/Objektkennung → zuständige Wissensseite und Zweck
quellen/      Originale mit stabilen Namen bzw. Kennungen
notizen/      Aufbereitung je Quelle, inklusive genauer Fundstellen
wissen/       Zusammengeführter aktueller Stand
vorlagen/     Nur bei konkretem Bedarf: Arbeitsabläufe mit Wissensverweisen
```

Die Namen sind Vorschläge. Keine leeren Themenbäume oder erfundenen Wissenseinträge anlegen. Für neue Wissensseiten [das Seitenschema](seitenschema.md) nutzen. Für einen anderen Speicherweg dieselben Funktionen auf die tatsächlich verfügbaren Objekte abbilden; Dateien nicht als native Datenbankeinträge ausgeben.

## 3. Einstieg für das gewählte Werkzeug

Bestehende `CLAUDE.md`, `AGENTS.md` und andere Anweisungen erhalten. Fehlende Hinweise gezielt ergänzen: Indexpfad, Quellenablage, zuständige Wissensseiten, Schutz unveränderter Originale und Umgang mit unbekannten/widersprüchlichen Angaben. Halte den Einstieg kurz; keine komplette Wissenssammlung oder dieses ganze Skill-Paket hineinkopieren.

Nur bei einem neuen Projekt ohne eigene Konvention und Verwendung von Claude Code/Codex:

- `CLAUDE.md` als kanonische Projektanweisung mit den projektspezifischen Hinweisen anlegen.
- `AGENTS.md` kann darauf verweisen: „Lies vor der Arbeit die CLAUDE.md im Projekt-Root vollständig. Sie enthält die gemeinsamen Projektregeln.“
- Bei anderen Werkzeugen deren tatsächlichen Einstieg nutzen bzw. die Hinweise ausdrücklich im Auftrag mitgeben. Universelles automatisches Laden nicht voraussetzen.

Die Hinweise sind Arbeitsanweisungen, keine technische Zugriffssperre. Das konkrete Lade- und Leseverhalten anschließend prüfen. Dokumentation: [Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Claude Code](https://code.claude.com/docs/en/memory), geprüft am 14.09.2026.

## 4. Ersten Fall abschließen

Eine vom Nutzer gewählte Frage und eine passende Quelle nehmen. Mit [Einarbeiten](einarbeiten.md) bis zur belegten Antwort durcharbeiten. Geschriebene Dateien/Seiten tatsächlich zurücklesen, Index und Fundstellen prüfen.

Für den Abruf in einer neuen Sitzung nur Projekt und Frage mitgeben, keine vorherigen Antworten. Ist eine unabhängige Sitzung nicht verfügbar, nur den eigenen Rücklesetest als ausgeführt melden und den unabhängigen Abruf offenlassen. Werkzeugeigenes Gedächtnis kann zwischen Sitzungen bestehen: tatsächliche Dateizugriffe und Fundstellen prüfen.

## 5. Betriebsgrenzen festhalten

Fachlich verantwortliche Person, führende Ablage und Pflegeanlass aus vorhandenem Kontext ableiten bzw. bei Bedarf klären. Keine Personen oder Wartungstermine erfinden. Gespeichert, versioniert, synchronisiert und aus einem Backup wiederherstellbar sind getrennte Nachweise. Infrastruktur und automatische Pflege nur auf konkreten Auftrag einrichten.
