from tests import BaseTestCase
from tasker.models import Post, User


class PostsModelTestCase(BaseTestCase):
    """Tests for posts db model"""

    def test_post_str_repr(self) -> None:
        """It tests posts model string representation"""
        user = self.user_seeder.create_user()
        post = self.posts_seeder.create_post(body='Have a nice day.', user_id=user.id)
        self.assertEqual(post.__repr__(), '<Post: Have a nice day.>')

    def test_saving_new_post(self):
        """It tests that saving new post works properly"""
        user = self.user_seeder.create_user()
        post = Post.save(body='First test Post', user_id=user.id)

        posts = Post.query.all()
        self.assertIsNotNone(post)
        self.assertIsInstance(post, Post)
        self.assertIsInstance(post.author, User)
        self.assertIn(post, posts)

    def test_get_non_deleted_posts(self) -> None:
        """I tests that non deleted posts find from db."""
        user = self.user_seeder.create_user()
        post = self.posts_seeder.custom_post(body='Test post that is displayed', user_id=user.id, deleted=False)
        deleted_post = self.posts_seeder.custom_post(body='Post that was deleted', user_id=user.id, deleted=True)
        posts = Post.get_posts()
        self.assertIn(post, posts)
        self.assertNotIn(deleted_post, posts)

    def test_get_latest_three_posts(self) -> None:
        """It  tests that the three most recent posts found in db."""
        self.posts_seeder.seed_sample_posts()
        latest_posts = Post.get_latest_posts()
        self.assertEqual(latest_posts.count(), 3)
        self.assertEqual([post.id for post in latest_posts], [6, 5, 4])

    def test_get_single_post(self) -> None:
        """It tests that it is possible to find post by id from db"""
        user = self.user_seeder.create_user()
        post1 = self.posts_seeder.create_post(body='This is post #1', user_id=user.id)
        post2 = self.posts_seeder.create_post(body='This is post #2', user_id=user.id)

        single_post = Post.get_single_post(id=post2.id)
        self.assertEqual(single_post.id, 2)
        self.assertNotEqual(single_post.id, post1.id)
