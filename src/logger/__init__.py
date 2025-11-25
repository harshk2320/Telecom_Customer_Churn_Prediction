import logging     # Python's built in logging framework (to print logs like DEBUG, INFO, ERRORS, etc)
import os   # For working with folders and paths. 
from datetime import datetime   # To work with date and time
from logging.handlers import RotatingFileHandler    # Special handler that automatically rotates files when they grow too big.



LOG_DIR = "log"     # Name of the folder where the logs will be saved.

LOG_FILE = f"{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"    # Generates log files based on current timestamp.
# Timestamp is used to prevent overwrite of previous logs. Every run gets a fresh file  

MAX_LOG_SIZE = 5 * 1024 * 1024   # Maximum file size 5 MB. When the file exceeds this size, it rotates (auto creates a new file).  

BACKUP_COUNT = 3    # Keeps only 3 old log files.

