# flask_api_example/main.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello")
def home():
    return jsonify(message="Hello, World!")

@app.route("/test")
def home():
    return jsonify(message="test fonctionnel!")


def start():
    app.run()