from tasker.tests import BaseTestCase
from tasker.models import Post, User


class PostsModelTestCase(BaseTestCase):
    """Tests for posts db model"""

    def test_saving_new_post(self):
        user = self.user_seeder.create_user()
        post = Post.save(body='First test Post', user_id=user.id)

        posts = Post.query.all()
        self.assertIsNotNone(post)
        self.assertIsInstance(post, Post)
        self.assertIsInstance(post.author, User)
        self.assertIn(post, posts)
