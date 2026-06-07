from database import galleries_collection

def search_by_name(name):
    return galleries_collection.find_one(
        {"name": {"$regex": name, "$options": "i"}}
    )

def filter_by_neighborhood(neighborhood):
    return list(galleries_collection.find(
        {"neighborhood": {"$regex": neighborhood, "$options": "i"}}
    ))

def filter_by_art_style(style):
    return list(galleries_collection.find(
        {"art_style": {"$regex": style, "$options": "i"}}
    ))

def list_all():
    return list(galleries_collection.find().sort("name", 1))

def get_all_neighborhoods():
    return sorted(galleries_collection.distinct("neighborhood"))

def get_all_styles():
    styles = set()
    for gallery in galleries_collection.find():
        for style in gallery.get("art_style", []):
            styles.add(style)
    return sorted(styles)