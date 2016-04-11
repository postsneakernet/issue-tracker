# config.py


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'developement key'
    #DATABASE_URI = 'postgresql://vagrant@localhost/issuetracker'
    DATABASE_URI = 'postgresql:///issuetracker'


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
