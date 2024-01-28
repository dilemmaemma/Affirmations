from models.nosql_models import Affirmation
from bson import ObjectId
import random

def generate_random_16bit_id():
    random_id = random.randint(0, 2**16 - 1)
    hex_string = format(random_id, '04x')
    object_id = ObjectId(hex_string.zfill(24))
    return object_id

def get_public_affirmations():
    return Affirmation.objects()

def get_public_affirmations_by_category(category):
    return Affirmation.objects(category=category)

def get_public_affirmations_by_keyword(keyword):
    return Affirmation.objects(keyword=keyword)

def get_public_affirmations_by_id(affirmation_id):
    return Affirmation.objects(affirmation_id=ObjectId(affirmation_id))

def get_public_affirmations_by_category_and_keyword(category, keyword):
    return Affirmation.objects(category=category, keyword=keyword)

def add_public_affirmation(user, user_id, category, keyword, affirmation_text):
    new_affirmation = Affirmation(
        user=user,
        user_id=user_id,
        affirmation_id=generate_random_16bit_id(),
        category=category,
        keyword=keyword,
        affirmation_text=affirmation_text
    )
    new_affirmation.save()
    
def update_public_affirmation(affirmation_id, category, keyword, affirmation_text):
    affirmation = get_public_affirmations_by_id(affirmation_id)
    if affirmation:
        affirmation.category = category
        affirmation.keyword = keyword
        affirmation.affirmation_text = affirmation_text
        try:
            affirmation.save()
            return affirmation
        except Exception as e:
            # Handle save error (e.g., validation error)
            print(f"Error updating affirmation: {e}")
            return None
    else:
        return None
    
def delete_public_affirmation(affirmation_id):
    affirmation = get_public_affirmations_by_id(affirmation_id)
    if affirmation:
        try:
            affirmation.delete()
            return affirmation
        except Exception as e:
            # Handle delete error
            print(f"Error deleting affirmation: {e}")
            return None
    else:
        return None