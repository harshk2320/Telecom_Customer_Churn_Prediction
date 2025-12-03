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

TIMESTAMP = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")    # This generates unique folder name for the run.

@dataclass
# It is python decorator which automatically generates method (__init__(),__repr__(),__eq__() etc)
# It is used for storing configurations without writing boiler plate codes

class TrainingPipelineConfig:
    """
    This class stores high level configuration for ML Training Pipeline.
    """

    pipeline_name: str = PIPELINE_NAME      # Name of the pipelien  
    artefacts_dir: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)    # Folder where my artifacts will be stored.
    timestamp: str = TIMESTAMP     # Used to track when the run happened.

training_class_pipeline: TrainingPipelineConfig = TrainingPipelineConfig()     # Creating an object for TrainingPipelineConfig class.

@dataclass

class DataIngestionConfig:
    """
    This class stores the paths used during data ingestion.
    """

    # Root directory for data ingestion artifacts.
    data_ingestion_dir: str = os.path.join(training_class_pipeline.artefacts_dir, DATA_INGESTION_DIR_NAME)
    
    # Location to save raw dataset from MongoDB.
    feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FILE_NAME)

    # Location for saving training dataset after splitting
    training_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)

    # Location for saving testing dataset after splitting.
    testing_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)

    # Percentage of data allocated for testing
    train_test_split_ratio: float = DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO

    # MongoDB Collection containing the raw data
    collection_name: str = DATA_INGESTION_COLLECTION_NAME

        





