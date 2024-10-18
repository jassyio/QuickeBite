from flask import Blueprint, request, jsonify
from .services import UserService
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

user_blueprint = Blueprint('users', __name__)
user_service = UserService()

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = user_service.create_user(data)
    return jsonify(user), 201

@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    token = user_service.authenticate_user(data['email'], data['password'])
    if token:
        return jsonify(token=token), 200
    return jsonify(error='Invalid credentials'), 401

@user_blueprint.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    user = user_service.get_user_by_id(current_user)
    return jsonify(user), 200

