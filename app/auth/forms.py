# Login and SignUp forms
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
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
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), email(message='Enter a valid email')])
    password= PasswordField('Password', validators=[DataRequired(),
                                                    Length(min=6, message='password must be 6 characters minimun')])
    confirm = PasswordField('Confirm Your Password',
                            validators=[DataRequired(),
                                        EqualTo('password', message='Password do not match.')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    ''' user login form '''
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
