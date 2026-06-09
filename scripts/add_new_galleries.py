from database import db

galleries_collection = db["galleries"]
exhibitions_collection = db["exhibitions"]

# ── Add new galleries ─────────────────────────────────
galleries_collection.insert_one({
    "name": "L'Space Gallery",
    "neighborhood": "Chelsea",
    "art_style": ["Photography", "Fiber Art", "Contemporary"],
    "type": "gallery",
    "alias": ["LSpace", "L Space", "Lspace"],
    "city": "New York"
})

galleries_collection.insert_one({
    "name": "MoMA PS1",
    "neighborhood": "Queens",
    "art_style": ["Contemporary", "Experimental Art"],
    "type": "museum",
    "alias": ["PS1", "PS 1", "MoMA PS 1"],
    "city": "New York"
})

# ── Add exhibitions ───────────────────────────────────
exhibitions_collection.insert_many([
    {
        "gallery_name": "L'Space Gallery",
        "title": "Shape of Dreams: Leonora Carrington",
        "artist": "Leonora Carrington",
        "style": ["Surrealism", "Sculpture"],
        "date_start": "2026-05-07",
        "date_end": "2026-07-25",
        "status": "open"
    },
    {
        "gallery_name": "MoMA PS1",
        "title": "Greater New York 2026",
        "artist": "53 artistas e coletivos de NYC",
        "style": ["Contemporary", "Experimental Art"],
        "date_start": "2026-04-16",
        "date_end": "2026-12-31",
        "status": "open"
    }
])

print("2 galleries and 2 exhibitions added!")