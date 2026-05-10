# Deployment Guide

This document explains how to deploy `dev-utility-lab` in a production environment using Docker and WSGI (Gunicorn).

## Prerequisites

* Docker & Docker Compose
* Production environment variables structured (copy `.env.example` to `.env`)

## Running with Docker Compose

This is the recommended strategy for deploying the platform.

```bash
docker-compose up --build -d
```

Validates health checks automatically via:
```bash
docker ps
# Status should say "up X minutes (healthy)"
```

## Running Bare Metal (WSGI)

If you prefer to map directly via systemd or supervisor, you can run the Gunicorn WSGI server directly:

```bash
pip install -e "."
pip install gunicorn psutil

export FLASK_ENV=production
gunicorn --bind 0.0.0.0:5000 --workers 4 --threads 2 "dashboard.app:app"
```

## Health Metrics

Query the production system telemetry:

```bash
curl http://localhost:5000/api/system-info
curl http://localhost:5000/api/metrics
```
