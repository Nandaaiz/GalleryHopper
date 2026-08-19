from database import db
from pymongo.errors import ServerSelectionTimeoutError

def get_collection():
    return db["galleries"]

def search_by_name(name):
    try:
        return get_collection().find_one(
            {"name": {"$regex": name, "$options": "i"}}
        )
    except Exception:
        return None

def filter_by_neighborhood(neighborhood, city="New York"):
    try:
        return list(get_collection().find({
            "neighborhood": {"$regex": neighborhood, "$options": "i"},
            "city": city
        }))
    except Exception:
        return []

def filter_by_art_style(style, city="New York"):
    try:
        return list(get_collection().find({
            "art_style": {"$regex": style, "$options": "i"},
            "city": city
        }))
    except Exception:
        return []

def list_all(city="New York"):
    try:
        return list(get_collection().find({"city": city}).sort("name", 1))
    except Exception:
        return []

def get_all_neighborhoods(city="New York"):
    try:
        return sorted(get_collection().distinct("neighborhood", {"city": city}))
    except Exception:
        return []

def get_all_styles(city="New York"):
    try:
        styles = set()
        for gallery in get_collection().find({"city": city}):
            for style in gallery.get("art_style", []):
                styles.add(style)
        return sorted(styles)
    except Exception:
        return []