from passlib.context import CryptContext

hash_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return hash_context.hash(password)

def verify_password(plain: str, hashed: str):
    return hash_context.verify(plain, hashed)

def hash_api_key(api_key:str):
    return hash_context.hash(api_key)

def verify_api_key(plain : str , hashed : str):
    return hash_context.verify(plain,hashed)
