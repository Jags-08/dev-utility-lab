# Architecture Topology Summaries 84545
1. **Ingress**: `src/warehouse/` -> handles telemetry normalization.
2. **Orchestration**: `dev_utils/federation/` -> handles latency-aware shard routing.
3. **Reliability**: `dev_utils/reliability/` -> predictive failover metrics.
