from flask import Flask
from app.routes import delivery_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Register Blueprints
    app.register_blueprint(delivery_blueprint, url_prefix='/deliveries')
    
    return app
