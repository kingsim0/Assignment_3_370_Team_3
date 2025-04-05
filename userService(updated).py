userService(updated).py

from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['ecommerce']
users_collection = db['users']

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users_collection.find_one({"id": user_id})
    if user:
        # Convert ObjectId to string for JSON serialization
        user['_id'] = str(user['_id'])
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    # Insert sample data if collection is empty
    if users_collection.count_documents({}) == 0:
        users_collection.insert_many([
            {"id": "1", "name": "Alice"},
            {"id": "2", "name": "Bob"}
        ])
    app.run(port=5000)