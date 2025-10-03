"""CLI runner for ingestion jobs.

Dispatches to specific pipelines (noop|prices|options).
Keeps imports lazy so early PRs don’t break if a package isn’t present yet.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import sys
from typing import Optional


def _import_prices_run():
    from profitscout_ingestion.pipelines.prices.pipeline import run as prices_run

    return prices_run


def _import_options_run():
    from profitscout_ingestion.pipelines.options.pipeline import run as options_run

    return options_run


def _utc_now_iso() -> str:
    """Return current UTC timestamp in ISO 8601 format."""
    return dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def _setup_logging(verbosity: int) -> None:
    """Configure basic structured logging with a simple JSON formatter."""
    level = logging.INFO if verbosity == 0 else logging.DEBUG
    logging.basicConfig(level=level, format="%(message)s", stream=sys.stdout)


def _log(event: str, **fields) -> None:
    """Emit a simple JSON record to stdout."""
    payload = {"ts": _utc_now_iso(), "service": "ingestion", "event": event}
    payload.update(fields)
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))


def _parse_tickers(csv: Optional[str]) -> list[str] | None:
    """Parse a comma-separated list of tickers into a list of strings."""
    if not csv:
        return None
    return [t.strip().upper() for t in csv.split(",") if t.strip()]


def main(argv: Optional[list[str]] = None) -> int:
    """Parse args and run the requested ingestion pipeline."""
    parser = argparse.ArgumentParser(description="ProfitScout ingestion runner.")
    parser.add_argument(
        "--pipeline", type=str, default="noop", help="Pipeline to run (noop|prices|options)."
    )
    parser.add_argument(
        "--run-date",
        type=str,
        default=dt.date.today().isoformat(),
        help="Logical run date in YYYY-MM-DD (defaults to today).",
    )
    parser.add_argument(
        "--tickers",
        type=str,
        default=None,
        help="Comma-separated list of tickers (used by some pipelines).",
    )
    parser.add_argument("-v", "--verbose", action="count", default=0, help="Increase verbosity.")
    args = parser.parse_args(argv)

    _setup_logging(args.verbose)
    _log("start", pipeline=args.pipeline, run_date=args.run_date)

    if args.pipeline == "noop":
        _log("summary", pipeline="noop", run_date=args.run_date, processed=0, errors=0)
        _log("end", pipeline="noop", run_date=args.run_date, status="ok")
        return 0

    if args.pipeline == "prices":
        prices_run = _import_prices_run()
        tickers = _parse_tickers(args.tickers)
        counters = prices_run(run_date=args.run_date, tickers=tickers)
        _log("end", pipeline="prices", run_date=args.run_date, status="ok", **counters)
        return 0

    if args.pipeline == "options":
        options_run = _import_options_run()
        tickers = _parse_tickers(args.tickers)
        counters = options_run(run_date=args.run_date, tickers=tickers)
        _log("end", pipeline="options", run_date=args.run_date, status="ok", **counters)
        return 0

    _log(
        "end",
        pipeline=args.pipeline,
        run_date=args.run_date,
        status="error",
        reason="unknown_pipeline",
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
