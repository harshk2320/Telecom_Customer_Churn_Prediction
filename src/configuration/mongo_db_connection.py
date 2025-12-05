import os   
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import MONGODB_URL_KEY, DATABASE_NAME

ca = certifi.where()    # It provides SSL certificate. Without this, a cloudDB like MongoDB Atlas will give timeout or SSL error.

class MongoDBClient:
    """
    This class is responsible for connecting to MongoDB Atlas only once.
    """
    
    client = None
    # client is shared by all objects created from this class.
        # First time it creates actual MongoDB Connection.
        # Next time it reuses the connection.
        # This improves performance.

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        """
        Initializes a connection to the MongoDB database. If no existing connection is found, it establishes a new one.

        Parameters:
        ----------
        database_name : str, optional
            Name of the MongoDB database to connect to. Default is set by DATABASE_NAME constant.

        Raises:
        ------
        MyException
            If there is an issue connecting to MongoDB or if the environment variable for the MongoDB URL is not set.
        """
        try:
            # Check if MongoDB Client connection has already been established; if not, create a new one.
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)   # Getting MONGODB_URL_KEY from environment variables.
                
                # If the key is missing.
                if mongo_db_url is None:
                    raise Exception(f"Environment variable '{MONGODB_URL_KEY}' is not set.")
                
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile = ca)
                # MongoClient() makes the connection.
                # tlsCAFile ensures secure TLS/SSL connection
                # This is stored in a class variable so everyone can use it.

            self.client = MongoDBClient.client  # Copies the reference to the shared MongoDB Client into this objects attribute self.client
            self.database = self.client[database_name]  # Gets a Database object from the MongoClient for the name database_name and stores it in self.database.
            self.database_name = database_name    # Stores the databse name as plain string in the instance for future reference.
            logging.info("MongoDB Connection Successful.")  # Sends the informational message to your configured logger.

        except Exception as e:
            # Raise the custom exception with the traceback details if the connection fails.
            raise MyException(e, sys)

            
                    
