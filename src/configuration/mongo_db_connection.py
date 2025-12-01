import os
import sys
import pymongo
import certifi

from src.exception import MyException
from src.logger import logging
from src.constants import MONGODB_URL_KEY, DATABASE_NAME

