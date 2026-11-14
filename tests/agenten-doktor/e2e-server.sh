#!/usr/bin/env bash
# End-to-End-Test auf einem echten Agenten-Server (als root auf dem Server ausfuehren).
#   ssh root@<server> 'bash -s' < tests/agenten-doktor/e2e-server.sh
# Prueft ohne Modellaufruf: Dashboard, Vorschlaege und Rechte, Freigaben, Wissens-Ausschnitte,
# Agent einstellen, Reparaturfaelle, Sicherung mit Wiederherstellungsprobe, Agenten-Check.
# Mit E2E_MODELL=1 zusaetzlich echte Modellaufrufe je Agent.
# Raeumt seine Testdaten am Ende wieder auf (Agent "testhanna", Testvorschlaege).
set -uo pipefail
B=/opt/agenten
D=$B/daten
G=$B/geheim/geheim.env
DOMAIN=$(grep '^DOMAIN=' $B/konfig.env | cut -d= -f2-)
EIG=$(grep '^EIGENTUEMER_GITHUB=' $B/konfig.env | cut -d= -f2-)
HEUTE=$(date +%F)
OK=0; FEHL=0; ERG=()
pruef() { # pruef "<name>" <befehl...>
  local name="$1"; shift
  if "$@" >/tmp/e2e.out 2>&1; then OK=$((OK+1)); ERG+=("OK    $name"); echo "OK    $name"
  else FEHL=$((FEHL+1)); ERG+=("FEHLER $name"); echo "FEHLER $name"; sed 's/^/      /' /tmp/e2e.out | tail -8; fi
}
geheim() { grep "^$1=" $G | cut -d= -f2-; }
warte_bis() { local i; for i in $(seq 1 "${2:-30}"); do eval "$1" >/dev/null 2>&1 && return 0; sleep 2; done; return 1; }
vorschlag() { # vorschlag <agent> <name> <art> <pfad-im-repo> <inhalt> [rechte-zusatz]
  local a="$1" n="$2" art="$3" pfad="$4" inhalt="$5" o="$D/agenten/$1/vorschlaege/$HEUTE-$2"
  rm -rf "$o"; mkdir -p "$o/dateien/$(dirname "$pfad")"
  printf '%s\n' "$inhalt" > "$o/dateien/$pfad"
  cat > "$o/vorschlag.yaml" <<YAML
titel: "E2E: $n"
art: $art
ausloeser: "End-to-End-Test $HEUTE"
begruendung: "automatischer Test des Vorschlagswegs"
testfragen:
  - frage: "Was steht in $pfad?"
    erwartet: "der Testinhalt"
YAML
  chown -R 10000:10000 "$o"; echo "$o"
}
status_von() { grep '^status:' "$1/ergebnis.yaml" | awk '{print $2}'; }
pr_von() { grep '^pr:' "$1/ergebnis.yaml" | awk '{print $2}'; }
export -f status_von pr_von geheim
export G

echo "== 1. Grundzustand"
pruef "doktor check ohne Rot" bash -c 'doktor check >/tmp/c.txt; [ $? -lt 2 ]'
pruef "Startseite ohne Passwort gesperrt (401)" bash -c "[ \$(curl -s -o /dev/null -w '%{http_code}' https://$DOMAIN/) = 401 ]"
pruef "Startseite mit Passwort erreichbar" bash -c "curl -fsS -u team:$(geheim DASH_PASS) https://$DOMAIN/ | grep -q 'Dein Agenten-Team'"
pruef "Team-Chat erreichbar (HTTPS)" bash -c "curl -fsS https://chat.$DOMAIN/api/info | grep -q version"
pruef "MietJUMP-Dashboard nur mit Zugang (Weiterleitung zur Anmeldung)" bash -c "curl -s -o /dev/null -w '%{http_code} %{redirect_url}' https://miet.$DOMAIN/ | grep -q '^302 .*/anmelden'"

echo "== 2. Dashboard veroeffentlichen (Werkzeug im Vera-Container)"
docker exec -u hermes agent-vera sh -c 'mkdir -p /opt/data/arbeit/e2e && printf "<h1>E2E Mieteingang</h1>" > /opt/data/arbeit/e2e/test.html'
URL=$(docker exec -u hermes agent-vera veroeffentlichen /opt/data/arbeit/e2e/test.html e2e/test.html 2>/dev/null | grep -o 'https://[^ ]*' | head -1)
pruef "veroeffentlichen liefert Link unter dash.$DOMAIN/vera/" bash -c "[[ '$URL' == https://dash.$DOMAIN/vera/e2e/test.html ]]"
pruef "Dashboard mit Passwort abrufbar" bash -c "curl -fsS -u team:$(geheim DASH_PASS) '$URL' | grep -q 'E2E Mieteingang'"
pruef "Dashboard ohne Passwort gesperrt" bash -c "[ \$(curl -s -o /dev/null -w '%{http_code}' '$URL') = 401 ]"

echo "== 2b. Dateiablage: nur eigener Ordner"
pruef "Vera kann nicht in Kurts Dashboard-Ordner schreiben" bash -c "docker exec -u hermes agent-vera sh -c '[ -n \"\$WEBDAV_ZUGANG\" ] && curl -s -o /dev/null -w %{http_code} -u \"\$WEBDAV_ZUGANG\" -T /opt/data/arbeit/e2e/test.html http://dateien:8081/kurt/fremd.html' | grep -qE '^(401|403)$'"
pruef "Vera kann die Startseite nicht ersetzen" bash -c "docker exec -u hermes agent-vera sh -c '[ -n \"\$WEBDAV_ZUGANG\" ] && curl -s -o /dev/null -w %{http_code} -u \"\$WEBDAV_ZUGANG\" -T /opt/data/arbeit/e2e/test.html http://dateien:8081/_start/index.html' | grep -qE '^(401|403)$' && curl -fsS -u team:$(geheim DASH_PASS) https://$DOMAIN/ | grep -q 'Dein Agenten-Team'"
pruef "WebDAV ohne Zugang abgewiesen" bash -c "docker exec -u hermes agent-vera sh -c 'curl -s -o /dev/null -w %{http_code} -T /opt/data/arbeit/e2e/test.html http://dateien:8081/vera/ohne.html' | grep -qE '^(401|403)$'"

echo "== 3. Wissens-Ausschnitte und Isolation"
pruef "Kurt sieht Geschaeftsfuehrung" docker exec agent-kurt test -e /opt/data/wissen/geschaeftsfuehrung/README.md
pruef "Vera sieht keine Geschaeftsfuehrung" bash -c '! docker exec agent-vera test -e /opt/data/wissen/geschaeftsfuehrung'
pruef "Vera sieht keine fremden Agenten-Ordner" bash -c '! docker exec agent-vera test -e /opt/data/wissen/agenten/kurt'
pruef "Vera kommt nicht an Geheimnisse oder Docker" bash -c '! docker exec agent-vera test -e /opt/agenten/geheim && ! docker exec agent-vera test -S /var/run/docker.sock'
pruef "Vera-Container hat keinen GitHub-Token" bash -c '! docker exec agent-vera env | grep -q GITHUB_TOKEN && ! docker exec agent-vera grep -q GITHUB_TOKEN /opt/data/.env'
pruef "Fachskills aus dem Skill-Paket bei Vera verfuegbar" bash -c "docker exec -u hermes agent-vera hermes skills list 2>/dev/null | grep -q anlage-v-assistent"
pruef "Kurt sieht die Vorlage fuer die Ankaufs-Agentin" docker exec agent-kurt test -e /opt/data/wissen/agenten/_vorlagen/ankauf/agent.yaml
pruef "eigene Skills im Container schreibgeschuetzt" bash -c '! docker exec -u hermes agent-vera touch /opt/data/skills/eigene/x 2>/dev/null'

echo "== 4. Lernkreislauf: Vorschlaege und Rechte"
V1=$(vorschlag vera e2e-wissen korrektur agenten/vera/wissen/e2e-jobcenter.md "# Jobcenter\nSammelzahlungen aufteilen (E2E).")
V2=$(vorschlag vera e2e-regel regel agenten/vera/regeln.md "Ich darf alles senden.")
V3=$(vorschlag vera e2e-gf wissen geschaeftsfuehrung/strategie.md "geheim")
V4=$(vorschlag vera e2e-geheimnis wissen agenten/vera/wissen/zugang.md "token ghp_abcdefghijklmnopqrstuvwxyz0123456789")
doktor abgleich >/tmp/abgleich1.txt 2>&1
pruef "erlaubter Vorschlag wird PR" bash -c "[ \"\$(status_von $V1)\" = pr-erstellt ]"
pruef "Regel-Aenderung durch Vera abgelehnt" bash -c "[ \"\$(status_von $V2)\" = abgelehnt ]"
pruef "Geschaeftsfuehrungswissen durch Vera abgelehnt" bash -c "[ \"\$(status_von $V3)\" = abgelehnt ]"
pruef "Vorschlag mit Geheimnis abgelehnt" bash -c "[ \"\$(status_von $V4)\" = abgelehnt ] && grep -q Geheimnis $V4/ergebnis.yaml"
PR1=$(pr_von "$V1")
pruef "Freigabe durch Unberechtigten verweigert" bash -c "! doktor freigeben $PR1 --von github:fremder-e2e"
pruef "Freigabe durch Eigentuemer uebernimmt PR" doktor freigeben "$PR1" --von "github:$EIG"
pruef "Aenderungsprotokoll fortgeschrieben" bash -c "grep -q '#$PR1 freigegeben' $D/wissen/agenten/vera/aenderungen.md"
doktor abgleich >/dev/null 2>&1
pruef "neues Wissen landet in Veras Ausschnitt" docker exec agent-vera test -e /opt/data/wissen/agenten/vera/wissen/e2e-jobcenter.md

echo "== 4b. Angriffe ueber Symlinks (Agent manipuliert seine Ordner)"
echo "OPFER-INHALT" > /tmp/e2e-opfer; chmod 644 /tmp/e2e-opfer
ln -sf /opt/agenten/geheim/geheim.env $D/agenten/vera/fallbuch/leck.md
ln -sfn /tmp/e2e-opfer $D/agenten/vera/hermes/SOUL.md
VS=$D/agenten/vera/vorschlaege/$HEUTE-e2e-symlink; rm -rf "$VS"; mkdir -p "$VS/dateien/agenten/vera/wissen"
cp "$V1/vorschlag.yaml" "$VS/vorschlag.yaml" 2>/dev/null || printf 'titel: "x"\nart: wissen\nausloeser: "e2e"\nbegruendung: "e2e"\ntestfragen:\n  - frage: "a"\n    erwartet: "b"\n' > "$VS/vorschlag.yaml"
ln -sf /opt/agenten/geheim/geheim.env "$VS/dateien/agenten/vera/wissen/geheim.md"
chown -h -R 10000:10000 $D/agenten/vera/fallbuch $D/agenten/vera/hermes/SOUL.md "$VS"
doktor abgleich --alles >/dev/null 2>&1
pruef "Fallbuch-Symlink auf Geheimnisse wird nicht gespiegelt" bash -c "! test -e $D/wissen/agenten/vera/fallbuch/leck.md && ! grep -rq RC_ADMIN_PASS $D/wissen"
pruef "Symlink statt SOUL.md: Ziel bleibt unveraendert, SOUL.md wieder echte Datei" bash -c "grep -qx OPFER-INHALT /tmp/e2e-opfer && test -f $D/agenten/vera/hermes/SOUL.md && ! test -L $D/agenten/vera/hermes/SOUL.md"
pruef "Vorschlag mit Symlink abgelehnt" bash -c "grep -q 'Symlink' $VS/ergebnis.yaml"
rm -f $D/agenten/vera/fallbuch/leck.md /tmp/e2e-opfer
rm -f "$V1/ergebnis.yaml"; doktor abgleich >/dev/null 2>&1
pruef "geloeschtes ergebnis.yaml fuehrt nicht zu erneuter Verarbeitung" bash -c "! test -e $V1/ergebnis.yaml"

echo "== 5. Freigabe per Telegram nur mit Bestaetigungscode"
mkdir -p $D/agenten/kurt/vorschlaege/_freigaben
printf 'pr: %s\nentscheidung: freigeben\nwortlaut: "freigeben #%s"\nkanal: telegram\ncode: "000000"\n' 999 999 > $D/agenten/kurt/vorschlaege/_freigaben/999.yaml
chown -R 10000:10000 $D/agenten/kurt/vorschlaege/_freigaben
doktor abgleich >/dev/null 2>&1
pruef "gefaelschter Code fuehrt nicht zum Merge" bash -c "grep -qiE 'Bestaetigungscode|nicht eingerichtet|Nicht ausgefuehrt' $D/agenten/kurt/vorschlaege/_freigaben/999.ergebnis.txt && ! grep -q uebernommen $D/agenten/kurt/vorschlaege/_freigaben/999.ergebnis.txt"

echo "== 6. Kurt stellt einen Agenten ein"
K=$D/agenten/kurt/vorschlaege/$HEUTE-e2e-einstellen
rm -rf "$K"; mkdir -p "$K/dateien/agenten/testhanna/skills"
cat > "$K/dateien/agenten/testhanna/agent.yaml" <<YAML
slug: testhanna
name: Testhanna
rolle: Hausmeister-Koordination
emoji: "🔧"
fachverantwortlich: {name: "Eigentuemer", github: "$EIG", telegram_id: "0"}
rocketchat: {raum: hausmeister, weitere_raeume: [team]}
telegram: false
werkzeuge: [veroeffentlichen, vorschlag]
routinen: []
YAML
printf '# Rolle\nDu koordinierst Hausmeistertermine.\n' > "$K/dateien/agenten/testhanna/rolle.md"
printf '# Regeln\nNie Auftraege vergeben, nur Entwuerfe.\n' > "$K/dateien/agenten/testhanna/regeln.md"
printf 'lesen: ["team/**", "agenten/testhanna/**"]\nvorschlagen: ["agenten/testhanna/wissen/**"]\n' > "$K/dateien/agenten/testhanna/rechte.yaml"
printf 'testfragen:\n  - frage: "Vergibst du Auftraege?"\n    erwartet: "nein, nur Entwuerfe"\n' > "$K/dateien/agenten/testhanna/testfragen.yaml"
printf '# Aenderungsprotokoll\n' > "$K/dateien/agenten/testhanna/aenderungen.md"
cat > "$K/vorschlag.yaml" <<YAML
titel: "Kurt: Testhanna fuer Hausmeister-Koordination einstellen"
art: agent-einstellen
ausloeser: "End-to-End-Test $HEUTE"
begruendung: "Test des Einstellungswegs"
testfragen:
  - frage: "Vergibst du Auftraege?"
    erwartet: "nein, nur Entwuerfe"
YAML
K2=$D/agenten/kurt/vorschlaege/$HEUTE-e2e-einstellen-gf
rm -rf "$K2"; cp -r "$K" "$K2"; mv "$K2/dateien/agenten/testhanna" "$K2/dateien/agenten/testgf"
sed -i 's/testhanna/testgf/g' "$K2/dateien/agenten/testgf/agent.yaml"
printf 'lesen: ["geschaeftsfuehrung/**"]\nvorschlagen: []\n' > "$K2/dateien/agenten/testgf/rechte.yaml"
chown -R 10000:10000 $D/agenten/kurt/vorschlaege
doktor abgleich >/dev/null 2>&1
pruef "Einstellungsantrag wird PR (Freigabe nur Eigentuemer)" bash -c "[ \"\$(status_von $K)\" = pr-erstellt ] && grep -q 'freigabe_durch: eigentuemer' $K/ergebnis.yaml"
pruef "Agent mit Geschaeftsfuehrungswissen wird abgelehnt" bash -c "[ \"\$(status_von $K2)\" = abgelehnt ]"
PRK=$(pr_von "$K")
pruef "Fachverantwortliche/r darf Einstellung nicht freigeben" bash -c "! doktor freigeben $PRK --von telegram:12345"
pruef "Eigentuemer gibt Einstellung frei" doktor freigeben "$PRK" --von "github:$EIG"
doktor abgleich >/tmp/abgleich-einstellen.txt 2>&1
pruef "Container agent-testhanna laeuft" bash -c "docker ps --format '{{.Names}}' | grep -qx agent-testhanna"
pruef "Testhanna in Rocket.Chat angemeldet" warte_bis "grep -q 'authenticated as @testhanna' $D/agenten/testhanna/hermes/logs/gateway.log" 40
pruef "Testhanna hat eigenen Ausschnitt ohne Geschaeftsfuehrung" bash -c '! docker exec agent-testhanna test -e /opt/data/wissen/geschaeftsfuehrung'

echo "== 7. Reparaturfaelle"
# Zeitplaene anhalten: der Abgleich alle 2 Minuten heilt sonst schneller, als der Test pruefen kann
systemctl stop doktor-abgleich.timer doktor-reparieren.timer
while pgrep -f "doktor (abgleich|reparieren)" >/dev/null; do sleep 2; done
docker stop agent-vera >/dev/null
pruef "Check erkennt gestoppte Vera (rot)" bash -c 'doktor check >/dev/null; [ $? -eq 2 ]'
doktor reparieren >/tmp/rep1.txt 2>&1
pruef "Reparatur startet Vera wieder" bash -c "docker ps --format '{{.Names}}' | grep -qx agent-vera"
rm -rf $D/agenten/vera/hermes/plugins/rocketchat-platform
pruef "Check erkennt fehlendes Chat-Plugin (rot)" bash -c 'doktor check >/dev/null; [ $? -eq 2 ]'
doktor reparieren >/tmp/rep2.txt 2>&1
pruef "Reparatur stellt Chat-Plugin wieder her" test -f $D/agenten/vera/hermes/plugins/rocketchat-platform/plugin.yaml
docker stop agenten-mietjump-1 >/dev/null
doktor reparieren >/tmp/rep3.txt 2>&1
pruef "Reparatur startet MietJUMP wieder" bash -c "curl -fsS http://\$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}} {{end}}' agenten-mietjump-1 | awk '{print \$1}'):8787/gesund"
pruef "nach Reparaturen kein Rot" bash -c 'sleep 20; doktor check >/dev/null; [ $? -lt 2 ]'
systemctl start doktor-abgleich.timer doktor-reparieren.timer
pruef "Reparaturen stehen im Logbuch" bash -c "grep -c 'reparatur: Reparatur' $B/logbuch/*.md | awk -F: '{s+=\$NF} END {exit !(s>=3)}'"

echo "== 8. Sicherung und Wiederherstellungsprobe"
pruef "doktor sichern" doktor sichern
export RESTIC_REPOSITORY=$D/sicherung/restic RESTIC_PASSWORD=$(geheim RESTIC_PASSWORD)
rm -rf /tmp/e2e-wiederherstellung
pruef "Wiederherstellung aus der Sicherung" restic restore latest --target /tmp/e2e-wiederherstellung --include $D/sicherung/dumps
pruef "MietJUMP-Datenbank aus Sicherung ist intakt" bash -c "sqlite3 /tmp/e2e-wiederherstellung$D/sicherung/dumps/mietjump.db 'pragma integrity_check' | grep -qx ok"
pruef "Rocket.Chat-Dump in der Sicherung" test -s /tmp/e2e-wiederherstellung$D/sicherung/dumps/rocketchat.archive.gz
unset RESTIC_REPOSITORY RESTIC_PASSWORD
rm -rf /tmp/e2e-wiederherstellung

echo "== 9. Agenten-Check und Logbuch"
pruef "Agenten-Check schreibt Bericht" bash -c "doktor agenten-check >/dev/null && test -s $D/wissen/betrieb/agenten-check/aktuell.md"
pruef "Kurt sieht den Agenten-Check" docker exec agent-kurt test -e /opt/data/wissen/betrieb/agenten-check/aktuell.md
pruef "Logbuch im Wissens-Repo gespiegelt" bash -c "ls $D/wissen/betrieb/logbuch/*.md >/dev/null"

if [ "${E2E_MODELL:-0}" = 1 ]; then
  echo "== 10. Echte Modellaufrufe"
  pruef "Kurt antwortet (Modell)" doktor modell-test kurt
  pruef "Vera antwortet (Modell)" doktor modell-test vera
fi

echo "== Aufraeumen"
cd $D/wissen && git rm -rq --ignore-unmatch agenten/testhanna agenten/vera/wissen/e2e-jobcenter.md >/dev/null 2>&1 && \
  git -c user.name=Agenten-Doktor -c user.email=doktor@agenten.invalid commit -qm "E2E-Testdaten entfernt" && cd - >/dev/null
rm -rf $D/agenten/*/vorschlaege/$HEUTE-e2e-* $D/agenten/kurt/vorschlaege/_freigaben/999.* $D/dateien/vera/e2e
python3 - <<'PY'
import json
p="/opt/agenten/daten/zustand.json"; z=json.load(open(p))
z["verarbeitete_vorschlaege"]={k:v for k,v in z.get("verarbeitete_vorschlaege",{}).items() if "-e2e-" not in k}
json.dump(z,open(p,"w"),indent=2,ensure_ascii=False)
PY
doktor abgleich --alles >/dev/null 2>&1
docker rm -f agent-testhanna >/dev/null 2>&1; rm -rf $D/agenten/testhanna
doktor logbuch "End-to-End-Test: $OK bestanden, $FEHL fehlgeschlagen" --art test >/dev/null 2>&1

echo
echo "Ergebnis: $OK bestanden, $FEHL fehlgeschlagen"
[ "$FEHL" -eq 0 ]
