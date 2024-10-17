from database import db
from utils.helpers import format_datetime


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))
    quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'quantity': self.quantity,
            'price': self.price,
            'created_at': format_datetime(self.created_at),
            'updated_at': format_datetime(self.updated_at),
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
