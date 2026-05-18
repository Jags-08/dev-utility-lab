class AdaptiveRetryGovernor:
    def calculate_backoff(self, pressure): return 2.0 * pressure
