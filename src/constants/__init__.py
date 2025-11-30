import os
from datetime import date


# MongoDB Connection/ Configuration
DATABASE_NAME = "Proj3"     # Name of MongDB Database. 
COLLECTION_NAME = "Proj3-Data"  # Name of the collection inside the DB where data is stored.
MONGODB_URL_KEY = "MONGODB_URL"  # The environment variable key for MongoDB URL.

# General Pipeline Setting
PIPELINE_NAME: str = ""     # Optional naming for your ML pipeline (empty for now).
ARTIFACT_DIR: str = "artifact"      # Folder where all outputs (cleaned data, models, report) are saved.

# Data Ingestion Related Constants (starts with "DATA_INGESTION")
DATA_INGESTION_COLLECTION_NAME: str = "Proj3-Data"  # Which MongoDB connection to read.
DATA_INGESTION_DIR_NAME: str = "data_ingestion"     # Folder for data ingestion artifacts.
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"    # Raw cleaned data stored here.
DATA_INGESTION_INGESTED_DIR:str = "ingested"    # Train/ Test filed stored here.
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: str =   0.25   # 25% Test and 75% Train.


