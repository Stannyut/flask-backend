# app.py

from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate

from database import db

from routes.product_routes import product_bp
from routes.finance_routes import finance_bp
from routes.delivery_routes import delivery_bp
from routes.invoice_routes import invoice_bp

app = Flask(__name__)
CORS(app, resources = {r"/*": {"origins": "http://localhost:5173"}})
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'  # Ensure the database URI is set
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, but recommended

# Register Blueprints
app.register_blueprint(product_bp, url_prefix = '/api/products')
app.register_blueprint(finance_bp, url_prefix ='/api/finances')
app.register_blueprint(delivery_bp, url_prefix  ='/api/delivery')
app.register_blueprint(invoice_bp, url_prefix = '/api/invoices')

@app.route('/')
def index():
    return jsonify(message="Welcome to the Inventory Management API! Refer to /api for more information.")

if __name__ == '__main__':
    app.run(debug=True, port=5000)