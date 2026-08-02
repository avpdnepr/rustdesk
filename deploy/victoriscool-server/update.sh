#!/usr/bin/env bash
set -Eeuo pipefail
cd "$(dirname "$0")"
./backup.sh
docker compose -f compose.yml pull
docker compose -f compose.yml up -d --build --remove-orphans
docker image prune -f
