# VictorIsCool Admin

This directory is reserved for the independent VictorIsCool management plane.

## Selected stack

- Backend: Rust, Axum, Tokio, SQLx
- Database: PostgreSQL
- Cache/presence: Redis
- Frontend: React, TypeScript, Vite
- Authentication: secure HTTP-only browser sessions, MFA, optional OIDC/LDAP
- Deployment: Docker Compose initially; Kubernetes-compatible services later

The management plane must not replace `hbbs` or `hbbr`. It manages identities, policies, inventory, auditing and releases while RustDesk services continue to handle rendezvous and relay traffic.

## Planned services

```text
admin/
  api/          Management REST API and background workers
  web/          Administrator web interface
  migrations/   PostgreSQL migrations
  deploy/       Docker Compose, reverse-proxy and operations files
  openapi/      Versioned API contract
```

## Initial database entities

- administrators
- users
- roles
- permissions
- teams
- devices
- device_groups
- device_enrollments
- device_presence
- policies
- policy_assignments
- sessions
- session_events
- audit_events
- address_books
- address_book_entries
- releases
- update_channels
- api_tokens
- webhooks

## Non-negotiable controls

- no plaintext passwords, private keys or permanent enrollment secrets;
- administrator MFA;
- explicit authorization checks for every object;
- append-only audit trail for privileged changes;
- signed policy and update payloads;
- pagination and filtering for all collection APIs;
- backup/restore documentation before production deployment;
- health, readiness and metrics endpoints.

See `docs/VICTORISCOOL_PLATFORM.md` for the product scope and phased implementation plan.
