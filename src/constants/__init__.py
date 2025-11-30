import os
from datetime import date


# MongoDB Connection/ Configuration
DATABASE_NAME = "Proj3"     # Name of MongDB Database. 
COLLECTION_NAME = "Proj3-Data"  # Name of the collection inside the DB where data is stored.
MONGODB_URL_KEY = "MONGODB_URL"  # The environment variable key for MongoDB URL.

# General Pipeline Setting
PIPELINE_NAME: str = ""     # Optional naming for your ML pipeline (empty for now).
ARTIFACT_DIR: str = "artifact"      # Folder where all outputs (cleaned data, models, report) are saved.




