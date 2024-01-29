from models.sql_models import db, Affirmations as SQLAffirmation
from sqlalchemy.exc import SQLAlchemyError
from seeds.nosql_seed import create_public_affirmation_for_no_sql
from flask import Flask
from bson import ObjectId
import random

def generate_random_24bit_id():
    random_id = random.randint(0, 2**24 - 1)
    hex_string = format(random_id, '06x')
    object_id = ObjectId(hex_string)
    return object_id

def sql_seed_data():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///affirmations.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    with app.app_context():
        # Implement dummy data
        dummy_data = [
            {'category': 'Life', 'keyword': 'Help', 'is_public': False, 'affirmation_text': 'Asking for help is a sign of self-respect and self-awareness'},
            {'category': 'Health', 'keyword': 'Wellness', 'is_public': False, 'affirmation_text': 'I am healthy and safe.'},
            {'category': 'Love', 'keyword': 'Relationships', 'is_public': True, 'affirmation_text': 'I am worthy of and attract love.'},
            {'category': 'Self-Help', 'keyword': 'Self-Improvement', 'is_public': True, 'affirmation_text': 'I alone hold the truth to who I am.'},
            {'category': 'Life', 'keyword': 'Freedom', 'is_public': False, 'affirmation_text': 'I have the freedom to pursue my life as I see fit.'},
            {'category': 'Healing', 'keyword': 'Ego Death','is_public': True, 'affirmation_text': 'I say goodbye to my old self and step into the new me'}
        ]
        
        # Add dummy data to database
        for data in dummy_data:
            affirmation_id = generate_random_24bit_id()  # Generating a 24-bit ID for SQL
            new_affirmation = SQLAffirmation(
                affirmation_id=affirmation_id,
                category=data['category'],
                keyword=data['keyword'],
                is_public=data['is_public'],
                affirmation_text=data['affirmation_text']
            )
            
            try:
                db.session.add(new_affirmation)
                db.session.commit()
                print(f"Added affirmation: {new_affirmation}")
                
                if data['is_public']:
                    # If the affirmation is public, create a corresponding NoSQL document
                    create_public_affirmation_for_no_sql(
                        user='dilemmaemma',
                        user_id=ObjectId(),
                        category=data['category'],
                        keyword=data['keyword'],
                        affirmation_text=data['affirmation_text'],
                        affirmation_id=affirmation_id  # Using the same affirmation_id for NoSQL
                    )
            except SQLAlchemyError as e:
                print(f"Error adding affirmation: {e}")
                db.session.rollback()

if __name__ == "__main__":
    sql_seed_data()
