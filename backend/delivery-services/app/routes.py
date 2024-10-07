from flask import Blueprint, request, jsonify
from app.services import create_delivery, get_delivery_by_id
from app.utils import token_required

delivery_blueprint = Blueprint('deliveries', __name__)

# Create a new delivery (Requires JWT authentication)
@delivery_blueprint.route('/', methods=['POST'])
@token_required
def create_delivery_route(user_id):
    data = request.get_json()
    delivery = create_delivery(user_id, data['address'])  # Use user_id from the JWT token
    return jsonify({
        "message": "Delivery created successfully",
        "delivery_id": delivery.id
    }), 201

# Get details of a specific delivery (Requires JWT authentication)
@delivery_blueprint.route('/<int:delivery_id>', methods=['GET'])
@token_required
def get_delivery_route(user_id, delivery_id):
    delivery = get_delivery_by_id(delivery_id)
    if delivery and delivery.user_id == user_id:
        return jsonify({
            "delivery_id": delivery.id,
            "user_id": delivery.user_id,
            "address": delivery.address,
            "status": delivery.status
        }), 200
    return jsonify({"error": "Delivery not found or unauthorized"}), 404
