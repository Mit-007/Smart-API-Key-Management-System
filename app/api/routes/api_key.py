from fastapi import APIRouter, Depends
from app.models.api_model import APIKey,APIKey_Upadate
from app.services.api_key_services import *
from app.dependencies.auth_dep import get_current_user

router = APIRouter(prefix="/Api_Mangement", tags=["Api_Mangement"])

@router.post("/create")
def create(api_key: APIKey, user=Depends(get_current_user)):
    create_api(api_key.dict())
    return {"msg": "api created"}

@router.get("/view")
def read_all_api_data(user=Depends(get_current_user)):
    return get_all_api()

@router.get("/view/{api_id}")
def read_single_api_data(api_id : int,user=Depends(get_current_user)):
    return get_single_api(api_id)

@router.delete("/delete/{api_id}")
def delete_api_data(api_id : int,user=Depends(get_current_user)):
    return delete_api(api_id)

@router.put("/update/{api_id}")
def upadte_api_data(api_id : int,activate :bool,user=Depends(get_current_user)):
    return update_api(api_id,activate)