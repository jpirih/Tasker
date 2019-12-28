from flask import Blueprint

bp = Blueprint('posts', __name__)
from tasker.posts import routes
