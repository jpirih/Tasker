import unittest
from tasker import create_app, db
from config import TestConfig
from tasker.data_seeder import UsersSeeder


class BaseTestCase(unittest.TestCase):
    """Base tests configuration"""
    app = create_app(TestConfig)
    client = app.test_client()
    app_context = app.app_context()
    app_context.push()

    user_seeder = UsersSeeder()

    def setUp(self) -> None:
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
