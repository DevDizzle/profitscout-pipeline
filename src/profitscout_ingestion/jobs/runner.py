"""CLI runner for ingestion jobs.

This is a minimal, non-op entrypoint we can wire to Cloud Run / Workflows.
It does not import profitscout_core yet, so it’s safe to land before those pieces exist.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import sys
from typing import Optional


def _utc_now_iso() -> str:
    """Return current UTC timestamp in ISO 8601 format."""
    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def _setup_logging(verbosity: int) -> None:
    """Configure basic structured logging with a simple JSON formatter."""
    level = logging.INFO if verbosity == 0 else logging.DEBUG
    logging.basicConfig(
        level=level,
        format="%(message)s",
        stream=sys.stdout,
    )


def _log(event: str, **fields) -> None:
    """Emit a simple JSON record to stdout."""
    payload = {"ts": _utc_now_iso(), "service": "ingestion", "event": event}
    payload.update(fields)
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))


def main(argv: Optional[list[str]] = None) -> int:
    """Parse args and perform a no-op run that logs start/summary/end."""
    parser = argparse.ArgumentParser(description="ProfitScout ingestion runner (stub).")
    parser.add_argument(
        "--pipeline",
        type=str,
        required=False,
        default="noop",
        help="Pipeline name to run (e.g., prices, options, calendar).",
    )
    parser.add_argument(
        "--run-date",
        type=str,
        required=False,
        default=dt.date.today().isoformat(),
        help="Logical run date in YYYY-MM-DD (defaults to today).",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase verbosity (-v for DEBUG).",
    )
    args = parser.parse_args(argv)

    _setup_logging(args.verbose)

    _log("start", pipeline=args.pipeline, run_date=args.run_date)
    # No-op work here; real pipelines will be wired in next PRs.
    _log("summary", pipeline=args.pipeline, run_date=args.run_date, processed=0, errors=0)
    _log("end", pipeline=args.pipeline, run_date=args.run_date, status="ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
