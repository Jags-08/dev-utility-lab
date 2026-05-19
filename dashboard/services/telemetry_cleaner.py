class TelemetryOptimizer:
    def strip_stale_metrics(self, data):
        return {k: v for k, v in data.items() if v.get('age', 0) < 30}
