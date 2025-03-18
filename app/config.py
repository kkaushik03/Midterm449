# app/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://kkaushik:134Drearth****@localhost/midtermdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_jwt_secret_key'  # Change this in production!
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB file size limit