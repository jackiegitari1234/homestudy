# The OS module in Python provides a way of using operating system dependent functionality. 
import os


'''configuration options'''


class Config(object):
    '''Parent configuration class'''
    DEBUG = False
    TESTING = False
    Database_Url = os.getenv("PRODUCTION_DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET")


class DevelopmentConfig(Config):
    '''configurations for development environment'''
    DEBUG = True
    Database_Url = os.getenv("MAIN_DATABASE_URL")


class TestingConfig(Config):
    '''configurations for test environment'''
    DEBUG = True
    TESTING = True
    Database_Url = os.getenv("TEST_DATABASE_URL")

# for heroku
class ProductionConfig(Config):
    '''configurations for production environment'''
    DEBUG = False
    TESTING = False
    Database_Url = os.getenv("PRODUCTION_DATABASE_URL")

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
