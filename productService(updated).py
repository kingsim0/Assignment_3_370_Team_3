productService(updated).py

from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']
products_collection = db['products']

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products_collection.find_one({"id": product_id})
    if product:
        # Convert ObjectId to string for JSON serialization
        product['_id'] = str(product['_id'])
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    # Insert sample data if collection is empty
    if products_collection.count_documents({}) == 0:
        products_collection.insert_many([
            {"id": "1001", "name": "Laptop", "price": 1200},
            {"id": "1002", "name": "Smartphone", "price": 800},
            {"id": "1003", "name": "Tablet", "price": 600}
        ])
    app.run(port=5002)