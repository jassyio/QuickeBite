import pytest
from app import create_app, db
from app.models import User
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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
        
def test_register_user(client):
    response = client.post('/register', data=json.dumps({
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }), headers={'Content-Type': 'application/json'})
    
    # Check if registration succeeded (should be 201)
    assert response.status_code == 201 or response.status_code == 400, f"Unexpected status code: {response.status_code}, response data: {response.data}"

    # Verify user is in the database
    with client.application.app_context():
        user = User.query.filter_by(username='testuser').first()
        assert user.email == 'testuser@example.com'

def test_register_duplicate_user(client):
    client.post('/register', data=json.dumps({
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }), headers={'Content-Type': 'application/json'})

    response = client.post('/register', data=json.dumps({
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }), headers={'Content-Type': 'application/json'})
    
    assert response.status_code == 400
    assert b'User registration failed' in response.data

def test_login_user(client):
    client.post('/register', data=json.dumps({
        'username': 'testuser',
        'email': 'testuser@example.com',
        'password': 'testpassword'
    }), headers={'Content-Type': 'application/json'})

    response = client.post('/login', data=json.dumps({
        'username': 'testuser',
        'password': 'testpassword'
    }), headers={'Content-Type': 'application/json'})

    assert response.status_code == 200
    assert b'Logged in successfully' in response.data
    assert b'access_token' in response.data

def test_login_invalid_credentials(client):
    response = client.post('/login', data=json.dumps({
        'username': 'testuser',
        'password': 'invalid'
    }), headers={'Content-Type': 'application/json'})

    assert response.status_code == 401
    assert b'Invalid credentials' in response.data