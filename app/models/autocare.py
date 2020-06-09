#!/usr/bin/python3
''' Models '''
from app import db
from datetime import datetime


class Logroutines(db.Model):
    ''' Autocare entity '''

    __tablename__ = "logroutines"

    log_id = db.Column(db.Integer, primary_key=True),
    routine_id = db.Column(db.Integer, primary_key=True),
    frecuency = db.Column(db.String(25), nullable=False, default='Ninguno'),

    name = db.Column(db.String(256), index=True, nullable=False, default='')
    
    employees = db.relationship('User', secondary=usercompanies, lazy='subquery',
            backref=db.backref('companies', lazy=True))
