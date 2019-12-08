from flask import Blueprint

bp = Blueprint('main', __name__)

from tasker.main import routes
