from fastapi import APIRouter, HTTPException
from app.models import User, CreateUser
from db.supabase import create_supabase_client, Client


router = APIRouter(prefix="/users", tags=["users"])

supabase = create_supabase_client()


# example of a query parameter
@router.get("/", summary="get all users")
async def get_all_users(limit : int = 10):
    # limit is an example of a a query parameter - we don't declare it in the path.
    # you should give query params default values, unless you're sure you want to require them
    # generally, these are filters


    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").select("*").execute()
    # print(users_data)
    # users = [User(**user_data) for user_data in users_data.data]
    return users_data.data


# a sample endpoint with a path parameter
@router.get("/{user_id}", summary="get a user by id")
async def get_user_by_id(user_id : int):
    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").select("*").eq("id", int(user_id)).execute()
    # print(users_data)
    # users = [User(**user_data) for user_data in users_data.data]
    return users_data.data

@router.get("/user/change_first_name/{user_id}/{new_name}", summary="change a user's first name")
async def change_user_first_name(user_id : int, new_name : str):
    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").update({"first_name": new_name}).eq("id", int(user_id)).execute()
    # print(users_data)
    # users = [User(**user_data) for user_data in users_data.data]
    return users_data.data

@router.get("/user/change_last_name/{user_id}/{new_name}", summary="change a user's last name")
async def change_user_last_name(user_id : int, new_name : str):
    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").update({"last_name": new_name}).eq("id", int(user_id)).execute()
    # print(users_data)
    # users = [User(**user_data) for user_data in users_data.data]
    return users_data.data

@router.get("/user/change_birthdate/{user_id}/{new_date}", summary="change a user's birthdate")
async def change_user_birthdate(user_id : int, new_date : str):
    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").update({"birthday": new_date}).eq("id", int(user_id)).execute()
    # print(users_data)
    # users = [User(**user_data) for user_data in users_data.data]
    return users_data.data

@router.get("/user/change_gender/{user_id}/{new_gender}", summary="change a user's gender")
async def change_user_gender(user_id : int, new_gender : str):
    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").update({"gender": new_gender}).eq("id", int(user_id)).execute()
    # print(users_data)
    # users = [User(**user_data) for user_data in users_data.data]
    return users_data.data

@router.get("/user/change_email/{user_id}/{new_email}", summary="change a user's email")
async def change_user_email(user_id : int, new_email : str):
    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").update({"email": new_email}).eq("id", int(user_id)).execute()
    # print(users_data)
    # users = [User(**user_data) for user_data in users_data.data]
    return users_data.data

@router.get("/user/change_phone_number/{user_id}/{new_phone_number}", summary="change a user's phone number")
async def change_user_phone_number(user_id : int, new_phone_number : str):
    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").update({"phone_number": new_phone_number}).eq("id", int(user_id)).execute()
    # print(users_data)
    # users = [User(**user_data) for user_data in users_data.data]
    return users_data.data

@router.get("/user/change_address/{user_id}/{new_address}", summary="change a user's address")
async def change_user_address(user_id : int, new_address : str):
    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").update({"address": new_address}).eq("id", int(user_id)).execute()
    # print(users_data)
    # users = [User(**user_data) for user_data in users_data.data]
    return users_data.data


# post a user to the database
# example of a request body
@router.post("/create", response_model=User, summary="create a user")
async def create_user(user : CreateUser):
   data = supabase.from_("users").upsert({**user.model_dump()}).execute()
   return data.data[0]


