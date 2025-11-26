## Libraries 
import logging     # Python's built in logging framework (to print logs like DEBUG, INFO, ERRORS, etc)
import os   # For working with folders and paths. 
from datetime import datetime   # To work with date and time
from logging.handlers import RotatingFileHandler    # Special handler that automatically rotates files when they grow too big.
# from from_root import from_root 

## Logging config constants
LOG_DIR = "logs"     # Name of the folder where the logs will be saved.

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"    # Generates log files based on current timestamp.
# Timestamp is used to prevent overwrite of previous logs. Every run gets a fresh file  

MAX_LOG_SIZE = 5 * 1024 * 1024   # Maximum file size 5 MB. When the file exceeds this size, it rotates (auto creates a new file).  

BACKUP_COUNT = 3    # Keeps only 3 old log files.



## Constructing log file path
log_dir_path = os.path.join(os.getcwd(), LOG_DIR)    # Path of the log directory.

os.makedirs(log_dir_path, exist_ok= True)   # Creates log folder if does not already exist.

log_file_path = os.path.join(log_dir_path, LOG_FILE)    # Path to log file.



def configure_logger():
    """
    This function is responsible for setting up the whole logging system for my project.
    It ensures that logs are stored in a structured format & are stored in file handler & console handler. 
    """
    
    logger = logging.getLogger()    
    # A logger is a manager that controls when, where and how the log messages are printed.
    # logging.getLogger() creates a main logging object.

    logger.setLevel(logging.DEBUG)
    # We basically set level as DEBUG, since its the lowest level hence allowing all types of logs.
     
    formatter = logging.Formatter("[%(asctime)s]%(name)s - %(levelname)s - %(message)s")
    # This basically decides how the log message would look like. It makes the logs neat, readable, & professional.


    ## File Handler
    # It sends logs to file. Here we will be using RotatingFileHandler which automatically creates a new log file when one becomes too big.
    file_handler = RotatingFileHandler(filename= log_file_path, maxBytes= MAX_LOG_SIZE, backupCount= BACKUP_COUNT)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)    # File stores all the logs from DEBUG to CRITICAL.

    
    ## Console Handler
    # It shows log in terminal/ screen.
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)   # We donts want debug messages in the console since they are too big and noisy. We want only important messages.

    ## Adding handler to the logger
    # Now we attach both the handlers to the logger.
    logger.addHandler(file_handler)     # All the messages appear in the file including deep debugging info.
    logger.addHandler(console_handler)    # Only important messages appear in the terminal 

                
configure_logger()    # Calling the logger config function
