import hashlib
from datetime import datetime
from tasker import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

"""association table followers """
followers = db.Table('followers',
                     db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
                     db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
                     )


class User(UserMixin, db.Model):
    """users database table model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
    posts = db.relationship('Post', backref='author')
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref=db.backref('followers', lazy='dynamic'),
        lazy='dynamic'
    )

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def __repr__(self) -> str:
        return '<User: {} - {}>'.format(self.username, self.email)

    def set_password_hash(self, password: str) -> None:
        """
        Sets password hash for extra security before saving to db.
        @param password:str
        @rtype None
        """
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self, password: str) -> bool:
        """
        Checks provided password with the saved password hash.
        @param password:str
        @rtype:bool
        """
        return check_password_hash(self.password_hash, password)

    def avatar(self, size: int) -> str:
        """
        Generates users profile avatar based on users email, size can be adjustable.
        :type size: int
        """
        digest = hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()
        gravatar_url = "https://www.gravatar.com/avatar/{}?d=identicon&s={}".format(digest, size)

        return gravatar_url

    """Followers functionality"""
    

    @classmethod
    def get_user_by_username(cls, username: str) -> 'User':
        """
        Gets user from db. based on given username
        @param username:str
        @rtype User
        @return user:User
        """
        user = cls.query.filter_by(username=username).first()
        return user

    @classmethod
    def get_user_by_email(cls, email: str) -> 'User':
        """
        Gets user form db by given email address
        @param email: str
        @rtype:User
        @return user:User
        """
        user = cls.query.filter_by(email=email).first()
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


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
