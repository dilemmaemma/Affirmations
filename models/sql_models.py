from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Rough Table Setup
#   id  | category | affirmation_id  | keyword   | is_public |                  affirmation_text
#   1   | healing  | <24 bit number> |ego death |   False   | I say goodbye to my old self and step into the new me

class Affirmations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    affirmation_id = db.ObjectIdField(unique=True)
    category = db.Column(db.String(50), nullable=False)
    keyword = db.Column(db.String(50), nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    affirmation_text = db.Column(db.Text, nullable=False)
    
def __repr__(self):
    return f"<Affirmation(category='{self.category}', keyword='{self.keyword}', is_public={self.is_public}, affirmation_text='{self.affirmation_text}')>"