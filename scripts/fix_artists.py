import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import db

exhibitions_collection = db["exhibitions"]

fixes = [
    {
        "title": "New Humans: Memories of the Future",
        "artist": "Group show — over 200 artists, writers, architects and filmmakers"
    },
    {
        "title": "Greater New York 2026",
        "artist": "Group show — 53 artists and collectives from NYC"
    },
    {
        "title": "Frida Kahlo & Diego Rivera: The Last Dream",
        "artist": "Frida Kahlo, Diego Rivera"
    },
    {
        "title": "Statics of an Egg",
        "artist": "Group show"
    },
    {
        "title": "LOUCHE: Sleeping Through the Apocalypse",
        "artist": "Group show"
    },
    {
        "title": "Patterns",
        "artist": "Group show — Tauba Auerbach, Frank Stella, Rashid Johnson and others"
    },
    {
        "title": "Carbon Life",
        "artist": "Group show"
    },
    {
        "title": "The Dinner of Sublimation",
        "artist": "Group show"
    },
    {
        "title": "Guggenheim Pop",
        "artist": "Group show"
    },
    {
        "title": "82nd Whitney Biennial",
        "artist": "Group show — 56 artists, duos and collectives"
    },
    {
        "title": "Sally Silberberg: Shifting Ground",
        "artist": "Sally Silberberg"
    },
]

def fix_all():
    for item in fixes:
        result = exhibitions_collection.update_one(
            {"title": item["title"]},
            {"$set": {"artist": item["artist"]}}
        )
        if result.matched_count > 0:
            print(f"✓ Fixed: {item['title'][:50]}")
        else:
            print(f"⚠ Not found: {item['title'][:50]}")
    print("Done!")

if __name__ == "__main__":
    fix_all()