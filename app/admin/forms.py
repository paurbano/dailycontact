# Add Routines and Symptomns forms
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, email

class RoutineForm(FlaskForm):
    ''' 
        Add Routine Form
    '''
    routine = StringField('Rutina', validators=[DataRequired()])
    active = BooleanField('')
    submit = SubmitField('Guardar')

class SymptomForm(FlaskForm):
    '''
    Add Symptom form
    '''
    symptom = StringField('Sintoma', validators=[DataRequired()])
    active = BooleanField('')
    submit = SubmitField('Guardar')

class CompanyForm(FlaskForm):
    '''
    Add Company form
    '''
    name = StringField('Nombre', validators=[DataRequired()])
    nit = StringField('Nit', validators=[DataRequired(), Length(min=12, max=15, message='Nit entre 12 y 15')])
    email_contact = StringField('Email Contacto', validators=[DataRequired(), email(message='Enter a valid email')])
    submit = SubmitField('Guardar')
