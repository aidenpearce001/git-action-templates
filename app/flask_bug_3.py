from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Insecure: Allows access from any domain

@app.route('/')
def hello():
    return 'Hello, World!'