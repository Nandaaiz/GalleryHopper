from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

def create_client():
    return MongoClient(
        MONGO_URI,
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=10000,
        connectTimeoutMS=10000,
        socketTimeoutMS=10000,
        retryWrites=True,
        retryReads=True
    )

client = create_client()
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