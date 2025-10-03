.PHONY: help run_ingestion run_noop run_prices run_options

help:
	@echo "Targets:"
	@echo "  run_ingestion    Run the ingestion runner with custom args"
	@echo "  run_noop         Quick smoke: no-op pipeline for today"
	@echo "  run_prices       Smoke: prices stub (tickers optional)"
	@echo "  run_options      Smoke: options stub (tickers optional)"

# Example:
#   make run_ingestion ARGS="--pipeline prices --run-date 2025-10-03 --tickers AAPL,MSFT -v"
run_ingestion:
	@python -m profitscout_ingestion.jobs.runner $(ARGS)

# Quick local smokes
run_noop:
	@python -m profitscout_ingestion.jobs.runner --pipeline noop

run_prices:
	@python -m profitscout_ingestion.jobs.runner --pipeline prices --run-date $$(date +%F) $(ARGS)

run_options:
	@python -m profitscout_ingestion.jobs.runner --pipeline options --run-date $$(date +%F) $(ARGS)


run_calendar:
	@python -m profitscout_ingestion.jobs.runner --pipeline calendar --run-date $$(date +%F) $(ARGS)
