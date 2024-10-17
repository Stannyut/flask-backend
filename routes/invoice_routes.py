# routes/invoice_routes.py

from flask import Blueprint, request, jsonify
from services.invoice_service import create_invoice

invoice_bp = Blueprint('invoice_bp', __name__)

@invoice_bp.route('/', methods=['POST'])
def add_invoice():
    data = request.json
    new_invoice = create_invoice(data)
    return jsonify(new_invoice.to_dict()), 201