from flask_mongoengine import MongoEngine

db = MongoEngine()

# Rough Table Setup
#   user      |   user_id       | affirmation_id  | category | keyword   |                  affirmation_text
# dilemmaemma | <12 bit number> | <12 bit number> | healing  | ego death | I say goodbye to my old self and step into the new me

class Affirmation(db.Document):
    user = db.StringField(max_length=25, default='Guest')
    user_id = db.ObjectIdField
    affirmation_id = db.ObjectIdField(unique=True)
    category = db.StringField(max_length=50, required=True)
    keyword = db.StringField(max_length=50, required=True)
    affirmation_text = db.StringField(required=True)