import pickle
import socket
import os
from xml.etree import ElementTree as ET
import yaml
import sqlite3

def validate_user(user):
    assert user.is_admin, "User must be an admin"
    # Perform admin-only actions
    return "Admin actions performed"

def unsafe_deserialization(data):
    # Deserializes data without any safety checks
    return pickle.loads(data)

def insecure_socket():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080))  # Insecure
    server_socket.listen(5)
    return "Server is listening"

def weak_key_generation():
    # Generates a weak cryptographic key
    key = os.urandom(8)  # Too short, easily brute-forced
    return key

def parse_xml(xml_string):
    tree = ET.fromstring(xml_string)  # Insecure
    return tree.tag

def unsafe_yaml_load(yaml_data):
    # Unsafe loading of YAML
    return yaml.load(yaml_data)

def unsafe_sql_query(user_input):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"  # Insecure
    cursor.execute(query)
    return cursor.fetchall()
