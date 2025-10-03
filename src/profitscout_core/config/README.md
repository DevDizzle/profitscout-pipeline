# config/

**Purpose:** Centralize configuration resolution.

Principles  
- Prefer **environment variables** (12-Factor).  
- In Cloud Run, inject secrets from **Secret Manager** instead of hardcoding or committing `.env`.  
- Local dev may use a `.env.local` kept **out of git**; secrets live in Secret Manager.

Common keys (non-secret examples — adjust later):
- `PS_BQ_PROJECT`, `PS_BQ_DATASET`
- `PS_GCS_BUCKET`
- `PS_REGION`
- `PS_ENV` (e.g., `local|staging|prod`)

References: 12-Factor config; Cloud Run secrets. :contentReference[oaicite:3]{index=3}
