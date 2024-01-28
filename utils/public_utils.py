from flask import request, jsonify
from helpers.nosql_helpers import (
    add_public_affirmation, 
    update_public_affirmation, 
    delete_public_affirmation
)

def create_public_affirmation(data):
    data = request.json
    add_public_affirmation(data['user'], data['user_id'], data['category'], data['keyword'], data['affirmation_text'])
    return jsonify({'message': 'Public affirmation added successfully'})

def update_public_affirmation(data):
    data = request.json
    affirmation_id = data.get('id')
    if not affirmation_id:
        return jsonify({'message': 'Missing affirmation ID in the request'}), 400

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

def delete_public_affirmation(data):
    data = request.json
    affirmation_id = data.get('id')
    if not affirmation_id:
        return jsonify({'message': 'Missing affirmation ID in the request'}), 400

    result = delete_public_affirmation(affirmation_id)
    return jsonify(result)