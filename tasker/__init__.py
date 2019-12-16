from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import BaseConfig
from tasker.main import bp as main_bp
from tasker.errors import bp as errors_bp

db = SQLAlchemy()
migrate = Migrate()


def create_app(config=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)
    from tasker import models

    app.register_blueprint(main_bp)
    app.register_blueprint(errors_bp)
    return app
