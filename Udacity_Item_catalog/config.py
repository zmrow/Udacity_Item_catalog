class Config(object):
    DEBUG = False
    DATABASE_URI = 'sqlite://:memory:'

class ProductionConfig(Config):
    #DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(app.root_path, 'catalog.db')
