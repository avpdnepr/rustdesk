# VictorIsCool server + web branch 1.0.0

This branch is dedicated to the self-hosted server deployment.

## Components

- RustDesk Server OSS `hbbs` and `hbbr`
- Docker Compose deployment
- authenticated FastAPI operational dashboard
- server status and public-key display
- downloadable client configuration
- install, update, backup, restore, status and uninstall scripts
- Nginx reverse-proxy example

## Network

- ID server: `217.24.161.103`
- Relay server: `217.24.161.103`
- Public key: `YQiOvC0OOyIJ1wT4v0SZs7YwLZWxEfkW8ZtzRMSdnUA=`
- TCP: `21115-21119`
- UDP: `21116`
- Dashboard: TCP `8080`

The private key and populated `.env` are intentionally excluded from this public repository. Use the separately delivered private server archive.

The included dashboard is an OSS operations panel, not the commercial RustDesk Server Pro console. Pro-only centralized users/devices, LDAP/OIDC, MFA, address books, audit controls and policy management require a valid Server Pro license or a separately implemented management platform.
