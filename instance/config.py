# The OS module in Python provides a way of using operating system dependent functionality. 
import os


'''configuration options'''


class Config(object):
    '''Parent configuration class'''
    DEBUG = False
    TESTING = False
    Database_Url = os.getenv("MAIN_DATABASE_URL")
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
    Database_Url = "postgres://imzqjryhkpdegq:a60f004d543330ea4c2f4bc1053cd84362409361323ecf7bf636e7135ecebd3b@ec2-23-21-165-188.compute-1.amazonaws.com:5432/dbdefc1ect0gdm"


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
