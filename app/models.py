from pydantic import BaseModel

class User(BaseModel):
    id: str
    created_at: str
    name: str
    email: str
