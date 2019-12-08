from flask import Blueprint

bp = Blueprint('errors', __name__)

from tasker.errors import handlers
