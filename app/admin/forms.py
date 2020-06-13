# Add Routines and Symptomns forms
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

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
