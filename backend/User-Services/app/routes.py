from flask import Blueprint, request, jsonify
from app.services import create_user, authenticate_user

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = create_user(data)
    return jsonify({"message": "User created successfully"}), 201

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = authenticate_user(data['email'], data['password'])
    if token:
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401
