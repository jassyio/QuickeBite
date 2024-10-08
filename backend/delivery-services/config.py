import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'lewis@uon')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://root@localhost:3307/delivery_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False