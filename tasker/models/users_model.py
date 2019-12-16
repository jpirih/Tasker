from datetime import datetime
from tasker import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """users database table model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return '<User: {} - {}>'.format(self.username, self.email)

    def set_password_hash(self, password: str) -> None:
        """
        Sets password hash for extra security before saving to db.
        @param password:str
        """
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password: str) -> bool:
        """
        Checks provided password with the saved password hash.
        @param password:str
        @rtype:bool
        """
        return check_password_hash(self.password_hash, password)

    @classmethod
    def get_user_by_username(cls, username:str) -> 'User':
        user = cls.query.filter_by(username=username).first()
        return user

    @classmethod
    def save(cls, username: str, email: str, password: str) -> 'User':
        """
        Saves new user to database and returns new user.
        @param username: str
        @param email: str
        @param password: str
        @return: User
        """
        user = cls(username=username, email=email)
        user.set_password_hash(password=password)
        db.session.add(user)
        db.session.commit()
        return user