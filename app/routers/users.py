from fastapi import APIRouter, HTTPException, Depends
from app.models import User, CreateUser
from db.supabase import create_supabase_client, Client
from .auth import get_current_user


router = APIRouter(prefix="/users", tags=["users"])

supabase = create_supabase_client()


# overall concepts


# example of a query parameter
@router.get("/", response_model=list[User], summary="get all users")
async def get_all_users(limit: int = 10):
    # limit is an example of a a query parameter - we don't declare it in the path.
    # you should give query params default values, unless you're sure you want to require them
    # generally, these are filters

    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").select("*").execute()
    users = [User(**user_data) for user_data in users_data.data]
    return users

# post a user to the database
# example of a request body
@router.post("/create", response_model=User, summary="create a user")
async def create_user(name: str, email: str, password: str):
    try:
        # check if user exists
        db_user = supabase.from_("users").select("*").eq("email", email).execute()
        if len(db_user.data) == 0:
            createdUser = supabase.auth.sign_up({"email": email, "password": password})
        else:
            # if the user exists, sign in, and use this and update it
            createdUser = supabase.auth.sign_in_with_password(
                {"email": email, "password": password}
            )
        new_user: CreateUser = CreateUser(name=name, id=createdUser.user.id)
        # I usually use upsert instead of update because i don't have to worry if an entry exists or not
        insert_user = (
            supabase.from_("users").upsert({**new_user.model_dump()}).execute()
        )
        return insert_user.data[0]
    # at this point there is an empty user in the db; we need to access the id of that empty user and add the details that we want
    except Exception as e:
        raise HTTPException(
            status_code=400, detail="User could not be created: " + str(e)
        )

# protected endpoint
@router.get("/protected", summary="protected endpoint")
async def protected_endpoint(current_user: User = Depends(get_current_user)):
    print(current_user)
    return current_user

@router.delete("/delete", summary="delete a user")
async def delete_user(current_user: User = Depends(get_current_user)):
    try:
        user = supabase.from_("users").delete().eq("id", current_user.id).execute()
        supabase.auth.sign_out()
        return {"message": "User deleted"}
    except Exception as e:
        raise HTTPException(
            status_code=400, detail="User could not be deleted: " + str(e)
        )



# a sample endpoint with a path parameter
#  IMPORTANT: the order of your endpoints matter.
@router.get("/{user_id}", response_model=User, summary="get a user by id")
async def get_user_by_id(user_id: str):
    # format that supabase returns is {data: [], ...}
    users_data = supabase.from_("users").select("*").eq("id", user_id).execute()
    # print(users_data)
    user = User(**users_data.data[0])
    return user