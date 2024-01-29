from models.nosql_models import no_db, Affirmation as NoSQLAffirmation
from models.sql_models import Affirmations as SQLAffirmation
from bson import ObjectId
from flask import Flask

def nosql_seed_data():
    app = Flask(__name__)
    app.config['MONGODB_SETTINGS'] = {'db': 'affirmations', 'host': 'localhost'}
    no_db.init_app(app)

    with app.app_context():
        # Fetch SQL affirmations where is_public is True
        sql_affirmations = SQLAffirmation.query.filter_by(is_public=True).all()

        # Add dummy data to NoSQL database, carrying over necessary fields
        for sql_affirmation in sql_affirmations:
            new_no_sql_affirmation = NoSQLAffirmation(
                user='dilemmaemma',  # My username
                user_id=ObjectId(),  # New ObjectId for each NoSQL affirmation
                affirmation_id=sql_affirmation.affirmation_id,
                category=sql_affirmation.category,
                keyword=sql_affirmation.keyword,
                affirmation_text=sql_affirmation.affirmation_text,
                is_public=sql_affirmation.is_public,
                created_at=sql_affirmation.created_at,
                updated_at=sql_affirmation.updated_at # Only gets implemented when we update public SQL affirmations
            )
            new_no_sql_affirmation.save()
            print(f"Added affirmation to NoSQL: {new_no_sql_affirmation}")

if __name__ == "__main__":
    nosql_seed_data()
