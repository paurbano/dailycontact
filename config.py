# config enviroment for app
from os import environ, path

basedir = path.abspath(path.dirname(__file__))
#load_dotenv(path.join(basedir, '.env'))

class Config:
    ''' set configuration enviroment variables '''
    DEBUG = True

    # general
    FLASK_APP = 'run.py'
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')
    
    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
