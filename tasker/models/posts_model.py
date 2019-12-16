from datetime import datetime

from tasker import db


class Post(db.Model):
    """blog posts database table model"""
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, body: str, user_id: int) -> None:
        self.body = body
        self.user_id = user_id

    def __repr__(self) -> str:
        return '<Post: {}>'.format(self.body)

    @classmethod
    def save(cls, body: str, user_id: int) -> 'Post':
        """
        Saves new post to the database and returns
        @rtype:Post
        """
        post = cls(body=body, user_id=user_id)
        db.session.add(post)
        db.session.commit()
        return post
