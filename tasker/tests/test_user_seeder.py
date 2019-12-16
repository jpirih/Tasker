from tasker.tests import BaseTestCase


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

