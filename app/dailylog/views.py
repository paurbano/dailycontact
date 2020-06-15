#!/usr/bin/python3
''' DailyLog '''
from flask import flash, render_template, url_for, redirect, request
from flask_login import login_required, logout_user, current_user, login_user

from . import dailylog
from app import db
from app.models.user import User
from app.models.dailylog import Dailylog
from app.models.symptom import Symptom
from app.models.routine import Routine
from app.models.interact import Interact
from app.dailylog.forms import DailyLogForm
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


@dailylog.route('/addlog', methods=['GET', 'POST'], strict_slashes=True)
@login_required
def newlog():
    ''' Add user log '''
    # if user is logged in
    if current_user.is_authenticated:
        form = DailyLogForm()
        sintomas = Symptom.query.filter_by(active=1)

        if request.method == 'POST': # form.validate_on_submit()
            user = User.query.get(current_user.id)
            list_sintomas = request.form.getlist('sintoma')
            transporte = form.type_tx.data
            tempmin = form.temp_ini.data
            tempfin = form.temp_final.data
            bitacora = Dailylog(temp_ini=tempmin, temp_end=tempfin,type_tx=transporte)
            # print(list_sintomas)
            # print(transporte)
            for sym_id in list_sintomas:
                sintoma = Symptom.query.get(sym_id)
                bitacora.symptoms.append(sintoma)
            
            user.logs.append(bitacora)
            try:
                db.session.add(user)
                db.session.commit()
                flash('Bitacora guardada!!')
            except Exception as e:
                flash('Error guardando bitacora {}'.format(e))
            return render_template('dailylog.html', form=form, sintomas=sintomas)
        
        return render_template('dailylog.html', form=form, sintomas=sintomas)

        # return render_template('dummy.html')


@dailylog.route('/interactions', strict_slashes=True)
@dailylog.route('/interactions/<uid>:int', strict_slashes=True)
@login_required
def interactions(uid=None):
    ''' list all user's interactions '''
    if uid is None:
        userlogs = User.query.get(current_user.id)
    else:
        userlogs = User.query.get(uid)
    return render_template('interactions.html',userlogs=userlogs)

@login_manager.unauthorized_handler
def unauthorized():
    ''' redirect unauthorized users to login '''
    flash('You must be logged in to view this page')
    return redirect(url_for('auth_bp.login'))
