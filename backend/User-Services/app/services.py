from .models import User
from . import db, bcrypt
from sqlalchemy.exc import IntegrityError
from .utils import generate_token, send_email, verify_token
from datetime import datetime
from flask import current_app

def create_user(username, email, password):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    try:
        user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        return user.id
    
    # this ensures the db remain consistent state and prevent any partial update
    except IntegrityError:
        db.session.rollback()
        return None
    
"""
    This function attempts to authenticate a user by querying the database for a user with the provided email.
    If a user is found and the provided password matches the hashed password stored in the database, the user's ID is returned.
    If no user is found or the passwords do not match, the function returns None.
"""

def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user.id
    return None    

def send_verification_email(user):
    token = generate_token(user.email, 'email-confirm')
    verification_link = f"{current_app.config['FRONTEND_URL']}/verify-email/{token}"
    send_email("Verify Your Email", user.email, f"Click the link to verify your email: {verification_link}")

def send_password_reset_email(user):
    token = generate_token(user.email, 'password-reset')
    user.password_reset_token = token
    user.password_reset_sent_at = datetime.utcnow()
    db.session.commit()
    reset_link = f"{current_app.config['FRONTEND_URL']}/reset-password/{token}"
    send_email("Reset Your Password", user.email, f"Click the link to reset your password: {reset_link}")

def reset_password(token, new_password):
    email = verify_token(token, purpose='password-reset')
    if email:
        user = User.query.filter_by(email=email).first()
        if user:
            user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')
            user.password_reset_token = None
            user.password_reset_sent_at = None
            db.session.commit()
            return True
    return False

def verify_email(token):
    email = verify_token(token, purpose='email-confirm')
    if email:
        user = User.query.filter_by(email=email).first()
        if user:
            user.email_verified = True
            db.session.commit()
            return True
    return False