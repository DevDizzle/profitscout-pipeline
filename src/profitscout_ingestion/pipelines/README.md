# Pipelines

This folder will host pipeline coordinators (e.g., daily_price_snapshot, options_chain_snapshot).
Each pipeline follows the same structure:
1) Fetch -> 2) Stage ndjson to GCS -> 3) Load to BigQuery (append/overwrite partition).
4) Emit structured logs and metrics at each step.

Notes
