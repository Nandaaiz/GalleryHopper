from database import db

# Verifica quantas galerias por cidade
nyc = db["galleries"].count_documents({"city": "New York"})
sp = db["galleries"].count_documents({"city": "São Paulo"})
sem_cidade = db["galleries"].count_documents({"city": {"$exists": False}})

print(f"New York: {nyc}")
print(f"São Paulo: {sp}")
print(f"Sem cidade: {sem_cidade}")