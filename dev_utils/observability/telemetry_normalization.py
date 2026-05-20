def normalize_telemetry_signals(raw_signals):
    """Cleans up unstructured signal metadata prior to compaction."""
    return [sig for sig in raw_signals if 'trace_id' in sig]
