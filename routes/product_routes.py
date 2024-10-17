# routes/product_routes.py

from flask import Blueprint, request, jsonify
from services.product_service import (
    get_all_products,
    get_product_by_id,
    add_product,
    delete_product
)
from utils.validators import validate_product_data

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    products = get_all_products()
    return jsonify([product.to_dict() for product in products])

@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.json
    new_product, errors = add_product(data)
    if errors:
        return jsonify({'errors': errors}), 400
    return jsonify(new_product.to_dict()), 201

@product_bp.route('/<int:product_id>', methods=['DELETE'])
def remove_product(product_id):
    success = delete_product(product_id)
    if success:
        return jsonify({'message': 'Product deleted'}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404