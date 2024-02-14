from fastapi import FastAPI
from db.supabase import create_supabase_client
from app.models import User

app = FastAPI()


supabase = create_supabase_client()

@app.get("/", )
async def root():
    return {"message": "Hello World"}


@app.get("/users", response_model=list[User], summary="get all users")
async def root():
    # format that supabse returns is {data: [], ...}
    users_data = supabase.from_("users").select("*").execute()
    # print(users_data)
    users = [User(**user_data) for user_data in users_data.data]
    return users


    