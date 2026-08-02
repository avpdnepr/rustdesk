#!/usr/bin/env bash
set -Eeuo pipefail
cd "$(dirname "$0")"
docker compose -f compose.yml down
printf 'Data and keys were kept in %s/data\n' "$PWD"
