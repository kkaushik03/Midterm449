# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)

    # Create uploads folder if it doesn't exist
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Import and register blueprints
    from app.auth import auth_bp
    from app.items import items_bp
    from app.file_routes import file_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(items_bp)
    app.register_blueprint(file_bp)

    # A public route can be registered here or in its own blueprint
    @app.route('/')
    def home():
        return "Welcome to the API. Use /login for authentication and /public/items for public information."

    # Create database tables (or use migrations for production)
    with app.app_context():
        db.create_all()

    return app