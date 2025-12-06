import os   # Create dictionaries, manipulate file paths.
import sys   # Proviide system information to exception.

import numpy    # Saving and loading arrays.
import yaml     # Reading & writing YAML files.
import dill     # Saving python object (Better than pickle)
from pandas import DataFrame    # Convert to dataframe

from src.exception import MyException   # Custom exception 
from src.logger import logging    # To log message.


def read_yaml_file(file_path: str) -> dict:
    """
    Opens a .yaml file. Reads its content into python dictionary, & then returns a dictionary.
    
    :param file_path: path to .yaml file
    :return: dict
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
        
    except Exception as e:
        raise MyException(e, sys)