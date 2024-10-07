import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'lewis@uon')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///deliveries.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False