"""Stub for the calendar/economic ingestion pipeline.

Public interface:
    run(run_date: str) -> dict[str, int]

This noop implementation only logs start/summary/end and returns counters.
Real extract/transform/load steps will be added incrementally.
"""

from __future__ import annotations

import datetime as dt
import json


def _utc_now_iso() -> str:
    """Return current UTC timestamp in ISO 8601 format."""
    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def _log(event: str, **fields) -> None:
    """Emit a simple JSON record to stdout."""
    payload = {"ts": _utc_now_iso(), "service": "ingestion", "pipeline": "calendar", "event": event}
    payload.update(fields)
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))


def run(run_date: str) -> dict[str, int]:
    """Execute the stub calendar pipeline for the given run_date.

    Args:
        run_date: Logical run date in YYYY-MM-DD format.

    Returns:
        A small counter dict with processed/error counts.

    """
    _log("start", run_date=run_date)
    # No-op: real implementation will be extract -> transform -> load
    counters = {"processed": 0, "errors": 0}
    _log("summary", run_date=run_date, **counters)
    _log("end", run_date=run_date, status="ok")
    return counters
