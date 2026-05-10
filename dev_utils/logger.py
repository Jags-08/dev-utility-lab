import logging
import sys
from typing import Optional

def setup_logger(name: str = "dev_utils", level: int = logging.INFO, log_file: Optional[str] = None) -> logging.Logger:
    """Configure and return a professional logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    if logger.hasHandlers():
        logger.handlers.clear()
        
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    # File handler
    if log_file:
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
    return logger

logger = setup_logger()
