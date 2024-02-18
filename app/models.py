from pydantic import BaseModel

class User(BaseModel):
    id: str
    created_at: str
    name: str
    email: str

class CreateUser(BaseModel):
    name: str
    email: str
