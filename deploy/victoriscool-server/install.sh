#!/usr/bin/env bash
set -Eeuo pipefail
cd "$(dirname "$0")"

if [[ ${EUID} -ne 0 ]]; then
  exec sudo "$0" "$@"
fi

if [[ ! -f .env ]]; then
  cp .env.example .env
  echo "Edit .env and set a strong ADMIN_PASSWORD before continuing."
  exit 1
fi

if [[ ! -f data/id_ed25519 || ! -f data/id_ed25519.pub ]]; then
  echo "Copy the matching id_ed25519 and id_ed25519.pub files from the private server archive into ./data/."
  exit 1
fi

command -v docker >/dev/null || { echo "Docker is required."; exit 1; }
docker compose version >/dev/null 2>&1 || { echo "Docker Compose plugin is required."; exit 1; }

chmod 600 .env data/id_ed25519
chmod 644 data/id_ed25519.pub

if command -v ufw >/dev/null; then
  ufw allow 21115:21119/tcp
  ufw allow 21116/udp
  ufw allow 8080/tcp
fi

docker compose -f compose.yml pull
docker compose -f compose.yml up -d --build

echo "VictorIsCool server started."
echo "Web panel: http://217.24.161.103:8080"
