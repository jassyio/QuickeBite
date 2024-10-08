import jwt
from datetime import datetime, timedelta
from app.models import User, db
from app.utils import hash_password, check_password
from flask import current_app
import logging
from database.redis.init_redis import get_redis_client

logging.basicConfig(level=logging.INFO)
def create_user(data):
    logging.info("Creating user")
    hashed_password = hash_password(data['password'])
    user = User(name=data['name'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(email, password):
    logging.info("Authenticating user")
    user = User.query.filter_by(email=email).first()
    if user and check_password(password, user.password):
        # Generate JWT
        token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(hours=24)
        }, current_app.config['SECRET_KEY'], algorithm='HS256')
        return token
    return None

def get_user_by_email(email):
    logging.info("Getting user by email")
    return User.query.filter_by(email=email).first()

def store_user_session(user_id, token):
    redis_client = get_redis_client()
    redis_client.set(f"user_session:{user_id}", token, ex=current_app.config['JWT_EXPIRATION_DELTA'])

def get_user_session(user_id):
    redis_client = get_redis_client()
    token = redis_client.get(f"user_session:{user_id}")
    return token.decode() if token else None