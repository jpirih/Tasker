from flask import Blueprint

bp = Blueprint('users', __name__, url_prefix='/users')

from tasker.users import routes
