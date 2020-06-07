#!/user/bin/python3
''' Symptom Entity '''

from app import db

class Symptom(db.Model):
    ''' 
        Symptom entity
    '''

    __tablename__ = "symptoms"
    
    id = db.Column(db.Integer, primary_key=True)
    symptom = db.Column(db.String(50), nullable=False, default='')
    active = db.Column(db.Boolean, nullable=False, default=1)
