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
    
def write_yaml_file(file_path: str, content: object, replace: bool ) -> None:
    """
    Writes any python object (dict, config, etc) into yaml file.
    
    :param file_path: Where to save the YAML file. 
    :param content: Python data (dict, list, object etc) to write into YAML
    :param replace: Whether to delete the existing file or not
    """
    try:
        # If replace = True & if it already exist -> Delete it before 
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        # Create parent folder if they dont exist.
        os.makedirs(os.path.dirname(file_path))

        # Open th file in write mode and dump the YAML content
        with open(file_path, "w") as file:
            yaml.dump(content, file)


    except Exception as e:
        raise MyException(e, sys)
    

def load_obect(file_name: str) -> object:
    """
    Gives back the trained model/ scaler/ encoder from a file so that we can use it later.
    """
    try:
        # Opening the file which has the model. This open the model.pkl in binary form.
        with open(file_name, "rb") as file_obj:
            
            # Loading the actual python model object
            obj = dill.load(file_obj)
        return obj

    except Exception as e:
        raise MyException(e, sys)    
    
