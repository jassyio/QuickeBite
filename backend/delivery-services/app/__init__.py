from flask import Flask
from app.routes import delivery_blueprint
from flask_sqlachemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('Config')

    db.init_app(app)

    migrate.init__app(app, db)
    
    # Register Blueprints
    app.register_blueprint(delivery_blueprint, url_prefix='/deliveries')
    
    return app
