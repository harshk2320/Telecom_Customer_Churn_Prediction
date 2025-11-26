## Below code is to check logging configuration
# from src.logger import logging

# logging.debug("This is a debug message")
# logging.debug("This is an info message")
# logging.warning("This is an warning message")
# logging.error("This is an error message")
# logging.critical("This is an Critical message")


## Below code is to check the exception config.

from src.logger import logging  
from src.exception import MyException
import sys


try:

    a= 1+ "Z"

except Exception as e:      # This catches any type of error. Here e = What error happened.
    logging.info(e)     # This will store the error message in logs which will also appear in console and in logs folder.
    raise MyException(e, sys) from e    # from e means it will tell python: MyException happened because of the original error.
    # MyException(e, sys) will:
        # Find where the error happened
        # Find the file name
        # Find the line number
        # Create a detailed professional message
        # Log it

