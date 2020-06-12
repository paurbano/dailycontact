# app/auth/views.py

import requests
import json
from flask import flash, render_template, url_for, redirect, request
from flask_login import login_required, logout_user, current_user, login_user
from oauthlib.oauth2 import WebApplicationClient

from datetime import datetime as dt
from . import auth_bp
from app.auth.forms import SignUpForm, LoginForm
from app.models.user import db, User
from app import login_manager, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_DISCOVERY_URL

# OAuth2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

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
        user_name = User.query.filter_by(username=signup_form.username.data).first()
        user_email = User.query.filter_by(email=signup_form.email.data).first()
        # print(user_exist)
        if user_name or user_email:
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
            return redirect(url_for('dailylog.userlogshistory'))
            # return render_template('dummy.html')

    return render_template('signup_2.html', form=signup_form,
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
        return redirect(url_for('dailylog.userlogshistory'))
        #return render_template('dummy.html')
    
    login_form = LoginForm()
    if login_form.validate_on_submit():
        # check if user exist and the password matches with the store it in Database
        user = User.query.filter_by(username=login_form.username.data).first()
        if user and user.check_password(password=login_form.password.data):
            login_user(user)
            # next_page = request.args.get('next')
            
            # redirect to DailyLog log page
            return redirect(url_for('dailylog.userlogshistory'))
            #return render_template('dummy.html')
        else:
            flash('Invalid Username or Password')
    return render_template('login.html', login_form=login_form, title='Login')

@auth_bp.route('/oauth', methods=['POST', 'GET'])
def oauth_login():
    ''' register with a google account'''
    # OAuth2 client setup
    # client = WebApplicationClient(GOOGLE_CLIENT_ID)
    
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

@auth_bp.route("/oauth/callback")
def callback():
    ''' Get authorization back from google and save it user'''

    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))

    # Now that we have tokens (yay) let's find and hit URL
    # from Google that gives you user's profile information,
    # including their Google Profile Image and Email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # We want to make sure their email is verified.
    # The user authenticated with Google, authorized our
    # app, and now we've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]
    else:
        return "User email not available or not verified by Google.", 400

    # Create a user in our db with the information provided
    # by Google
    new_user = User(
        oauth_id=unique_id, username=users_name, email=users_email, created_at=dt.now()
    )

    # Doesn't exist? Add to database
    if not User.query.filter_by(oauth_id=unique_id).first():
        db.session.add(new_user)
        db.session.commit() # create new user

    # Begin user session by logging the user in
    login_user(User.query.filter_by(oauth_id=unique_id).first())

    # Send user to DailyLog
    # redirect to DailyLog log page
    return redirect(url_for('dailylog.userlogshistory'))
    #return render_template('dummy.html')

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

def get_google_provider_cfg():
    try:
        return requests.get(GOOGLE_DISCOVERY_URL).json()
    except:
        return None

# test function
def hola():
    return "Funciono!"
