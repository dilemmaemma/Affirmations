from flask import jsonify, request, Blueprint
from models.sql_models import db, Affirmations
from pymongo import MongoClient
from config import DEVELOPER_USERNAME, DEVELOPER_PASSWORD, MONGO_URI, NODB_NAME

dev_tools_bp = Blueprint('dev_tools', __name__)

@dev_tools_bp.route('/delete-all-entries', methods=['POST'])
def delete_all_entries():
    data = request.json
    
    # Check if the request is from an authorized developer
    username = data.get('username')
    password = data.get('password')

    if username == DEVELOPER_USERNAME and password == DEVELOPER_PASSWORD:
        try:
            # Delete all entries from the SQL database
            db.session.query(Affirmations).delete()
            db.session.commit()

            # Connect to MongoDB and delete all documents in the collection
            client = MongoClient(MONGO_URI)
            db_mongo = client[NODB_NAME]
            mongo_collection = db_mongo['your_mongo_collection_name']  # Replace with your MongoDB collection name
            mongo_collection.delete_many({})
            
            return jsonify({'message': 'All entries deleted successfully'}), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'Unauthorized'}), 401
