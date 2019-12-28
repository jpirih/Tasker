from tasker.tests import BaseTestCase


class PostsModuleTestCase(BaseTestCase):
    """All posts related views test class"""

    def test_posts_index(self) -> None:
        """It tests posts list main page"""
        self.user_seeder.create_user()
        self.login_user(username='john', password='john123')
        response = self.client.get('/posts')
        self.assertIn(b'Microblog - Posts', response.data)
        self.assertEqual(response.status_code, 200)

    def test_auth_user_can_post_new_post(self) -> None:
        """It test that logged in user can post new post"""
        self.user_seeder.create_user()
        self.login_user(username='john', password='john123')
        response = self.client.post('/posts', data=dict(body="This is new post form John"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is new post form John', response.data)
