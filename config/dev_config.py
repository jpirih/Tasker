from config import BaseConfig


class DevConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = 'developers top secret'
