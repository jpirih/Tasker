from config import BaseConfig


class TestConfig(BaseConfig):
    """App testing environment configuration"""
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
