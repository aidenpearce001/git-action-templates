import os
import requests
import hashlib

def unsafe_exec(user_input):
    exec(user_input)  # Unsafe if user_input is untrusted
    return "Executed user input"

# Imagine user_input being something malicious
def connect_api():
    api_key = "ABCD1234"  # Hardcoded API key
    # Code to connect to an API
    return "API connected with key: " + api_key

def insecure_file_creation():
    with open("sensitive_data.txt", "w") as file:
        file.write("Very sensitive data")
    os.chmod("sensitive_data.txt", 0o777)  # Insecure file permissions
    return "File created with insecure permissions"

def insecure_https_request():
    response = requests.get("https://example.com", verify=False)  # Insecure
    return response.content

def vulnerable_hash_function(data):
    # SHA-1 is considered broken and vulnerable
    return hashlib.sha1(data.encode()).hexdigest()

def load_untrusted_configuration(file_path):
    with open(file_path, "r") as file:
        exec(file.read())  # Executes untrusted configuration
    return "Configuration loaded"

# This can be dangerous if the file_path leads to a file with malicious content

