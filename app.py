from flask import Flask, jsonify

app = Flask(__name__)

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

@app.route('/affirmations/global', methods=['GET'])
def affirmations_global():
    return jsonify({'message': 'This is the get route for global affirmations'})

@app.route('/affirmations/global', methods=['POST'])  # Used only if the user selects to have their affirmation uploaded publicly
def affirmations_global_post():
    return jsonify({'message': 'This is the post route for global affirmations'})

@app.route('/affirmations/global', methods=['PUT'])  # Might change to patch
def affirmations_global_put():
    return jsonify({'message': 'This is the put route for global affirmations'})

@app.route('/affirmations/global', methods=['DELETE'])
def affirmations_global_delete():
    return jsonify({'message': 'This is the delete route for global affirmations'})

@app.route('/affirmations/<category>', methods=['GET'])
def affirmations_category(category):
    return jsonify({'message': f'This is the get route for the affirmations {category} category'})

@app.route('/affirmations/global/<category>', methods=['GET'])
def affirmations_global_category(category):
    return jsonify({'message': f'This is the get route for the global affirmations {category} category'})

@app.route('/affirmations/<keyword>', methods=['GET'])
def affirmations_keyword(keyword):
    return jsonify({'message': f'This is the get route for the affirmations {keyword} keyword'})

@app.route('/affirmations/global/<keyword>', methods=['GET'])
def affirmations_global_keyword(keyword):
    return jsonify({'message': f'This is the get route for the global affirmations {keyword} keyword'})

@app.route('/affirmations/<category>/<keyword>', methods=['GET'])
def affirmations_category_keyword(category, keyword):
    return jsonify({'message': f'This is the get route for the affirmations {category} category and {keyword} keyword'})

@app.route('/affirmations/global/<category>/<keyword>', methods=['GET'])
def affirmations_global_category_keyword(category, keyword):
    return jsonify({'message': f'This is the get route for the global affirmations {category} category and {keyword} keyword'})

if __name__ == '__main__':
    app.run(debug=True)