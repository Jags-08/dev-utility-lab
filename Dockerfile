FROM python:3.9-slim`nWORKDIR /app`nCOPY . /app`nRUN pip install -r requirements-dev.txt`nCMD ["python", "scripts/benchmarks/build_dashboard.py"]
