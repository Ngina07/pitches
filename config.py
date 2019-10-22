import os

class Config:

    SECRET_KEY = '830548fc746b58e082e0f2fe9ba4a7ff'

    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
# class TestConfig(Config):
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:1234@localhost/pitches_test'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:1234@localhost/pitches'  
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
# 'test':TestConfig
}