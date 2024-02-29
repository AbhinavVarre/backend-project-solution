from fastapi import FastAPI
from db.supabase import create_supabase_client
from app.models import User
from fastapi.routing import APIRoute
from fastapi.middleware.cors import CORSMiddleware
from .routers import users, auth


#  uvicorn app.main:app --reload

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users",
    },
    {
        "name": "auth",
        "description": "User Auth functions",
    },
]


def custom_generate_unique_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}"


app = FastAPI(generate_unique_id_function=custom_generate_unique_id)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


supabase = create_supabase_client()


@app.get("/", tags=["root"])
async def root():
    return {"message": "Hello World"}


app.include_router(users.router)
app.include_router(auth.router)
