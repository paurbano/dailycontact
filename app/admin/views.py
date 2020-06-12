#!/usr/bin/python3
''' DailyLog '''
from flask import flash, render_template, url_for, redirect
from flask_login import login_required, logout_user, current_user, login_user

from . import admin_bp
from app import db
from app.models.user import User
from app.models.symptom import Symptom
from app.models.routine import Routine
from app import login_manager
from app.admin.forms import *

@admin_bp.route('/')
@login_required
def index():
    '''
        Index admin
    '''
    if current_user.admin:
        return render_template('dashboard.html')

    return redirect(url_for('dailylog.userlogshistory'))

@admin_bp.route('/routines/add', strict_slashes=True, methods=['GET', 'POST'])
@login_required
def addroutine():
    '''
     add routine
    '''
    if current_user.admin:
        add_form = RoutineForm()

        if add_form.validate_on_submit():
            new_routine = Routine(routine=add_form.routine.data,
                                  active=add_form.active.data)
            try:
                db.session.add(new_routine)
                db.session.commit()
                flash('Routine added successfully!!')
            except Exception as e:
                flash('An error occur saving Routine: {}'.format(e))
            
            return redirect(url_for('admin.list_routines'))

        return render_template('/routine.html', form=add_form, add_routine=False)

    return redirect(url_for('auth_bp.login'))

@admin_bp.route('/routines', strict_slashes=True)
@login_required
def list_routines():
    ''' 
        list all routines
    '''
    routines = Routine.query.all()
    add_form = RoutineForm()
    return render_template('routine.html',  form=add_form, routines=routines, add_routine=False)
