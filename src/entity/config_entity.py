"""
This code defines configuration for training a machine learning pipeline. 
These configurations helps so that we dont have to hardcode paths everywhere

These classes store path like:

    1. Where to save raw data

    2. Where to save transformed data

    3. Where to save trained model

    4. Expected accuracy

    5. Collection name from MongoDB Etc.
    
"""


import os   # Used for creating folder paths. 
from src.constants import *     # Contains global constants and file paths.
from dataclasses import dataclass   # It automatically creates constructor such as (__init__(),     __repr__(), __eq__())
from datetime import datetime   # Generate timestamps to create unique directories.

