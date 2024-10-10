from flask import Flask
from app.routes import delivery_blueprint
from database.mysql.init_mysql import migrate, db


def create_app():
    app = Flask(__name__)
    app.config.from_object('Config')

    db.init_app(app)

    migrate.init__app(app, db)
    
    # Register Blueprints
    app.register_blueprint(delivery_blueprint, url_prefix='/deliveries')
    
    return app
