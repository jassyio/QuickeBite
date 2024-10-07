import jwt
from flask import request, jsonify, current_app
from functools import wraps
import logging

logging.basicConfig(level=logging.INFO)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing"}), 403

        try:
            token = token.split(" ")[1]  # Remove 'Bearer' from the token
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            user_id = data['user_id']  # Extract user_id from token payload
        except Exception as e:
            logging.error(f"Token validation failed: {str(e)}")
            return jsonify({"message": "Token is invalid", "error": str(e)}), 403
        
        return f(user_id, *args, **kwargs)  # Pass user_id to the route handler

    return decorated

def validate_delivery_data(data):
    required_fields = ['order_id' 'delivery_person_id']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    
    return True, "valid data"

def validate_address(address):
    # Placeholder for real address validation logic
    return True if address else False
