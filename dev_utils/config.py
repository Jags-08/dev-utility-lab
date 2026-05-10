import os
from typing import Any, Dict, Optional

class Config:
    """Configuration management supporting environment variables and fallbacks."""
    
    def __init__(self, default_config: Optional[Dict[str, Any]] = None) -> None:
        self._config = default_config or {}

    def get(self, key: str, fallback: Any = None) -> Any:
        """Get a value from env vars, config dict, or fallback."""
        env_val = os.getenv(key)
        if env_val is not None:
            return env_val
        return self._config.get(key, fallback)

    def require(self, key: str) -> Any:
        """Require a configuration key to be present."""
        val = self.get(key)
        if val is None:
            raise KeyError(f"Missing required configuration key: {key}")
        return val

config = Config()
