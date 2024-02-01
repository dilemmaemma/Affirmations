from flask import Flask
from routes import private_routes_bp, public_routes_bp
from models.sql_models import db
from models.nosql_models import no_db
from seeds.sql_seed import sql_seed_data
from seeds.nosql_seed import nosql_seed_data

app = Flask(__name__)

# Configure SQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///affirmations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Configure NoSQL database
app.config['MONGODB_SETTINGS'] = {
    'db': 'Affirmation',
    'host': 'localhost'
}

# Initialize SQL database
db.init_app(app)

# Use the application context
with app.app_context():
    # Create the SQL database tables
    db.create_all()
    # Seed SQL data

# Initialize NoSQL database
no_db.init_app(app)

# Use the application context for NoSQL seeding
with app.app_context():
    # Seed NoSQL data
    nosql_seed_data()

# Register Blueprints
app.register_blueprint(private_routes_bp)
app.register_blueprint(public_routes_bp)

if __name__ == '__main__':
    app.run(debug=True)