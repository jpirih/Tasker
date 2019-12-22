from flask import Blueprint

bp = Blueprint(__name__, 'users', url_prefix='/users')

from tasker.users import routes
