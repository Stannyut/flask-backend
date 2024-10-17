# routes/delivery_routes.py

from flask import Blueprint, jsonify, request
from services.delivery_service import get_all_deliveries, create_delivery

delivery_bp = Blueprint('delivery_bp', __name__)

@delivery_bp.route('/', methods=['GET'])
def get_deliveries():
    deliveries = get_all_deliveries()
    return jsonify([delivery.to_dict() for delivery in deliveries])

@delivery_bp.route('/', methods=['POST'])
def add_delivery():
    data = request.json
    new_delivery = create_delivery(data)
    return jsonify(new_delivery.to_dict()), 201