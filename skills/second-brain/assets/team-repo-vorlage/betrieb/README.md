# Betrieb

Wie der Agenten-Server läuft. Der Doktor schreibt, du liest. Agenten lesen hier nur, wenn ihre `rechte.yaml` es erlaubt (normalerweise nur Kurt). Freigabe für Änderungen an dieser Datei: nur Eigentümer.

## Adressen

| Dienst | Adresse |
|---|---|
| Chat (Rocket.Chat) | https://chat.{{DOMAIN}} |
| Dashboards und veröffentlichte Dateien | https://dash.{{DOMAIN}} |
| MietJUMP | https://miet.{{DOMAIN}} |

Zugangsdaten stehen nie hier, sondern nur auf dem Server in `geheim/geheim.env`.

## Logbuch

Jeder `doktor`-Befehl schreibt einen Eintrag. Format und Lesehilfe: [logbuch/README.md](logbuch/README.md).

## Die wichtigsten Befehle (auf dem Server)

| Wenn | Befehl |
|---|---|
| Kurzer Überblick | `doktor status` |
| Ist alles gesund? | `doktor check` |
| Etwas ist rot | `doktor reparieren` |
| Vorschläge abholen, Ausschnitte neu rendern | `doktor abgleich` |
| PR freigeben | `doktor freigeben <pr> --von github:<login>` oder `--von telegram:<id>` |
| Sicherung | `doktor sichern` |

Vollständige Liste: Anleitung des Skills `agenten-doktor`.
