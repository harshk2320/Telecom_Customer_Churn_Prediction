import os   # Create dictionaries, manipulate file paths.
import sys   # Proviide system information to exception.

import numpy as np   # Saving and loading arrays.
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
    

def load_object(file_name: str) -> object:
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
    
def save_numpy_array_data(file_path: str, array: np.array):
    """
    It saves the numpy array/ data to a file so that we can load it later.
    :param file_path: Where to save th numpy array.
    :param array: Actual numpy array that you want to save on the disk.
    """
    try:
        # Getting the directory path
        dir_path = os.path.dirname(file_path)
        
        # Create the directory if it does not exist
        os.makedirs(dir_path, exist_ok= True)

        # Opening the file in binary write mode
        with open(file_path, "wb") as file_obj:
            
            # Save the numpy array
            np.save(file_obj, array)

    except Exception as e:
        raise MyException(e, sys)
    

def load_numpy_array_data(file_path: str) -> np.array:
    """
    This function loads a saved numpy array (.npy) from disk back to python.
    :param file_path: Where to save th numpy array.
    """

    try:
        # Opening the file in read binary mode
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
        
    except Exception as e:
        raise MyException(e, sys)
    

def save_object(file_path: str, obj: object) -> None:
    """
    This function saves python object (model, encoder, scaler, etc) in to a fill using dill
    :param file_path: Where you want to save the object.
    :param obj: what object you want to save (model, encoder, scaler etc)
    """
    logging.info("Entered the save_object method of utils.")

    try:
        # Create directory if not exist
        os.makedirs(os.path.dirname(file_path), exist_ok= True)
        
        # Open the file write binary mode
        with open(file_path, "wb") as file_obj:
            
            # Save the object using dill
            dill.dump(obj, file_obj)

        logging.info("Exiting the save_object method of utils.")

    except Exception as e:
        raise MyException(e, sys)