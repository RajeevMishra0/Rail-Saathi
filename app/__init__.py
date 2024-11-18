# Flask app initialization
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
csrf = CSRFProtect()
# Initialize the Migrate extension
migrate = Migrate()

def create_app():
    """Factory function to create and configure the Flask app."""
    # app = Flask(__name__)
    
    # Base directory for SQLite or other paths
    basedir = os.path.abspath(os.path.dirname(__file__)) # Get the absolute path to the current directory
    # Initialize the Flask app with template folder and configurations
    app = Flask(__name__, template_folder=os.path.join(basedir, 'templates'))
    # App configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', f"sqlite:///{os.path.join(basedir, 'railsaathi.db')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')
    
    # Initialize extensions with the app instance
    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)  # Add this line to link the Migrate extension
    
    # Import routes (if needed) or register blueprints here
    # Register blueprints (routes will be modularized in separate files)
    from app.routes import all_blueprints  # Assuming `all_blueprints` is a list of all blueprints 
    # Import blueprints from routes.py
    for blueprint in all_blueprints:
        app.register_blueprint(blueprint)
    
    with app.app_context():
        # Import models to ensure they are registered with SQLAlchemy
        from app import models
        
        # Optional: Create the database if using SQLite
        # db.create_all()
        # Ensure migrations handle schema creation
        pass

    return app

# You can keep any other imports here if needed, but routes are now in app.py