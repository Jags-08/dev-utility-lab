from dev_utils.math_ops import add
from dev_utils.logger import logger

def automation_task() -> None:
    logger.info("Starting automation task...")
    result = add(5, 15)
    logger.info(f"Task complete. Result: {result}")

if __name__ == "__main__":
    automation_task()
