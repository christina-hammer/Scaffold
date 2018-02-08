#This code originates from Scott Rodkey's Flask deployment tutorial at 
#https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
application.config.from_object('config')
db = SQLAlchemy(application)
