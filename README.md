<h1 align="center">DailyContact</h1>

For those who have to accomplish Covid-19 biosafety protocols, Daily Contact is a tool that allows you to keep logs about symptoms, routines, people and places where you have been interacting the last 14 days. Unlike other Covid-19 apps, we do NOT need your location or contacts, we respect your privacy. You can try it [here](http://35.185.87.254/)

<p align="center">
  <img src="https://github.com/paurbano/dailycontact/blob/master/app/static/dist/img/landing.png"
       alt="DailyContact"
  />
</p>

## Features :

- Register as User
- Register and consult your Daily Logs
- Manage and customize companies, routines and symptoms

It´s easy to use, just signup and start!!

<p align="center">
  <img src="https://github.com/paurbano/dailycontact/blob/master/app/static/dist/img/signup.PNG"
       alt="DailyContactLogin"
  />
</p>

<p align="center">
  <img src="https://github.com/paurbano/dailycontact/tree/master/app/static/dist/img/servicios.PNG"
       alt="DailyContactServicios"
  />
</p>

## Project structure and architecture

For these project we use three technologies MySql as Database, Flask-Python for backend and bootstrap for front-end

These is how project is structured
<p align="center">
  <img src="https://github.com/paurbano/dailycontact/tree/master/app/static/dist/img/stucture.png"
       alt="DailyContactStructure"
  />
</p>

- [Admin](https://github.com/paurbano/dailycontact/tree/master/app/admin): Manage content like companies, routines and symptoms 
- [Auth](https://github.com/paurbano/dailycontact/tree/master/app/auth): All about users login, signup and credentials
- [DailyLog](https://github.com/paurbano/dailycontact/tree/master/app/dailylog): Add logs and show history about it
- [Models](https://github.com/paurbano/dailycontact/tree/master/app/models): Classes and data model

The architecture is so simple:
<p align="center">
  <img src="https://github.com/paurbano/dailycontact/blob/master/app/static/dist/img/architecture.png"
       alt="DailyContactStructure"
  />
</p>

If you want to try it locally

## Installation

First at all install Mysql Server:

    $ sudo apt-get update
    $ sudo apt-get install mysql-server-5.7

Then clone the project and install libraries

    $ git clone https://github.com/paurbano/dailycontact.git
    $ cd dailycontact
    $ sudo pip3 install -r requirements.txt
    $ cat setup_mysql_dev.sql | mysql -uroot -hlocalhost -p

If you have problems installing with requirements file, you can install every component individually.

    $ pip3 install Flask
    $ pip3 install Flask-login
    $ pip3 install Flask-wtf
    $ pip3 install Flask-sqlalchemy

And that´s for all other in the list

Then you have to setup environment variables, you have to change the values for your owm machine!!

    $ export SECRET_KEY='¿?0)(ñ1}23fsgd4fe57jvqwa*-@'
    $ export SQLALCHEMY_DATABASE_URI=''mysql+pymysql://{_username_}:{_userpassword_}@localhost:3306/daily_dev_db''
    $ export FLASK_ENV='Production'
 
 For Google Authentication you can contact us for originals credentials or create a new ones for your server, for that go to [Google developers credentials page](https://console.developers.google.com/apis/credentials).

    $ export GOOGLE_CLIENT_ID='your_client_ID'
    $ export GOOGLE_CLIENT_SECRET='your_secret_ID'
    $ export export GOOGLE_DISCOVERY_URL='https://accounts.google.com/.well-known/openid-configuration'

or you can create a bash file and put all this variables.

## To run the project

    $ python3 run.py

### Authors
Aiko Mi(https://www.linkedin.com/in/aiko-mi-1293ba1a0/)
Jackson Moreno(https://www.linkedin.com/in/jaarmore)
Pablo Andrés Urbano(https://www.linkedin.com/in/pablourbanodelacruz)
