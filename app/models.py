from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: str
    created_at: str    
    name: Optional[str]
    email: Optional[str]

class CreateUser(BaseModel):
    id: str
    name: str


class Token(BaseModel):
    access_token: str
    token_type: str