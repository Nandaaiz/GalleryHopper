from database import galleries_collection

results = list(galleries_collection.find({"neighborhood": "Lower East Side"}))
print(len(results))
for g in results:
    print(g["name"])