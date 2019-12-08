from flask import Flask
from config import BaseConfig
from tasker.main import bp as main_bp
from tasker.errors import bp as errors_bp


def create_app(config=BaseConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(main_bp)
    app.register_blueprint(errors_bp)
    return app

