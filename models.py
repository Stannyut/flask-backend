from database import db
from utils.helpers import format_datetime

class Product(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    sku = db.Column(db.String(50), nullable=False, primary_key=True, unique=True)  # Add SKU field
    condition = db.Column(db.String(20), nullable=False, default='New')  # Add condition field
    location = db.Column(db.String(100), nullable=False)  # Add location field
    available = db.Column(db.Integer, default=0)  # Add available stock field
    reserved = db.Column(db.Integer, default=0)  # Add reserved stock field
    onHand = db.Column(db.Integer, default=0)  # Add on-hand stock field
    price = db.Column(db.Float, nullable=False)  # Add price field

    def to_dict(self):
        return {
            # 'id': self.id,
            'name': self.name,
            'sku': self.sku,
            'condition': self.condition,
            'location': self.location,
            'available': self.available,
            'reserved': self.reserved,
            'onHand': self.onHand,
            'price': self.price,
        }


        

class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, paid, canceled
    issued_at = db.Column(db.DateTime, default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'amount': self.amount,
            'status': self.status,
            'issued_at': format_datetime(self.issued_at),
        }


class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id'), nullable=False)
    delivery_status = db.Column(db.String(50), default='pending')  # pending, shipped, delivered
    address = db.Column(db.String(200), nullable=False)
    delivery_date = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'invoice_id': self.invoice_id,
            'delivery_status': self.delivery_status,
            'address': self.address,
            'delivery_date': format_datetime(self.delivery_date) if self.delivery_date else None,
        }


class FinanceReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_sales = db.Column(db.Float, default=0.0)
    expenses = db.Column(db.Float, default=0.0)
    profits = db.Column(db.Float, default=0.0)
    report_date = db.Column(db.DateTime, default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'total_sales': self.total_sales,
            'expenses': self.expenses,
            'profits': self.profits,
            'report_date': format_datetime(self.report_date),
        }
