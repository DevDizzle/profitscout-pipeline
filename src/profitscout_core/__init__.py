"""profitscout_core.

Shared, framework-agnostic helpers used by all pipeline layers:
- config/: 12-Factor config resolution, Secret Manager integration
- logging/: structured JSON logging for Cloud Logging
- gcp_clients/: thin client factories (BQ, GCS, Secret Manager, Pub/Sub)
- schemas/: shared data contracts (BQ / JSON artifacts)
- io/: common read/write helpers (GCS, BQ load jobs)
- util/: tiny cross-cutting helpers (uuids, timestamps)

NOTE: This package defines *interfaces* in PR2; implementations arrive in PR3+.
"""

__all__ = ["config", "logging", "gcp_clients", "schemas", "io", "util"]
