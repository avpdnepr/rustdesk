#!/usr/bin/env bash
set -Eeuo pipefail
cd "$(dirname "$0")"
mkdir -p backups
stamp=$(date -u +%Y%m%dT%H%M%SZ)
tar --exclude='./backups' -czf "backups/victor-server-${stamp}.tar.gz" data .env compose.yml web README.md
retention=${BACKUP_RETENTION_DAYS:-30}
find backups -type f -name 'victor-server-*.tar.gz' -mtime +"$retention" -delete
sha256sum "backups/victor-server-${stamp}.tar.gz" > "backups/victor-server-${stamp}.tar.gz.sha256"
echo "backups/victor-server-${stamp}.tar.gz"
