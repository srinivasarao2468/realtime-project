import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import json_util

MONGO_SERVER = os.environ.get('MONGO_SERVER')

# MongoDB URI
uri = f"mongodb://admin:admin123@MONGO_SERVER:27017/"

# Create a Flask app
app = Flask(__name__)

# Create a MongoClient
client = MongoClient(uri)

# Function to get or create the MongoDB collection
def get_or_create_collection(db, collection_name):
    if collection_name in db.list_collection_names():
        # The collection already exists; return it
        return db[collection_name]
    else:
        # The collection doesn't exist; create it
        return db.create_collection(collection_name)

# Routes

@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.json
    db = client.get_database("sampledb")  # Get or create the database
    collection = get_or_create_collection(db, "samplecollection")  # Get or create the collection
    result = collection.insert_one(data)
    return jsonify({"message": "Data inserted successfully", "id": str(result.inserted_id)})

@app.route('/retrieve', methods=['GET'])
def retrieve_data():
    db = client.get_database("sampledb")  # Get or create the database
    collection = get_or_create_collection(db, "samplecollection")  # Get or create the collection
    data = list(collection.find())
	serialized_data = json_util.dumps(data)
    return jsonify(serialized_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
