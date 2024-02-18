from fastapi import FastAPI
from db.supabase import create_supabase_client
from app.models import User
from fastapi.middleware.cors import CORSMiddleware
from .routers import users


#  uvicorn app.main:app --reload 

tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users",
    },
   
]


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


supabase = create_supabase_client()

@app.get("/", )
async def root():
    return {"message": "Hello World"}

app.include_router(users.router)



    