from typing import List
from datetime import datetime
from tasker.data_seeder import UsersSeeder
from tasker.models import Post
from tasker import db


class PostsSeeder:
    """Provides sample blog posts for testing data """
    user_seeder = UsersSeeder()
    POSTS: List = [
        {'body': 'What a wonderful day', 'user_id': 1},
        {'body': 'Dreaming is good sometimes', 'user_id': 2},
        {'body': 'Programming is fun! ', 'user_id': 2},
        {'body': 'Eating pancakes for dinner.', 'user_id': 1},
        {'body': 'Writing some python for fun', 'user_id': 1},
        {'body': 'Santa Clause is coming to town.', 'user_id': 3},
    ]

    def seed_sample_posts(self) -> None:
        """Provides sample posts for development and testing"""
        self.user_seeder.seed_sample_users()
        counter: int = 0
        for post in self.POSTS:
            Post.save(body=post['body'], user_id=post['user_id'])
            counter += 1
        print('{} post were seeded successfully'.format(counter))

    def create_post(self, body: str, user_id: int) -> Post:
        """
        Saves new post to database and returns new post for testing
        @param body: str
        @param user_id: int
        @return Post
        """
        post = Post.save(body=body, user_id=user_id)
        return post

    def custom_post(self, body: str, user_id: int, deleted: bool = False,
                    timestamp: datetime = datetime.utcnow()) -> Post:
        """Saving new post with some custom fields"""
        post = Post(body=body, user_id=user_id, deleted=deleted, timestamp=timestamp)
        db.session.add(post)
        db.session.commit()
        return post
