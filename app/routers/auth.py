from fastapi import Depends, status, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from db.supabase import create_supabase_client
from app.models import Token
from app.models import User

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
supabase = create_supabase_client()


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:

        data = supabase.auth.get_user(token)
        user = supabase.from_("users").select("*").eq("id", data.user.id).execute()
        return User(**user.data[0])
    except Exception as e:
        print(e)  # Handle exceptions appropriately
        raise credential_exception


@router.get("/current-user")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/token", response_model=Token)
async def set_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    data = supabase.auth.sign_in_with_password({"email": form_data.username, "password": form_data.password})
    if not data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    print(data.session.access_token)
    return {"access_token": data.session.access_token, "token_type": "bearer"}