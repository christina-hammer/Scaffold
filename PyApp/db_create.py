#This code originates from Scott Rodkey's Flask deployment tutorial at 
#https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80

from application import db
from application.models import Data

db.create_all()

print("DB created.")
