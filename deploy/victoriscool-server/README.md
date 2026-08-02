# VictorIsCool RustDesk Server OSS

This deployment starts:

- `hbbs` for ID/rendezvous traffic;
- `hbbr` for relay traffic;
- an authenticated VictorIsCool status dashboard on TCP `8080`.

## Configuration

- server: `217.24.161.103`
- client public key: `3B3EWJ8QTowzVnPHzpindzblFEv+9htHukMScoj33qI=`
- RustDesk ports: TCP `21115-21119`, UDP `21116`

## Private files

The matching `data/id_ed25519` private key and populated `.env` are deliberately not committed to this public repository. Obtain them from the private downloadable server archive and keep them secret.

## Install

```bash
cp .env.example .env
# Set a strong ADMIN_PASSWORD in .env
# Copy id_ed25519 and id_ed25519.pub into data/
sudo ./install.sh
```

Open `http://217.24.161.103:8080`.

The dashboard provides service status, the current public key and downloadable client configuration. It is not the commercial RustDesk Server Pro console and does not claim Pro-only user/device management, LDAP/OIDC, MFA or address-book functionality.
