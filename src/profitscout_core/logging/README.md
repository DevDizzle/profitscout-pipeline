# logging/

**Purpose:** Emit **structured JSON** logs with consistent fields so they’re queryable and low-noise in Cloud Logging.

Minimum fields to include on each record (when we implement):  
- `service` (ingestion|enrichment|serving), `component`, `severity`, `event`, `run_date`, optional `ticker`, `trace_id`.

References: Cloud Logging structured logs; std-lib integration. :contentReference[oaicite:4]{index=4}
