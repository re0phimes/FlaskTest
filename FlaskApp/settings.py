from flask_sqlalchemy import SQLAlchemy
from FlaskApp import app

# class BaseConfig(object):
#     SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     MAIL_SERVER = os.getenv('MAIL_SERVER')    MAIL_PORT = 465    MAIL_USE_SSL = True    MAIL_USERNAME = os.getenv('MAIL_USERNAME')    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')    MAIL_DEFAULT_SENDER = ('Bluelog Admin', MAIL_USERNAME)
#     BLUELOG_EMAIL = os.getenv('BLUELOG_EMAIL')    BLUELOG_POST_PER_PAGE = 10    BLUELOG_MANAGE_POST_PER_PAGE = 15
#
#
# class DevelopmentConfig(BaseConfig)
#     SQLALCHEMY_DATABASE_URI =
