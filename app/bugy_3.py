users = {
    "admin": "password123",  # Insecure: Password is stored in plaintext
    "user": "mypassword"
}

def check_login(username, password):
    return users.get(username) == password

