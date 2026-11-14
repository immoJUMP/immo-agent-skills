#!/bin/bash
# Nachweis: Hermes v0.22.2 mit der Doktor-Konfiguration (alt/neu), Start, Neustart, Stopp gegen die Telegram-Attrappe.
set -u
cd /root/tgtest
BILD=docker.io/nousresearch/hermes-agent:v0.22.2
docker network create tgnetz >/dev/null 2>&1 || true
docker rm -f tgattrappe agent-test >/dev/null 2>&1 || true
mkdir -p log && : > log/aufrufe.jsonl
docker run -d --name tgattrappe --network tgnetz -v "$PWD/tgattrappe.py:/a.py:ro" -v "$PWD/log:/log" python:3.12-alpine python /a.py >/dev/null
lauf() {
  local v="$1"
  rm -rf "daten-$v"; mkdir -p "daten-$v"; cp "config-$v.yaml" "daten-$v/config.yaml"; chown -R 10000:10000 "daten-$v"
  : > log/aufrufe.jsonl
  docker run -d --name agent-test --network tgnetz -e HERMES_UID=10000 -e HERMES_GID=10000 \
    -e TELEGRAM_BOT_TOKEN=123456:TESTTOKEN -e TELEGRAM_ALLOWED_USERS=4711 -e TELEGRAM_HOME_CHANNEL=4711 \
    -e OPENROUTER_API_KEY=dummy -e TZ=Europe/Berlin -v "$PWD/daten-$v:/opt/data" "$BILD" gateway run >/dev/null
  sleep 60; echo "-- $v nach Start: $(grep -c . log/aufrufe.jsonl) Aufrufe, getMe: $(grep -c '"getMe"' log/aufrufe.jsonl)"
  docker restart agent-test >/dev/null; sleep 60
  docker stop agent-test >/dev/null; sleep 5
  docker logs agent-test 2>&1 | grep -i -E "telegram|restart notification|shutdown notification|suppress|home channel" | tail -8 > "log/hermes-$v.txt"
  docker rm agent-test >/dev/null
  echo "== $v: Nachrichten an den Eigentuemer (sendMessage):"
  grep '"sendMessage"' log/aufrufe.jsonl || echo "   keine"
  echo "== $v: alle Methoden: $(python3 -c "import json,collections;print(dict(collections.Counter(json.loads(l)['methode'] for l in open('log/aufrufe.jsonl'))))")"
  cp log/aufrufe.jsonl "log/aufrufe-$v.jsonl"
}
docker pull -q "$BILD" >/dev/null
lauf alt
lauf neu
docker rm -f tgattrappe >/dev/null
