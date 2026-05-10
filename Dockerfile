FROM python:3.11-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    APP_HOME=/app

WORKDIR ${APP_HOME}

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependencies
COPY requirements-dev.txt setup.py README.md ./
COPY dev_utils/ ./dev_utils/
COPY dashboard/ ./dashboard/
COPY benchmarks/ ./benchmarks/

# Install the application and gunicorn
RUN pip install --no-cache-dir gunicorn
RUN pip install --no-cache-dir -e ".[dashboard]"

# Configure user
RUN useradd -m appuser && chown -R appuser:appuser ${APP_HOME}
USER appuser

EXPOSE 5000

# Healthcheck
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/api/health || exit 1

# Start gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "--threads", "2", "dashboard.app:app"]
