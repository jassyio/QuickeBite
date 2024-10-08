from flask import Blueprint, request, jsonify
from app.services import create_user, authenticate_user, store_user_session, get_user_session
from app.models import User
from database.mysql.init_mysql import db

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

@user_blueprint.route('/profile', methods='GET')
def profile():
    user_id = request.headers.get('user_id')
    session = get_user_session(user_id)
    if session:
        user = User.query.get(user_id)
        return jsonify({
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "preferences": user.preferences
        }), 200
    return jsonify({"error": "Unauthorized access"}), 403