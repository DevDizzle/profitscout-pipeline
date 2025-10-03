# Environment Variables (non-secret examples)

PS_ENV=staging|prod
PS_REGION=us-central1

BigQuery
PS_BQ_PROJECT=your-project
PS_BQ_DATASET=profitscout

Cloud Storage
PS_GCS_BUCKET=profitscout-data

Secrets (bound via Secret Manager on Cloud Run)
PS_FMP_API_KEY=sm://secret/fmp_api_key          # example format; binding happens in deploy config
PS_OTHER_API_KEY=sm://secret/other_api_key
