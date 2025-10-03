# Artifacts & Tables

Staging format: newline-delimited JSON (ndjson) in GCS (one record per line).
Why: BigQuery recommends ndjson for JSON loads.

Load patterns:
- Append to partitioned tables by `as_of_date` (or overwrite partition during backfill).
- Co-locate GCS bucket and BQ dataset in the same region.

References: BigQuery JSON loads; location constraints.
