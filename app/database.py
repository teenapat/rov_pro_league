import sys
import os

# เพิ่ม path ไปยังโฟลเดอร์หลัก
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import config  # ✅ ตอนนี้ Python หา config.py ได้แล้ว

from pymongo import MongoClient

# เชื่อมต่อ MongoDB
client = MongoClient(config.MONGO_URI)
db = client[config.DB_NAME]

# Collections
matches = db["matches"]
games = db["games"]
players = db["players"]

print("✅ Connected to MongoDB successfully!")
