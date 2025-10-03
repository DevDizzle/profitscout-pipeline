# syntax=docker/dockerfile:1

# Small, secure base
FROM python:3.11-slim

# Runtime env
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

# System deps (minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# App directory
WORKDIR /app

# Make src importable
ENV PYTHONPATH=/app/src

# (Optional) If/when you add runtime deps to pyproject, copy it here first for layer caching:
# COPY pyproject.toml ./
# RUN pip install --upgrade pip && pip install .

# Copy source (no external deps yet)
COPY src ./src

# Use a non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Default entrypoint: stub runner (noop|prices|options|calendar)
ENTRYPOINT ["python", "-m", "profitscout_ingestion.jobs.runner"]
CMD ["--pipeline", "noop"]
