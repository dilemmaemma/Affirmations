from flask import jsonify, Blueprint
from helpers.nosql_helpers import (
    get_public_affirmations, 
    get_public_affirmations_by_category, 
    get_public_affirmations_by_keyword, 
    get_public_affirmations_by_category_and_keyword, 
    get_public_affirmations_by_id
)
from config import COLLECTION

public_routes_bp = Blueprint('public_routes', __name__)

def serialize_public_affirmation(affirmation):
    return {
        'user': affirmation.user,
        'user_id': affirmation.user_id,
        'affirmation_id': str(affirmation.id),
        'category': affirmation.category,
        'keyword': affirmation.keyword,
        'affirmation_text': affirmation.affirmation_text,
        'created_at': affirmation.created_at.isoformat(),
        'updated_at': affirmation.updated_at.isoformat() if affirmation.updated_at else None
    }

@public_routes_bp.route('/affirmations/public', methods=['GET'])
def get_all_public_affirmations():
    affirmations = get_public_affirmations(collection_name=COLLECTION)
    serialized_affirmations = [serialize_public_affirmation(affirmation) for affirmation in affirmations]
    return jsonify(serialized_affirmations)

@public_routes_bp.route('/affirmations/public/<int:affirmation_id>', methods=['GET'])
def get_single_public_affirmation(affirmation_id):
    affirmation = get_public_affirmations_by_id(affirmation_id)
    if affirmation:
        return jsonify(serialize_public_affirmation(affirmation))
    return jsonify({'message': 'Affirmation not found'}), 404

@public_routes_bp.route('/affirmations/public/category:<category>', methods=['GET'])
def get_public_affirmations_from_category(category):
    affirmations = get_public_affirmations_by_category(category)
    serialized_affirmations = [serialize_public_affirmation(affirmation) for affirmation in affirmations]
    return jsonify(serialized_affirmations)

@public_routes_bp.route('/affirmations/public/keyword:<keyword>', methods=['GET'])
def get_public_affirmations_from_keyword(keyword):
    affirmations = get_public_affirmations_by_keyword(keyword)
    serialized_affirmations = [serialize_public_affirmation(affirmation) for affirmation in affirmations]
    return jsonify(serialized_affirmations)

@public_routes_bp.route('/affirmations/public/category:<category>/keyword:<keyword>', methods=['GET'])
def get_public_affirmations_from_category_and_keyword(category, keyword):
    affirmations = get_public_affirmations_by_category_and_keyword(category, keyword)
    serialized_affirmations = [serialize_public_affirmation(affirmation) for affirmation in affirmations]
    return jsonify(serialized_affirmations)