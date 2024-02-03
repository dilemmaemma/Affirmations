from models.sql_models import db, Affirmations as SQLAffirmation
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from datetime import datetime
import random
import uuid

def generate_random_24bit_id():
    # Generate a random 24-bit ID
    random_id = random.randint(0, 2**24 - 1)

    # Convert the 24-bit ID to a 6-character hex string
    hex_string = format(random_id, '06x')

    # Generate a UUID from the hex string
    unique_id = uuid.UUID(hex_string.zfill(32))

    return str(unique_id)

def sql_seed_data(app):
    app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///affirmations.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
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
                affirmation_text=data['affirmation_text'],
                created_at=datetime.utcnow()
            )
            
            try:
                db.session.add(new_affirmation)
                db.session.commit()
                print(f"Added affirmation: {new_affirmation}")
                
            except SQLAlchemyError as e:
                print(f"Error adding affirmation: {e}")
                db.session.rollback()

if __name__ == "__main__":
    app = Flask(__name__)
    sql_seed_data(app)