# Nachweis: keine Technik im Telegram-Chat des Eigentümers

Prüft die Regel aus `references/sicherheit.md` (Abschnitt „Meldungen an den Eigentümer“) ohne echten
Telegram-Bot: Eine Attrappe der Bot-API (`tgattrappe.py`) beantwortet alle Aufrufe und schreibt jede
Nachricht mit. Nur auf einem Wegwerf-Server laufen lassen, nie auf einem Server mit Teilnehmern.

1. Konfiguration erzeugen (auf dem Mac, braucht `pyyaml`), einmal aus dem alten und einmal aus dem
   neuen Doktor-Code:
   `python3 erzeuge.py <pfad>/doktor-alt config-alt.yaml` und `python3 erzeuge.py <pfad>/doktor config-neu.yaml`
2. Wegwerf-Server anlegen, z. B. `doktor-lokal.sh hetzner-anlegen doktor-telegramtest cx23,cpx22`, und
   `tgattrappe.py`, `lauf.sh`, beide `config-*.yaml`, `stoerung.py` sowie den neuen `doktor` als
   `doktor-neu` nach `/root/tgtest/` kopieren.
3. `bash /root/tgtest/lauf.sh`: Hermes (Image wie im Doktor) startet je Konfiguration, wird neu
   gestartet und gestoppt. Erwartung: alt mit Nachrichten an den Eigentümer, neu „keine“.
4. Attrappe mit `-p 127.0.0.1:8081:8081` starten (siehe Kopf von `stoerung.py`), dann
   `python3 /root/tgtest/stoerung.py`. Erwartung: vier rote Reparaturläufe ergeben genau eine Nachricht
   in Klartext, die Behebung keine.
5. Server und Firewall wieder löschen.

Ergebnis am 14.11.2026 (Hermes v0.22.2, cx23): alt 2 Nachrichten („Hermes wird heruntergefahren, Ihre
aktuelle Aufgabe wird unterbrochen …“ bei Neustart und Stopp), neu 0. Störung: 1 Nachricht nach dem
zweiten roten Lauf, danach und bei Behebung keine.
