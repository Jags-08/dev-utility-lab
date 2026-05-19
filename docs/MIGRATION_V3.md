# V3.0.0 Migration & Compatibility Matrix

| Subsystem | v2.9.x Status | v3.0.x Handling | Remediation |
|---|---|---|---|
| REST API | Deprecated | **Hard 404** | Use `TopologyAwareClient` |
| Quorum | Loose Consensus | Strict Majority | Update node cluster sizing |
| Retries | Static Bound | Adaptive Jitter | Included in SDK globally |

## End-of-Life Windows
Legacy endpoints will be fully pruned 180 days post-GA.
