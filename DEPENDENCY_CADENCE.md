# Dependency Cadence

To minimize disruption during our passive operational phase, non-critical dependency updates will be bundled quarterly.
Critical zero-day vulnerabilities (CVSS > 8.0) trigger immediate out-of-band updates.


## Telemetry Dependencies

Telemetry libraries follow the standard quarterly update cadence, but require explicit schema-validation passing prior to merge.
## Federation Compatibility
All underlying dependency bumps MUST be cross-verified against the upstream LTS compatibility matrix before landing in the main ecosystem.