from flask_mongoengine import MongoEngine

no_db = MongoEngine()

# Rough Table Setup
#   user      |   user_id       | affirmation_id  | category | keyword   |                  affirmation_text                     | created at | updated at
# dilemmaemma | <12 bit number> | <24 bit number> | healing  | ego death | I say goodbye to my old self and step into the new me | 2021-05-17 | 2021-05-17

class Affirmation(no_db.Document):
    user = no_db.StringField(max_length=25, default='Guest')
    user_id = no_db.ObjectIdField(required=True)
    affirmation_id = no_db.ObjectIdField(unique=True, required=True)
    category = no_db.StringField(max_length=50, required=True)
    keyword = no_db.StringField(max_length=50, required=True)
    affirmation_text = no_db.StringField(required=True)
    created_at = no_db.DateTimeField(required=True)
    updated_at = no_db.DateTimeField(required=False)