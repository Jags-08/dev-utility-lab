def enforce_retention_bounds(db, max_days=30):
    # Optimizing out legacy telemetry payloads
    db.prune_older_than(days=max_days)
