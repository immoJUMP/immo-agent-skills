#!/usr/bin/env bash
# doktor-lokal: Mac-Seite des Agenten-Doktors.
#
# Geheimnisse (Hetzner-Token, Tailscale-Schluessel, Bot-Token ...) liegen im
# macOS-Schluesselbund, Dienst "agenten-doktor", Konto "<projekt>/<name>".
# Kein Geheimnis landet in argv, in Dateien oder in der Ausgabe:
#   - Werte kommen aus der Zwischenablage (der Doktor klickt in Chrome auf
#     "Kopieren") und gehen per stdin an `security -i`.
#   - API-Aufrufe lesen den Token per `curl -K -` von stdin.
#
# Aufruf: doktor-lokal.sh <befehl> [argumente]   (Hilfe: ohne Argumente)
set -euo pipefail

PROJEKT="${DOKTOR_PROJEKT:-agenten}"
HIER="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVER_DIR="$HIER/../server"
KC_DIENST="agenten-doktor"
HZ_API="https://api.hetzner.cloud/v1"

fehler() { echo "FEHLER: $*" >&2; exit 1; }
info() { echo "• $*" >&2; }

# ---------- Schluesselbund ----------

kc_konto() { echo "$PROJEKT/$1"; }

# Liefert den Wert auf stdout (nur fuer Pipes innerhalb dieses Skripts).
kc_lesen() {
  local name="$1"
  # Sonderfall Testbetrieb: eigener Schluesselbund-Dienst fuer den Hetzner-Token
  if [ "$name" = "hetzner" ] && [ -n "${DOKTOR_HETZNER_KC_DIENST:-}" ]; then
    security find-generic-password -s "$DOKTOR_HETZNER_KC_DIENST" -w 2>/dev/null && return 0
  fi
  security find-generic-password -s "$KC_DIENST" -a "$(kc_konto "$name")" -w 2>/dev/null
}

kc_vorhanden() { kc_lesen "$1" >/dev/null 2>&1; }

# Wert von stdin in den Schluesselbund (ueber `security -i`, also nicht in argv).
kc_schreiben() {
  local name="$1" wert
  IFS= read -r wert || true
  wert="${wert%$'\r'}"
  [ -n "$wert" ] || fehler "Leerer Wert fuer $name. Ist die Zwischenablage leer?"
  case "$wert" in *[[:space:]\"\\]*) fehler "Wert fuer $name enthaelt Leer- oder Sonderzeichen, bitte pruefen.";; esac
  printf 'add-generic-password -U -s %s -a %s -w %s\n' "$KC_DIENST" "$(kc_konto "$name")" "$wert" | security -i >/dev/null
  info "$name im Schluesselbund gespeichert (Dienst $KC_DIENST, Konto $(kc_konto "$name"))."
}

# ---------- Hetzner ----------

hz() { # hz METHOD PFAD [JSON]
  local m="$1" p="$2" body="${3:-}" t
  t="$(kc_lesen hetzner)" || fehler "Kein Hetzner-Token im Schluesselbund. Erst: $0 token-speichern hetzner"
  if [ -n "$body" ]; then
    printf 'header = "Authorization: Bearer %s"\nheader = "Content-Type: application/json"\n' "$t" \
      | curl -sS -K - -X "$m" "$HZ_API$p" --data "$body"
  else
    printf 'header = "Authorization: Bearer %s"\n' "$t" | curl -sS -K - -X "$m" "$HZ_API$p"
  fi
}

hz_pruefen() { # Fehlerobjekt der Hetzner-API in eine lesbare Meldung uebersetzen
  local antwort="$1"
  if echo "$antwort" | jq -e '.error' >/dev/null 2>&1; then
    fehler "Hetzner meldet: $(echo "$antwort" | jq -r '.error.code + ": " + .error.message')"
  fi
  echo "$antwort"
}

eigene_ip() { # mehrere Dienste, weil einzelne gesperrt oder langsam sein koennen
  local u ip
  for u in https://checkip.amazonaws.com https://ifconfig.me/ip https://ipv4.icanhazip.com https://api.ipify.org; do
    ip="$(curl -fsS4 -m 6 "$u" 2>/dev/null | tr -d '[:space:]')" || continue
    [[ "$ip" =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]] && { echo "$ip"; return 0; }
  done
  fehler "Eigene oeffentliche IP nicht ermittelbar."
}

ssh_schluessel() {
  local k="$HOME/.ssh/agenten-doktor_ed25519"
  if [ ! -f "$k" ]; then
    ssh-keygen -q -t ed25519 -N "" -C "agenten-doktor@$(hostname -s)" -f "$k"
    info "Neuer SSH-Schluessel $k angelegt."
  fi
  echo "$k"
}

cmd_hetzner_anlegen() {
  # typ darf eine Liste sein ("cx43,cx53,cpx32"): der erste, den Hetzner gerade anbietet, gewinnt.
  local name="${1:?Servername}" typen="${2:-cx43}" ort="${3:-nbg1}" typ=""
  local key pub fp ip fw_id srv antwort
  key="$(ssh_schluessel)"; pub="$(cat "$key.pub")"
  # SSH-Schluessel im Projekt hinterlegen (idempotent ueber den Fingerabdruck)
  fp="$(ssh-keygen -E md5 -lf "$key.pub" | awk '{print $2}' | sed 's/^MD5://')"
  if ! hz GET "/ssh_keys?fingerprint=$fp" | jq -e '.ssh_keys[0]' >/dev/null; then
    hz_pruefen "$(hz POST /ssh_keys "$(jq -nc --arg n "agenten-doktor-$name" --arg k "$pub" '{name:$n, public_key:$k}')")" >/dev/null
    info "SSH-Schluessel bei Hetzner hinterlegt."
  fi
  local key_id
  key_id="$(hz GET "/ssh_keys?fingerprint=$fp" | jq -r '.ssh_keys[0].id')"
  ip="$(eigene_ip)"
  # Firewall: 80/443 offen, Tailscale direkt, SSH nur von der eigenen IP
  fw_id="$(hz GET "/firewalls?name=$name" | jq -r '.firewalls[0].id // empty')"
  local regeln
  regeln="$(jq -nc --arg ip "$ip/32" '[
    {direction:"in", protocol:"tcp", port:"22",    source_ips:[$ip], description:"SSH nur Einrichtung"},
    {direction:"in", protocol:"tcp", port:"80",    source_ips:["0.0.0.0/0","::/0"], description:"HTTP fuer Zertifikate"},
    {direction:"in", protocol:"tcp", port:"443",   source_ips:["0.0.0.0/0","::/0"], description:"HTTPS"},
    {direction:"in", protocol:"udp", port:"443",   source_ips:["0.0.0.0/0","::/0"], description:"HTTP/3"},
    {direction:"in", protocol:"udp", port:"41641", source_ips:["0.0.0.0/0","::/0"], description:"Tailscale direkt"},
    {direction:"in", protocol:"icmp",              source_ips:["0.0.0.0/0","::/0"], description:"Ping"}]')"
  if [ -z "$fw_id" ]; then
    antwort="$(hz_pruefen "$(hz POST /firewalls "$(jq -nc --arg n "$name" --argjson r "$regeln" '{name:$n, rules:$r}')")")"
    fw_id="$(echo "$antwort" | jq -r '.firewall.id')"
    info "Firewall $name angelegt (SSH nur von $ip)."
  fi
  srv="$(hz GET "/servers?name=$name" | jq -r '.servers[0].id // empty')"
  if [ -n "$srv" ]; then
    info "Server $name gibt es schon (id $srv), lege keinen zweiten an."
  else
    # Beliebte Typen (z.B. cx43) sind oft kurz ausverkauft: mehrere Runden ueber
    # den Wunschort und die Ausweichorte in Deutschland und Finnland.
    local body versuch l code orte frei t
    orte="$ort $(echo nbg1 fsn1 hel1 | tr ' ' '\n' | grep -vx "$ort" | tr '\n' ' ')"
    for versuch in 1 2 3 4 5 6; do
      for t in $(echo "$typen" | tr ',' ' '); do
      # Wo bietet Hetzner den Typ gerade an? (server_types[].locations[].available)
      frei="$(hz GET "/server_types?name=$t" | jq -r '[.server_types[0].locations[]? | select(.available == true) | .name] | join(" ")' 2>/dev/null || true)"
      if [ -z "$frei" ]; then info "$t ist laut Hetzner gerade an keinem Standort frei."; continue; fi
      for l in $orte; do
        case " $frei " in *" $l "*) ;; *) continue ;; esac
        typ="$t"
        body="$(jq -nc --arg n "$name" --arg t "$typ" --arg l "$l" --argjson kid "$key_id" --argjson fw "$fw_id" \
          --rawfile ud "$SERVER_DIR/cloud-init.yaml" \
          '{name:$n, server_type:$t, location:$l, image:"ubuntu-24.04", ssh_keys:[$kid],
            firewalls:[{firewall:$fw}], user_data:$ud, labels:{"verwaltet-von":"agenten-doktor"},
            public_net:{enable_ipv4:true, enable_ipv6:true}}')"
        antwort="$(hz POST /servers "$body")"
        if echo "$antwort" | jq -e '.server.id' >/dev/null 2>&1; then
          srv="$(echo "$antwort" | jq -r '.server.id')"
          info "Server $name ($typ, $l) wird angelegt, id $srv (Runde $versuch)."
          break 3
        fi
        code="$(echo "$antwort" | jq -r '.error.code // "unbekannt"')"
        case "$code" in
          resource_unavailable|unavailable|placement_error|server_type_unavailable|conflict|rate_limit_exceeded)
            info "$typ in $l gerade nicht verfuegbar ($code), versuche weiter ..." ;;
          *) hz_pruefen "$antwort" >/dev/null ;;
        esac
      done
      done
      sleep $((versuch * 10))
    done
    [ -n "$srv" ] || fehler "Keiner der Typen ($typen) ist in nbg1, fsn1 oder hel1 frei. Ausweichtyp mit Preis nennen (vorbereitung-pruefen zeigt die Lage) oder spaeter erneut."
  fi
  # warten bis laufend
  local i status
  for i in $(seq 1 60); do
    status="$(hz GET "/servers/$srv" | jq -r '.server.status')"
    [ "$status" = "running" ] && break
    sleep 5
  done
  hz GET "/servers/$srv" | jq '{id: .server.id, name: .server.name, status: .server.status,
     ipv4: .server.public_net.ipv4.ip, ipv6: .server.public_net.ipv6.ip, typ: .server.server_type.name,
     ort: .server.datacenter.location.name}'
}

cmd_hetzner_status() {
  hz GET "/servers?label_selector=verwaltet-von%3Dagenten-doktor" | jq '[.servers[] | {id, name, status,
    ipv4: .public_net.ipv4.ip, typ: .server_type.name, ort: .datacenter.location.name, angelegt: .created}]'
}

cmd_ssh_schliessen() { # Port 22 von aussen schliessen, Zugriff nur noch ueber Tailscale
  local name="${1:?Servername}" fw_id regeln
  fw_id="$(hz GET "/firewalls?name=$name" | jq -r '.firewalls[0].id // empty')"
  [ -n "$fw_id" ] || fehler "Firewall $name nicht gefunden."
  regeln="$(hz GET "/firewalls/$fw_id" | jq -c '[.firewall.rules[] | select(.port != "22")]')"
  hz_pruefen "$(hz POST "/firewalls/$fw_id/actions/set_rules" "$(jq -nc --argjson r "$regeln" '{rules:$r}')")" >/dev/null
  info "Port 22 ist von aussen geschlossen. SSH nur noch ueber Tailscale."
}

cmd_ssh_oeffnen() { # Notfall: SSH fuer die aktuelle eigene IP wieder oeffnen
  local name="${1:?Servername}" fw_id regeln ip
  ip="$(eigene_ip)"
  fw_id="$(hz GET "/firewalls?name=$name" | jq -r '.firewalls[0].id // empty')"
  regeln="$(hz GET "/firewalls/$fw_id" | jq -c --arg ip "$ip/32" '[.firewall.rules[] | select(.port != "22")] +
     [{direction:"in", protocol:"tcp", port:"22", source_ips:[$ip], description:"SSH Notzugang"}]')"
  hz_pruefen "$(hz POST "/firewalls/$fw_id/actions/set_rules" "$(jq -nc --argjson r "$regeln" '{rules:$r}')")" >/dev/null
  info "SSH fuer $ip geoeffnet. Nach der Reparatur wieder schliessen: $0 ssh-schliessen $name"
}

# ---------- Kopieren und entfernt ausfuehren ----------

SSH_OPTS=(-o StrictHostKeyChecking=accept-new -o ConnectTimeout=15 -o ServerAliveInterval=30)
VORLAGE_DIR="$HIER/../../../second-brain/assets/team-repo-vorlage"

cmd_ssh() { # Befehl auf dem Server ausfuehren
  local ziel="${1:?root@host}"; shift
  ssh -i "$(ssh_schluessel)" "${SSH_OPTS[@]}" "$ziel" "$@"
}

cmd_hochladen() { # Installer-Dateien auf den Server kopieren (ohne Geheimnisse)
  local ziel="${1:?root@host}" key
  key="$(ssh_schluessel)"
  rsync -az --delete --exclude '.env' --exclude 'daten/' --exclude 'geheim/' --exclude '__pycache__' \
    -e "ssh -i $key ${SSH_OPTS[*]}" "$SERVER_DIR/" "$ziel:/opt/agenten/installer/"
  if [ -d "$VORLAGE_DIR" ]; then
    rsync -az --delete -e "ssh -i $key ${SSH_OPTS[*]}" "$VORLAGE_DIR/" "$ziel:/opt/agenten/installer/wissens-vorlage/"
  fi
  # Fachskills des Skill-Pakets (z.B. anlage-v-assistent, deal-screener), die Agenten per fach_skills nutzen
  rsync -az --delete --exclude 'agenten-doktor/' --exclude 'second-brain/assets/' --exclude '__pycache__' \
    -e "ssh -i $key ${SSH_OPTS[*]}" "$HIER/../../../" "$ziel:/opt/agenten/installer/fach-skills/"
  ssh -i "$key" "${SSH_OPTS[@]}" "$ziel" 'install -m 0755 /opt/agenten/installer/bin/doktor /usr/local/bin/doktor \
    && chmod 0755 /opt/agenten/installer/werkzeuge/* 2>/dev/null; true'
  info "Installer nach $ziel:/opt/agenten/installer kopiert, Befehl 'doktor' installiert."
}

cmd_mietjump_hochladen() { # MietJUMP-Stand auf den Server, ohne .git und ohne Daten
  # Quelle: angegebener Checkout, sonst eigener Klon unter ~/.agenten-doktor/mietjump (privates Repo,
  # Lesezugriff als Outside Collaborator noetig; gh muss angemeldet sein).
  local ziel="${1:?root@host}" quelle="${2:-}" ref="${3:-}" key
  key="$(ssh_schluessel)"
  if [ -z "$quelle" ]; then
    quelle="$HOME/.agenten-doktor/mietjump"
    if [ -d "$quelle/.git" ]; then
      git -C "$quelle" fetch -q origin && git -C "$quelle" checkout -q "${MIETJUMP_REF:-main}" && git -C "$quelle" pull -q --ff-only || true
    else
      mkdir -p "$(dirname "$quelle")"
      gh repo clone "${MIETJUMP_REPO:-immodigit/mietjump}" "$quelle" -- -q \
        || fehler "MietJUMP-Repo nicht klonbar. Hast du Lesezugriff auf ${MIETJUMP_REPO:-immodigit/mietjump}? (bei ImmoDigit anfragen)"
      [ -n "${MIETJUMP_REF:-}" ] && git -C "$quelle" checkout -q "$MIETJUMP_REF"
    fi
  fi
  ref="${ref:-HEAD}"
  [ -d "$quelle/.git" ] || [ -f "$quelle/.git" ] || fehler "$quelle ist kein git-Checkout von MietJUMP."
  git -C "$quelle" cat-file -e "$ref:Dockerfile" 2>/dev/null \
    || fehler "Dieser MietJUMP-Stand hat noch keinen Serverbetrieb (Dockerfile fehlt). Branch mit Selbstbetrieb waehlen (MIETJUMP_REF)."
  git -C "$quelle" archive --format=tar "$ref" \
    | ssh -i "$key" "${SSH_OPTS[@]}" "$ziel" 'rm -rf /opt/agenten/mietjump-quelle && mkdir -p /opt/agenten/mietjump-quelle && tar -x -C /opt/agenten/mietjump-quelle'
  info "MietJUMP ($(git -C "$quelle" rev-parse --short "$ref") aus $quelle) nach $ziel:/opt/agenten/mietjump-quelle kopiert."
}

cmd_datei_senden() { # Datei (z.B. Kontoauszug CAMT/CSV) in den Arbeitsordner eines Agenten legen
  local ziel="${1:?root@host}" datei="${2:?datei}" agent="${3:-vera}" unterordner="${4:-bank}" key name
  key="$(ssh_schluessel)"
  [ -f "$datei" ] || fehler "$datei nicht gefunden."
  # printf statt Pipe aus basename: dessen Zeilenende wuerde tr sonst zu "_" am Namensende machen
  name="$(printf '%s' "$(basename "$datei")" | tr -c 'A-Za-z0-9._-' '_')"
  [[ "$agent" =~ ^[a-z][a-z0-9-]{1,30}$ && "$unterordner" =~ ^[a-z0-9_-]{1,30}$ ]] || fehler "ungueltiger Agent oder Ordner"
  # Geschrieben wird mit den Rechten des Agenten (UID 10000), nicht als root: Dann kann ein vom Agenten
  # gelegter Symlink (auch zwischen Pruefung und Schreiben) nirgends hinfuehren, wo der Agent nicht
  # ohnehin schreiben darf. Erst Temp-Datei (mktemp, exklusiv), dann mv -fT auf den Zielnamen.
  ssh -i "$key" "${SSH_OPTS[@]}" "$ziel" "setpriv --reuid=10000 --regid=10000 --clear-groups sh -c 'd=/opt/agenten/daten/agenten/$agent/arbeit/$unterordner; mkdir -p \"\$d\" && t=\$(mktemp -p \"\$d\" .eingang.XXXXXX) && cat > \"\$t\" && mv -fT \"\$t\" \"\$d/$name\"'" < "$datei"
  info "$name liegt bei $agent unter arbeit/$unterordner/. Sag dem Agenten Bescheid (oder die Routine holt es ab)."
}

cmd_konfig_setzen() { # Zeilen KEY=WERT von stdin in /opt/agenten/konfig.env uebernehmen (nicht geheim)
  local ziel="${1:?root@host}"
  cmd_ssh "$ziel" 'umask 022; f=/opt/agenten/konfig.env; touch $f; while IFS= read -r z; do
      [ -n "$z" ] || continue; k="${z%%=*}"; grep -v "^$k=" $f > $f.neu || true; echo "$z" >> $f.neu; mv $f.neu $f; done; cat $f'
}

cmd_tailscale_beitritt() { # gespeicherten Tailscale-Schluessel nutzen, Server ins Tailnet bringen
  local ziel="${1:?root@host}" name="${2:-agenten}" key
  key="$(ssh_schluessel)"
  kc_vorhanden tailscale || fehler "Kein Tailscale-Schluessel im Schluesselbund. Erst: $0 token-speichern tailscale"
  kc_lesen tailscale | ssh -i "$key" "${SSH_OPTS[@]}" "$ziel" "umask 077; cat > /root/.ts-schluessel; \
    tailscale up --auth-key=file:/root/.ts-schluessel --hostname=$name --accept-dns=false; rc=\$?; rm -f /root/.ts-schluessel; \
    iptables -C DOCKER-USER -o tailscale0 -m conntrack --ctstate NEW -j REJECT 2>/dev/null || iptables -I DOCKER-USER -o tailscale0 -m conntrack --ctstate NEW -j REJECT; \
    iptables -C OUTPUT -o tailscale0 -m conntrack --ctstate NEW -j REJECT 2>/dev/null || iptables -A OUTPUT -o tailscale0 -m conntrack --ctstate NEW -j REJECT; \
    tailscale ip -4; exit \$rc"
  info "Server ist im Tailnet. Er kann selbst keine Verbindungen zu deinen anderen Geraeten aufbauen (nur Antworten)."
}

cmd_codex_anmelden() { # Geraete-Anmeldung ChatGPT/Codex fuer einen Agenten; gibt Link und Code aus
  local ziel="${1:?root@host}" slug="${2:?agent}" log
  log="$(mktemp -t codex-anmeldung)"
  ( cmd_ssh "$ziel" "docker exec -u hermes agent-$slug hermes auth add openai-codex --no-browser --timeout 900" >"$log" 2>&1 & )
  for _ in $(seq 1 30); do
    if grep -qiE 'https://[^ ]+' "$log" && grep -qiE '[A-Z0-9]{4}-[A-Z0-9]{4,5}' "$log"; then break; fi
    sleep 2
  done
  grep -oE 'https://[^ ]+' "$log" | head -1
  grep -oE '\b[A-Z0-9]{4}-[A-Z0-9]{4,5}\b' "$log" | head -1
  info "Link oeffnen, Code bestaetigen. Protokoll: $log (enthaelt keine Geheimnisse, nur Link und Code)."
}

cmd_dns_pruefen() { # zeigt, ob <name> auf <ip> zeigt (oeffentliche Aufloesung)
  local name="${1:?name}" ip="${2:?ip}" ist
  ist="$(dig +short "$name" A | tail -1)"
  if [ "$ist" = "$ip" ]; then info "$name zeigt auf $ip."; else fehler "$name zeigt auf '${ist:-nichts}', erwartet $ip."; fi
}

cmd_wissen_repo_anlegen() { # privates GitHub-Repo fuer die Wissensbasis (Inhalt fuellt der Server-Doktor)
  local repo="${1:?owner/name}"
  if gh repo view "$repo" >/dev/null 2>&1; then info "Repo $repo gibt es schon, wird angebunden."; return 0; fi
  gh repo create "$repo" --private --description "Wissensbasis und Agenten-Definitionen (Agenten-Doktor)" >/dev/null
  info "Privates Repo $repo angelegt."
}

# Geheimnis aus dem Schluesselbund auf den Server legen (per stdin, nie argv).
cmd_geheimnis_senden() {
  local ziel="${1:?root@host}" name="${2:?name}" schluessel="${3:?ENV_SCHLUESSEL}" key
  key="$(ssh_schluessel)"
  kc_vorhanden "$name" || fehler "$name fehlt im Schluesselbund."
  kc_lesen "$name" | ssh -i "$key" "$ziel" "doktor geheimnis-setzen $schluessel"
  info "$schluessel auf dem Server gesetzt."
}

cmd_hetzner_schutz() { # Loeschschutz (kostenlos) und optional Hetzner-Backups (+20 % Serverpreis)
  local name="${1:?Servername}" backups="${2:-}" srv
  srv="$(hz GET "/servers?name=$name" | jq -r '.servers[0].id // empty')"
  [ -n "$srv" ] || fehler "Server $name nicht gefunden."
  hz_pruefen "$(hz POST "/servers/$srv/actions/change_protection" '{"delete":true,"rebuild":true}')" >/dev/null
  info "Loesch- und Neuaufbau-Schutz fuer $name aktiv."
  if [ "$backups" = "--backups" ]; then
    hz_pruefen "$(hz POST "/servers/$srv/actions/enable_backup" '{}')" >/dev/null
    info "Hetzner-Backups aktiv (7 taegliche Abbilder, +20 % Serverpreis)."
  fi
}

# ---------- Vorbereitungs-Check (vor dem Durchlauf, aendert nichts) ----------

VP_ROT=0; VP_GELB=0
vp() { # vp <gruen|gelb|rot> <was> <hinweis>
  case "$1" in
    gruen) printf '🟢 %-34s %s\n' "$2" "$3" ;;
    gelb)  printf '🟡 %-34s %s\n' "$2" "$3"; VP_GELB=$((VP_GELB + 1)) ;;
    rot)   printf '🔴 %-34s %s\n' "$2" "$3"; VP_ROT=$((VP_ROT + 1)) ;;
  esac
}

vp_bot() { # Telegram-Bot pruefen, gibt den Botnamen auf stdout
  kc_lesen "$1" | awk '{print "url = \"https://api.telegram.org/bot" $0 "/getMe\""}' \
    | curl -sS -m 15 -K - 2>/dev/null | jq -r 'if .ok then .result.username else empty end' 2>/dev/null || true
}

cmd_vorbereitung_pruefen() {
  # Liest optional ~/.agenten-doktor/<projekt>/start.env (nicht geheim: DOMAIN, MODELL_ANBIETER,
  # WISSEN_REPO, POSTFACH, MIETJUMP=ja|nein, SERVER_TYPEN=cx43,cx53,cpx32). Prueft nur, legt nichts an.
  local start="$HOME/.agenten-doktor/$PROJEKT/start.env" w fehlt="" v t name1 name2 ts
  local DOMAIN="" MODELL_ANBIETER="" WISSEN_REPO="" POSTFACH="" MIETJUMP="ja" SERVER_TYPEN="cx43"
  if [ -f "$start" ]; then
    while IFS='=' read -r k v; do
      case "$k" in DOMAIN|MODELL_ANBIETER|WISSEN_REPO|POSTFACH|MIETJUMP|SERVER_TYPEN) printf -v "$k" '%s' "${v%$'\r'}" ;; esac
    done < <(grep -E '^[A-Z_]+=' "$start")
  fi
  echo "Vorbereitungs-Check, Projekt $PROJEKT ($(date '+%d.%m.%Y %H:%M'))"
  echo

  # 1. Werkzeuge auf dem Mac
  for w in jq curl rsync ssh scp gh python3 security pbpaste dig nc; do
    command -v "$w" >/dev/null 2>&1 || fehlt="$fehlt $w"
  done
  if [ -z "$fehlt" ]; then vp gruen "Werkzeuge" "alle da"
  else vp rot "Werkzeuge" "fehlt:$fehlt (brew install$fehlt)"; fi
  if python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3, 11) else 1)' 2>/dev/null; then
    vp gruen "Python" "$(python3 --version 2>&1)"
  else vp rot "Python" "mindestens 3.11 noetig (brew install python)"; fi

  # 2. GitHub und MietJUMP-Zugriff
  if gh auth status >/dev/null 2>&1; then
    vp gruen "GitHub-Anmeldung (gh)" "$(gh api user --jq .login 2>/dev/null)"
    if [ "$MIETJUMP" != "nein" ]; then
      if gh api "repos/${MIETJUMP_REPO:-immodigit/mietjump}" --silent >/dev/null 2>&1; then
        vp gruen "MietJUMP-Lesezugriff" "${MIETJUMP_REPO:-immodigit/mietjump}"
      elif gh api user/repository_invitations --jq '.[].repository.full_name' 2>/dev/null | grep -qix "${MIETJUMP_REPO:-immodigit/mietjump}"; then
        vp rot "MietJUMP-Lesezugriff" "Einladung liegt vor, aber nicht angenommen: github.com/${MIETJUMP_REPO:-immodigit/mietjump}/invitations"
      else
        vp rot "MietJUMP-Lesezugriff" "kein Zugriff, bei ImmoDigit Einladung anfragen"
      fi
    fi
    if [ -n "$WISSEN_REPO" ]; then
      v="$(gh repo view "$WISSEN_REPO" --json visibility --jq .visibility 2>/dev/null || true)"
      case "$v" in
        PRIVATE) vp gruen "Wissens-Repo" "$WISSEN_REPO (privat)" ;;
        "")      vp gelb "Wissens-Repo" "$WISSEN_REPO gibt es noch nicht, legt der Doktor an" ;;
        *)       vp rot "Wissens-Repo" "$WISSEN_REPO ist $v, muss privat sein" ;;
      esac
    fi
  else
    vp rot "GitHub-Anmeldung (gh)" "nicht angemeldet: gh auth login --web --git-protocol https"
  fi

  # 3. Tailscale auf dem Mac (fuer SSH ueber das private Netz)
  ts=""
  for t in /Applications/Tailscale.app/Contents/MacOS/Tailscale "$(command -v tailscale 2>/dev/null || true)"; do
    [ -n "$t" ] && [ -x "$t" ] && { ts="$t"; break; }
  done
  if [ -z "$ts" ]; then vp rot "Tailscale auf dem Mac" "App fehlt (App Store: Tailscale), dann anmelden"
  elif "$ts" status >/dev/null 2>&1; then vp gruen "Tailscale auf dem Mac" "angemeldet"
  else vp rot "Tailscale auf dem Mac" "App da, aber nicht angemeldet oder nicht gestartet"; fi

  # 4. Zugaenge im Schluesselbund: vorhanden wird live geprueft, fehlend legt der Doktor im Durchlauf an
  if kc_vorhanden hetzner; then
    v="$(hz GET '/servers?per_page=1' 2>/dev/null | jq -r 'if .error then "FEHLER " + .error.code else (.meta.pagination.total_entries | tostring) end' 2>/dev/null || echo "FEHLER netz")"
    case "$v" in
      FEHLER*) vp rot "Hetzner-Token" "ungueltig oder gesperrt ($v), neu erzeugen" ;;
      *)
        vp gruen "Hetzner-Token" "gueltig, $v Server im Projekt"
        # Verfuegbarkeit steht je Standort am Servertyp (locations[].available), nur EU-Standorte
        local erster="${SERVER_TYPEN%%,*}" typ_frei="" typ_orte=""
        for t in $(echo "$SERVER_TYPEN" | tr ',' ' '); do
          v="$(hz GET "/server_types?name=$t" 2>/dev/null \
            | jq -r '[.server_types[0].locations[]? | select(.available == true) | .name | select(. == "nbg1" or . == "fsn1" or . == "hel1")] | join(" ")' 2>/dev/null || true)"
          [ -n "$v" ] && { typ_frei="$t"; typ_orte="$v"; break; }
        done
        if [ "$typ_frei" = "$erster" ]; then vp gruen "Servertyp $erster frei" "$typ_orte"
        elif [ -n "$typ_frei" ]; then vp gelb "Servertyp $erster frei" "nein, Ausweichtyp $typ_frei frei ($typ_orte), Preis pruefen"
        else vp gelb "Servertyp frei" "keiner von $SERVER_TYPEN frei, Ausweichtyp in den Start-Prompt (z. B. cx53, cpx32)"; fi ;;
    esac
  else vp gelb "Hetzner-Token" "fehlt, erzeugt der Doktor in Chrome (Hetzner-Konto muss geprueft sein)"; fi

  if kc_vorhanden github; then
    local gh_url="https://api.github.com/user"
    [ -n "$WISSEN_REPO" ] && gh_url="https://api.github.com/repos/$WISSEN_REPO"
    v="$(kc_lesen github | awk '{print "header = \"Authorization: Bearer " $0 "\""}' \
      | curl -sS -m 10 -K - "$gh_url" 2>/dev/null \
      | jq -r '.full_name // .login // ("FEHLER " + (.message // "?"))' 2>/dev/null || echo "FEHLER netz")"
    case "$v" in FEHLER*) vp rot "GitHub-Token (Wissens-Repo)" "$v" ;; *) vp gruen "GitHub-Token (Wissens-Repo)" "$v" ;; esac
  else vp gelb "GitHub-Token (Wissens-Repo)" "fehlt, erzeugt der Doktor in Chrome"; fi

  name1=""; name2=""
  if kc_vorhanden telegram; then
    name1="$(vp_bot telegram || true)"
    if [ -n "$name1" ]; then vp gruen "Telegram-Bot Kurt" "@$name1"; else vp rot "Telegram-Bot Kurt" "Token ungueltig"; fi
  else vp gelb "Telegram-Bot Kurt" "fehlt, legt der Doktor in Telegram Web an (Konto unter 19 Bots!)"; fi
  if kc_vorhanden doktor-telegram; then
    name2="$(vp_bot doktor-telegram || true)"
    if [ -z "$name2" ]; then vp rot "Telegram-Bot Doktor" "Token ungueltig"
    elif [ "$name2" = "$name1" ]; then vp rot "Telegram-Bot Doktor" "derselbe Bot wie Kurt, braucht einen eigenen"
    else vp gruen "Telegram-Bot Doktor" "@$name2"; fi
  else vp gelb "Telegram-Bot Doktor" "fehlt, legt der Doktor an"; fi

  case "$MODELL_ANBIETER" in
    meridian)
      if kc_vorhanden claude-oauth; then vp gruen "Modell (Meridian)" "Token vorhanden"
      else vp rot "Modell (Meridian)" "fehlt: claude setup-token im eigenen Terminal, dann token-speichern claude-oauth"; fi ;;
    openai)
      if kc_vorhanden openai; then
        v="$(kc_lesen openai | awk '{print "header = \"Authorization: Bearer " $0 "\""}' | curl -sS -m 10 -o /dev/null -w '%{http_code}' -K - https://api.openai.com/v1/models 2>/dev/null || true)"
        if [ "$v" = "200" ]; then vp gruen "Modell (OpenAI)" "Schluessel gueltig"; else vp rot "Modell (OpenAI)" "Schluessel abgelehnt (HTTP $v)"; fi
      else vp rot "Modell (OpenAI)" "fehlt: Schluessel mit Ausgabelimit anlegen, token-speichern openai"; fi ;;
    openrouter)
      if kc_vorhanden openrouter; then
        v="$(kc_lesen openrouter | awk '{print "header = \"Authorization: Bearer " $0 "\""}' | curl -sS -m 10 -o /dev/null -w '%{http_code}' -K - https://openrouter.ai/api/v1/key 2>/dev/null || true)"
        if [ "$v" = "200" ]; then vp gruen "Modell (OpenRouter)" "Schluessel gueltig"; else vp rot "Modell (OpenRouter)" "Schluessel abgelehnt (HTTP $v)"; fi
      else vp rot "Modell (OpenRouter)" "fehlt: Schluessel mit Limit anlegen, token-speichern openrouter"; fi ;;
    codex|"")
      vp gelb "Modell (ChatGPT/Codex)" "Anmeldung je Agent am Ende des Durchlaufs (zwei Geraetecodes bestaetigen)" ;;
    *) vp rot "Modell" "unbekannter MODELL_ANBIETER=$MODELL_ANBIETER" ;;
  esac

  if kc_vorhanden gmail-client-id && kc_vorhanden gmail-client-secret && kc_vorhanden gmail-refresh-token; then
    t="$( { printf 'data = "grant_type=refresh_token&client_id='; kc_lesen gmail-client-id | tr -d '\n'
            printf '&client_secret='; kc_lesen gmail-client-secret | tr -d '\n'
            printf '&refresh_token='; kc_lesen gmail-refresh-token | tr -d '\n'; printf '"\n'; } \
          | curl -sS -m 10 -K - https://oauth2.googleapis.com/token 2>/dev/null | jq -r '.access_token // ("FEHLER " + (.error // "?"))' 2>/dev/null || echo "FEHLER netz")"
    case "$t" in
      FEHLER*) vp rot "Gmail fuer Vera" "Anmeldung abgelaufen ($t), google-anmeldung.py erneut" ;;
      *) v="$(printf 'header = "Authorization: Bearer %s"\n' "$t" | curl -sS -m 10 -K - https://gmail.googleapis.com/gmail/v1/users/me/profile 2>/dev/null | jq -r '.emailAddress // empty' 2>/dev/null || true)"
         t=""
         if [ -n "$v" ]; then vp gruen "Gmail fuer Vera" "$v"
           [ -n "$POSTFACH" ] && [ "$(echo "$POSTFACH" | tr 'A-Z' 'a-z')" != "$(echo "$v" | tr 'A-Z' 'a-z')" ] && vp rot "Gmail-Postfach" "verbunden ist $v, gewuenscht $POSTFACH"
         else vp rot "Gmail fuer Vera" "Token da, aber Gmail antwortet nicht"; fi ;;
    esac
  else vp gelb "Gmail fuer Vera" "fehlt, richtet der Doktor ein (Google-Anmeldung in Chrome noetig)"; fi

  if kc_vorhanden tailscale; then vp gruen "Tailscale-Schluessel" "vorhanden (gilt 1 Tag, einmal nutzbar)"
  else vp gelb "Tailscale-Schluessel" "fehlt, erzeugt der Doktor in Chrome"; fi

  # 5. Adresse
  case "$DOMAIN" in
    "") vp rot "Adresse" "nicht festgelegt: Subdomain unter cl.immodigit.de oder eigene Domain im Start-Prompt nennen" ;;
    *.cl.immodigit.de) vp gruen "Adresse" "$DOMAIN (DNS-Eintraege setzt ImmoDigit, sobald die IP da ist)" ;;
    *) v="$(dig +short "$DOMAIN" A 2>/dev/null | tail -1 || true)"
       if [ -n "$v" ]; then
         vp gelb "Adresse" "$DOMAIN zeigt schon auf $v. Wird auf den neuen Server umgestellt: nur eine freie Subdomain nehmen (z. B. agenten.meinefirma.de)"
       else
         vp gruen "Adresse" "$DOMAIN (noch kein Eintrag; Anmeldung beim DNS-Anbieter in Chrome noetig)"
       fi ;;
  esac

  echo
  echo "Nicht per Befehl pruefbar: Anmeldungen in Chrome bei Hetzner, GitHub, Google (Veras Postfach),"
  echo "Telegram Web und Tailscale prueft der Doktor per Tab-Abfrage. Die Zahl der Telegram-Bots"
  echo "(hoechstens 18) pruefst du selbst: /mybots an @BotFather (Checkliste Nr. 6)."
  echo
  if [ "$VP_ROT" -eq 0 ]; then
    echo "Ergebnis: bereit ($VP_GELB Punkte erledigt der Doktor im Durchlauf)."
  else
    echo "Ergebnis: $VP_ROT Punkt(e) rot. Erst beheben, dann erneut pruefen."
  fi
  mkdir -p "$HOME/.agenten-doktor/$PROJEKT"
  printf -- '- %s Vorbereitungs-Check: %s rot, %s gelb\n' "$(date '+%Y-%m-%d %H:%M')" "$VP_ROT" "$VP_GELB" \
    >> "$HOME/.agenten-doktor/$PROJEKT/logbuch.md"
  [ "$VP_ROT" -eq 0 ]
}

usage() {
  cat <<EOF
doktor-lokal (Projekt: $PROJEKT, setzen mit DOKTOR_PROJEKT=...)

  vorbereitung-pruefen          prueft alle Voraussetzungen, aendert nichts (vor dem Start)
  token-speichern <name>        Wert aus der Zwischenablage in den Schluesselbund
                                (danach wird die Zwischenablage geleert)
  token-pruefen <name...>       zeigt nur vorhanden/fehlt
  hetzner-anlegen <name> [typ] [ort]   VM mit Firewall und Grundausstattung
  hetzner-status                alle vom Doktor verwalteten Server
  hetzner-schutz <name> [--backups]   Loeschschutz an, optional Hetzner-Backups (+20 %)
  ssh-schliessen <name>         Port 22 von aussen zu (nach Tailscale-Beitritt)
  ssh-oeffnen <name>            Notzugang fuer die eigene IP
  hochladen <root@host>         Installer-Dateien und Wissens-Vorlage auf den Server
  ssh <root@host> <befehl>      Befehl auf dem Server (z.B. "doktor check")
  mietjump-hochladen <root@host> [quelle] [ref]   MietJUMP-Stand auf den Server
                                (ohne quelle: Klon von immodigit/mietjump unter ~/.agenten-doktor/mietjump)
  datei-senden <root@host> <datei> [agent] [ordner]  z.B. Kontoauszug an Vera (arbeit/bank/)
  konfig-setzen <root@host>     KEY=WERT-Zeilen von stdin in konfig.env (nicht geheim)
  tailscale-beitritt <root@host> [name]   Server ins Tailnet, Ausgang zu anderen Geraeten gesperrt
  codex-anmelden <root@host> <agent>      ChatGPT/Codex-Anmeldung: Link und Code fuer Chrome
  dns-pruefen <name> <ip>       oeffentliche Aufloesung pruefen
  wissen-repo-anlegen <owner/name>        privates GitHub-Repo anlegen
  geheimnis-senden <root@host> <name> <ENV_SCHLUESSEL>
EOF
}

befehl="${1:-}"; shift || true
case "$befehl" in
  token-speichern) pbpaste | kc_schreiben "${1:?name}"; printf '' | pbcopy ;;
  token-speichern-stdin) kc_schreiben "${1:?name}" ;;
  vorbereitung-pruefen) cmd_vorbereitung_pruefen ;;
  token-pruefen) for n in "$@"; do if kc_vorhanden "$n"; then echo "$n: vorhanden"; else echo "$n: fehlt"; fi; done ;;
  hetzner-anlegen) cmd_hetzner_anlegen "$@" ;;
  hetzner-status) cmd_hetzner_status ;;
  ssh-schliessen) cmd_ssh_schliessen "$@" ;;
  hetzner-schutz) cmd_hetzner_schutz "$@" ;;
  ssh-oeffnen) cmd_ssh_oeffnen "$@" ;;
  hochladen) cmd_hochladen "$@" ;;
  ssh) cmd_ssh "$@" ;;
  mietjump-hochladen) cmd_mietjump_hochladen "$@" ;;
  datei-senden) cmd_datei_senden "$@" ;;
  konfig-setzen) cmd_konfig_setzen "$@" ;;
  tailscale-beitritt) cmd_tailscale_beitritt "$@" ;;
  codex-anmelden) cmd_codex_anmelden "$@" ;;
  dns-pruefen) cmd_dns_pruefen "$@" ;;
  wissen-repo-anlegen) cmd_wissen_repo_anlegen "$@" ;;
  geheimnis-senden) cmd_geheimnis_senden "$@" ;;
  *) usage ;;
esac
