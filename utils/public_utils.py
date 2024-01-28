from flask import request, jsonify
from bson import ObjectId
from helpers.nosql_helpers import (
    add_public_affirmation, 
    update_public_affirmation, 
    delete_public_affirmation
)

def create_public_affirmation(data):
    data = request.json
    add_public_affirmation(data['user'], ObjectId(data['user_id']), data['category'], data['keyword'], data['affirmation_text'])
    return jsonify({'message': 'Public affirmation added successfully'})

def update_public_affirmation(data):
    data = request.json
    affirmation_id = data.get('id')
    
    try:
        if not affirmation_id:
            raise ValueError('Missing affirmation ID in the request')

        updated_affirmation = update_public_affirmation(
            affirmation_id,
            data.get('category'),
            data.get('keyword'),
            data.get('affirmation_text')
        )

        if updated_affirmation:
            return jsonify({'message': 'Public affirmation updated successfully'})
        else:
            return jsonify({'message': 'Public affirmation not found'}), 404

    except ValueError as ve:
        return jsonify({'message': str(ve)}), 400
    except Exception as e:
        return jsonify({'message': f'An unexpected error occurred: {e}'}), 500

def delete_public_affirmation(data):
    data = request.json
    affirmation_id = data.get('id')
    if not affirmation_id:
        return jsonify({'message': 'Missing affirmation ID in the request'}), 400

    deleted_affirmation = delete_public_affirmation(affirmation_id)
    if deleted_affirmation:
        return jsonify({'message': 'Public affirmation deleted successfully'})
    else:
        return jsonify({'message': 'Public affirmation not found'}), 404
