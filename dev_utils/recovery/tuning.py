
import time
import logging

class RollbackTimingOptimizer:
    def __init__(self, base_delay=1.5, max_retry=3):
        self.base_delay = base_delay
        self.max_retry = max_retry

    def calculate_optimal_backoff(self, attempt_count):
        # Exponential backoff stabilization
        return min(self.base_delay * (2 ** attempt_count), 15.0)

class ReplayRecoveryTuner:
    def __init__(self, tolerance_ms=50):
        self.tolerance_ms = tolerance_ms

    def assert_replay_consistency(self, original_state, replay_state):
        drift = abs(original_state.get('timestamp', 0) - replay_state.get('timestamp', 0))
        if drift > self.tolerance_ms:
            logging.warning(f"Replay drift {drift}ms exceeds tolerance {self.tolerance_ms}ms")
            return False
        return True
