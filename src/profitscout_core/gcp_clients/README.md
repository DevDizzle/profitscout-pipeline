# gcp_clients/

**Purpose:** One place to create configured clients with retries/backoff and short defaults.

Planned factories:  
- `bq_client()`  
- `gcs_client()`  
- `secret_manager_client()`  
- `pubsub_publisher()` (if needed later)

Notes: use library-native retries (google-api-core) and document idempotency expectations.  
Refs: client best practices & retries. :contentReference[oaicite:5]{index=5}
