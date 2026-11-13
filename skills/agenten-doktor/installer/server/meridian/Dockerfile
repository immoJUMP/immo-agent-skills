# Meridian: reicht ein Claude-Code-Abo (Setup-Token) als Anthropic-kompatible API weiter.
# ACHTUNG: Die Nutzung von Pro/Max-Zugangsdaten in Fremd-Harnesses wie Hermes ist laut
# Anthropic-Verbraucherbedingungen nicht erlaubt (Kontosperre moeglich). Nur auf
# ausdruecklichen Wunsch des Eigentuemers, siehe references/modelle-und-kosten.md.
# Versionen fest: Meridian 1.77.1 mit Claude Code 2.1.283 (aeltere Kombinationen rufen
# Werkzeuge mit neueren Modellen in Schleife auf bzw. lehnen das Modell ab).
FROM node:24-alpine
ARG MERIDIAN_VERSION=1.77.1
ARG CLAUDE_CODE_VERSION=2.1.283
RUN apk add --no-cache bash ca-certificates \
 && npm install -g --omit=dev @anthropic-ai/claude-code@${CLAUDE_CODE_VERSION} @rynfar/meridian@${MERIDIAN_VERSION} \
 && npm cache clean --force \
 && (cat /proc/sys/kernel/random/uuid | tr -d '-' > /etc/machine-id)
USER node
ENV HOME=/home/node MERIDIAN_HOST=0.0.0.0 MERIDIAN_PORT=3456 MERIDIAN_PASSTHROUGH=1
EXPOSE 3456
HEALTHCHECK --interval=30s --timeout=5s --retries=3 CMD wget -qO- http://127.0.0.1:3456/health >/dev/null || exit 1
CMD ["meridian"]
