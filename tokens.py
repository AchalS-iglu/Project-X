import os
from dotenv import load_dotenv

load_dotenv()

IMGUR_CLIENT_ID =  os.environ.get("IMGUR_CLIENT_ID")
IMGUR_CLIENT_SECRET = os.environ.get("IMGUR_CLIENT_SECRET")