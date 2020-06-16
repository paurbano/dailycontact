#!/usr/bin/python3
''' DailyLog '''
from flask import flash, render_template, url_for, redirect
from flask_login import login_required, logout_user, current_user, login_user

from . import admin_bp
from app import db
from app.models.user import User
from app.models.symptom import Symptom
from app.models.routine import Routine
from app.models.company import Company
from app import login_manager
from app.admin.forms import *

@admin_bp.route('/')
@login_required
def dashboard():
    '''
        Index admin
    '''
    if current_user.admin:
        return render_template('dashboard.html', username=current_user.username)

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
            new_routine = Routine(routine=add_form.routine.data)
            try:
                db.session.add(new_routine)
                db.session.commit()
                flash('Routine added successfully!!')
            except Exception as e:
                flash('An error occur saving Routine: {}'.format(e))
            
            return redirect(url_for('admin_bp.list_routines'))

        return render_template('/routine.html', form=add_form, add_routine=False, username=current_user.username)

    return redirect(url_for('auth_bp.login'))

@admin_bp.route('/routines/<id>', strict_slashes=True)
@login_required
def updateroutine(id=None):
    ''' 
        Update a routine
    '''
    if current_user.admin:
        form = RoutineForm()
        routines = Routine.query.all()
        if id is not None:
            for routine in routines:
                if routine.id == int(id):
                    _routine = routine
            
            if _routine.active is True:
                _routine.active = 0
            else:
                _routine.active = 1

            try:
                db.session.add(_routine)
                db.session.commit()
            except Exception as e:
                flash('Error actualizando Rutina {}'.format(e))
        return render_template('routine.html', form=form, routines=routines, username=current_user.username)
    return redirect(url_for('auth_bp.login'))


@admin_bp.route('/routines', strict_slashes=True, methods=['GET', 'POST'])
@login_required
def list_routines():
    ''' 
        list all routines
    '''
    if current_user.admin:
        routines = Routine.query.all()
        form = RoutineForm()
        return render_template('routine.html', form=form,
                               routines=routines,add_routine=False)
    return redirect(url_for('auth_bp.login'))

@admin_bp.route('/symptoms/add', strict_slashes=True, methods=['GET', 'POST'])
@login_required
def addsymptom():
    '''
     add symptom
    '''
    if current_user.admin:
        add_form = SymptomForm()

        if add_form.validate_on_submit():
            new_symptom = Symptom(symptom=add_form.symptom.data,
                                  active=add_form.active.data)
            try:
                db.session.add(new_symptom)
                db.session.commit()
                flash('Symptom added successfully!!')
            except Exception as e:
                flash('An error occur saving Symptom: {}'.format(e))
            
            return redirect(url_for('admin_bp.list_symptoms'))

        return render_template('/symptom.html', form=add_form, username=current_user.username)

    return redirect(url_for('auth_bp.login'))

@admin_bp.route('/symptoms', strict_slashes=True, methods=['GET', 'POST'])
@login_required
def list_symptoms():
    ''' 
        list all symptoms
    '''
    if current_user.admin:
        symptoms = Symptom.query.all()
        form = SymptomForm()
        return render_template('symptom.html', form=form, symptoms=symptoms, username=current_user.username)
    return redirect(url_for('auth_bp.login'))

@admin_bp.route('/symptoms/<int:id>', strict_slashes=True)
@login_required
def updatesymptom(id=None):
    ''' 
        Update a symptom
    '''
    if current_user.admin:
        form = SymptomForm()
        symptoms = Symptom.query.all()
        if id is not None:
            for sintoma in symptoms:
                if sintoma.id == int(id):
                    symptom = sintoma
            
            if symptom.active is True:
                symptom.active = 0
            else:
                symptom.active = 1

            try:
                db.session.add(symptom)
                db.session.commit()
            except Exception as e:
                flash('Error actualizando Sintoma: {}'.format(e))
        return render_template('symptom.html', form=form, symptoms=symptoms, username=current_user.username)
    return redirect(url_for('auth_bp.login'))

@admin_bp.route('/companies/add', strict_slashes=True, methods=['GET','POST'])
@login_required
def addcompany():
    '''
    add company
    '''
    if current_user.admin:
        form = CompanyForm()
        if form.validate_on_submit:
            exist = Company.query.filter_by(nit=form.nit.data).first()
            
            if not exist:
                company = Company(name=form.name.data, nit=form.nit.data,
                                  email_contact=form.email_contact.data)
                try:
                    db.session.add(company)
                    db.session.commit()
                    flash('Company added successfully!!')
                except Exception as e:
                    flash('Can´t added company {}'.format(e))
                
                return redirect(url_for('admin_bp.list_companies'))
        return render_template('/company.html', form=form, username=current_user.username)
    return redirect(url_for('auth_bp.login'))

@admin_bp.route('/companies', strict_slashes=True, methods=['GET', 'POST'])
@login_required
def list_companies():
    ''' 
        list all companies
    '''
    if current_user.admin:
        companies = Company.query.all()
        form = CompanyForm()
        return render_template('company.html', form=form, companies=companies, username=current_user.username)
    return redirect(url_for('auth_bp.login'))

@admin_bp.route('/companies/<int:id>', strict_slashes=True)
@login_required
def updatecompanies(id=None):
    ''' 
        Update a company
    '''
    if current_user.admin:
        form = CompanyForm()
        companies = Company.query.all()
        if id is not None:
            for company in companies:
                if company.id == int(id):
                    _company = company
            
            if _company.active is True:
                _company.active = 0
            else:
                _company.active = 1

            try:
                db.session.add(_company)
                db.session.commit()
            except Exception as e:
                flash('Error actualizando Empresa: {}'.format(e))
        return render_template('company.html', form=form, companies=companies, username=current_user.username)
    return redirect(url_for('auth_bp.login'))

@login_manager.unauthorized_handler
def unauthorized():
    ''' redirect unauthorized users to login '''
    flash('You must be logged in to view this page')
    return redirect(url_for('auth_bp.login'))
