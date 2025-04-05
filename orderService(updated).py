orderService(updated).py

from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']
orders_collection = db['orders']

@app.route('/orders', methods=['GET'])
def get_orders_by_user():
    user_id = request.args.get('user_id')
    user_orders = list(orders_collection.find({"user_id": user_id}))
    # Convert ObjectId to string for each order
    for order in user_orders:
        order['_id'] = str(order['_id'])
    return jsonify(user_orders)

if __name__ == '__main__':
    # Insert sample data if collection is empty
    if orders_collection.count_documents({}) == 0:
        orders_collection.insert_many([
            {"order_id": "101", "user_id": "1", "product_id": "1001"},
            {"order_id": "102", "user_id": "1", "product_id": "1002"},
            {"order_id": "103", "user_id": "2", "product_id": "1003"}
        ])
    app.run(port=5001)