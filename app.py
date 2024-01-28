from flask import Flask, request, jsonify
from models.sql_models import db, Affirmation
from models.nosql_models import no_db, Affirmation
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
from helpers.nosql_helpers import (
    get_public_affirmations, 
    add_public_affirmation, 
    update_public_affirmation, 
    delete_public_affirmation, 
    get_public_affirmations_by_category, 
    get_public_affirmations_by_keyword, 
    get_public_affirmations_by_category_and_keyword, 
    get_public_affirmations_by_id)

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'affirmations',
    'host': 'localhost'
}
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///affirmations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQL database
db.init_app(app)

# Initialize NoSQL database
no_db.init_app(app)

# Routes

# Private Routes
@app.route('/affirmations', methods=['GET'])
def get_all_affirmations():
    affirmations = get_affirmations()
    return jsonify(affirmations)

@app.route('/affirmations/<int:affirmation_id>', methods=['GET'])
def get_single_affirmation(affirmation_id):
    affirmation = get_affirmation_by_id(affirmation_id)
    if affirmation:
        return jsonify(affirmation)
    return jsonify({'message': 'Affirmation not found'}), 404

@app.route('/affirmations', methods=['POST'])
def create_affirmation():
    data = request.json
    add_affirmation(data['category'], data['keyword'], data['is_public'], data['affirmation_text'])
    if data['is_public']:
        add_public_affirmation(data['user'], data['user_id'], data['category'], data['keyword'], data['affirmation_text']) # Create a way to pull user and id from profile
    return jsonify({'message': 'Affirmation added successfully'}), 201

def update_affirmation(affirmation_id):
    data = request.json
    update_affirmation(data['affirmation_id'], data['category'], data['keyword'], data['is_public'], data['affirmation_text'])
    if data['is_public'] and affirmation_id == data['affirmation_id']:
        update_public_affirmation(data['affirmation_id'], data['user'], data['user_id'], data['category'], data['keyword'], data['affirmation_text']) # Create a way to pull user and id from profile
    return jsonify({'message': 'Affirmation updated successfully'})

@app.route('/affirmations', methods=['DELETE'])
def delete_affirmation(affirmation_id):
    data = request.json
    delete_affirmation(affirmation_id)
    if data['is_public'] and affirmation_id == data['affirmation_id']:
        delete_public_affirmation(affirmation_id)
    return jsonify({'message': 'Affirmation deleted successfully'})

@app.route('/affirmations/category:<category>', methods=['GET'])
def get_affirmations_from_category(category):
    affirmations = get_affirmation_by_category(category)
    return jsonify(affirmations)

@app.route('/affirmations/keyword:<keyword>', methods=['GET'])
def get_affirmations_from_keyword(keyword):
    affirmations = get_affirmation_by_keyword(keyword)
    return jsonify(affirmations)

@app.route('/affirmations/category:<category>/keyword:<keyword>', methods=['GET'])
def get_affirmations_from_category_and_keyword(category, keyword):
    affirmations = get_affirmation_by_category_and_keyword(category, keyword)
    return jsonify(affirmations)

# Public Routes
@app.route('/affirmations/public', methods=['GET'])
def get_all_public_affirmations():
    affirmations = get_public_affirmations()
    return jsonify(affirmations)

@app.route('/affirmations/public/<int:affirmation_id>', methods=['GET'])
def get_single_public_affirmation(affirmation_id):
    affirmation = get_public_affirmations_by_id(affirmation_id)
    if affirmation:
        return jsonify(affirmation)
    return jsonify({'message': 'Affirmation not found'}), 404

@app.route('/affirmations/public', methods=['POST'])  # Used only if the user selects to have their affirmation uploaded publicly
def create_public_affirmation():
    data = request.json
    add_public_affirmation(data['user'], data['user_id'], data['category'], data['keyword'], data['affirmation_text'])

@app.route('/affirmations/public', methods=['PUT']) # Used only if the user selects to have their affirmation uploaded publicly
def update_public_affirmation():
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

@app.route('/affirmations/public', methods=['DELETE']) # Used only if the user selects to have their affirmation uploaded publicly
def delete_public_affirmation():
    data = request.json
    affirmation_id = data.get('id')
    if not affirmation_id:
        return jsonify({'message': 'Missing affirmation ID in the request'}), 400

    result = delete_public_affirmation(affirmation_id)
    return jsonify(result)

@app.route('/affirmations/public/category:<category>', methods=['GET'])
def get_public_affirmations_from_category(category):
    affirmations = get_public_affirmations_by_category(category)
    return jsonify(affirmations)

@app.route('/affirmations/public/keyword:<keyword>', methods=['GET'])
def get_public_affirmations_from_keyword(keyword):
    affirmations = get_public_affirmations_by_keyword(keyword)
    return jsonify(affirmations)

@app.route('/affirmations/public/category:<category>/keyword:<keyword>', methods=['GET'])
def get_public_affirmations_from_category_and_keyword(category, keyword):
    affirmations = get_public_affirmations_by_category_and_keyword(category, keyword)
    return jsonify(affirmations)

if __name__ == '__main__':
    app.run(debug=True)