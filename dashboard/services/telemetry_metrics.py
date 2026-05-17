
from dev_utils.incident.telemetry_normalization import normalize_telemetry_batch

class StabilizationMetrics:
    def __init__(self):
        self.historical_drifts = []

    def ingest_drifts(self, drifts):
        normalized = normalize_telemetry_batch(drifts)
        self.historical_drifts.extend(normalized)
    
    def get_stabilization_trend(self):
        if not self.historical_drifts:
            return "Stable (No Data)"
        recent = self.historical_drifts[-10:]
        avg_drift = sum(recent) / len(recent)
        return "Warning" if avg_drift > 20 else "Stable"
