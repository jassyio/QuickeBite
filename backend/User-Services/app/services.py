import jwt
from datetime import datetime, timedelta
from app.models import User, db
from app.utils import hash_password, check_password
from flask import current_app

def create_user(data):
    hashed_password = hash_password(data['password'])
    user = User(name=data['name'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(email, password):
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
    return User.query.filter_by(email=email).first()
