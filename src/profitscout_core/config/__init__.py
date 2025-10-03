"""Environment-first configuration resolution for ProfitScout.

Implements Twelve-Factor-style config via environment variables so deploys can
change behavior without code changes. Values are parsed once and cached.
"""

from __future__ import annotations

import os
from functools import lru_cache
from typing import Dict, List, Tuple

from .models import IngestionConfig

# Mapping of env var -> (attribute name on IngestionConfig, required?)
_ENV_MAP: Dict[str, Tuple[str, bool]] = {
    "PS_ENV": ("env", True),
    "PS_REGION": ("region", True),
    "PS_BQ_PROJECT": ("bq_project", True),
    "PS_BQ_DATASET_INGESTION": ("bq_dataset_ingestion", True),
    "PS_GCS_BUCKET_INGESTION": ("gcs_bucket_ingestion", True),
    "PS_LOG_LEVEL": ("log_level", False),
}


def _collect_missing(env_map: Dict[str, Tuple[str, bool]], source: Dict[str, str]) -> List[str]:
    """Return a sorted list of required env var names that are missing."""
    missing = [k for k, (_attr, req) in env_map.items() if req and k not in source]
    missing.sort()
    return missing


@lru_cache(maxsize=1)
def get_config() -> IngestionConfig:
    """Return the resolved ingestion configuration (cached).

    Reads values from `os.environ` based on _ENV_MAP and returns a typed model.
    Raises a ValueError listing any missing required variables.
    """
    env = os.environ
    missing = _collect_missing(_ENV_MAP, env)
    if missing:
        raise ValueError(
            "Missing required environment variables: "
            + ", ".join(missing)
            + ". Set these in your environment (or Cloud Run service) before running."
        )

    kwargs = {}
    for var, (attr, _required) in _ENV_MAP.items():
        if var in env:
            kwargs[attr] = env[var]
    return IngestionConfig(**kwargs)  # type: ignore[arg-type]


__all__ = ["IngestionConfig", "get_config"]
