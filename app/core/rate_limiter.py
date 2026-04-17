from datetime import datetime,timedelta
from fastapi import HTTPException
from app.database.connection import api_collection


def rate_limiter(api_data : dict):
    MAX_LIMIT = 100 
    if datetime.utcnow() - api_data.get("last_call_time") > timedelta(minutes=1):
        api_collection.update_one(
            {"_id":api_data["_id"]},
            {"$set":{"request_counter":0,"last_call_time":datetime.utcnow()}}
        )

    if api_data.get("request_counter") >= MAX_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    
    return True