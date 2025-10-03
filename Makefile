.PHONY: help run_ingestion run_noop

help:
	@echo "Targets:"
	@echo "  run_ingestion    Run the ingestion runner with custom args"
	@echo "  run_noop         Quick smoke: no-op pipeline for today"

# Example:
#   make run_ingestion ARGS="--pipeline prices --run-date 2025-10-03 -v"
run_ingestion:
	@python -m profitscout_ingestion.jobs.runner $(ARGS)

# Quick local smoke (no-op; logs start/summary/end)
run_noop:
	@python -m profitscout_ingestion.jobs.runner --pipeline noop
