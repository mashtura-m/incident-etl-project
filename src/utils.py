"""
utils.py
Utility functions for the ETL pipeline.
"""

import logging
from datetime import datetime

# Configure default logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def log_message(message: str, level: str = "info") -> None:
    """
    Log a message using Python's logging module.

    Args:
        message (str): Message to log.
        level (str, optional): Logging level ('debug', 'info', 'warning', 'error'). Defaults to 'info'.
    """
    level = level.lower()
    if level == "debug":
        logging.debug(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    else:
        logging.info(message)

def timestamp() -> str:
    """
    Return the current UTC timestamp in ISO 8601 format.

    Returns:
        str: ISO formatted timestamp.
    """
    return datetime.utcnow().isoformat()
