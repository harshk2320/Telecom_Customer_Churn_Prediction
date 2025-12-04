import sys

from src.exception import MyException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionArtifact


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        # When we create a TrainPipeline object, 
        # it automatically creates a DataIngestionConfig which stores the configs like where to save train & test data,
        #  split ratio etc.

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of the training pipeline is responsible for starting data ingestion componen 
        & returns DataIngestionArtifacts (training file path, testing file path)
        """
        try:
            logging.info("Entered the start_data_ingestion method of the TrainPipeline class.")
            logging.info("Getting the data from MongoDB.")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train & test set from MongoDB.")
            logging.info("Exited start_data_ingestion method of the TrainPipeline class.")
            return data_ingestion_artifact
        
        except Exception as e:
            raise MyException(e, sys)


    def run_pipeline(self, ) -> None:
        """
        This method is responsible for running the pipeline.
        """

        try: 
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise MyException(e, sys)        
