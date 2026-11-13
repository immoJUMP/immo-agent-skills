# Durchlauf: ein Start-Prompt, danach keine Rückfragen

Ziel: Der Nutzer erledigt vorher, was nur er tun kann: Konten, Anmeldungen, Entscheidungen.
Dann wirft er **einen** Start-Prompt ein, und der Doktor baut alles allein auf. Er meldet sich
nur an den angekündigten Berührungspunkten und am Ende.

Grundlage ist der erste echte Aufbau auf einer Hetzner-VM (13. und 14.11.2026). Jede Rückfrage
und jedes „geht nicht“ von dort steht jetzt in der Checkliste, im Vorbereitungs-Check oder im
Start-Prompt (Abschnitt 6).

## 1. Drei Stufen

| Stufe | Wann | Wer | Dauer |
|---|---|---|---|
| 1. Checkliste | 1 bis 3 Tage vorher | Nutzer allein | 30 bis 45 Min., dazu Wartezeit der Hetzner-Prüfung |
| 2. Vorbereitungs-Check (Prompt 1) | am Vortag oder 1 Stunde vorher | Doktor, ändert nichts | 3 Min. |
| 3. Start-Prompt (Prompt 2) | zum Starttermin | Doktor allein | 35 bis 50 Min. |

Stufe 3 beginnt nur, wenn Stufe 2 **kein Rot** zeigt. Gelb heißt: erledigt der Doktor im Durchlauf.

## 2. Stufe 1: Checkliste (nur der Nutzer)

| Nr. | Was | Woran man sieht, dass es erledigt ist |
|---|---|---|
| 1 | **Hetzner-Konto** mit Identitätsprüfung und Zahlungsmittel, Vertrag zur Auftragsverarbeitung im Kundenkonto abgeschlossen | Console zeigt keinen Prüfhinweis, Projekt `agenten` angelegt |
| 2 | **Mac:** Claude Code aktuell, Erweiterung Claude in Chrome verbunden, Homebrew, dann `brew install gh jq python` | `claude --version`, Chrome-Erweiterung zeigt „verbunden“ |
| 3 | **Tailscale-App** auf dem Mac installiert und angemeldet, **mit demselben Konto** wie später in Chrome | Menüleiste zeigt „Connected“ |
| 4 | **Chrome angemeldet** bei: Hetzner Console, GitHub, Google mit **Veras Postfach**, Telegram Web (per QR-Code vom Handy), Tailscale Admin | je ein Tab ohne Anmeldemaske |
| 5 | **Google Cloud einmal geöffnet** (`console.cloud.google.com`) mit Veras Postfach, Land gewählt, Nutzungsbedingungen bestätigt | Console zeigt das Dashboard, keinen Begrüßungsdialog |
| 6 | **Telegram:** höchstens 18 Bots im Konto (in Telegram an `@BotFather` `/mybots` schicken). Der Doktor legt zwei an, Telegram erlaubt 20 | Liste zeigt 18 oder weniger |
| 7 | **GitHub:** `gh auth login --web --git-protocol https` im eigenen Terminal, Einladung zu MietJUMP angenommen (`github.com/immodigit/mietjump/invitations`) | `gh auth status` grün |
| 8 | **Modellzugang:** ChatGPT Plus oder Pro aktiv (Standard, Anmeldung am Ende des Durchlaufs) **oder** API-Schlüssel mit Ausgabelimit im Schlüsselbund (`doktor-lokal.sh token-speichern openai` bzw. `openrouter`). Meridian nur nach schriftlicher Aufklärung, dann `claude setup-token` im eigenen Terminal und `token-speichern claude-oauth` | Check zeigt „Modell“ nicht rot |
| 9 | **Entscheidungen** für den Start-Prompt: Adresse, Modell, Postfach, Repo, Kostenrahmen | Felder im Start-Prompt ausgefüllt |
| 10 | Bei Subdomain unter `cl.immodigit.de`: Name mit ImmoDigit abgesprochen, ImmoDigit am Starttermin erreichbar (zwei DNS-Einträge, 1 Minute) | Zusage von ImmoDigit |

## 3. Stufe 2: Vorbereitungs-Check (Prompt 1)

Der Nutzer schreibt:

> Agenten-Doktor, prüf meine Vorbereitung für den Aufbau. Ändere nichts.
> (darunter die ausgefüllten „Meine Angaben“ aus dem Start-Prompt, Abschnitt 4)

Der Doktor:

1. schreibt die Angaben nach `~/.agenten-doktor/<projekt>/start.env` (nichts Geheimes:
   `DOMAIN`, `MODELL_ANBIETER`, `WISSEN_REPO`, `POSTFACH`, `MIETJUMP`, `SERVER_TYPEN`),
2. ruft `doktor-lokal.sh vorbereitung-pruefen` auf. Der Befehl prüft Werkzeuge, Python,
   `gh`-Anmeldung, MietJUMP-Zugriff, Wissens-Repo, Tailscale auf dem Mac, vorhandene Zugänge
   live (Hetzner, GitHub, beide Telegram-Bots, Modell, Gmail mit Abgleich der Adresse), die
   Verfügbarkeit der Servertypen in Deutschland und Finnland und die Adresse. Er legt nichts an,
   schreibt eine Zeile ins Vorlauf-Logbuch und endet mit Exit 0 nur ohne Rot,
3. prüft in Chrome per Tab-Abfrage und Screenshot die Anmeldungen aus Checkliste Nr. 4 und 5,
4. antwortet mit der Tabelle (rot, gelb, grün) und je Rot **einem** Satz, was zu tun ist.

Rot behebt der Nutzer, dann Prompt 1 erneut. Gelb ist in Ordnung.

## 4. Stufe 3: der Start-Prompt (Prompt 2)

Zum Kopieren, Felder in spitzen Klammern ausfüllen:

```text
Agenten-Doktor, bau mein Agenten-Team auf. Durchlauf ohne Rückfragen.

Meine Angaben:
- Projekt: agenten
- Name: <Vorname Nachname>, Firma: <Firma>
- GitHub-Name: <github-name>
- Adresse: <kuerzel>.cl.immodigit.de (oder eigene Domain: <domain>)
- Modell: codex (oder openai, openrouter, meridian)
- Postfach für Vera: <adresse@gmail.com>
- Wissens-Repo: neu als <github-name>/agenten-wissen (oder vorhanden: <owner/name>)
- Voice: nein
- MietJUMP: ja
- Kostenrahmen: bis 45 EUR im Monat für Server und Backups, Modell nach meinem Tarif

Ich erlaube dir für diesen Aufbau ausdrücklich:
1. Hetzner: im Projekt "agenten" einen API-Token erzeugen, einen Server cx43 anlegen
   (ist er ausverkauft: cx53 oder cpx32 im Kostenrahmen), mit Firewall, Löschschutz und Backups.
2. GitHub: ein privates Repo anlegen und einen fein granularen Token nur für dieses Repo erzeugen.
3. Telegram: über BotFather zwei Bots anlegen (Kurt und Doktor) und beiden "Start" schreiben.
4. Google: ein Cloud-Projekt anlegen, die Gmail-API einschalten, Bedingungen der Google Cloud
   akzeptieren, den Zustimmungsbildschirm einrichten, die App auf "In Produktion" stellen,
   einen Desktop-Client anlegen, dessen JSON-Datei herunterladen und danach löschen, und die
   Zustimmung für mein Postfach erteilen.
5. Tailscale: die Policy um den Tag für den Server ergänzen und einen einmaligen Schlüssel erzeugen.
6. DNS: bei eigener Domain die Einträge für den Server anlegen.
7. Zugänge über die Kopier-Knöpfe in meinen Schlüsselbund legen und auf den neuen Server übertragen.
8. Auf dem neuen Server als root alles ausführen, was der Aufbau braucht.

Nicht erlaubt: Mails oder Nachrichten an andere senden, Zahlungen, Löschen außerhalb des neuen
Servers, Passwörter oder Zwei-Faktor-Codes eingeben.
Entscheide alles Weitere selbst nach den Standardwerten des Skills, schreib es ins Logbuch und
frag mich nur, wenn du ohne mich nicht weiterkommst. Am Ende eine Nachricht: was läuft und was
ich noch tun muss.
```

Warum der Freigabeblock so ausführlich ist: Claude Code hält im Schutzmodus Handlungen an, die
Kosten auslösen, Bedingungen akzeptieren, DNS ändern oder Zugänge erzeugen, solange der Nutzer
sie nicht im Chat ausdrücklich erlaubt hat. Beim ersten Durchlauf stand der Aufbau deshalb
mehrmals still. Jede Handlung steht hier einzeln, damit nichts mehr anhält.

## 5. Regeln für den Doktor im Durchlauf

**Erkennen:** Die Nachricht enthält „Durchlauf ohne Rückfragen“, die Angaben und den
Freigabeblock. Dann gilt dieser Abschnitt statt der gebündelten Rückfrage aus der SKILL.md.

**Keine Rückfragen.** Fehlt eine Angabe, nimmst du den Standardwert, schreibst ihn ins
Vorlauf-Logbuch und machst weiter:

| Punkt | Standard |
|---|---|
| Projekt, Servername | `agenten` |
| Servertypen | `cx43,cx53,cpx32`, nur Typen, deren Preis mit Backups im Kostenrahmen liegt |
| Standort | `nbg1`, dann `fsn1`, `hel1` |
| Backups | an, wenn der Kostenrahmen sie trägt, sonst aus und im Bericht nennen |
| Wissens-Repo | `<github-name>/agenten-wissen`, privat |
| Bots | `<Kürzel>KurtBot` und `<Kürzel>DoktorBot`, bei belegtem Namen Ziffer anhängen |
| `ACME_EMAIL` | Veras Postfach |
| Modell | `codex` |
| `DEMO_DATEN` | `nein` (nur ein Testserver bekommt `ja`) |
| MietJUMP | `ja`, Stand `main` |
| SSH schließen | nur, wenn der Mac im selben Tailnet ist wie der Server, sonst offen lassen (Firewall: nur die IP des Macs) und im Bericht nennen |

**Anhalten und fragen nur bei:**

1. Rot im Vorbereitungs-Check, das sich nicht mit einem eigenen Schritt beheben lässt.
2. Kosten über dem Kostenrahmen.
3. Passwort, Zwei-Faktor-Code, Passkey, Identitätsprüfung, Zahlungsdaten.
4. Meridian ohne schriftliche Aufklärung im Logbuch.
5. Eine Seite sieht anders aus als beschrieben **und** ein falscher Klick wäre nicht umkehrbar.

Alles andere: Standard nehmen, ins Logbuch, weiter. Scheitert ein **optionaler** Teil
(Telegram, Gmail, Doktor-Bot) zweimal, lässt du ihn aus, baust den Rest fertig und nennst ihn am
Ende als offenen Punkt. Der Server läuft auch ohne ihn.

**Berührungspunkte** kündigst du **zu Beginn in einer Nachricht** an, damit der Nutzer weiß,
wann er gebraucht wird:

- Google fragt eventuell nach dem Passwort von Veras Postfach (ca. Minute 15).
- GitHub fragt eventuell nach dem Passkey (ca. Minute 10).
- Nur bei `codex`: zwei Gerätecodes bestätigen, gebündelt am Ende (ca. Minute 40).
- Nur bei Subdomain unter `cl.immodigit.de`: ImmoDigit setzt zwei DNS-Einträge. Die
  Nachricht dafür schreibst du fertig vor (Name und IP), der Nutzer leitet sie weiter.
  Bis die Einträge stehen, machst du mit den übrigen Schritten weiter.

## 6. Reihenfolge mit Wartezeiten

Die Schritte verweisen auf [aufbau.md](aufbau.md). Gemessen beim ersten Durchlauf: VM 1 Min.,
Grundausstattung 4 Min., Installation 8 bis 12 Min., Chrome-Schritte für Zugänge zusammen
15 bis 20 Min. Wer wartet, arbeitet parallel weiter:

| Min. | Schritt | parallel |
|---|---|---|
| 0 | `vorbereitung-pruefen` erneut, Berührungspunkte ankündigen | |
| 2 | Hetzner-Token (aufbau 3), VM mit Typenliste (aufbau 4), Schutz und Backups | Grundausstattung läuft 4 bis 10 Min. |
| 5 | DNS (aufbau 5): eigene Domain in Chrome, sonst Nachricht an ImmoDigit | DNS wird wirksam |
| 6 | Wissens-Repo und GitHub-Token (aufbau 7, 8) | |
| 10 | Zwei Telegram-Bots, „Start“ an beide, Telegram-ID (aufbau 9, 10) | |
| 14 | Gmail: Cloud-Projekt, Zustimmungsbildschirm, In Produktion, Desktop-Client, `google-anmeldung.py` (aufbau 11) | |
| 22 | Tailscale: Policy, Schlüssel, Beitritt, SSH über Tailscale testen (aufbau 6) | |
| 25 | `hochladen`, `mietjump-hochladen`, `konfig-setzen`, Geheimnisse senden (aufbau 14) | |
| 27 | `doktor installieren` im Hintergrund (aufbau 15) | Vorlauf-Logbuch schreiben, `dns-pruefen` |
| 38 | Modell: bei `codex` beide Gerätecodes in einer Nachricht, dann `doktor modell-test` | |
| 40 | Abnahme, automatischer Teil: `doktor check --modell`, Adressen ohne Zertifikatswarnung, `doktor sichern`, Port 22 von außen | |
| 45 | Abschlussnachricht | |

**Abschlussnachricht**, höchstens zwölf Zeilen: Adressen (Startseite, Team-Chat, Dashboards,
MietJUMP), Kurt in Telegram, was grün ist, was offen ist, und die eine Zeile für
`doktor zugangsdaten`, die der Nutzer **in seinem eigenen Terminal** ausführt. Dann die
gemeinsame Abnahme (aufbau 16, Punkte 2 bis 6): Kurt per Sprachnachricht, Vera mit dem
Mieteingang, Freigabeweg, Manipulationsprobe, Lernkreislauf. Die braucht den Nutzer und ist
der Moment, in dem er sein Team zum ersten Mal arbeiten sieht.

## 7. Was beim ersten Durchlauf hakte und wo es jetzt abgefangen ist

| Was passierte | Ursache | Jetzt |
|---|---|---|
| Telegram-Bot ließ sich nicht anlegen | Konto hatte 20 Bots, das Maximum | Checkliste Nr. 6 |
| Tailscale-Schritt hing | In Chrome kein Tailscale-Konto, Mac in einem anderen Tailnet als der Server | Checkliste Nr. 3 und 4, Check prüft die Mac-Anmeldung, SSH bleibt offen, solange der Mac nicht im selben Tailnet ist |
| Gmail-Schritt hing | Veras Postfach nicht in Chrome angemeldet, Google-Cloud-Bedingungen nie bestätigt | Checkliste Nr. 4 und 5 |
| Aufbau stand mehrmals still | Schutzmodus von Claude Code hielt DNS-Einträge, fremde Zugänge und das Akzeptieren von Bedingungen an | Freigabeblock im Start-Prompt, jede Handlung einzeln |
| cx43 nicht zu bekommen | Typ zeitweise an allen drei Standorten ausverkauft (am 14.11.2026 gegen 0 Uhr belegt) | Typenliste im Start-Prompt, `hetzner-anlegen` fragt vorher die Verfügbarkeit ab, Check zeigt die Lage |
| Modellzugang fehlte am Ende | Zugang erst nach der Installation beschafft | Check zeigt Meridian und API ohne Schlüssel rot, Checkliste Nr. 8 |
| Vera meldete 654 Sollstellungen und falsche Rückstände | Skill buchte Sollstellungen ohne Übernahmemonat, MietJUMP buchte bis zum Vertragsbeginn zurück | Skill verlangt `ab`, ohne bekannten Übernahmemonat nur den Prüfmonat. Vera hatte es selbst erkannt, nichts freigegeben und nachgefragt |
| Kopieren eines Tokens per Skript kopierte nichts | Seite reagiert nur auf echte Klicks | echter Klick an die berechnete Stelle, [chrome-ablaeufe.md](chrome-ablaeufe.md) |
| Agenten nach Neustart ohne MietJUMP-Werkzeuge | Agent startete vor MietJUMP, Hermes parkte die Verbindung | `doktor nach-start` nach jedem Hochfahren |

## 8. Prüfpunkt des Durchlaufs

Der Durchlauf ist fertig, wenn `doktor check --modell` grün ist, die Abschlussnachricht
verschickt ist und im Logbuch jeder Standardwert steht, den du statt einer Rückfrage genommen
hast.
