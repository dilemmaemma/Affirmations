from models.nosql_models import no_db, Affirmation as NoSQLAffirmation
from models.sql_models import Affirmations as SQLAffirmation
from bson import ObjectId
from flask import Flask
from mongoengine import disconnect

def nosql_seed_data(app):
    with app.app_context():
        # Fetch SQL affirmations where is_public is True
        sql_affirmations = SQLAffirmation.query.filter_by(is_public=True).all()

        # Add dummy data to NoSQL database, carrying over necessary fields
        for sql_affirmation in sql_affirmations:
            # Specify the fields you want to copy
            fields_to_copy = ['category', 'keyword', 'affirmation_text', 'created_at']
            # Create a dictionary containing the selected fields
            no_sql_data = {field: getattr(sql_affirmation, field) for field in fields_to_copy}

            # Generate a new ObjectId for the affirmation_id
            no_sql_data['affirmation_id'] = str(ObjectId())

            # Create a new NoSQLAffirmation instance using the selected fields
            new_no_sql_affirmation = NoSQLAffirmation(
                user='dilemmaemma',  # My username
                user_id=str(ObjectId()),  # New ObjectId for each NoSQL affirmation
                **no_sql_data
            )

            new_no_sql_affirmation.save()
            print(f"Added affirmation to NoSQL: {new_no_sql_affirmation}")

if __name__ == "__main__":
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {'db': 'affirmations', 'host': 'localhost'}
    disconnect(alias='default')
    no_db.init_app(app)
    nosql_seed_data(app)