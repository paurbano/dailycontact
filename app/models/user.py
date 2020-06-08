#!/usr/bin/python3
''' App Models '''
from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


# Many to many relationships between users and logs
userlogs = db.Table('userlogs',
        db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
        db.Column('log_id', db.Integer, db.ForeignKey('dailylogs.id'), primary_key=True)
)

# many to many between users and companies
usercompanies = db.Table('usercompanies',
        db.Column('cmp_id', db.Integer, db.ForeignKey('companies.id'), primary_key=True),
        db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

class User(UserMixin, db.Model):
    ''' User entity '''

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    oauth_id = db.Column(db.String(256), index=True, default='')
    username = db.Column(db.String(64), index=True, unique=True,
                         nullable=False)
    email = db.Column(db.String(64), index=True, nullable=False)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    admin = db.Column(db.Boolean, nullable=False, default=0)
    logs = db.relationship('Dailylog', secondary=userlogs, lazy='subquery',
            backref=db.backref('users', lazy=True))
    companies = db.relationship('Companies', secondary=usercompanies, lazy='subquery',
            backref=db.backref('users', lazy=True))

    @property
    def password(self):
        ''' prevent password accesed'''
        raise AttributeError('password is not accesible')

    @password.setter
    def password(self, password):
        '''set password to hash password '''
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        ''' check hashed password '''
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User {}'.format(self.username)

@login_manager.user_loader
def load_user(id):
    ''' check if user is loggedin '''
    return User.query.get(id)
