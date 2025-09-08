import logging
import os

# Configure the logger
def setup_logger(log_file='cleansweep.log'):
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

# Log an info message
def log_info(message):
    logging.info(message)

# Log a warning message
def log_warning(message):
    logging.warning(message)

# Log an error message
def log_error(message):
    logging.error(message)

# Log a debug message
def log_debug(message):
    logging.debug(message)

# Log an exception
def log_exception(exc):
    logging.exception("An exception occurred: %s", exc)

# Ensure the log directory exists
def ensure_log_directory(log_file='cleansweep.log'):
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

# Initialize the logger
def initialize_logger(log_file='cleansweep.log'):
    ensure_log_directory(log_file)
    setup_logger(log_file)
    log_info("Logger initialized.")

Finish Production Ready