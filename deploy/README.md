# Deploy (Staging) — Ingestion

This folder documents how we deploy the **ingestion** image to **Cloud Run (staging)** safely.
We’ll use a staging service named:

- **Service**: `profitscout-ingestion-staging`
- **Region**: _configurable_ (default `us-central1`)
- **Project**: _configurable_ via secrets/vars in CI

## What the CI will do (staging only)
1. Build Docker image from the repo root `Dockerfile`.
2. Tag and push to **Artifact Registry**: `LOCATION-docker.pkg.dev/PROJECT/REPOSITORY/IMAGE:SHA`.
3. Deploy to **Cloud Run** service `profitscout-ingestion-staging` with:
   - CPU: 1 (or repo default)
   - Memory: 512Mi (adjust later)
   - Concurrency: 10
   - Min instances: 0 (scale-to-zero in staging)
   - **Env vars** from `deploy/ingestion.staging.env.example` (non-secrets)
   - **Secrets** via Secret Manager (referenced by name only; configured in Cloud Run)

> Production deploy remains out-of-scope for PR3; we’ll canary later from a separate workflow.

## Required CI inputs (as GitHub Secrets/Variables)
- **Secrets**
  - `GCP_PROJECT_ID` — e.g., `my-gcp-project`
  - `GCP_REGION` — e.g., `us-central1`
  - `GAR_REPOSITORY` — Artifact Registry repo name, e.g., `profitscout`
  - `WIF_PROVIDER` — (if using Workload Identity) full provider resource ID
  - `WIF_SERVICE_ACCOUNT` — (if using Workload Identity) email of the deploy SA
  - _OR_ `GCP_SA_KEY` — JSON key for a CI service account (fallback if WIF not set)
- **Vars** (GitHub “Variables” or set inline in workflow)
  - `INGESTION_SERVICE` — default `profitscout-ingestion-staging`

## Non-secret env (staging)
Copy `deploy/ingestion.staging.env.example` and configure in Cloud Run (Environment variables):
- `PS_BQ_PROJECT` — GCP project for datasets
- `PS_BQ_DATASET_INGESTION` — dataset for ingestion staging, e.g., `ps_ingest_staging`
- `PS_GCS_BUCKET_INGESTION` — e.g., `profitscout-staging-data`
- `PS_REGION` — e.g., `us-central1`
- `PS_ENV` — `staging`

> **Do not** commit secrets. API keys are provided via **Secret Manager**, bound to the service.

## Manual quick test
Once deployed, you can test the container by overriding args:
- Noop: `--pipeline noop`
- Prices: `--pipeline prices --run-date 2025-10-03 --tickers AAPL,MSFT`
- Options: `--pipeline options --run-date 2025-10-03 --tickers AAPL,MSFT`
- Calendar: `--pipeline calendar --run-date 2025-10-03`

We’ll wire these to a Workflows/Scheduler job later.

