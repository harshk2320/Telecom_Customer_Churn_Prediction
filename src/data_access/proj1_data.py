import sys      # Its needed to pass on the traceback info to MyException.
import numpy as np     # Needed to handle data cleaning and formating.
import pandas as pd     # Needed to handle data cleaning and formating.
from typing import Optional   # Allows a parametre to be either str or None.

from src.configuration.mongo_db_connection import MongoDBClient     # This class helps creating MongoDB Connection
from src.constants import DATABASE_NAME    # It comes from the constant file.
from src.exception import MyException   # It used for raising custom exception.


