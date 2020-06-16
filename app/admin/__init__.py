# use of Blueprint to create module administration
''' admin module '''

from flask import Blueprint

admin_bp = Blueprint('admin_bp', __name__)

from . import views
