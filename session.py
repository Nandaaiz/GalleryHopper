import json
import os

SESSION_FILE = "session.json"

def save_session(email):
    with open(SESSION_FILE, "w") as f:
        json.dump({"email": email}, f)

def load_session():
    try:
        with open(SESSION_FILE, "r") as f:
            return json.load(f)
    except:
        return None

def clear_session():
    try:
        os.remove(SESSION_FILE)
    except:
        pass