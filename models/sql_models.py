from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Rough Table Setup
#   id  | category | affirmation_id  | keyword   | is_public |                  affirmation_text                    | created at | updated at
#   1   | healing  | <24 bit number> |ego death |   False   | I say goodbye to my old self and step into the new me | 2021-05-17 | 2021-05-17

class Affirmations(db.Model):
    __tablename__ = 'Affirmations'
    
    id = db.Column(db.Integer, primary_key=True)
    affirmation_id = db.Column(db.String(24), unique=True, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    keyword = db.Column(db.String(50), nullable=False)
    is_public = db.Column(db.Boolean, default=False)
    affirmation_text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=True)
    
def __repr__(self):
        return f"<Affirmation(category='{self.category}', keyword='{self.keyword}', is_public={self.is_public}, affirmation_text='{self.affirmation_text}', created_at={self.created_at})>"