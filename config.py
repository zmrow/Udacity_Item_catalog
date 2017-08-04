import os

class Config(object):
    DEBUG = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    pass
    #DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///catalog.db'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(app.root_path, 'catalog.db')
