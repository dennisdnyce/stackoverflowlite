import os

'''API configuration files'''

class Config(object):
    '''Parent configuration class'''
    DEBUG = False
    SECRET_KEY = 'iamasecuredkey'
    ENV = 'development'


class DevelopmentConfig(Config):
    '''configurations for development environment'''
    DEBUG = True


class StagingConfig(Config):
    '''configurations for staging environment'''
    DEBUG = True


class ProductionConfig(Config):
    '''configurations for production environment'''
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    '''configurations for testing environment'''
    DEBUG = True
    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
