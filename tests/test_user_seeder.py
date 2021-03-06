from tasker.models import User
from tests import BaseTestCase

base = BaseTestCase()


class UserSeederTestCase(BaseTestCase):
    """Tests for user data seeder"""

    def test_creating_default_user(self) -> None:
        """It tests creating default user with no params user john"""
        user = self.user_seeder.create_user()
        self.assertEqual(user.username, 'john')
        self.assertEqual(user.email, 'john@exmaple.com')

    def test_creating_new_testing_user(self) -> None:
        """ It tests creating user with defined params"""
        user = self.user_seeder.create_user(username='ana', email='ana@example.com', password='ana123')
        self.assertEqual(user.username, 'ana')
        self.assertEqual(user.email, 'ana@example.com')
        self.assertNotEqual(user.username, 'john')

    def test_seeding_sample_users(self) -> None:
        """It tests that sample users get saved to db properly"""
        self.user_seeder.seed_sample_users()
        sample_users = User.query.all()
        self.assertEqual(len(sample_users), 3)

