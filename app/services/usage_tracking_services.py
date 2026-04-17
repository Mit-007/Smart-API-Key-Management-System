from app.database.connection import usage_tracking_collection
from fastapi import HTTPException , Body
from app.utils.hash import hash_api_key

def create_usage_history(data):
    return usage_tracking_collection.insert_one(data)