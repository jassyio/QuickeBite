from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from .services import DeliveryService

delivery_bp = Blueprint('delivery', __name__)
delivery_service = DeliveryService()

@delivery_bp.route('/deliveries', methods=['POST'])
@jwt_required()
def create_delivery():
    data = request.get_json()
    result = delivery_service.create_delivery(data)
    return jsonify(result), 201 if 'id' in result else 400

@delivery_bp.route('/deliveries', methods=['GET'])
@jwt_required()
def get_all_deliveries():
    deliveries = delivery_service.get_all_deliveries()
    return jsonify(deliveries), 200

@delivery_bp.route('/deliveries/<int:delivery_id>', methods=['GET'])
@jwt_required()
def get_delivery(delivery_id):
    delivery = delivery_service.get_delivery_by_id(delivery_id)
    if delivery:
        return jsonify(delivery), 200
    return jsonify({'message': 'Delivery not found'}), 404

@delivery_bp.route('/deliveries/<int:delivery_id>', methods=['PUT'])
@jwt_required()
def update_delivery(delivery_id):
    data = request.get_json()
    result = delivery_service.update_delivery(delivery_id, data)
    if result:
        return jsonify(result), 200
    return jsonify({'message': 'Delivery not found'}), 404

@delivery_bp.route('/deliveries/<int:delivery_id>', methods=['DELETE'])
@jwt_required()
def delete_delivery(delivery_id):
    result = delivery_service.delete_delivery(delivery_id)
    if result:
        return jsonify({'message': 'Delivery deleted successfully'}), 200
    return jsonify({'message': 'Delivery not found'}), 404