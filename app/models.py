from pydantic import BaseModel

class User(BaseModel):
    id: int
    created_at: str
    first_name: str
    last_name: str
    birthday: str
    gender: str
    email: str
    phone_number: str
    address: str

class CreateUser(BaseModel):
    name: str
    email: str
