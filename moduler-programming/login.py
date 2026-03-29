def login(username, password):
    # Simple hardcoded
    users = {"admin": "admin123", "student1": "pass123"}
    if username in users and users[username] == password:
        return True, "admin" if username == "admin" else "student"
    return False, None