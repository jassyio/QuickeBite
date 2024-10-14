from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, db
import jwt
import datetime

def create_user(data):
    hashed_password = generate_password_hash(data['password'])
    user = User(name=data['name'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password_hash(user.password, data['password']):
        token = jwt.encode({'user_id': user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, 'secret', algorithm='HS256')
        return token
    return None
