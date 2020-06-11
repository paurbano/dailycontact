#!/user/bin/python3
'''Class routines '''
from app import db

class Routine(db.Model):
    ''' 
        Routine entity
    '''

    __tablename__ = "routines"
    
    id = db.Column(db.Integer, primary_key=True)
    routine = db.Column(db.String(50), nullable=False, default='')
    active = db.Column(db.Boolean, nullable=False, default=1)
    logs = db.relationship('Userlog_Routines', back_populates='routines')
