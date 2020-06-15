#!/usr/bin/python3
''' DailyLog '''
from flask import flash, render_template, url_for, redirect
from flask_login import login_required, logout_user, current_user, login_user

from . import dailylog
from app import db
from app.models.user import User
from app.models.dailylog import *
from app.models.symptom import Symptom
from app.models.routine import Routine
from app.models.interact import Interact
from app import login_manager


@dailylog.route('/logshistory/', strict_slashes=True)
@dailylog.route('/logshistory/<id>', strict_slashes=True)
@login_required
def userlogshistory(id=None):
    ''' SHow history of user logs '''
    # if user is logged in
    if current_user.is_authenticated:
        userlogs = User.query.get(current_user.id)
        return render_template('loghistory.html', userlogs=userlogs,
                               id=id, title='History Of Logs',
                               username=current_user.username)


@dailylog.route('/addlog', strict_slashes=True, methods=['GET', 'POST'])
@login_required
def newlog():
    ''' Add user log '''
    # if user is logged in
    if current_user.is_authenticated:
        return render_template('newlog.html', content=current_user)


@login_manager.unauthorized_handler
def unauthorized():
    ''' redirect unauthorized users to login '''
    flash('You must be logged in to view this page')
    return redirect(url_for('auth_bp.login'))
