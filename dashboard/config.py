import os
from typing import Any, Dict


class BaseConfig:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-do-not-use-in-prod")
    APP_VERSION = "0.2.0"
    DEBUG = False
    TESTING = False
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = "DEBUG"


class TestingConfig(BaseConfig):
    TESTING = True
    SECRET_KEY = "test-secret"
    LOG_LEVEL = "DEBUG"


class ProductionConfig(BaseConfig):
    DEBUG = False


config_profiles: Dict[str, Any] = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}


def get_config() -> Any:
    env = os.getenv("FLASK_ENV", "development")
    return config_profiles.get(env, config_profiles["default"])
