from tasker.tests import BaseTestCase


class MainTestCase(BaseTestCase):
    """Static pages test case"""

    def test_homepage(self) -> None:
        """It tests that anyone can see main page"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_page_not_found(self) -> None:
        """It tests that error handlers work properly"""
        response = self.client.get('/sirov-burek')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'404', response.data)
