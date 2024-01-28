from flask_mongoengine import MongoEngine

no_db = MongoEngine()

# Rough Table Setup
#   user      |   user_id       | affirmation_id  | category | keyword   |                  affirmation_text
# dilemmaemma | <12 bit number> | <12 bit number> | healing  | ego death | I say goodbye to my old self and step into the new me

class Affirmation(no_db.Document):
    user = no_db.StringField(max_length=25, default='Guest')
    user_id = no_db.ObjectIdField
    affirmation_id = no_db.ObjectIdField(unique=True)
    category = no_db.StringField(max_length=50, required=True)
    keyword = no_db.StringField(max_length=50, required=True)
    affirmation_text = no_db.StringField(required=True)