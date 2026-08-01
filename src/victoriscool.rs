//! VictorIsCool client branding and self-hosted server defaults.
//!
//! These defaults are applied from the shared Rust layer, so the same
//! configuration is used by Windows, Linux, macOS, and Android builds.

use hbb_common::config;
use std::sync::Once;

pub const APP_NAME: &str = "VictorIsCool";
pub const BRAND_PRIMARY_COLOR: &str = "#1565C0";
pub const ID_SERVER: &str = "217.24.161.103";
pub const RELAY_SERVER: &str = "217.24.161.103";
pub const PUBLIC_KEY: &str = "kNaWnMAVkriT2rFWeeLn5/WrP2aVJMJiq2KBATs8FV4=";
pub const DEFAULT_LANGUAGE: &str = "uk";
pub const SUPPORTED_LANGUAGES: &[&str] = &["de", "en", "uk"];

/// Reserved management-plane endpoints. These constants document the client
/// integration boundary; production URLs should use HTTPS hostnames rather
/// than the raw relay IP before device enrollment is enabled.
pub const MANAGEMENT_API_PATH: &str = "/api/v1";
pub const DEVICE_ENROLLMENT_PATH: &str = "/api/v1/devices/enroll";
pub const DEVICE_POLICY_PATH: &str = "/api/v1/device/policy";
pub const DEVICE_EVENTS_PATH: &str = "/api/v1/device/events";

static APPLY_DEFAULTS: Once = Once::new();

/// Apply VictorIsCool defaults once per process.
///
/// The settings remain user-configurable because they are registered as
/// defaults rather than override/hard settings. A signed custom client config,
/// command-line import, or a user-selected value can still replace them.
pub fn apply_defaults() {
    APPLY_DEFAULTS.call_once(|| {
        *config::APP_NAME.write().unwrap() = APP_NAME.to_owned();

        {
            let mut defaults = config::DEFAULT_SETTINGS.write().unwrap();
            defaults.insert(
                "custom-rendezvous-server".to_owned(),
                ID_SERVER.to_owned(),
            );
            defaults.insert("relay-server".to_owned(), RELAY_SERVER.to_owned());
            defaults.insert("key".to_owned(), PUBLIC_KEY.to_owned());
        }

        {
            let mut local_defaults = config::DEFAULT_LOCAL_SETTINGS.write().unwrap();
            local_defaults.insert("lang".to_owned(), DEFAULT_LANGUAGE.to_owned());
        }
    });
}
