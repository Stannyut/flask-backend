# services/delivery_service.py

from models import Delivery
from database import db

def get_all_deliveries():
    return Delivery.query.all()

def create_delivery(data):
    new_delivery = Delivery(
        invoice_id=data['invoice_id'],
        delivery_status=data.get('delivery_status', 'pending'),
        address=data['address'],
        delivery_date=data.get('delivery_date')
    )
    db.session.add(new_delivery)
    db.session.commit()
    return new_delivery