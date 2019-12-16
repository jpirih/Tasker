# Base configuration file
import os


class BaseConfig:
    """Basic app configuration"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'top_secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
