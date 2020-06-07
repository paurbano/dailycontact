# use of Blueprint to create module Authorization
''' auth module '''

from flask import Blueprint

auth_bp = Blueprint('auth_bp', __name__)

from . import views