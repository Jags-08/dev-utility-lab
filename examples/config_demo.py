from dev_utils.config import config

def config_task() -> None:
    # Get with fallback
    host = config.get("DB_HOST", "localhost")
    print(f"Connecting to {host}...")

    # Optional: require missing key
    try:
        config.require("API_KEY")
    except KeyError as e:
        print(f"Expected error: {e}")

if __name__ == "__main__":
    config_task()
