import pytest
from app import create_app, db
from app.models import User
from app.services import generate_token, verify_email, reset_password
from flask import json
from datetime import datetime, timedelta

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

# Test email verification
def test_email_verification(client):
    # Register a user
    client.post('/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    })
    
    # Get user from database
    user = User.query.filter_by(email='testuser@example.com').first()
    assert user is not None

    # Verify email token
    token = generate_token(user.email, 'email-confirm')
    verify_response = client.get(f'/verify-email/{token}')
    assert verify_response.status_code == 200

    # Ensure the email_verified field is updated
    user = User.query.filter_by(email='testuser@example.com').first()
    assert user.email_verified == True

def test_invalid_email_verification_token(client):
    # Test invalid email verification token
    invalid_token = "invalid_token"
    verify_response = client.get(f'/verify-email/{invalid_token}')
    assert verify_response.status_code == 400

# Test password reset functionality
def test_password_reset_request(client):
    # Register a user
    client.post('/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    })

    # Request password reset
    reset_response = client.post('/password-reset', json={'email': 'testuser@example.com'})
    assert reset_response.status_code == 200

    # Verify reset token is generated
    user = User.query.filter_by(email='testuser@example.com').first()
    assert user.password_reset_token is not None
    assert user.password_reset_sent_at is not None

def test_password_reset_with_valid_token(client):
    # Register a user
    client.post('/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    })

    # Request password reset
    reset_response = client.post('/password-reset', json={'email': 'testuser@example.com'})
    assert reset_response.status_code == 200

    # Get user from database
    user = User.query.filter_by(email='testuser@example.com').first()

    # Verify reset token
    token = user.password_reset_token
    new_password = "newpassword456"
    reset_password_response = client.post(f'/reset-password/{token}', json={'new_password': new_password})
    assert reset_password_response.status_code == 200

    # Verify the password is updated
    user = User.query.filter_by(email='testuser@example.com').first()
    assert user is not None
    assert user.password_reset_token is None  # Reset token should be cleared
    assert user.password_reset_sent_at is None  # Reset time should be cleared

def test_invalid_password_reset_token(client):
    # Test invalid password reset token
    invalid_token = "invalid_token"
    reset_response = client.post(f'/reset-password/{invalid_token}', json={'new_password': 'newpassword123'})
    assert reset_response.status_code == 400

def test_expired_password_reset_token(client, mocker):
    # Register a user
    client.post('/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    })

    # Request password reset
    client.post('/password-reset', json={'email': 'testuser@example.com'})

    # Get user from database
    user = User.query.filter_by(email='testuser@example.com').first()

    # Manually set the password_reset_sent_at to a time in the past to simulate an expired token
    expired_time = datetime.utcnow() - timedelta(hours=2)
    mocker.patch.object(User, 'password_reset_sent_at', new_callable=mocker.PropertyMock, return_value=expired_time)

    # Attempt to reset password with expired token
    reset_password_response = client.post(f'/reset-password/{user.password_reset_token}', json={'new_password': 'newpassword123'})
    assert reset_password_response.status_code == 400