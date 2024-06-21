from pymongo import MongoClient
from os import environ

client = MongoClient(environ.get("MONGO_URI"))

db = client.test_db_traduzo
