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

    assert response.status_code == 201
    assert b'User registered successfully' in response.data

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
    assert b'Username already exists' in response.data

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