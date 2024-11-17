import os
basedir = os.path.abspath(os.path.dirname(__file__))
def init_app(app):
            pass

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False
    SECRET_KEY = 'dev'
class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
