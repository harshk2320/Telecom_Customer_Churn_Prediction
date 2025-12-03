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


class DataIngestion:
        def __init__(self, data_ingestion_config: DataIngestionConfig = DataIngestionConfig()):
                """
                Creates DataIngestionConfig() object. Stores it inside the class as self.data_ingestion_config. 
                This configuration contains feature_store_file_path, training_file_path, test_file_path, split ratio, 
                MongoDB Connection name.
                """
                try:
                        self.data_ingestion_config = data_ingestion_config
                
                except Exception as e:
                        raise MyException(e, sys)
                

        def export_data_into_feature_store(self)->DataFrame:
                """
                Fetch the data from MongoDB. This returns a pandas Dataframe.
                """

                try:
                        logging.info("Exporting data from MongoDB.")    # Logging the process
                        my_data = Proj3Data     # Creating an object of Proj3Data.
                        
                        # export_collection_as_dataframe() is used to get data from MongoDB and returns it as dataframe.
                        dataframe = my_data.export_collection_as_dataframe(collection_name= self.data_ingestion_config.collection_name)
                        
                        logging.info(f"Shape of the dataframe: {dataframe.shape}")  # Logging the no of rows and columns.
                        
                        # Saving the dataframe into feature store. We store it so that we dont have to hit MongoDB again.
                        feature_store_file_path = self.data_ingestion_config.feature_store_file_path    # This line fetches the file path where you want to store your file path.
                        dir_path = os.path.dirname(feature_store_file_path)     # This function removes the file name and only returns the file path.
                        os.makedirs(dir_path, exist_ok= True)   # This creates the folder if they do not exist.
                        logging.info(f"Saving exported data into feature store file path: {feature_store_file_path}")   # Logging the process.
                        dataframe.to_csv(feature_store_file_path, index= False)     # This line saves pandas dataframe into a CSV file at the path you specified.
                        return dataframe    # Returns dataframe so that it can be used for splitting train & test.
                
                except Exception as e:
                        raise MyException(e, sys)
                
        
        def split_data_as_train_test(self, dataframe: DataFrame) -> None:
                """
                This method splits the dataframe into train and test based on the split ratio. 
                It creates a folder in S3 bucket.
                """

                logging.info("Entered split_data_as_train_test method of DataIngestion Class.")
                
                try:
                        train_set, test_set = train_test_split(dataframe, test_size= self.data_ingestion_config.train_test_split_ratio)
                        logging.info("Performed train test split on the dataframe.")
                        logging.info("Exited split_data_as_train_test method of the DataIngestion Class.")
                        dir_path =  os.path.dirname(self.data_ingestion_config.training_file_path)
                        os.makedirs(dir_path, exist_ok=  True)    # Ensure the directory exist before saving the file.

                        logging.info(f"Exporting train & test file path.")
                        train_set.to_csv(self.data_ingestion_config.training_file_path, index= False, header = True)
                        test_set.to_csv(self.data_ingestion_config.testing_file_path, index= False, header = True)

                        logging.info("Exported train & test file.")                
                
                except Exception as e:
                        raise MyException(e, sys)
                
        def initiate_data_ingestion(self) -> DataIngestionArtifact:
                """
                This method initiates the data ingestion component of the training pipeline.
                Train set and test set are returned as the artifact of data ingestion component.
                """
                logging.info("Entered initiate_data_ingestion method of DataIngestion Class.")

                try:
                        dataframe = self.export_data_into_feature_store()
                        logging.info("Got the data from MongoDB.")
                        self.split_data_as_train_test(dataframe)
                        
                        logging.info("Performed train test split on the dataset.")
                        logging.info("Exited split_data_as_train_test method of DataIngestion Class.")

                        data_ingestion_artifact = DataIngestionArtifact(trained_file_path= self.data_ingestion_config.training_file_path, 
                                                                        test_file_path= self.data_ingestion_config.testing_file_path)
                        
                        logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")

                        return data_ingestion_artifact
                
                except Exception as e:
                        raise MyException(e, sys)


                


                



                        