from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import BaseConfig
from flask_login import LoginManager
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
login = LoginManager(app)
from tasker.models import Post, User, PostsSchema, UsersSchema
from tasker.users import UsersView
user_view = UsersView()
app.add_url_rule('/users/login', 'login', lambda: user_view.login(), methods=['GET', 'POST'])
app.add_url_rule('/users/logout', 'logout', lambda: user_view.logout())
app.add_url_rule('/users/register', 'register', lambda: user_view.register(), methods=['GET', 'POST'])

login.login_view = 'login'
from tasker.errors import ErrorsHandler
from tasker.main import MainView
from tasker.posts import PostsView
from tasker.api import UsersApiView

app.register_error_handler(404, lambda e: ErrorsHandler.page_not_found(e))
MainView.register(app)
PostsView.register(app)
UsersApiView.register(app)

