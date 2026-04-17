from pymongo import MongoClient
from app.core.config import MONGO_URL,DB_NAME

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

user_collection = db["user_details"]
api_collection = db["api_details"]
usage_tracking_collection = db["api_usage_tracking_details"]
