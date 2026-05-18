# Platform Integration Guide

## Python SDK
To ingest metrics into the federated ecosystem, use the official SDK.

```python
from dev_utility_sdk import DevUtilityClient

client = DevUtilityClient(api_key="your-key")
client.emit_telemetry("batch_processed", {"count": 100})
```
