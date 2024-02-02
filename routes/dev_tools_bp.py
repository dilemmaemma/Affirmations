from flask import jsonify, request, Blueprint
from models.sql_models import db, Affirmations  # Import the necessary models and db object
from config import DEVELOPER_USERNAME, DEVELOPER_PASSWORD

dev_tools_bp = Blueprint('dev_tools', __name__)

@dev_tools_bp.route('/delete-all-entries', methods=['POST'])
def delete_all_entries():
    # Check if the request is from an authorized developer
    username = request.form.get('username')
    password = request.form.get('password')

    if username == DEVELOPER_USERNAME and password == DEVELOPER_PASSWORD:
        try:
            # Delete all entries from the database
            db.session.query(Affirmations).delete()
            db.session.commit()
            return jsonify({'message': 'All entries deleted successfully'}), 200

        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'Unauthorized'}), 401
