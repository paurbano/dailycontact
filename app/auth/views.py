# app/auth/views.py

from flask import flash, render_template, url_for, redirect
from flask_login import login_required, logout_user, current_user, login_user

from datetime import datetime as dt
from . import auth_bp
from app.auth.forms import SignUpForm, LoginForm
from app.models.user import db, User
from app import login_manager


@auth_bp.route('/')
@auth_bp.route('/index')
def home():
    return render_template('index.html', title='Daily Contact')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    '''
    Add user through signup form

    GET: Serve sign-up page.
    POST: Validate form, create account, redirect user to dashboard
    '''
    # username = request.args.get("user")
    # email = request.args.get("email")
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        user_exist = User.query.filter_by(username=signup_form.username.data).first()
        user_exist = User.query.filter_by(email=signup_form.email.data).first()
        # print(user_exist)
        if user_exist is not None:
            #return make_response("usuario {} o correo {}  ya existe!".format(user_exist.username, user_exist.email))
            flash('A user already exists with that username or email')
        else:
            new_user = User(username=signup_form.username.data,
                        email=signup_form.email.data,
                        password=signup_form.password.data,
                        created_at=dt.now())
            try:
                db.session.add(new_user)
                db.session.commit() # create new user
                login_user(new_user) # log in as new created user
            except TypeError as err:
                flash('Problem creating user:{}'.format(err))
            except Exception as err:
                flash(err)
            # redirect to daily-Log, uncomment when is ready!
            # return redirect(url_for('dailyLog.routines'))
            return render_template('dummy.html')

    return render_template('signup.jinja2', form=signup_form,
                           title='Sign Up',
                           template='signup-page',
                           body="Sign up for a user account.")


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    ''' 
        Login form

        GET: Serve login page.
        POST: Validate form and redirect user to register Daily log
    '''
    # if user is logged in
    if current_user.is_authenticated:
        # uncommet when is ready
        # return redirect(url_for('dailylog.routines'))
        return render_template('dummy.html')
    
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # check if user exist and the password matches with the store it in Database
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and user.check_password(password=login_form.password.data):
            login_user(user)
            # next_page = request.args.get('next')
            
            # redirect to DailyLog log page
            # return redirect(url_for('dailylog.routines'))
            return render_template('dummy.html')
        else:
            flash('Invalid Username or Password')
    return render_template('login.html', login_form=login_form, title='Login')

@auth_bp.route('/logout')
@login_required #this is for allow access to route only to loggin users
def logout():
    '''
        Logout a user
    '''
    logout_user()
    flash('You have successfully been logged out')

    return redirect(url_for('auth_bp.login'))

@login_manager.unauthorized_handler
def unauthorized():
    ''' redirect unauthorized users to login '''
    flash('You must be logged in to view this page')
    return redirect(url_for('auth_bp.login'))


# test function
def hola():
    return "Funciono!"
