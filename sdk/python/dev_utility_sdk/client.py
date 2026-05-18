import logging

class DevUtilityClient:
    def __init__(self, api_key, endpoint="https://api.dev-utility.local"):
        self.api_key = api_key
        self.endpoint = endpoint
        self.logger = logging.getLogger("DevUtilitySDK")

    def emit_telemetry(self, event_name, payload):
        self.logger.info(f"Emitting {event_name} to {self.endpoint}")
        return True
