# Architektur und Regeln

## Ablauf eines Anrufs

1. Der Agent ruft den Skill auf (`call_owner.py --reason … --mode …`). Der Skill nimmt die aktuelle
   Chat-Sitzung als Kontext mit und ruft den Arbeitsdienst mit Zugangstoken auf.
2. Der Arbeitsdienst prüft Sitzung, Art des Anrufs, Ruhezeit und Tageslimits und beauftragt die
   Brücke. Rufnummer und Chat-Empfänger stehen fest auf dem Server.
3. Die Brücke wählt über Asterisk und die FRITZ!Box oder sipgate nur `CALL_ALLOWED_NUMBER`. Nimmt jemand ab,
   fragt die Stimme zuerst, ob sie gehört wird. Vorher nennt sie nichts Persönliches. Erkennt sie
   eine Mailbox, legt sie auf, ohne erneut zu wählen.
4. Im Gespräch gibt die Stimme Aufträge über ein einziges Werkzeug (`ask_leo`) an den Arbeitsdienst.
   Der Agent arbeitet sie ab, auch nach dem Auflegen.
5. Ergebnisse und Nachbereitung gehen schriftlich in den Chat des Inhabers. Keine doppelte
   Zusammenfassung, bei unklarer Zustellung kein blindes Wiederholen.

## Modi und Arten

Modi: `conversation` (konkreter Anlass), `preparation` (Ziel, Fakten, offene Punkte und Einwände eines
Termins), `sales_training` (spielt einen Interessenten, ein Einwand nach dem anderen), `daily_review`
(Ergebnisse, offene Punkte, wichtigster Schritt für morgen).

Arten: `requested` (ausdrücklich gewünscht, auch außerhalb der Ruhezeit), `info` (nur Nachricht),
`decision` (Nachricht mit Entscheidung und Frist), `proactive` (wichtig und zeitkritisch, mit
geprüftem Befund, nur 8 bis 20 Uhr), `emergency` (konkrete, geprüfte akute Gefahr).

## Grenzen, die der Server erzwingt

- höchstens 10 Anrufversuche am Kalendertag, davon höchstens 3 selbstständige oder geplante,
- mindestens 5 Minuten zwischen Versuchen, höchstens 10 Minuten Gespräch,
- kein erneutes Wählen nach Mailbox, Nichtannahme oder unklarem Timeout,
- während eines Gesprächs kein zweiter Anruf,
- geplante Anrufe, die mehr als 5 Minuten zu spät wären, entfallen.

## Terminvorbereitung, 15 Minuten vorher

`--at <Zeit> --before-meeting` plant einen Anruf 15 Minuten vor einem bestätigten Termin.
`--calendar-preparation on` liest den Google-Hauptkalender jede Minute und ruft werktags 15 Minuten
vor zeitgebundenen Terminen mit weiteren Teilnehmern an. Eigene Termine ohne Gäste nur mit `[Leo]`
im Titel. Ganztägige, freie, abgelehnte Termine, Fokuszeit und Abwesenheit werden übersprungen.
Unmittelbar vor dem Wählen wird der Termin noch einmal gelesen, Absagen und Verschiebungen werden
übernommen. Für Besichtigungen: Markierung im Titel an den eigenen Kalender anpassen.

Werktäglicher Tagesabschluss: `--routines '18:00'`, abschalten mit `--routines off`.

## Anbieter: FRITZ!Box oder sipgate

`SIP_PROVIDER` wählt die Anmeldung, der Rest bleibt gleich (`voice_protocol.pjsip_config`).

| | fritzbox (Vorgabe, Leo) | sipgate |
|---|---|---|
| Server | im Netz der FRITZ!Box oder per WireGuard | öffentliche IP, z. B. Hetzner |
| Verbindung | TCP zur Box, Port 5060 | UDP zu `sipgate.de` mit Outbound-Proxy |
| Anmeldung | Benutzer des IP-Telefons in der FRITZ!Box | SIP-ID und SIP-Passwort des VoIP-Geräts |
| `SIP_MEDIA_ADDRESS` | IP des Servers im Heimnetz | öffentliche IP des Servers |
| Lokale Netze | Kubernetes-Pod-Netz (`10.42.0.0/16`) | Docker- und private Netze, per `SIP_LOCAL_NETS` änderbar |
| Firewall | nichts nach außen | SIP-Port und RTP 26000 bis 26020 (UDP) nur für die IP-Bereiche von sipgate |

Bei sipgate muss das VoIP-Gerät eine Rufnummer für ausgehende Anrufe haben. Anrufe ins Mobilfunknetz
brauchen Guthaben oder einen Tarif, das bucht der Inhaber selbst. Die Konfiguration für `fritzbox` ist
Zeichen für Zeichen die von Leo, ein Test sichert das ab.

## Stimme

Bevorzugt: privater ElevenLabs-Gesprächsagent. Einstellungen bei Leo: Deutsch, Modell
`eleven_flash_v2_5`, Audio `ulaw_8000` in beide Richtungen, leere erste Nachricht, 60 Sekunden
Wartezeit in der Rufphase, als einziges Werkzeug das Client-Tool `ask_leo`, Gesprächsmodell im
Agenten `gpt-4.1-mini`. Den Vorschlag dafür erzeugt `voice_provider.agent_spec(voice_id, bridge.PERSONA)`.
Stimme vorher mit einer neutralen Sprachprobe prüfen, nie mit echten Daten.

Ersatzweg: Fehlender Zugang, Fehler, Timeout oder 45 Sekunden ohne Lebenszeichen wechseln auf das
Echtzeit-Sprachmodell von OpenAI (`LIVE_VOICE` ist die Stimme). Der Gesprächsverlauf geht mit.
Während eines Anrufs gibt es keinen Rückwechsel. Der nächste Anruf versucht ElevenLabs wieder.

## Sicherheit und Datenschutz

- Nur Anrufe an den Inhaber. Kontakttelefonie (Mieter, Makler) ist bewusst nicht eingebaut und
  braucht einen eigenen Dienst mit Freigabe je Anruf.
- Keine Aufzeichnung und keine Transkription von Gesprächen mit anderen Personen ohne
  ausdrückliche Zustimmung aller Beteiligten.
- Zugangsdaten nur in der Geheimnis-Ablage, nie in Git, Chat, Prompt oder Logbuch.
  `telephony-client.json` ist privat und gehört nie in ein Repository.
- Gesprächsaudio geht an ElevenLabs bzw. OpenAI. Verträge zur Auftragsverarbeitung prüfen.
- Status `connected` belegt nur die Annahme, `human_confirmed_at` nur eine erkannte menschliche
  Antwort. Beides ist keine Identitätsprüfung.

## Prüfreihenfolge vor dem ersten echten Anruf

1. Tests ohne übersprungene Fälle.
2. `sip_probe.py`: SIP-Anmeldung an der FRITZ!Box oder bei sipgate, ohne zu wählen.
3. `open_elevenlabs()`: Sprachsitzung bei ElevenLabs, ohne Anruf. Nur `ulaw_8000` in beide Richtungen gilt.
4. `call_owner.py --check`: Zugang aus dem Chat, ohne Anruf, ohne Nachricht.
5. Erst dann ein echter Testanruf, ausdrücklich vom Inhaber gewünscht.
