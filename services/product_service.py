# services/product_service.py

from models import Product
from database import db
from utils.validators import validate_product_data

def get_all_products():
    return Product.query.all()

def get_product_by_id(product_id):
    return Product.query.get(product_id)

def add_product(data):
    errors = validate_product_data(data)
    if errors:
        return None, errors
    new_product = Product(
        name=data['name'],
        description=data.get('description', ''),
        quantity=data['quantity'],
        price=data['price']
    )
    db.session.add(new_product)
    db.session.commit()
    return new_product, None

def delete_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        db.session.delete(product)
        db.session.commit()
        return True
    return False