# Add Routines and Symptomns forms
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

class RoutineForm(FlaskForm):
    ''' 
        Add Routine Form
    '''
    routine = StringField('Rutina', validators=[DataRequired()])
    active = BooleanField('Activo')
    submit = SubmitField('Guardar')

class SymptomForm(FlaskForm):
    '''
    Add Symptom form
    '''
    routine = StringField('Rutina', validators=[DataRequired()])
    active = BooleanField('Activo')
    submit = SubmitField('Guardar')
