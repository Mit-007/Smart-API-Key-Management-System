import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL=os.getenv("MONGODB_URL")
DB_NAME=os.getenv("DB_NAME")

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))


# if not MONGO_URL:
#     raise ValueError("MONGO_URL not found in .env")