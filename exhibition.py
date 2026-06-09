from database import db

exhibitions_collection = db["exhibitions"]

class Exhibition:
    def __init__(self, data):
        self.gallery_name = data.get("gallery_name")
        self.title = data.get("title")
        self.artist = data.get("artist")
        self.style = data.get("style", [])
        self.date_start = data.get("date_start")
        self.date_end = data.get("date_end")
        self.status = data.get("status")

def get_exhibitions_by_gallery(gallery_name):
    results = exhibitions_collection.find(
        {"gallery_name": {"$regex": gallery_name, "$options": "i"}}
    )
    return list(results)

def get_open_exhibitions():
    return list(exhibitions_collection.find({"status": "open"}).sort("date_end", 1))