# schemas/

**Purpose:** Canonical table & JSON artifact contracts.

Guidelines
- Favor **additive** (backward-compatible) changes.  
- For breaking changes, consider a **new table** or a **versioned view**; document the migration window.  
- Keep a short changelog per schema.

This folder will later expose helpers like:
- `price_snapshot_schema()`  
- `options_chain_schema()`  
- `signal_record_schema()`
