from flask import Flask
from routes import private_routes_bp, public_routes_bp
from models.sql_models import db
from models.nosql_models import no_db

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'db': 'affirmations',
    'host': 'localhost'
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///affirmations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQL database
db.init_app(app)
# Use the application context
with app.app_context():
    # Create the database tables
    db.create_all()

# Initialize NoSQL database
no_db.init_app(app)

# Register Blueprints
app.register_blueprint(private_routes_bp)
app.register_blueprint(public_routes_bp)

if __name__ == '__main__':
    app.run(debug=True)