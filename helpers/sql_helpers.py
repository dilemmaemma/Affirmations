from models.sql_models import db, Affirmations
from sqlalchemy.exc import SQLAlchemyError
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

def get_affirmations():
    return Affirmations.query.all()

def get_affirmation_by_category(category):
    return Affirmations.query.filter_by(category=category)

def get_affirmation_by_keyword(keyword):
    return Affirmations.query.filter_by(keyword=keyword)

def get_affirmation_by_category_and_keyword(category, keyword):
    return Affirmations.query.filter_by(category=category, keyword=keyword)

def get_affirmation_by_id(affirmation_id):
    return Affirmations.query.get(affirmation_id)

def add_affirmation(category, keyword, is_public, affirmation_text):
    new_affirmation = Affirmations(
        affirmation_id=generate_random_24bit_id(),
        category=category,
        keyword=keyword,
        is_public=is_public,
        affirmation_text=affirmation_text
    )

    try:
        db.session.add(new_affirmation)
        db.session.commit()
    except SQLAlchemyError as e:
        print(f"Error adding affirmation: {e}")
        db.session.rollback()

def update_affirmation(affirmation_id, category, keyword, is_public, affirmation_text):
    affirmation = get_affirmation_by_id(affirmation_id)
    if affirmation:
        try:
            affirmation.category = category
            affirmation.keyword = keyword
            affirmation.is_public = is_public
            affirmation.affirmation_text = affirmation_text
            db.session.commit()
            return affirmation
        except SQLAlchemyError as e:
            print(f"Error updating affirmation: {e}")
            db.session.rollback()
    else:
        return None

def delete_affirmation(affirmation_id):
    affirmation = get_affirmation_by_id(affirmation_id)
    if affirmation:
        try:
            db.session.delete(affirmation)
            db.session.commit()
        except SQLAlchemyError as e:
            print(f"Error deleting affirmation: {e}")
            db.session.rollback()
