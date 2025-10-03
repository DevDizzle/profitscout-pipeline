# profitscout_core

Shared primitives for the ProfitScout pipeline. Design goals:
- **12-Factor config** via environment variables with Secret Manager bindings in Cloud Run.  
- **Structured JSON logging** so fields are queryable in Cloud Logging.
- **Thin GCP client factories** with sane retries/backoff.
- **Stable data contracts** surfaced from `schemas/` to reduce downstream breakage.

References:
- 12-Factor “Config” (env vars first). :contentReference[oaicite:0]{index=0}
- Cloud Run + Secret Manager (env/volume injection). :contentReference[oaicite:1]{index=1}
- Structured logging on Google Cloud. :contentReference[oaicite:2]{index=2}
