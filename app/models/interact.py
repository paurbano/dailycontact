#!/user/bin/python3
'''Class Interact '''
from app import db

class Interact(db.Model):
    ''' 
        Interact entity
    '''

    __tablename__ = "interacts"
    
    id = db.Column(db.Integer, primary_key=True)
    log_id = db.Column(db.Integer, db.ForeignKey('dailylogs.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False, default='')
    tipe = db.Column(db.String(1), nullable=False, default='')
