import sys      # Its needed to pass on the traceback info to MyException.
import numpy as np     # Needed to handle data cleaning and formating.
import pandas as pd     # Needed to handle data cleaning and formating.
from typing import Optional   # Allows a parametre to be either str or None.

from src.configuration.mongo_db_connection import MongoDBClient     # This class helps creating MongoDB Connection
from src.constants import DATABASE_NAME    # It comes from the constant file.
from src.exception import MyException   # It used for raising custom exception.


class Proj3Data:
    """
    A class to export MongoDB records as pandas dataframe.
    """

    def __init__(self)-> None:
        try:
            self.mongo_client = MongoDBClient(database_name= DATABASE_NAME)  # This creates a MongoDB client object using the class we created earlier.
    
        except Exception as e:
            raise MyException(e, sys)

    def export_collection_as_dataframe(self, collection_name: str, database_name: Optional[str] = None) -> pd.DataFrame:

        """
        Exports an entire MongoDB collection as pandas dataframe.
        
        Parametre:
        ----------
        collection_name: Name of the mongoDB collection to import data from.
        database_name: Name of the database(Optional) --> Defaults to DATABASE_NAME.


        Returns:
        --------
        Dataframe containing the collection data, with "_id" removed and "na" values replaced with NaN.
        
        """
        try:
            
            # Access the specified collection from the default or specified database.
            if database_name is None:
                collection = self.mongo_client.database[collection_name]

            else:
                collection = self.mongo_client[database_name, collection_name]

            # Convert collection data to dataframe and preprocess.
            print("Fetching data from mongoDB.")
            df = pd.DataFrame(list(collection.find()))
            print(f"Data fetched with length: {len(df)}")

            if "id" in df.columns.to_list():
                df = df.drop(columns= ["id"])

            df.replace({"na": np.nan}, inplace= True)
            return df
        
        except Exception as e:
            raise MyException(e, sys)
        
            
            
        