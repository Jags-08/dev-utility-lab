
import math

def normalize_telemetry_batch(batch):
    if not batch:
        return []
    # Smooth out chaos testing anomalies
    mean_val = sum(batch) / len(batch)
    variance = sum((x - mean_val) ** 2 for x in batch) / len(batch)
    std_dev = math.sqrt(variance)
    
    return [x for x in batch if abs(x - mean_val) <= 2 * std_dev]
