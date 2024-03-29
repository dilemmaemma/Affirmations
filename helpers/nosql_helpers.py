from models.nosql_models import Affirmation
from bson import ObjectId
from config import COLLECTION

def get_public_affirmations(collection_name=COLLECTION):
    return Affirmation.objects.using(collection_name)

def get_public_affirmations_by_category(category):
    return Affirmation.objects(category=category)

def get_public_affirmations_by_keyword(keyword):
    return Affirmation.objects(keyword=keyword)

def get_public_affirmations_by_id(affirmation_id):
    return Affirmation.objects(affirmation_id=ObjectId(affirmation_id))

def get_public_affirmations_by_category_and_keyword(category, keyword):
    return Affirmation.objects(category=category, keyword=keyword)

def add_public_affirmation(user, user_id, category, keyword, affirmation_id, affirmation_text):
    new_affirmation = Affirmation(
        user=user,
        user_id=user_id,
        affirmation_id=affirmation_id,
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