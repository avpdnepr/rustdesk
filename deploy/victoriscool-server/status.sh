#!/usr/bin/env bash
set -Eeuo pipefail
cd "$(dirname "$0")"
docker compose -f compose.yml ps
printf '\nPublic key: '
cat data/id_ed25519.pub
