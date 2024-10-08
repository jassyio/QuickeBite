from flask import Flask
from app.routes import user_blueprint
from config import Config
from database.mysql.init_mysql import db
from database.redis.init_redis import get_redis_client

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize Database
    db.init_app(app)

    # Initialize Redis
    with app.app_context():
        redis_client = get_redis_client()
        app.redis = redis_client
    
    # Register Blueprints
    app.register_blueprint(user_blueprint, url_prefix='/users')
    
    return app
