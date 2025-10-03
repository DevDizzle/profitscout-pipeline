# profitscout_ingestion

Ingestion layer for ProfitScout.

## Structure
- `pipelines/` — data-source specific pipelines (prices, options, calendar, etc.)
- `orchestrators/` — run coordination, batching, concurrency controls
- `clients/` — ingestion-only API wrappers (shared code lives in `profitscout_core`)
- `jobs/` — small entrypoints for Cloud Run / Cloud Workflows

## Contracts
- **Inputs:** external APIs (auth via Secret Manager), env-configured settings
- **Outputs:** GCS landing artifacts and BigQuery tables (append or upsert), unchanged in this PR

## Logging
Emit structured JSON with minimum fields:
`service="ingestion"`, `pipeline`, `run_id`, `run_date`, optional `ticker`, `severity`, `event`.

## Idempotency & Retries
- Idempotent writes where feasible (deterministic object keys / dedup keys)
- Exponential backoff on external calls; throttle via env var when needed
