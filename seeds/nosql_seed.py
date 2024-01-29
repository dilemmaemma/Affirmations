from models.nosql_models import no_db, Affirmation as NoSQLAffirmation
from bson import ObjectId
from flask import Flask

def create_public_affirmation_for_no_sql(user, user_id, category, keyword, affirmation_text, affirmation_id):
    new_affirmation = NoSQLAffirmation(
        user=user,
        user_id=user_id,
        affirmation_id=affirmation_id,
        category=category,
        keyword=keyword,
        affirmation_text=affirmation_text
    )
    new_affirmation.save()
    print(f"Added affirmation: {new_affirmation}")

def nosql_seed_data():
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {'db': 'affirmations', 'host': 'localhost'}
    no_db.init_app(app)
    
    with app.app_context():
        # Implement dummy data
        dummy_data = [
            {'user': 'dilemmaemma', 'user_id': ObjectId(), 'category': 'Love', 'keyword': 'Relationships', 'affirmation_text': 'I am worthy of and attract love.'},
            {'user': 'dilemmaemma', 'user_id': ObjectId(), 'category': 'Self-Help', 'keyword': 'Self-Improvement', 'affirmation_text': 'I alone hold the truth to who I am.'},
            {'user': 'dilemmaemma', 'user_id': ObjectId(), 'category': 'Healing', 'keyword': 'Ego Death', 'affirmation_text': 'I say goodbye to my old self and step into the new me'}
        ]
        
        # Add dummy data to the database
        for data in dummy_data:
            new_affirmation = NoSQLAffirmation(
                user=data['user'],
                user_id=data['user_id'],
                category=data['category'],
                keyword=data['keyword'],
                affirmation_text=data['affirmation_text']
            )
            new_affirmation.save()
            print(f"Added affirmation: {new_affirmation}")

if __name__ == "__main__":
    nosql_seed_data()
