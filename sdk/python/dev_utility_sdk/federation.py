class FederatedClient:
    def __init__(self, use_adaptive_retry=True):
        self.adaptive = use_adaptive_retry
    def dispatch(self, payload):
        return True
