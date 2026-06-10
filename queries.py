from pymongo.errors import ServerSelectionTimeoutError, AutoReconnect
import database

def get_collection():
    try:
        database.client.admin.command('ping')
    except Exception:
        database.client = database.create_client()
        database.db = database.client["galleryhopper"]
    return database.db["galleries"]

def search_by_name(name):
    try:
        return get_collection().find_one(
            {"name": {"$regex": name, "$options": "i"}}
        )
    except Exception:
        return None

def filter_by_neighborhood(neighborhood):
    try:
        return list(get_collection().find(
            {"neighborhood": {"$regex": neighborhood, "$options": "i"}}
        ))
    except Exception:
        return []

def filter_by_art_style(style):
    try:
        return list(get_collection().find(
            {"art_style": {"$regex": style, "$options": "i"}}
        ))
    except Exception:
        return []

def list_all():
    try:
        return list(get_collection().find().sort("name", 1))
    except Exception:
        return []

def get_all_neighborhoods():
    try:
        return sorted(get_collection().distinct("neighborhood"))
    except Exception:
        return []

def get_all_styles():
    try:
        styles = set()
        for gallery in get_collection().find():
            for style in gallery.get("art_style", []):
                styles.add(style)
        return sorted(styles)
    except Exception:
        return []