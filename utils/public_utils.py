from flask import jsonify
from datetime import datetime
from helpers.nosql_helpers import (
    add_public_affirmation, 
    update_public_affirmation, 
    delete_public_affirmation
)

def create_public_affirmation(user, user_id, affirmation_id, category, keyword, affirmation_text):
    add_public_affirmation(
        user,
        user_id,
        affirmation_id,
        category,
        keyword,
        affirmation_text,
        created_at=datetime.utcnow()
    )
    return jsonify({'message': 'Public affirmation added successfully'})

def update_public_affirmation(affirmation_id, user, user_id, category, keyword, affirmation_text):
    
    try:
        if not affirmation_id:
            raise ValueError('Missing affirmation ID in the request')

        updated_affirmation = update_public_affirmation(
            affirmation_id,
            user,
            user_id,
            category,
            keyword,
            affirmation_text,
            updated_at=datetime.utcnow()
        )

        if updated_affirmation:
            return jsonify({'message': 'Public affirmation updated successfully'})
        else:
            return jsonify({'message': 'Public affirmation not found'}), 404

    except ValueError as ve:
        return jsonify({'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'message': f'An unexpected error occurred: {e}'}), 500

def delete_public_affirmation(affirmation_id):
    if not affirmation_id:
        return jsonify({'message': 'Missing affirmation ID in the request'}), 400

    deleted_affirmation = delete_public_affirmation(affirmation_id)
    if deleted_affirmation:
        return jsonify({'message': 'Public affirmation deleted successfully'})
    else:
        return jsonify({'message': 'Public affirmation not found'}), 404
