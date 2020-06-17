# Login and SignUp forms
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, SelectField
from wtforms.validators import DataRequired, email, EqualTo, Length

'''
# we can validate if user already exist here import User class from models
from app.models.user import User
# create a functions that query  User.query.filter_by(email=form.email.data).first()
def validate_email(self, email):
        # validate if email already exist
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Email is already register')

    def validate_username(self, username):
        # validate if email already exist
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Username is already register')
'''
class SignUpForm(FlaskForm):
    '''
    Users signup form
    '''
    company = SelectField('Empresa', choices=[('Independiente','Independiente'),('Holberton School','Holberton School'),('Zonamerica','zonamerica')], validators=[DataRequired()])
    username = StringField('Usuario', validators=[DataRequired()])
    email = StringField('Correo Electronico', validators=[DataRequired(), email(message='Ingreso un correo valido')])
    password= PasswordField('Contrasena', validators=[DataRequired(),
                                                    Length(min=6, message='Contrasena debe tener 6 caracteres minimo')])
    confirm = PasswordField('Confirme su contrasena',
                            validators=[DataRequired(),
                                        EqualTo('password', message='contrasena no coincide')])
    submit = SubmitField('Registrame')

class LoginForm(FlaskForm):
    ''' user login form '''
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contrasena', validators=[DataRequired()])
    submit =   SubmitField('Entrar')
    
