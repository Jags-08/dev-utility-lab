#!/usr/bin/env bash
set -e

echo "🚀 Bootstrapping dev-utility-lab Developer Ecosystem..."

# Create a deterministic virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -e ".[dev]"
pip install pre-commit

# Setup dev tools
pre-commit install

echo "✅ Bootstrap complete! Run 'source .venv/bin/activate' to begin."
