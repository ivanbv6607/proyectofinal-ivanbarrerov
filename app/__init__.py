from flask import Flask
from app.config.db import db
from app.config.config import Config
from app.config.routes import register_routes
from app.config.auth import login_manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

def create_app(Config):
        app = Flask(__name__, template_folder="views")
        app.config.from_object(Config)

        db = SQLAlchemy(app)
        migrate = Migrate(app, db)
        login_manager.init_app(app)
        register_routes(app)

# Setup console logging
        if not app.debug:
                stream_handler = logging.StreamHandler()
                stream_handler.setLevel(logging.INFO)
                app.logger.addHandler(stream_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info('Flask App startup')

"""def create_app(config):
        app = Flask(__name__, template_folder="views")
        app.config.from_object(Config)
        
        db.init_app(app)
        migrate = Migrate(app, db)
        login_manager.init_app(app)
        register_routes(app)

        with app.app_context():
                db.create_all()

        return app  """
        
