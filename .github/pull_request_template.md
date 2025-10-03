## Title
feat(ingestion): migrate ingestion layer to monorepo (staging + canary)

## Purpose
Briefly summarize what this PR does and why (ingestion-only migration; no schema changes).

## Scope (In / Out)
- In: ingestion package move, config/logging unification, tests, staging deploy, canary plan
- Out: enrichment, serving, schema changes

## Migration Map (old -> new)
| Area | Old Path | New Path |
|------|----------|----------|
| Entry | … | src/profitscout_ingestion/jobs/... |
| Pipelines | … | src/profitscout_ingestion/pipelines/... |
| Orchestrators | … | src/profitscout_ingestion/orchestrators/... |
| Clients (API) | … | src/profitscout_ingestion/clients/... |

## Inputs & Outputs (Contracts)
- Inputs: external APIs (list), config/env vars (list)
- Outputs: GCS objects (paths/naming), BigQuery tables (dataset.table, partitioning)

## Config (env) & Secrets
- Env vars: PS_BQ_PROJECT, PS_BQ_DATASET_INGESTION, PS_GCS_BUCKET_INGESTION, PS_REGION, PS_ENV
- Secrets (by name only): e.g., FMP_API_KEY (via Secret Manager binding in Cloud Run)

## Observability
- Structured logging: service=ingestion, pipeline, run_id, run_date, ticker, severity, event
- Metrics to watch during canary: error rate, API failures, BQ write errors, latency

## Idempotency / Retries / Rate Limits
- Write idempotency approach (GCS/BQ)
- Retry/backoff notes
- Rate limit knob(s)

## Testing
- Unit: config resolution, parser/client stubs
- Smoke (staging): tiny ticker set; verify GCS objects & BQ rows

## Staging Deploy Plan
- Deploy to ingestion-staging Cloud Run
- Run smoke test & verify logs/artifacts

## Production Canary Plan
- 5% → 25% → 100% traffic split across one pipeline window

## Rollback
- Flip traffic to previous revision immediately if failures

## Risks & Mitigations
- (e.g., API quota → throttle var; schema mismatch → contract tests)

## Checklist
- [ ] Imports refactored to use profitscout_core
- [ ] Env & secrets documented
- [ ] Unit tests pass
- [ ] Staging smoke green
- [ ] Canary criteria defined
