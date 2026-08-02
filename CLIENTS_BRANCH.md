# VictorIsCool client branch 1.0.0

This branch is dedicated to branded client builds.

## Targets

- Windows x86_64 and ARM64
- Ubuntu/Linux x86_64 and ARM64
- macOS Intel and Apple Silicon
- Android ARM64, ARMv7 and x86_64

## Embedded defaults

- Application: `VictorIsCool`
- Primary colour: `#1565C0`
- ID server: `217.24.161.103`
- Relay server: `217.24.161.103`
- Public key: `YQiOvC0OOyIJ1wT4v0SZs7YwLZWxEfkW8ZtzRMSdnUA=`
- Languages: German, English and Ukrainian
- Default language: Ukrainian (`uk`)

GitHub Actions packages the platform binaries as workflow artifacts. Production Windows Authenticode signing, Apple Developer ID signing/notarization and Android application signing require owner-provided certificates stored as GitHub Actions secrets.
