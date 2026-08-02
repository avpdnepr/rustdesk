# VictorIsCool RustDesk Server OSS

This branch contains the server and web deployment for VictorIsCool 1.0.0.

## Included

- `hbbs` for ID/rendezvous traffic;
- `hbbr` for relay traffic;
- authenticated VictorIsCool status dashboard on TCP `8080`;
- install, update, backup, restore, status and uninstall scripts;
- Nginx reverse-proxy example;
- downloadable client configuration.

## Configuration

- server: `217.24.161.103`
- client public key: `YQiOvC0OOyIJ1wT4v0SZs7YwLZWxEfkW8ZtzRMSdnUA=`
- RustDesk ports: TCP `21115-21119`, UDP `21116`

## Private files

The matching `data/id_ed25519` private key and populated `.env` are deliberately not committed to this public repository. They are provided only in the private server archive. Never publish or commit the private key.

## Install

```bash
cp .env.example .env
# Set a strong ADMIN_PASSWORD in .env
# Copy id_ed25519 and id_ed25519.pub into data/
sudo ./install.sh
```

Open `http://217.24.161.103:8080`.

For Internet exposure, place the dashboard behind HTTPS and restrict it with an IP allow-list or VPN.

The dashboard provides service status, the current public key and downloadable client configuration. It is not the commercial RustDesk Server Pro console and does not include Pro-only user/device management, LDAP/OIDC, administrator MFA, address books or enterprise policies.
