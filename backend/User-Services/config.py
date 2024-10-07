import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'lewis254')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///users.db')
    SQLALCHEMY_TRACK_MODIFICATION = False
    