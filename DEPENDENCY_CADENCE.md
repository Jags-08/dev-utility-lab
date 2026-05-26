# Dependency Cadence

To minimize disruption during our passive operational phase, non-critical dependency updates will be bundled quarterly.
Critical zero-day vulnerabilities (CVSS > 8.0) trigger immediate out-of-band updates.


## Telemetry Dependencies

Updates to telemetry libraries are deferred to bi-annual cycles unless a CVSS > 7.0 is flagged, strictly to prevent observability schema breakage.