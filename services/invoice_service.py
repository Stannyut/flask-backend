# services/invoice_service.py

from models import Invoice
from database import db

def create_invoice(data):
    new_invoice = Invoice(
        product_id=data['product_id'],
        amount=data['amount'],
        status=data.get('status', 'pending')
    )
    db.session.add(new_invoice)
    db.session.commit()
    return new_invoice