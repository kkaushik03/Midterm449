'''
config.py
Contains configuration settings for the Flask application.
Includes database connection settings, secret keys, and JWT configurations.
Ensures environment-based configurations can be easily modified.
'''
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://kkaushik:134Drearth****@localhost/midtermdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_jwt_secret_key'  
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  