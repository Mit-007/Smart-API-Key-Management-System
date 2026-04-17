from pydantic import BaseModel
from typing import Annotated

class APIKey(BaseModel):
    id: Annotated[int, ...]
    key_name: Annotated[str, ...] 
    is_active: Annotated[bool, ...]
    request_counter: Annotated[int, ...]

class APIKey_Upadate(BaseModel):
    is_active:Annotated[bool,...]