# from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from flask import current_app
from itsdangerous import URLSafeTimedSerializer
from argon2 import PasswordHasher

# bcrypt = Bcrypt()
ph = PasswordHasher()
mail = Mail()

# def hash_password(password):
#     # return bcrypt.generate_password_hash(password).decode('utf-8')

# def check_password(hashed_password, password):
#     # return bcrypt.check_password_hash(hashed_password, password)

def hash_password(password):
    return ph.hash(password)

def check_password(hashed_password, password):
    try:
        return ph.verify(hashed_password, password)
    except Exception as e:
        print(f'Error verifying password: {e}')
        return False
    
def generate_token(email, purpose):
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return s.dumps({'email': email, 'purpose': purpose})

def verify_token(token, expiration=3600, purpose='email-confirm'):
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        email, purpose_received = s.loads(token, max_age=expiration)
        if purpose == purpose_received:
            return email
        else:
            return None
    except Exception as e:
        print(f'Error verifying token: {e}')
        return None

def send_email(subject, recipients, body):
    msg = Message(subject, recipients=recipients)
    msg.body = body
    mail.send(msg)