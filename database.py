from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["galleryhopper"]

galleries_collection = db["galleries"]

def test_connection():
    try:
        client.admin.command('ping')
        print("Connected to MongoDB!")
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    test_connection()