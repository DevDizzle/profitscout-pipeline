# io/

**Purpose:** Common I/O helpers with safe defaults.

Planned helpers
- GCS: `gcs_write_json()`, `gcs_read_json()`, JSONL helpers for staging.  
- BigQuery: `bq_load_jsonl()`, `bq_upsert()` with write disposition and partition/cluster options.

Design notes
- Document idempotency/consistency and when to prefer append vs upsert.
