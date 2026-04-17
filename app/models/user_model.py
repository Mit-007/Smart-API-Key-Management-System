from pydantic import BaseModel,EmailStr
from typing import Annotated

class User(BaseModel):
    email : Annotated[EmailStr,...]
    password : Annotated[str,...]

