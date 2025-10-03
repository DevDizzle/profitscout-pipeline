"""profitscout_ingestion.

Ingestion layer for ProfitScout. This package will host:
- pipelines/: data-source specific ingestion pipelines (prices, options, calendar)
- orchestrators/: batch/concurrency and run coordination
- clients/: ingestion-only API wrappers (shared code lives in profitscout_core)
- jobs/: small entrypoints used by Cloud Run / Workflows

Note: Subpackages will be added incrementally in this PR to keep diffs small.
"""

__all__ = ["pipelines", "orchestrators", "clients", "jobs"]
