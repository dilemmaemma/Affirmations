from models.sql_models import db, Affirmations as SQLAffirmation
from sqlalchemy.exc import SQLAlchemyError
from flask import Flask
from bson import ObjectId
import random

def generate_random_16bit_id():
    random_id = random.randint(0, 2**16 - 1)
    hex_string = format(random_id, '04x')
    object_id = ObjectId(hex_string.zfill(24))
    return object_id

def seed_data():
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
        ]
        
        # Add dummy data to database
        for data in dummy_data:
            new_affirmation = SQLAffirmation(
                affirmation_id=generate_random_16bit_id(),
                category=data['category'],
                keyword=data['keyword'],
                is_public=data['is_public'],
                affirmation_text=data['affirmation_text']
            )
            
            try:
                db.session.add(new_affirmation)
                db.session.commit()
                print(f"Added affirmation: {new_affirmation}")
            except SQLAlchemyError as e:
                print(f"Error adding affirmation: {e}")
                db.session.rollback()
                
    if __name__ == "__main__":
        seed_data()