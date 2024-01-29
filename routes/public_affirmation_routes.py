from flask import jsonify, Blueprint
from helpers.nosql_helpers import (
    get_public_affirmations, 
    get_public_affirmations_by_category, 
    get_public_affirmations_by_keyword, 
    get_public_affirmations_by_category_and_keyword, 
    get_public_affirmations_by_id)

public_routes_bp = Blueprint('public_routes', __name__)

@public_routes_bp.route('/affirmations/public', methods=['GET'])
def get_all_public_affirmations():
    affirmations = get_public_affirmations()
    return jsonify(affirmations)

@public_routes_bp.route('/affirmations/public/<int:affirmation_id>', methods=['GET'])
def get_single_public_affirmation(affirmation_id):
    affirmation = get_public_affirmations_by_id(affirmation_id)
    if affirmation:
        return jsonify(affirmation)
    return jsonify({'message': 'Affirmation not found'}), 404

@public_routes_bp.route('/affirmations/public/category:<category>', methods=['GET'])
def get_public_affirmations_from_category(category):
    affirmations = get_public_affirmations_by_category(category)
    return jsonify(affirmations)

@public_routes_bp.route('/affirmations/public/keyword:<keyword>', methods=['GET'])
def get_public_affirmations_from_keyword(keyword):
    affirmations = get_public_affirmations_by_keyword(keyword)
    return jsonify(affirmations)

@public_routes_bp.route('/affirmations/public/category:<category>/keyword:<keyword>', methods=['GET'])
def get_public_affirmations_from_category_and_keyword(category, keyword):
    affirmations = get_public_affirmations_by_category_and_keyword(category, keyword)
    return jsonify(affirmations)