from models.nosql_models import no_db, Affirmation as NoSQLAffirmation
from models.sql_models import Affirmations as SQLAffirmation
from bson import ObjectId
from flask import Flask
from mongoengine import disconnect

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'db': 'affirmations', 'host': 'localhost'}
disconnect(alias='default')
no_db.init_app(app)

def nosql_seed_data():
    with app.app_context():
        # Fetch SQL affirmations where is_public is True
        sql_affirmations = SQLAffirmation.query.filter_by(is_public=True).all()

        # Add dummy data to NoSQL database, carrying over necessary fields
        for sql_affirmation in sql_affirmations:
            new_no_sql_affirmation = NoSQLAffirmation(
                user='dilemmaemma',  # My username
                user_id=ObjectId(),  # New ObjectId for each NoSQL affirmation
                affirmation_id=sql_affirmation.affirmation_id,
                **sql_affirmation.__dict__
            )
            new_no_sql_affirmation.save()
            print(f"Added affirmation to NoSQL: {new_no_sql_affirmation}")

if __name__ == "__main__":
    nosql_seed_data()