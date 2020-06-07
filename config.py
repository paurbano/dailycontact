# config enviroment for app
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    ''' set configuration enviroment variables '''
    DEBUG = False

    # general
    FLASK_APP = 'run.py'
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY') 
    # SECRET_KEY = 'p9Bv<3Eid9%$i01'
    
    # Flask-SQLAlchemy
    # SQLALCHEMY_DATABASE_URI = 'mysql://covid_dev:covid19_dev@localhost/daily_dev_db'
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
