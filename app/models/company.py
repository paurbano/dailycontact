#!/usr/bin/python3
''' Models '''
from app import db
from datetime import datetime

# many to many between users and companies
usercompanies = db.Table('usercompanies',
        db.Column('cmp_id', db.Integer, db.ForeignKey('companies.id'), primary_key=True),
        db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)

class Company(db.Model):
    ''' Company entity '''

    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, nullable=False, default='')
    nit = db.Column(db.String(15), index=True, default='')
    email_contact= db.Column(db.String(60), nullable=False, default='')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    active = db.Column(db.Boolean, nullable=False, default=1)
    employees = db.relationship('User', secondary=usercompanies, lazy='subquery',
            backref=db.backref('companies', lazy=True))
