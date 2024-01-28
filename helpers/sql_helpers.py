from models.sql_models import db, Affirmations

def get_affirmations():
    return Affirmations.query.all()

def get_affirmations_by_category(category):
    return Affirmations.query.filter_by(category=category).first()

def get_affirmations_by_keyword(keyword):
    return Affirmations.query.filter_by(keyword=keyword).first()

def get_affirmations_by_id(affirmation_id):
    return Affirmations.query.get(affirmation_id)

def add_affirmation(category, keyword, is_public, affirmation_text):
    new_affirmation = Affirmations(
        category=category,
        keyword=keyword,
        is_public=is_public,
        affirmation_text=affirmation_text
    )

    db.session.add(new_affirmation)
    db.session.commit()

def update_affirmation(affirmation_id, category, keyword, is_public, affirmation_text):
    affirmation = get_affirmations_by_id(affirmation_id)
    if affirmation:
        affirmation.category = category
        affirmation.keyword = keyword
        affirmation.is_public = is_public
        affirmation.affirmation_text = affirmation_text
        db.session.commit()
        return affirmation
    else:
        return None

def delete_affirmation(affirmation_id):
    affirmation = get_affirmations_by_id(affirmation_id)
    if affirmation:
        db.session.delete(affirmation)
        db.session.commit()
