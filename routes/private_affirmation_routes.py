from flask import jsonify, request, Blueprint
from bson import ObjectId
from datetime import datetime
from helpers.sql_helpers import (
    get_affirmations,
    get_affirmation_by_category,
    get_affirmation_by_keyword,
    get_affirmation_by_category_and_keyword,
    get_affirmation_by_id,
    add_affirmation,
    update_affirmation,
    delete_affirmation
)
from utils.public_utils import (
    create_public_affirmation,
    update_public_affirmation,
    delete_public_affirmation
)

private_routes_bp = Blueprint('private_routes', __name__)

def serialize_affirmation(affirmation):
    return {
        'id': str(affirmation.id),
        'category': affirmation.category,
        'keyword': affirmation.keyword,
        'is_public': affirmation.is_public,
        'affirmation_text': affirmation.affirmation_text,
        'created_at': affirmation.created_at.isoformat(),
        'updated_at': affirmation.updated_at.isoformat() if affirmation.updated_at else None
    }

@private_routes_bp.route('/affirmations', methods=['GET'])
def get_all_affirmations():
    affirmations = get_affirmations()
    serialized_affirmations = [serialize_affirmation(affirmation) for affirmation in affirmations]
    return jsonify(serialized_affirmations)

@private_routes_bp.route('/affirmations/<int:affirmation_id>', methods=['GET'])
def get_single_affirmation(affirmation_id):
    affirmation = get_affirmation_by_id(affirmation_id)
    if affirmation:
        return jsonify(serialize_affirmation(affirmation))
    return jsonify({'message': 'Affirmation not found'}), 404

@private_routes_bp.route('/affirmations', methods=['POST'])
def create_affirmation():
    data = request.json
    added_affirmation = add_affirmation(
        data['category'],
        data['keyword'],
        data['is_public'],
        data['affirmation_text'],
        created_at=datetime.utcnow()
    )
    if data['is_public']:
        created_public_affirmation = create_public_affirmation(
            data['user'],
            ObjectId(data['user_id']),
            data['affirmation_id'],
            data['category'],
            data['keyword'],
            data['affirmation_text']
        )
    return jsonify({
        'message': 'Affirmation added successfully',
        'affirmation': serialize_affirmation(added_affirmation),
        'public_affirmation': serialize_affirmation(created_public_affirmation) if data['is_public'] else None
    }), 201

@private_routes_bp.route('/affirmations/<int:affirmation_id>', methods=['PUT'])
def update_affirmation_route(affirmation_id):
    data = request.json
    updated_affirmation = update_affirmation(
        affirmation_id,
        data['category'],
        data['keyword'],
        data['is_public'],
        data['affirmation_text'],
        updated_at=datetime.utcnow()
    )
    if data['is_public']:
        updated_public_affirmation = update_public_affirmation(
            data['user'],
            ObjectId(data['user_id']),
            affirmation_id,
            data['category'],
            data['keyword'],
            data['affirmation_text'],
        )
    return jsonify({
        'message': 'Affirmation updated successfully',
        'affirmation': serialize_affirmation(updated_affirmation),
        'public_affirmation': serialize_affirmation(updated_public_affirmation) if data['is_public'] else None
    })

@private_routes_bp.route('/affirmations/<int:affirmation_id>', methods=['DELETE'])
def delete_affirmation_route(affirmation_id):
    deleted_affirmation = delete_affirmation(affirmation_id)
    data = request.json
    if data['is_public']:
        deleted_public_affirmation = delete_public_affirmation(affirmation_id)
    return jsonify({
        'message': 'Affirmation deleted successfully',
        'affirmation': serialize_affirmation(deleted_affirmation),
        'public_affirmation': serialize_affirmation(deleted_public_affirmation) if data['is_public'] else None
    })

@private_routes_bp.route('/affirmations/category:<category>', methods=['GET'])
def get_affirmations_from_category(category):
    affirmations = get_affirmation_by_category(category)
    serialized_affirmations = [serialize_affirmation(affirmation) for affirmation in affirmations]
    return jsonify(serialized_affirmations)

@private_routes_bp.route('/affirmations/keyword:<keyword>', methods=['GET'])
def get_affirmations_from_keyword(keyword):
    affirmations = get_affirmation_by_keyword(keyword)
    serialized_affirmations = [serialize_affirmation(affirmation) for affirmation in affirmations]
    return jsonify(serialized_affirmations)

@private_routes_bp.route('/affirmations/category:<category>/keyword:<keyword>', methods=['GET'])
def get_affirmations_from_category_and_keyword(category, keyword):
    affirmations = get_affirmation_by_category_and_keyword(category, keyword)
    serialized_affirmations = [serialize_affirmation(affirmation) for affirmation in affirmations]
    return jsonify(serialized_affirmations)
