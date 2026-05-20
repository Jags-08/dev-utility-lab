def balance_federation_pressure(region_metrics):
    smoothed_metrics = {r: m * 0.9 for r, m in region_metrics.items()}
    return smoothed_metrics
