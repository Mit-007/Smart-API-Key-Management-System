from app.utils.hash import hash_password, verify_password
from  app.database.connection import user_collection
from fastapi import HTTPException

def create_user(user_data):
    return user_collection.insert_one(user_data)

def get_user_by_email(email):
    return user_collection.find_one({"email": email})

def register_user(user):
    user_data = user.model_dump()

    if len(user_data["password"]) > 72:
        raise HTTPException(status_code=400, detail="Password too long")

    user_data["password"] = hash_password(user_data["password"])

    return user_collection.insert_one(user_data)

def authenticate_user(email, password):
    user = get_user_by_email(email)

    if not user or not verify_password(password, user["password"]):
        return None

    return user