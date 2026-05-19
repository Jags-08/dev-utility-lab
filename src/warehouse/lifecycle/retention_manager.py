def adaptive_archive(telemetry_batch, age_days):
    if age_days > 90:
        return "cold_storage"
    return "hot_indexes"
