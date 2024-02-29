import os
from supabase import Client, create_client
from dotenv import load_dotenv

load_dotenv()

api_url: str = os.getenv("url")
key: str = os.getenv("api")
print(api_url)
def create_supabase_client():
    supabase: Client = create_client(api_url, key)
    return supabase

