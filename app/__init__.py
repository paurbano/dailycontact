# app/__init__.py
# here is where initialize app config and plugins
from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from config import Config #archivo config.py

# db initialization
db = SQLAlchemy()

# Init Login
login_manager=LoginManager()

#init bootstrap
bootstrap= Bootstrap()

# google ID's API Configuration
GOOGLE_CLIENT_ID = environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = environ.get("GOOGLE_DISCOVERY_URL", None)

def create_app():
    ''' Core application '''
    # Initialize the app
    app = Flask(__name__)

    # Load the config file
    app.config.from_object(Config)

    # this must be move to config.py
    '''
    app.config['SQLALCHEMY_DATABASE_URI'] = 
    app.config['SECRET_KEY'] = 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =
    '''
    # Initialize plugins - database and Login
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    # others plugins i.e - remenber initialized first
    bootstrap.init_app(app)
    # mail.init_app(app)

    with app.app_context():
        # models
        from app.models import user
        from app.models import routine
        from app.models import symptom
        from app.models import dailylog
        from app.models import interact
        from app.models import company

        # register BluePrints
        from app.auth import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/')

        from app.admin import admin_bp
        app.register_blueprint(admin_bp, url_prefix ='/admin')
        
        from app.dailylog import dailylog
        app.register_blueprint(dailylog, url_prefix='/dailylog')


        # < -- here register other BluePrints -->
        #

        # create database tables from models
        db.create_all()
        return app
