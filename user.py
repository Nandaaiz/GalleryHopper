import bcrypt
from database import db

users_collection = db["users"]

class UserManager:
    def __init__(self):
        # Hash table para guardar usuario logado em memoria
        self._logged_users = {}

    def register(self, name, email, password):
        # Verifica se email ja existe
        if users_collection.find_one({"email": email}):
            return False, "Email already registered."

        # Criptografa a senha
        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

        # Insere no MongoDB
        users_collection.insert_one({
            "name": name,
            "email": email,
            "password": hashed,
            "visited": []
        })
        return True, "Account created successfully!"

    def login(self, email, password):
        # Busca usuario no banco
        user = users_collection.find_one({"email": email})
        if not user:
            return False, "Email not found."

        # Verifica a senha
        if bcrypt.checkpw(password.encode("utf-8"), user["password"]):
            # Guarda na hash table em memoria
            self._logged_users[email] = user
            return True, user
        else:
            return False, "Incorrect password."

    def logout(self, email):
        if email in self._logged_users:
            del self._logged_users[email]

    def get_logged_user(self, email):
        return self._logged_users.get(email)

    def add_to_visited(self, email, gallery_name):
        users_collection.update_one(
            {"email": email},
            {"$addToSet": {"visited": gallery_name}}
        )
        # Atualiza na hash table tbm
        if email in self._logged_users:
            self._logged_users[email]["visited"].append(gallery_name)

# Instancia global
user_manager = UserManager()