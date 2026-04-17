from app.database.connection import api_collection
from fastapi import HTTPException , Body
from app.utils.hash import hash_api_key
from datetime import datetime

def create_api(data):
    data["_id"]=data["id"]
    del data["id"]
    data["key_name"]=hash_api_key(data["key_name"])
    data["last_call_time"]=datetime.utcnow()
    return api_collection.insert_one(data)

def get_all_api():
    return list(api_collection.find())

def get_single_api(api_id):
    api_data = api_collection.find_one({"_id":api_id})
    if api_data==None:
        raise HTTPException(status_code=404 , detail="api Not found")
    
    return api_data

def update_student(api_id:int,update_data):
    api_data = api_collection.find_one({"_id":api_id})
    if api_data==None:
        raise HTTPException(status_code=404 , detail="api Not found")

    api_collection.update_one(
        {"_id": api_id},
        {"$set": {"is_active":update_data}}
    )

    if update_data==True :
        return{"msg" : "api activated "}

    return {"msg": "api deactivated"}

def delete_api(api_id):
    api_data = api_collection.find_one({"_id":api_id})
    if api_data==None:
        raise HTTPException(status_code=404 , detail="api Not found")
    
    api_collection.delete_one({"_id":api_id})
    return {"msg": "api deleted successfully"}