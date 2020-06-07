# app/__init__.py
# here is where initialize app config and plugins

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# db initialization
db = SQLAlchemy()

# Init Login
login_manager=LoginManager()


def create_app():
    ''' Core application '''
    # Initialize the app
    app = Flask(__name__)

    # Load the config file
    # app.config.from_pyfile('config.py')

    # this must be move to config.py
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://covid_dev:covid19_dev@localhost:3306/daily_dev_db'
    app.config['SECRET_KEY'] = '!wdcvfer3$4rfvbgt%5'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize plugins - database and Login
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    # others plugins i.e - remenber initialized first
    # bootstrap.init_app(app)
    # mail.init_app(app)
    
    # google ID's API Configuration
    GOOGLE_CLIENT_ID ="" # os.environ.get("GOOGLE_CLIENT_ID", None)
    GOOGLE_CLIENT_SECRET = "" # os.environ.get("GOOGLE_CLIENT_SECRET", None)
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )

    with app.app_context():
        # models
        from app.models import user
        from app.models import routine
        from app.models import symptom
        from app.models import dailylog
        from app.models import interact

        # register BluePrints
        from app.auth import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/')

        # < -- here register other BluePrints -->
        #

        # create database tables from models
        db.create_all()
        return app
