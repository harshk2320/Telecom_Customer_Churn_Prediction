"""
DataIngestion is a class responsible for extracting data from MongoDB and 
storing it into CSV file then splitting into training and testing. 
This is the first step in ML Pipeline.
"""

import os      # Creates a folder and build file paths
import sys    # pass system details to custom exception
from pandas import DataFrame    # Handles dataframe related operation.
from sklearn.model_selection import train_test_split    # Performs train test split

from src.entity.config_entity import DataIngestionConfig    # Configuration for Data Ingestion.
from src.entity.artifact_entity import DataIngestionArtifact    # Output artifacts (file path)
from src.exception import MyException   # Custom exception handling
from src.logger import logging   # Logging for debugging and monitoring 
from src.data_access.proj1_data import Proj3Data    # MongoDB data extraction