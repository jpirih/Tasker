from tasker.models import Post
from tests import BaseTestCase


class PostsSeederTestCase(BaseTestCase):
    """Posts seeder related posts"""
    def test_create_test_post(self) -> None:
        """It tests that test post can be created."""
        # given we have a test user  he can create sample post
        user = self.user_seeder.create_user()
        self.posts_seeder.create_post(body='This is test post by John', user_id=user.id)
        post = Post.query.get(1)
        self.assertEqual(post.author.username, 'john')

    def test_seeding_sample_posts_list(self) -> None:
        """It tests that sample posts list can be populated properly"""
        self.posts_seeder.seed_sample_posts()
        sample_posts = Post.query.all()
        self.assertEqual(len(sample_posts), 6)
