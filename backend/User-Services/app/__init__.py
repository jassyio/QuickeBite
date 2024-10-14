from flask import Flask
from .routes import user_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    app.register_blueprint(user_blueprint, url_prefix='/api/users')
    return app
