from database import db

results = list(db["galleries"].find({"art_style": {"$regex": "Latin", "$options": "i"}}))
print(f"Found: {len(results)}")
for g in results:
    print(f"  {g['name']} — {g['city']}")
