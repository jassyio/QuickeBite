import pytest
from app import create_app, db
from app.models import User
from unittest.mock import patch
from flask import json

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

# Test email verification failure
@patch('app.utils.send_email')  # Mock the send_email function
def test_email_verification_failure(mock_send_email, client):
    # Simulate email sending failure
    mock_send_email.side_effect = Exception("Email service unavailable")

    # Register a user (which should attempt to send a verification email)
    response = client.post('/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    })
    
    # Ensure the registration still succeeds, but email sending fails
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['message'] == 'User registered successfully. Please verify your email.'

    # Confirm that send_email was called and failed
    assert mock_send_email.called

# Test password reset email failure
@patch('app.utils.send_email')  # Mock the send_email function
def test_password_reset_email_failure(mock_send_email, client):
    # Register a user
    client.post('/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    })

    # Simulate email sending failure
    mock_send_email.side_effect = Exception("Email service unavailable")

    # Request password reset (which should attempt to send an email)
    response = client.post('/password-reset', json={'email': 'testuser@example.com'})
    
    # Ensure the request succeeds (but email failed to send)
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == "If this email is registered, you will receive a password reset link"

    # Confirm that send_email was called and failed
    assert mock_send_email.called

# Test that the system logs email failures
@patch('app.utils.send_email')  # Mock the send_email function
@patch('logging.error')  # Mock the logging function
def test_email_failure_logging(mock_log_error, mock_send_email, client):
    # Simulate email sending failure
    mock_send_email.side_effect = Exception("Email service unavailable")

    # Register a user
    response = client.post('/register', json={
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'password123'
    })
    
    # Ensure that the email failure is logged
    assert mock_log_error.called
    assert "Email service unavailable" in mock_log_error.call_args[0][0]  # Ensure correct error is logged
