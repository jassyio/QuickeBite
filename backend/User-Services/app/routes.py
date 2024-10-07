from flask import Blueprint, request, jsonify
from .services import (
    create_user, authenticate_user, send_verification_email, 
    send_password_reset_email, reset_password, verify_email
)
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from .models import User

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"message": "Invalid input"}), 400  # Explicit validation

    user = create_user(data['username'], data['email'], data['password'])
    
    if user:
        send_verification_email(user)
        return jsonify({"message": "User registered successfully. Please verify your email."}), 201
    else:
        return jsonify({"message": "User registration failed"}), 400


@user_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = authenticate_user(data['username'], data['password'])
    if user:
        if not user.email_verified:
            return jsonify({"message": "Email not verified"}), 403
        access_token = create_access_token(identity={'id': user.id, 'role': user.role})
        refresh_token = create_refresh_token(identity={'id': user.id, 'role': user.role})
        return jsonify(access_token=access_token, refresh_token=refresh_token), 200
    return jsonify({"message": "Invalid credentials"}), 401


@user_blueprint.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)  # Require refresh token
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    return jsonify(access_token=access_token), 200


@user_blueprint.route('/verify-email/<token>', methods=['GET'])
def verify_email_route(token):
    if verify_email(token):
        return jsonify({"message": "Email verified successfully"}), 200
    return jsonify({"message": "Invalid or expired token"}), 400


@user_blueprint.route('/password-reset', methods=['POST'])
def request_password_reset():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user:
        send_password_reset_email(user)
    return jsonify({"message": "If this email is registered, you will receive a password reset link"}), 200


@user_blueprint.route('/reset-password/<token>', methods=['POST'])
def reset_password_route(token):
    data = request.get_json()
    if reset_password(token, data['new_password']):
        return jsonify({"message": "Password reset successfully"}), 200
    return jsonify({"message": "Invalid or expired token"}), 400