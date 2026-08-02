#!/usr/bin/env bash
set -Eeuo pipefail
if [[ $# -ne 1 ]]; then
  echo "Usage: $0 backup.tar.gz"
  exit 2
fi
cd "$(dirname "$0")"
docker compose -f compose.yml down
tar -xzf "$1"
chmod 600 .env data/id_ed25519
docker compose -f compose.yml up -d --build
