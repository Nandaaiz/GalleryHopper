import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import db

galleries_collection = db["galleries"]
exhibitions_collection = db["exhibitions"]


def remove_gallery(name):
    gallery = galleries_collection.find_one({"name": {"$regex": name, "$options": "i"}})

    if not gallery:
        print(f"Gallery '{name}' not found.")
        return

    gallery_name = gallery["name"]

    galleries_collection.delete_one({"_id": gallery["_id"]})
    result = exhibitions_collection.delete_many({"gallery_name": gallery_name})

    print(f"✓ Removed: {gallery_name}")
    print(f"✓ Removed {result.deleted_count} exhibitions")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 remove_gallery.py 'Gallery Name'")
    else:
        name = sys.argv[1]
        remove_gallery(name)