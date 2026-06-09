import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import db

exhibitions_collection = db["exhibitions"]

exhibitions_collection.insert_many([
    {
        "gallery_name": "Amant",
        "title": "Kim Gordon: Count Your Chickens",
        "artist": "Kim Gordon",
        "style": ["Contemporary", "Installation"],
        "date_start": "2026-03-19",
        "date_end": "2026-08-16",
        "status": "open",
        "description": "Kim Gordon, co-founder of Sonic Youth, visual artist and writer. An exhibition continuing her multimedia practice exploring sound, language and visual culture."
    },
    {
        "gallery_name": "Amant",
        "title": "CFGNY: Puddles into Pond",
        "artist": "CFGNY",
        "style": ["Contemporary", "Fashion"],
        "date_start": "2026-03-19",
        "date_end": "2026-08-16",
        "status": "open",
        "description": "CFGNY (Concept Foreign Garments New York) is an interdisciplinary collective blurring the boundaries between fashion, art and queer Asian culture."
    },
    {
        "gallery_name": "Amant",
        "title": "Christelle Oyiri: Belief May Vary",
        "artist": "Christelle Oyiri",
        "style": ["Contemporary", "Sound Art"],
        "date_start": "2026-03-19",
        "date_end": "2026-08-16",
        "status": "open",
        "description": "Work by the French artist and DJ exploring spirituality, belief and sound culture through immersive installations and visual art."
    },
    {
        "gallery_name": "Amant",
        "title": "Klein: Rack It!",
        "artist": "Klein",
        "style": ["Contemporary", "Performance"],
        "date_start": "2026-06-12",
        "date_end": "2026-08-02",
        "status": "open",
        "description": "New exhibition and book launch by Klein, an artist and performer whose cross-disciplinary practice unites music, performance and visual arts."
    },
])

print("4 Amant exhibitions added!")