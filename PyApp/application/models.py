#This code originates from Scott Rodkey's Flask deployment tutorial at 
#https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80

from application import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    
    def __init__(self, notes):
        self.notes = notes

    def __repr__(self):
        return '<Data %r>' % self.notes