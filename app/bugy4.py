import subprocess
import hashlib
import dill
import socket
import telnetlib

def run_command(user_input):
    command = "echo " + user_input  # Insecure if user_input is not sanitized
    subprocess.Popen(command, shell=True)
    return "Command executed"

def hash_password(password):
    # MD5 is not suitable for password hashing
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    return hashed_password

def dynamic_import(module_name):
    # Insecure if module_name is controllable by user
    module = __import__(module_name)
    return module

def unsafe_deserialization(serialized_data):
    # Deserializes data without any safety checks
    return dill.loads(serialized_data)

def send_sensitive_data(data):
    s = socket.socket()
    s.connect(('example.com', 80))
    s.sendall(data.encode())  # Insecure: Data is sent in plain text
    s.close()

    return "Data sent"

def telnet_connection():
    tn = telnetlib.Telnet('example.com')
    tn.read_until(b"login: ")
    tn.write(b"user\n")
    tn.read_until(b"Password: ")
    tn.write(b"password\n")  # Insecure: Credentials sent in plain text
    return "Connected via Telnet"

