# VictorIsCool platform

VictorIsCool is a branded, self-hosted remote-support platform based on RustDesk.

## Product defaults

- Product name: `VictorIsCool`
- Primary color: blue (`#1565C0`)
- ID/rendezvous server: `217.24.161.103`
- Relay server: `217.24.161.103`
- Supported UI languages: German (`de`), English (`en`), Ukrainian (`uk`)
- Initial UI language: Ukrainian (`uk`)
- Target clients: Windows, Linux, macOS, Android

The embedded public key must match the private key used by the production `hbbs` service. Replacing the server key requires rebuilding or centrally reprovisioning the clients.

## Components

1. **VictorIsCool clients**
   - branded Flutter UI and platform metadata;
   - predefined self-hosted network settings;
   - remote desktop, file transfer, clipboard, audio, chat, TCP tunnelling, terminal and recording features supported by the upstream client;
   - device enrollment and policy retrieval from the management API;
   - signed update channel.

2. **RustDesk infrastructure**
   - `hbbs` for rendezvous and ID registration;
   - `hbbr` for relayed sessions;
   - TLS reverse proxy for web/API traffic;
   - persistent logs and metrics.

3. **VictorIsCool Management API**
   - administrator authentication and MFA;
   - device enrollment and inventory;
   - users, teams, roles and permissions;
   - centrally managed client policies;
   - session audit events;
   - address books and device groups;
   - release/update management;
   - server health and relay statistics;
   - API tokens and webhooks.

4. **VictorIsCool Admin Web**
   - dashboard;
   - devices and online state;
   - users, teams and RBAC;
   - sessions and audit history;
   - policies and deployment profiles;
   - address books;
   - releases and update rings;
   - infrastructure health;
   - security settings.

## Roles

- `super_admin`: unrestricted platform administration;
- `admin`: device, user, policy and session administration;
- `operator`: remote-support access to assigned groups;
- `auditor`: read-only access to sessions and audit logs;
- `user`: access only to explicitly assigned devices.

Every privileged action must be recorded in an immutable audit event with actor, action, target, source IP, timestamp and result.

## Security requirements

- HTTPS only for the web panel and management API;
- Argon2id password hashing;
- TOTP/WebAuthn MFA for administrators;
- short-lived access tokens and rotated refresh tokens;
- encrypted secrets at rest;
- rate limiting and account lockout;
- CSRF protection for browser sessions;
- signed device enrollment tokens;
- signed client policies and update manifests;
- tenant-safe authorization checks on every API request;
- configurable session approval and unattended-access policies;
- exportable audit logs and retention controls.

## Initial API surface

- `POST /api/v1/auth/login`
- `POST /api/v1/auth/mfa/verify`
- `POST /api/v1/auth/refresh`
- `GET /api/v1/devices`
- `POST /api/v1/devices/enroll`
- `GET /api/v1/devices/{id}`
- `PATCH /api/v1/devices/{id}`
- `POST /api/v1/devices/{id}/commands`
- `GET /api/v1/sessions`
- `GET /api/v1/audit-events`
- `GET /api/v1/users`
- `GET /api/v1/roles`
- `GET /api/v1/policies`
- `POST /api/v1/policies`
- `POST /api/v1/policies/{id}/assign`
- `GET /api/v1/releases`
- `POST /api/v1/releases`
- `GET /api/v1/infrastructure/health`

## Delivery phases

### Phase 1 — branded clients

- product name and blue theme;
- icons and platform bundle metadata;
- embedded ID, relay and public key;
- German, English and Ukrainian language selection;
- build workflows for all target platforms.

### Phase 2 — management foundation

- PostgreSQL schema;
- API service;
- administrator authentication and MFA;
- device enrollment, inventory and online state;
- audit log;
- initial web dashboard.

### Phase 3 — central administration

- users, groups and RBAC;
- device policies;
- session history and approval workflows;
- address books;
- release and update management;
- notifications and webhooks.

### Phase 4 — advanced operations

- HA deployment;
- metrics, alerting and backups;
- LDAP/OIDC integration;
- multi-tenant boundaries if required;
- compliance exports and retention policies.

## Licensing

The RustDesk-derived client remains subject to GNU AGPLv3. Distributed modified clients must be accompanied by access to the corresponding source code and the applicable notices. Any separately developed management components should keep a clear architectural boundary and have an explicitly selected license.
