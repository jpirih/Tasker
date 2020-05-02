import unittest
from tasker import app, db
from config import TestConfig
from tasker.data_seeder import UsersSeeder, PostsSeeder


class BaseTestCase(unittest.TestCase):
    """Base tests configuration"""
    app.config.from_object(TestConfig)
    client = app.test_client()
    app_context = app.app_context()
    app_context.push()
    user_seeder = UsersSeeder()
    posts_seeder = PostsSeeder()

    def setUp(self) -> None:
        db.create_all()

    def tearDown(self) -> None:
        self.logout_user()
        db.session.remove()
        db.drop_all()

    # helper functions
    def login_user(self, username: str, password: str):
        login_data = dict(username=username, password=password)
        return self.client.post('/users/login', data=login_data, follow_redirects=True)

    def logout_user(self):
        return self.client.get('users/logout', follow_redirects=True)

    def register_user(self, username: str, email: str, password: str, password2: str):
        user_data = dict(username=username, email=email, password=password, password2=password2)
        return self.client.post('/users/register', data=user_data, follow_redirects=True)
