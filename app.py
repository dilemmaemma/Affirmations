from flask import Flask, request, jsonify
from models.nosql_models import db, Affirmation
from helpers.nosql_helpers import get_public_affirmations, add_public_affirmation, update_public_affirmation, delete_public_affirmation, get_public_affirmations_by_category, get_public_affirmations_by_keyword, get_public_affirmations_by_category_and_keyword, get_public_affirmations_by_id

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'affirmations',
    'host': 'localhost'
}

db.init_app(app)

@app.route('/affirmations', methods=['GET'])
def affirmations():
    return jsonify({'message': 'This is the get route for affirmations'})

@app.route('/affirmations', methods=['POST'])
def affirmations_post():
    return jsonify({'message': 'This is the post route for affirmations'})

@app.route('/affirmations', methods=['PUT'])  # Might change to patch
def affirmations_put():
    return jsonify({'message': 'This is the put route for affirmations'})

@app.route('/affirmations', methods=['DELETE'])
def affirmations_delete():
    return jsonify({'message': 'This is the delete route for affirmations'})

@app.route('/affirmations/<category>', methods=['GET'])
def affirmations_category(category):
    return jsonify({'message': f'This is the get route for the affirmations {category} category'})

@app.route('/affirmations/<keyword>', methods=['GET'])
def affirmations_keyword(keyword):
    return jsonify({'message': f'This is the get route for the affirmations {keyword} keyword'})

@app.route('/affirmations/<category>/<keyword>', methods=['GET'])
def affirmations_category_keyword(category, keyword):
    return jsonify({'message': f'This is the get route for the affirmations {category} category and {keyword} keyword'})

@app.route('/affirmations/public', methods=['GET'])
def affirmations_public():
    affirmations = get_public_affirmations()
    return jsonify(affirmations)

@app.route('/affirmations/public', methods=['POST'])  # Used only if the user selects to have their affirmation uploaded publicly
def affirmations_public_post():
    data = request.json
    add_public_affirmation(data['user'], data['user_id'], data['category'], data['keyword'], data['affirmation_text'])

@app.route('/affirmations/public', methods=['PUT'])  # Might change to patch
def affirmations_public_put():
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

@app.route('/affirmations/public', methods=['DELETE'])
def affirmations_public_delete():
    data = request.json
    affirmation_id = data.get('id')
    if not affirmation_id:
        return jsonify({'message': 'Missing affirmation ID in the request'}), 400

    result = delete_public_affirmation(affirmation_id)
    return jsonify(result)

@app.route('/affirmations/public/<category>', methods=['GET'])
def affirmations_public_category(category):
    affirmations = get_public_affirmations_by_category(category)
    return jsonify(affirmations)

@app.route('/affirmations/public/<keyword>', methods=['GET'])
def affirmations_public_keyword(keyword):
    affirmations = get_public_affirmations_by_keyword(keyword)
    return jsonify(affirmations)

@app.route('/affirmations/public/<category>/<keyword>', methods=['GET'])
def affirmations_public_category_keyword(category, keyword):
    affirmations = get_public_affirmations_by_category_and_keyword(category, keyword)
    return jsonify(affirmations)

if __name__ == '__main__':
    app.run(debug=True)