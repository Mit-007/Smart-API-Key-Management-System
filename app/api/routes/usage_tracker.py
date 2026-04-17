from fastapi import APIRouter, Depends , Header
from app.services.api_key_services import *
from app.services.usage_tracking_services import create_usage_history
from app.utils.hash import verify_api_key
from datetime import datetime
from app.core.rate_limiter import rate_limiter

router = APIRouter(prefix="/usage_tracker", tags=["usage_tracker"])

MAX_LIMIT=100

@router.get("/call_api")
def use_api(x_api_key: str = Header(...)):

    api_key_parts=x_api_key.split("/",2)
    api_key = api_key_parts[1]
    api_data = None
    for doc in api_collection.find():
        if verify_api_key(api_key,doc["key_name"]):
            api_data = doc
            break

    if not api_data:
        raise HTTPException(status_code=401, detail="Invalid API key")

    if not api_data.get("is_active"):
        raise HTTPException(status_code=403, detail="API key is inactive")
    
    # if datetime.utcnow() - api_data.get("last_call_time") > timedelta(minutes=1):
    #     api_collection.update_one(
    #         {"_id":api_data["_id"]},
    #         {"$set":{"request_counter":0,"last_call_time":datetime.utcnow()}}
    #     )

    # if api_data.get("request_counter") >= MAX_LIMIT:
    #     raise HTTPException(status_code=429, detail="Rate limit exceeded")
     
    res = rate_limiter(api_data)

    api_collection.update_one(
        {"_id": api_data["_id"]},
        {"$inc": {"request_counter": 1}}
    )
    api_collection.update_one(
        {"_id": api_data["_id"]},
        {"$set": {"last_call_time":datetime.utcnow()}}
    )

    data = {
        "api_id": str(api_data["_id"]),
        "endpoint": f"/{api_key_parts[2]}",
        "timestamp": datetime.utcnow(),
        "status_code": 200,
    }

    create_usage_history(data)

    return {"msg": "API accessed successfully"}
