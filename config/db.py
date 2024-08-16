from pymongo import MongoClient
from dotenv  import load_dotenv
import os

load_dotenv()

mongouri = os.getenv('MONGODB_URI')

conn = MongoClient(mongouri)
