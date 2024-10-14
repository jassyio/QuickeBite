from . import db, bcrypt
from .models import User
from flask_jwt_extended import create_access_token

class UserService:
    def create_user(self, user_data):
        if User.query.filter_by(email=user_data['email']).first():
            return {'error': 'Email already registered'}
        
        new_user = User(
            username=user_data['username'],
            email=user_data['email'],
            password_hash=bcrypt.generate_password_hash(user_data['password']).decode('utf-8')
        )
        db.session.add(new_user)
        db.session.commit()
        return {'id': new_user.id, 'username': new_user.username}

    def authenticate_user(self, credentials):
        user = User.query.filter_by(email=credentials['email']).first()
        if user and bcrypt.check_password_hash(user.password_hash, credentials['password']):
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}
        return {'error': 'Invalid credentials'}

    def get_user_by_id(self, user_id):
        user = User.query.get(user_id)
        return {'id': user.id, 'username': user.username}
    