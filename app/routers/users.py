from fastapi import APIRouter, HTTPException
from app.models import User, CreateUser
from db.supabase import create_supabase_client, Client


router = APIRouter(prefix="/users", tags=["users"])

supabase = create_supabase_client()


# example of a query parameter
@router.get("/", response_model=list[User], summary="get all users")
async def get_all_users(limit : int = 10):
    # limit is an example of a a query parameter - we don't declare it in the path.
    # you should give query params default values, unless you're sure you want to require them
    # generally, these are filters


    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").select("*").execute()
    # print(users_data)
    users = [User(**user_data) for user_data in users_data.data]
    return users


# a sample endpoint with a path parameter
@router.get("/{user_id}", response_model=list[User], summary="get a user by id")
async def get_user_by_id(user_id : str):
    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").select("*").eq("id", user_id).execute()
    # print(users_data)
    users = [User(**user_data) for user_data in users_data.data]
    return users

# post a user to the database
# example of a request body
@router.post("/create", response_model=User, summary="create a user")
async def create_user(user : CreateUser):
   data = supabase.from_("users").upsert({**user.model_dump()}).execute()
   return data.data[0]


