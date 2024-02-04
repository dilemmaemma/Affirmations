from models.nosql_models import no_db, Affirmation as NoSQLAffirmation
from models.sql_models import Affirmations as SQLAffirmation
from bson import ObjectId
from flask import Flask
from config import MONGO_URI, NODB_NAME

def nosql_seed_data(app):
    app.config['MONGODB_SETTINGS'] = {
        'db': NODB_NAME, 
        'host': MONGO_URI
    }

    # Connect to MongoDB outside of the app context
    with app.app_context():
        # Fetch SQL affirmations where is_public is True
        sql_affirmations = SQLAffirmation.query.filter_by(is_public=True).all()

        # Add dummy data to NoSQL database, carrying over necessary fields
        for sql_affirmation in sql_affirmations:
            # Specify the fields you want to copy
            fields_to_copy = ['category', 'keyword', 'affirmation_text', 'created_at', 'updated_at']

            # Create a dictionary containing the selected fields
            no_sql_data = {field: getattr(sql_affirmation, field) for field in fields_to_copy}

            # Generate a new ObjectId for the affirmation_id
            no_sql_data['affirmation_id'] = str(ObjectId())

            try:
                # Create a new NoSQLAffirmation instance using the selected fields
                new_no_sql_affirmation = NoSQLAffirmation(
                    user='dilemmaemma',  # My username
                    user_id=str(ObjectId()),  # New ObjectId for each NoSQL affirmation
                    **no_sql_data
                )

                new_no_sql_affirmation.save()
                print(f"Added affirmation to NoSQL: {new_no_sql_affirmation}")
            except Exception as e:
                print(f"Error handling affirmation: {e}")

if __name__ == "__main__":
    app = Flask(__name__)
    nosql_seed_data(app)