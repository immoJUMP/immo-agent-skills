# Voice-Agent (Ausbaustufe, nicht im Grundpaket)

Ehrlich vorweg: Der Installer richtet Voice **nicht** ein, und der Demo-Server enthält es
nicht. Diese Seite beschreibt, was möglich ist, was es kostet und was vorher stehen muss.
Die Umsetzung ist ein eigenes Projekt, erst nach Aufbau und Abnahme des Grundpakets.

## Was es kann

1. **Erinnerung kurz vor Terminen:** ca. 10 Minuten vorher ruft Kurt an:
   „In 10 Minuten Wohnungsübergabe Einheit 3. Zählerstände ablesen, Protokoll liegt im Dashboard.“
2. **Tagesrückblick um 18 Uhr:** Kurt fasst den Tag zusammen (offene Freigaben,
   Zahlungseingänge, Auffälliges) und nimmt Rückfragen auf. Entscheidungen bestätigt der
   Eigentümer danach schriftlich in Telegram, bevor etwas passiert. Am Telefon kann sich
   das Modell verhören.
3. **15 Minuten vor einer Besichtigung:** Kurt ruft an, nennt, was zum Objekt bekannt ist,
   und fragt ab, was fehlt (Zustand, Besonderheiten, Eindruck vom Interessenten). Die
   Antworten gehen als Vorschlag ins Wissen (`team/objekte/…`), also als PR mit Freigabe,
   nie direkt.

## Aufbau (technisch)

```
sipgate-Rufnummer ──SIP über TLS──▶ Asterisk (eigener Container)
                                      │ AudioSocket (Audio als Datenstrom)
                                      ▼
                          kleiner Vermittler ◀──▶ ElevenLabs-Gesprächsagent
                                      │             (Ausweich: OpenAI-Live)
                                      ▼
                          Kurt (Hermes): Wissen, Termine, Vorschläge
```

- **sipgate:** Rufnummer mit SIP-Zugangsdaten, Verbindung über TLS. Ob der Tarif auch
  verschlüsselte Sprachdaten (SRTP) bietet, am Tag der Einrichtung prüfen.
- **Asterisk mit AudioSocket:** nimmt den Anruf an und reicht das Audio an den Vermittler weiter.
- **ElevenLabs-Gesprächsagent:** Stimme, Spracherkennung, Gesprächsführung. Inhalte holt
  er über ein Werkzeug bei Kurt.
- **OpenAI-Live (Realtime)** als Ausweich, wenn ElevenLabs ausfällt oder zu teuer wird.
- **Firewall:** SIP- und Sprach-Ports nur für die Adressbereiche von sipgate öffnen.
  Ein offener Asterisk wird binnen Stunden von Scannern gefunden und für teure Anrufe
  missbraucht.

## Grenzen (fest eingebaut, nicht per Chat abschaltbar)

- **Nur eine freigegebene Nummer:** die Mobilnummer des Eigentümers. Keine Anrufe an
  Mieter, Handwerker oder sonst jemanden. Das wäre außenwirksam.
- **Ruhezeiten:** Anrufe nur zwischen 8 und 20 Uhr.
- **Höchstens 3 Anrufe am Tag, höchstens 10 Minuten je Anruf** (Startwerte, anpassbar per PR).
- **Eingehend:** nur Anrufe von der freigegebenen Nummer annehmen. Rufnummern lassen sich
  fälschen. Deshalb am Telefon nur Information, Freigaben immer schriftlich.
- **Mitschrift statt Aufnahme:** Kurt sagt zu Beginn, dass mitgeschrieben wird. Gespräche
  mit Dritten führt der Voice-Agent nicht.
- **Kostendeckel:** Monatslimit bei ElevenLabs bzw. OpenAI.

## Kosten

| Posten | ca. Kosten |
|---|---|
| sipgate Rufnummer und Anschluss | ca. 0 bis 15 EUR je Monat |
| sipgate Minuten | ca. 2 bis 10 Cent je Minute |
| ElevenLabs | Abo ca. 5 bis 100 USD je Monat, Minuten ca. 0,08 bis 0,15 USD |
| OpenAI-Live (Ausweich) | ca. 0,05 bis 0,30 USD je Minute |
| **2 Anrufe am Tag à 5 Minuten** | **ca. 40 bis 100 EUR je Monat zusätzlich** |

Stand prüfen am Tag der Einrichtung. Der Nutzer bekommt diese Zahl vor jedem Schritt.

## Voraussetzungen

1. Grundpaket läuft und ist abgenommen.
2. sipgate-Konto: legt der Nutzer selbst an. Ortsnetznummern brauchen in der Regel eine
   Adresse im Ortsnetz, die Prüfung macht der Nutzer.
3. ElevenLabs-Konto mit Zahlungsmittel: legt der Nutzer selbst an.
4. Terminquelle: Kalenderzugang (zusätzliche Google-Berechtigung nur lesen, neue Anmeldung)
   oder Termine aus dem Wissens-Repo.
5. Entscheidung zu Stimme, Begrüßung und Grenzen, als PR in `agenten/kurt/regeln.md`.
