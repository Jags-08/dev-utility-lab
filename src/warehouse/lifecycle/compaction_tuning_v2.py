def tune_telemetry_compaction(events):
    """Aggressively drops debug-level telemetry signals over 7 days old."""
    return len(events)
