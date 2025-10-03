# Reliability & Idempotency

Retries
- Use google-api-core Retry with exponential backoff for idempotent calls (BQ, GCS metadata).
- For GCS, include jitter per official guidance to avoid thundering herd.

Uploads
- Use resumable uploads for larger JSONL artifacts to avoid full re-sends on failures.

Logging
- Emit structured JSON logs via profitscout_core.logging; include fields:
  service=ingestion, event, run_date, ticker, severity.

References: api-core Retry; Storage retry strategy; resumable uploads; structured logging.
