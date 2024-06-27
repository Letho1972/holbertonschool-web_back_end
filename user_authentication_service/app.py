#!/usr/bin/env python3

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

AUTH = Auth()

""" Set up a basic Flask app """

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """ a single GET route ("/")"""

    return jsonify({
        'message': 'Hello, World!',
        'status': 'success'
    })


@app.route('/users', methods=['POST'])
def register_user():
    """Register user"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
