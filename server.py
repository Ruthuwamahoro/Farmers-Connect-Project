from flask import Flask, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {
        "id": 1,
        "product_name": "Product 1",
        "invoice_number": "INV001",
        "store_name": "Store A",
        "price": 19.99,
        "date": "2023-01-01",
    },
    {
        "id": 2,
        "product_name": "Product 2",
        "invoice_number": "INV002",
        "store_name": "Store B",
        "price": 29.99,
        "date": "2023-01-02",
    },
    # Add more products as needed
]

# Endpoint to get all products
@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Run the server
if __name__ == '__main__':
    app.run()