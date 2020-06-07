# use of Blueprint to create module dailylog
''' dailylog module '''

from flask import Blueprint

dailylog = Blueprint('dailylog', __name__)

from . import views
