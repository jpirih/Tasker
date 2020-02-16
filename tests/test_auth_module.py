from tests import BaseTestCase


class AuthTestCase(BaseTestCase):
    """Users users and profiles related tests."""

    def test_display_login_page(self) -> None:
        """It tests that guest can see login page"""
        response = self.client.get('/users/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sign In', response.data)

    def test_registered_user_can_login(self) -> None:
        """ It test that registered user can login"""
        self.user_seeder.create_user()
        login_data = dict(username='john', password='john123')
        response = self.client.post('/users/login', data=login_data, follow_redirects=True)
        self.assertIn(b'Welcome', response.data)
        self.assertEqual(response.status_code, 200)

    def test_user_must_provide_valid_credentials(self) -> None:
        """It tests that user can not log in with wrong credentials."""
        self.user_seeder.create_user()
        response = self.login_user(username='johny', password='john123')
        self.assertIn(b'Invalid credentials. Please try again.', response.data)

    def test_username_is_required(self) -> None:
        """It tests that username is required for login."""
        self.user_seeder.create_user()
        response = self.login_user(username=None, password='john123')

        self.assertIn(b'This field is required', response.data)

    def test_password_is_required(self) -> None:
        """It tests that username is required for login."""
        self.user_seeder.create_user()
        response = self.login_user(username='john', password=None)

        self.assertIn(b'This field is required', response.data)

    def test_auth_user_cant_login_again(self) -> None:
        """It tests that already logged in user cant access login page"""
        self.user_seeder.create_user()
        self.login_user(username='john', password='john123')

        response = self.client.get('/users/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_auth_user_can_logout(self) -> None:
        """It tests that auth user can logout when he likes."""
        user = self.user_seeder.create_user()
        self.login_user(username=user.username, password='john123')

        response = self.client.get('/users/logout', follow_redirects=True)
        self.assertIn(b'You were successfully logged out.', response.data)

    def test_guest_cannot_logout(self) -> None:
        """It tests that guest cannot logout"""
        response = self.logout_user()
        self.assertIn(b'Sign In', response.data)
        self.assertEqual(response.status_code, 200)

    def test_registration_page(self) -> None:
        """It test that anyone can access registration page"""
        response = self.client.get('/users/register')
        self.assertIn(b'Register New User', response.data)
        self.assertEqual(response.status_code, 200)

    def test_anyone_can_register_new_user(self) -> None:
        """It tests that anyone can register new user """
        user_data = dict(username='johanna', email='johana@exmample.com', password='johanna123', password2='johanna123')
        response = self.client.post('/users/register', data=user_data, follow_redirects=True)

        self.assertIn(b'Sign In', response.data)
        self.assertIn(b'johanna', response.data)
        self.assertEqual(response.status_code, 200)

    def test_username_must_be_unique(self) -> None:
        """It tests that username must be unique"""
        self.user_seeder.create_user()
        response = self.register_user(username='john', email='john2@exmample.com', password='johny', password2='johny')
        self.assertIn(b'Please choose different username', response.data)

    def test_email_must_be_unique(self) -> None:
        """It tests that username must be unique"""
        user = self.user_seeder.create_user()
        response = self.register_user(username='janez', email=user.email, password='johny', password2='johny')
        self.assertIn(b'Please choose different email.', response.data)
