from datetime import datetime
from sqlalchemy import desc

from tasker import db, ma


class Post(db.Model):
    """blog posts database table model"""
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    deleted = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, body: str, user_id: int, deleted: bool = False, timestamp: datetime = datetime.utcnow()) -> None:
        self.body = body
        self.user_id = user_id
        self.deleted = deleted
        self.timestamp = timestamp

    def __repr__(self) -> str:
        return '<Post: {}>'.format(self.body)

    @classmethod
    def save(cls, body: str, user_id: int) -> 'Post':
        """
        Saves new post to the database and returns
        @param body: str
        @param user_id: int
        @rtype:Post
        """
        post = cls(body=body, user_id=user_id)
        db.session.add(post)
        db.session.commit()
        return post

    @classmethod
    def get_posts(cls) -> 'Post':
        """
        Gets the list of non deleted posts from db
        @return posts: Post
        """
        posts = cls.query.filter_by(deleted=False).order_by(cls.timestamp.desc()).all()
        return posts

    @classmethod
    def get_single_post(cls, id: int) -> 'Post':
        """
        Gets post by id from database
        @param id:
        @return post: Post
        """
        post = cls.query.get(id)
        return post

    @classmethod
    def get_latest_posts(cls) -> 'Post':
        """Gets latest 3 latest added posts"""
        latest_posts = cls.query.order_by(desc(Post.timestamp)).limit(3)
        return latest_posts


