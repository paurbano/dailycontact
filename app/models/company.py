#!/usr/bin/python3
''' Models '''
from app import db
from datetime import datetime


class Company(db.Model):
    ''' Company entity '''

    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, nullable=False, default='')
    nit = db.Column(db.String(15), index=True, default='')
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    employees = db.relationship('User', backref='users', lazy=True)
    active = db.Column(db.Boolean, nullable=False, default=1)
