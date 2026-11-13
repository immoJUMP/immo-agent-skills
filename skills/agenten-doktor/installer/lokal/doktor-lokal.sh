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
  local name="${1:?Servername}" typ="${2:-cx43}" ort="${3:-nbg1}"
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
    local body versuch l code orte
    orte="$ort $(echo nbg1 fsn1 hel1 | tr ' ' '\n' | grep -vx "$ort" | tr '\n' ' ')"
    for versuch in 1 2 3 4 5 6; do
      for l in $orte; do
        body="$(jq -nc --arg n "$name" --arg t "$typ" --arg l "$l" --argjson kid "$key_id" --argjson fw "$fw_id" \
          --rawfile ud "$SERVER_DIR/cloud-init.yaml" \
          '{name:$n, server_type:$t, location:$l, image:"ubuntu-24.04", ssh_keys:[$kid],
            firewalls:[{firewall:$fw}], user_data:$ud, labels:{"verwaltet-von":"agenten-doktor"},
            public_net:{enable_ipv4:true, enable_ipv6:true}}')"
        antwort="$(hz POST /servers "$body")"
        if echo "$antwort" | jq -e '.server.id' >/dev/null 2>&1; then
          srv="$(echo "$antwort" | jq -r '.server.id')"
          info "Server $name ($typ, $l) wird angelegt, id $srv (Runde $versuch)."
          break 2
        fi
        code="$(echo "$antwort" | jq -r '.error.code // "unbekannt"')"
        case "$code" in
          resource_unavailable|unavailable|placement_error|server_type_unavailable|conflict|rate_limit_exceeded)
            info "$typ in $l gerade nicht verfuegbar ($code), versuche weiter ..." ;;
          *) hz_pruefen "$antwort" >/dev/null ;;
        esac
      done
      sleep $((versuch * 10))
    done
    [ -n "$srv" ] || fehler "$typ ist an keinem Standort verfuegbar. Spaeter erneut versuchen oder anderen Typ waehlen (z.B. cx33, cpx31)."
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
        || fehler "MietJUMP-Repo nicht klonbar. Hast du Lesezugriff auf ${MIETJUMP_REPO:-immodigit/mietjump}? (Christian fragen)"
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
  name="$(basename "$datei" | tr -c 'A-Za-z0-9._-' '_')"
  [[ "$agent" =~ ^[a-z][a-z0-9-]{1,30}$ && "$unterordner" =~ ^[a-z0-9_-]{1,30}$ ]] || fehler "ungueltiger Agent oder Ordner"
  # Erst in eine neue Temp-Datei (mktemp legt exklusiv an), dann per mv ersetzen: ein vom Agenten
  # angelegter Symlink am Zielnamen wird ersetzt statt verfolgt.
  ssh -i "$key" "${SSH_OPTS[@]}" "$ziel" "d=/opt/agenten/daten/agenten/$agent/arbeit/$unterordner; [ ! -L \$d ] || exit 3; mkdir -p \$d && t=\$(mktemp -p \$d .eingang.XXXXXX) && cat > \$t && mv -fT \$t \$d/$name && chown -h 10000:10000 \$d \$d/$name" < "$datei"
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

usage() {
  cat <<EOF
doktor-lokal (Projekt: $PROJEKT, setzen mit DOKTOR_PROJEKT=...)

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
