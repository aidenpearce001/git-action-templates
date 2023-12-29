import tempfile
import subprocess
import hashlib

def unsafe_eval():
    user_input = "2 + 2"  # Imagine this as user-provided input
    result = eval(user_input)  # Insecure
    return result

print(unsafe_eval())

def connect_database():
    username = "admin"
    password = "12345"  # Hardcoded password
    # Code to connect to the database
    print(username, password)
    return "Database connected"

print(connect_database())

def insecure_temp_file():
    temp = tempfile.mktemp()  # Insecure way to create a temporary file
    with open(temp, 'w') as file:
        file.write("Temporary data")
    return temp

print(insecure_temp_file())

def subprocess_vulnerability():
    subprocess.call("ls", shell=True)  # Insecure subprocess call

subprocess_vulnerability()

def weak_crypto():
    # Weak cryptographic hash
    hash_object = hashlib.md5(b'Hello World')
    return hash_object.hexdigest()

print(weak_crypto())

