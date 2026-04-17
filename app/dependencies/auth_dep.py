from app.core.token import verify_token
from fastapi import Depends,HTTPException,Header

def get_current_user(Access_token: str = Header):
    if not Access_token:
        raise HTTPException(status_code=401, detail="Token missing")

    try:
        token = Access_token.split(" ")[1]
    except:
        raise HTTPException(status_code=401, detail="Invalid token format")

    payload = verify_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")

    return 

