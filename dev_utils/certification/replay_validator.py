
import hashlib
import json

class ReplayValidator:
    def validate_state(self, initial_state, reconstructed_state):
        h_initial = hashlib.sha256(json.dumps(initial_state, sort_keys=True).encode()).hexdigest()
        h_recon = hashlib.sha256(json.dumps(reconstructed_state, sort_keys=True).encode()).hexdigest()
        return h_initial == h_recon

    def certify_execution(self, logs):
        failures = [log for log in logs if 'error' in log.lower()]
        return len(failures) == 0
