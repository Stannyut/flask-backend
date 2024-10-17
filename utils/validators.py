# utils/validators.py

def validate_product_data(data):
    errors = []

    # Convert price and quantity to the appropriate types
    try:
        data['price'] = float(data['price'])  # Convert price to a float
    except ValueError:
        errors.append("Price must be a valid number.")

    try:
        data['quantity'] = int(data['quantity'])  # Convert quantity to an integer
    except ValueError:
        errors.append("Quantity must be a valid integer.")

    # Perform validation
    if 'name' not in data or not data['name']:
        errors.append("Name is required.")
    if 'price' in data and data['price'] < 0:
        errors.append("Price must be a positive value.")
    if 'quantity' in data and data['quantity'] < 0:
        errors.append("Quantity cannot be negative.")

    return errors
