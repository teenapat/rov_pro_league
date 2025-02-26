import os
from dotenv import load_dotenv

# โหลดค่าจาก .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "rov_pro_league"
