"""Typed configuration models for ProfitScout core."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class IngestionConfig:
    """Non-secret configuration used by the ingestion layer.

    Values are sourced from environment variables in get_config().
    All values are strings to keep transport/simple overrides trivial.
    """

    env: str  # e.g., "staging", "prod"
    region: str  # e.g., "us-central1"
    bq_project: str  # GCP project hosting datasets
    bq_dataset_ingestion: str  # BigQuery dataset name for ingestion outputs
    gcs_bucket_ingestion: str  # GCS bucket for landing/intermediate artifacts
    log_level: str = "INFO"  # Logging verbosity (INFO, DEBUG, etc.)
