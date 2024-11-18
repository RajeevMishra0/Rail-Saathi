# SQLAlchemy models
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    session_configs = db.relationship('SessionConfig', back_populates='user')  # Relationship to SessionConfig

class Train(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    seats_available = db.Column(db.Integer, nullable=False)

class SessionConfig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(128), unique=True, nullable=False)
    value = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Nullable for global configs
    
    user = db.relationship('User', back_populates='session_configs')  # Bidirectional relationship with User model
    
    def __repr__(self):
        return f"<SessionConfig {self.key}={self.value}>"

# Create the table (or run migrations to create it)
# db.create_all()