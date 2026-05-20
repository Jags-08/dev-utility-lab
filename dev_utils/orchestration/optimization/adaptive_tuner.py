class AdaptiveExecutionTuner:
    def __init__(self, baseline_latency=5.0):
        self.baseline = baseline_latency

    def tune_workload(self, current_latency, active_nodes):
        if current_latency > self.baseline * 1.5:
            return active_nodes + 2 # Aggressive autonomic scale-out
        elif current_latency < self.baseline * 0.5 and active_nodes > 3:
            return active_nodes - 1 # Scale-in optimization
        return active_nodes
