from flask import Flask
from models.sql_models import db as sql_db
from models.nosql_models import no_db
from seeds.sql_seed import sql_seed_data
from seeds.nosql_seed import nosql_seed_data
from routes import private_routes_bp, public_routes_bp, dev_tools_bp
from config import DATABASE_URI, NODB_NAME, MONGO_URI
import mongoengine

app = Flask(__name__)

# Configure SQL database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQL database
sql_db.init_app(app)

# Initialize NoSQL database
no_db.init_app(app)

# Use the application context
with app.app_context():
    # Seed SQL data
    sql_seed_data(app)

# Configure NoSQL database
app.config['MONGODB_SETTINGS'] = {
    'db': NODB_NAME,
    'host': MONGO_URI,
}

# Use the application context for NoSQL seeding
with app.app_context():
    # Seed NoSQL data
    nosql_seed_data(app)

# Register Blueprints
app.register_blueprint(private_routes_bp)
app.register_blueprint(public_routes_bp)
app.register_blueprint(dev_tools_bp)

if __name__ == '__main__':
    app.run(debug=True)