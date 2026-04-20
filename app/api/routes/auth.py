from fastapi import APIRouter, HTTPException ,Depends , Body
from app.models.user_model import User
from app.services.user_services import register_user, authenticate_user
from app.core.security import create_access_token,create_refresh_token
from jose import jwt,JWTError
from app.core.config import SECRET_KEY,ALGORITHM

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
def register(user: User):
    register_user(user)
    return {"msg": "User created"}

@router.post("/login")
def login(user: User):
    db_user = authenticate_user(user.email, user.password)

    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": db_user["email"]})
    refresh_token = create_refresh_token({"sub": db_user["email"]})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@router.post("/refresh/")
def refresh_token(refresh_token : str = Body(...)):
    try:
        payload = jwt.decode(refresh_token,SECRET_KEY,algorithms=[ALGORITHM])
        if payload.get("type") != "refresh" :
            raise HTTPException(status_code=401 , detail="invalid token type")
        
        email=payload.get("sub")

        new_access_token= create_access_token({"sub":email})

        return {"access_token" : new_access_token}

    except JWTError:
        raise HTTPException(status_code=401 , detail="Invalid and expired refresh token")