import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class Mongo_Service:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Mongo_Service, cls).__new__(cls)
            uri = os.getenv('MONGO_URI',"mongodb://localhost:27017")
            db_name = os.getenv('MONGO_DB_NAME',"fullstack_logs_db")
            cls._instance.client = MongoClient(uri)
            cls._instance.db = cls._instance.client[db_name]
        return cls._instance


    @property
    def logs_collection(self):
        return self.db['workout_execution_logs']

mongo_db = Mongo_Service()

