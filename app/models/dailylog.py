#!/user/bin/python3
'''Class dailylog '''
from app import db
from datetime import datetime

# Many to many relationships between userslogs and symptoms
userlogsymptoms = db.Table('user_log_symptoms',
        db.Column('log_id', db.Integer, db.ForeignKey('dailylogs.id'), primary_key=True),
        db.Column('symptom_id', db.Integer, db.ForeignKey('symptoms.id'), primary_key=True)
)

# Many to many relationships between userslogs and routines
userlogroutines = db.Table('user_log_routines',
        db.Column('log_id', db.Integer, db.ForeignKey('dailylogs.id'), primary_key=True),
        db.Column('routine_id', db.Integer, db.ForeignKey('routines.id'), primary_key=True)
)

class Dailylog(db.Model):
    ''' 
        Dailylog entity
    '''

    __tablename__ = "dailylogs"
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    symptoms = db.relationship('Symptom', secondary=userlogsymptoms, lazy='subquery',
            backref=db.backref('symptoms', lazy=True))
    routines = db.relationship('Routine', secondary=userlogroutines, lazy='subquery',
            backref=db.backref('routines', lazy=True))
    whointeracts= db.relationship('Interact', backref='dailylogs', lazy=True)
