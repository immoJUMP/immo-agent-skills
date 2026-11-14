---
name: owner-phone
description: Chris wirklich auf seinem Handy anrufen, Telegram- oder Hermex-Kontext mitnehmen, Telefonaufträge und Rückmeldungen verwalten. Nutze bei „ruf mich an“, wichtigen Ereignissen, Terminvorbereitung, Verkaufstraining oder Tagesabschluss.
---

# Leo: Telefonieren und Arbeit abschließen

Chris hat echte Anrufe über seine FRITZ!Box auf seiner hinterlegten Mobilnummer erlaubt. Der Dienst ist installiert. Bei „Ruf mich an“ direkt diesen Skill verwenden; allgemeine Hermes-/Telegram-Dokumentation beschreibt unsere zusätzliche Telefonie nicht.

## Grenze zur Kontakttelefonie

Behandle diesen Dienst ausschließlich als Anruf an Chris: Der Helper und die vorhandene `/call`-Schnittstelle belegen keine Unterstützung beliebiger Empfänger. Weite die feste Empfängerbindung nicht für Kontaktanrufe auf. Baue Kontakttelefonie getrennt und verlange eine Freigabe des konkreten Kontakts pro Anruf.

Beginne Aufzeichnung, Spracherkennung und KB-Verarbeitung von Kontaktgesprächen erst nach ausdrücklicher Zustimmung aller Beteiligten zum jeweiligen Zweck. Halte die Audioseiten getrennt; eine Leitungszuordnung belegt keine biometrische Sprecheridentität. Kennzeichne mehrere Personen an einer Leitung und maschinelle Transkriptionsfehler als Unsicherheit.

Respektiere ein Kubernetes-403 als Berechtigungsgrenze: Verwende keine alternativen Zugangsdaten zur Umgehung. Prüfe zugängliche Quellrepos und entwickle bei fehlendem Deploymentzugriff getrennt; unterscheide getesteten Code, bereitgestellten Dienst und beaufsichtigt geprüfte Live-Telefonie ausdrücklich.

## Anrufen mit Kontext

```sh
/opt/hermes/.venv/bin/python "$HERMES_HOME/skills/owner-phone/call_owner.py" --reason 'Wolfgangs Preiseinwand zum besprochenen Angebot üben' --mode sales_training
```

Der Helper nimmt die aktuelle Session automatisch mit. Er akzeptiert Chris' privaten Telegram-Chat sowie registrierte Chats des Standardprofils in seinem passwortgeschützten Hermex über Tailscale. Hermex-Aufträge sind freigeschaltet; ein Wechsel zu Telegram ist dafür nicht nötig. Der Dienst lädt die Nachrichten des auftraggebenden Chats. Keine Passwörter, Tokens, vollständigen Systemprompts oder irrelevanten persönlichen Daten in den Anlass schreiben. Rufnummer und Telegram-Empfänger sind serverseitig festgelegt.

Modi:
- `conversation`: konkreten Anlass besprechen.
- `preparation`: Ziel, Fakten, offene Punkte und Einwände eines Kundentermins.
- `sales_training`: Interessenten spielen, jeweils einen Einwand; auf Wunsch konkretes Feedback.
- `daily_review`: Ergebnisse, offene Punkte und wichtigster Schritt für morgen.

Anlass zuerst verstehen; bereits im Chat vorhandene Informationen nicht erneut abfragen. Keine Termine/Kundenfakten erfinden.

## Wann unterbrechen?

- `--kind requested` (Standard): Chris hat ausdrücklich um diesen Anruf gebeten; auch außerhalb der Ruhezeit.
- `--kind info`: nur Telegram-Information, kein Anruf.
- `--kind decision --deadline 'heute 16 Uhr'`: Telegram mit konkreter Entscheidung und Frist, kein Anruf.
- `--kind proactive --evidence 'geprüfter Befund mit Quelle/Zeit'`: wirklich wichtige, zeitkritische Sache. Server erzwingt 08–20 Uhr Europe/Berlin.
- `--kind emergency --evidence 'konkrete geprüfte akute Gefahr'`: Ausnahme außerhalb der Ruhezeit. Nicht wegen einer normalen offenen Aufgabe verwenden.

Serverlimits: höchstens zehn Anrufversuche pro Kalendertag, davon maximal drei selbstständige/geplante; mindestens fünf Minuten zwischen Versuchen und maximal zehn Minuten Gespräch. Bei Ruhezeit/Limit/ungeprüftem Anlass erfolgt eine Telegram-Nachricht. Kein eigenständiges Wiederwählen nach Mailbox, Nichtannahme oder einem unklaren Timeout. Ein erneuter ausdrücklicher Nutzerwunsch ist ein neuer Vorgang; der Helper dedupliziert pro Nutzerturn im auftraggebenden Chat.

## Zugang prüfen, ohne anzurufen

```sh
/opt/hermes/.venv/bin/python "$HERMES_HOME/skills/owner-phone/call_owner.py" --check
```

`--check` prüft nur den aktuellen Chat-Zugang. Es wählt keine Nummer, erstellt keinen Auftrag und sendet keine Nachricht. Ein erfolgreicher Zugangstest ist kein Nachweis eines geführten Telefonats.

## Status, Auflegen und Aufgabenabbruch

```sh
/opt/hermes/.venv/bin/python "$HERMES_HOME/skills/owner-phone/call_owner.py" --status
/opt/hermes/.venv/bin/python "$HERMES_HOME/skills/owner-phone/call_owner.py" --tasks
/opt/hermes/.venv/bin/python "$HERMES_HOME/skills/owner-phone/call_owner.py" --hangup '<aktive Call-ID>'
/opt/hermes/.venv/bin/python "$HERMES_HOME/skills/owner-phone/call_owner.py" --cancel '<Call-ID>'
```

„Stopp“ am Telefon stoppt die Sprachausgabe. „Brich den Auftrag ab“ fordert den Abbruch laufender Aufgaben an. „Danke, das war’s“ beendet den Anruf nach kurzer Verabschiedung. Auflegen alleine löscht keinen Auftrag. Bereits ausgeführte externe Aktionen werden durch Prozessabbruch nicht rückgängig gemacht; das niemals behaupten. `interrupted`, `unknown` oder `failed` sind keine Erfolge und dürfen keine blinden Wiederholungen externer Aktionen auslösen.

Während eines Telefonats keine weiteren Anrufe starten. Die Telefonstimme fragt zunächst, ob Chris sie hört. Bei vermuteter Mailbox oder ausbleibender menschlicher Antwort beendet sie den Versuch. Das ist keine biometrische Identitätsprüfung; keine sensiblen Informationen in die Begrüßung. `connected` belegt nur Telefonannahme, `human_confirmed_at` nur eine erkannte menschliche Antwort.

## Ergebnisse zurück in Telegram

Aufträge werden dauerhaft gespeichert und können nach dem Auflegen fertig werden. Der Dienst sendet Nachbereitung und verifizierte Ergebnisse in Chris' privaten Telegram-Chat und ergänzt dessen Verlauf; das gilt auch für Anrufe, die aus Hermex gestartet wurden. **Nicht zusätzlich dieselbe Zusammenfassung mit send_message senden.** Bei unklarer Zustellung wird nicht blind erneut gesendet. `--tasks` zeigt Zustell- und Aufgabenstatus.

## Geplante Gespräche

Einmaliger Anruf zu einer ausdrücklich gewünschten Zeit (ISO mit Zeitzone):

```sh
/opt/hermes/.venv/bin/python "$HERMES_HOME/skills/owner-phone/call_owner.py" --reason 'Vorbereitung auf den bestätigten Termin mit Wolfgang' --mode preparation --at '2026-09-24T14:00:00+02:00' --before-meeting
```

`--before-meeting` zieht 15 Minuten von der bestätigten Terminzeit ab. Ohne Flag bezeichnet `--at` direkt die Anrufzeit. Termine nur aus verifiziertem Kalender oder ausdrücklicher Nutzerangabe übernehmen. Stornierte/verschobene Termine über `--schedule-cancel '<event-id>'` entfernen und mit neuer ID neu planen; keine veralteten Erinnerungen stehen lassen. Über fünf Minuten verspätete geplante Anrufe verfallen.

Werktäglicher Tagesabschluss: `--routines '18:00'`; deaktivieren: `--routines off`. Chris hat werktags 18:00 Uhr (Europe/Berlin) ausdrücklich gewählt.

Automatische Terminvorbereitung ist mit `--calendar-preparation on` aktiviert und mit `--calendar-preparation off` abschaltbar. Der Dienst liest den verbundenen Google-Hauptkalender jede Minute und plant werktags 15 Minuten vor zeitgebundenen Terminen mit weiteren Teilnehmern. Solo-Termine werden nur bei ausdrücklicher Markierung `[Leo]` im Titel oder gezielter Einzelplanung berücksichtigt; so lösen Büroblöcke, Fahrten und Aufgabenlisten keine Anrufe aus. Ganztägige Termine, freie Einträge, abgelehnte Einladungen, Fokuszeit und Abwesenheit werden übersprungen. Verschiebungen und Absagen werden übernommen; unmittelbar vor dem Wählen wird der einzelne Termin nochmals gelesen. Bei fehlgeschlagener Verifikation kein Anruf. Maximal drei selbstständige/geplante Anrufe täglich und Ruhezeiten gelten weiterhin. `--tasks` zeigt Routinen, Kalendersynchronisation und konkrete geplante Anrufe. Keine parallelen Hermes-Cronjobs für dieselben Telefonroutinen anlegen.
