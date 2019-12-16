from tasker.tests import BaseTestCase
from tasker.models import User


class UserModelTestCase(BaseTestCase):
    """Tests for user db table model"""

    def test_password_hash(self) -> None:
        """Tests if password hashing works properly"""
        user = User(username='kekec', email='kekec@example.com')
        user.set_password_hash('kekec123')
        self.assertTrue(user.check_password_hash('kekec123'))
        self.assertFalse(user.check_password_hash('john123'))

    def test_saving_user(self) -> None:
        """Tests that user saving works properly"""
        u = User.save(username='john', email='john@emxample.com', password='john123')
        user = User.get_user_by_username(username=u.username)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, 'john')
        self.assertIsInstance(u, User)

    def test_get_user_by_username(self) -> None:
        """Tests finding user  from db by username"""
        user = self.user_seeder.create_user()
        u = User.get_user_by_username(username=user.username)
        self.assertIsNotNone(u)
        self.assertEqual(u.username, 'john')
