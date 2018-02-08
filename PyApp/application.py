#Christina Hammer w/ code from 
#Scott Rodkey (for database components) - https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80

#Last Edit: 2/06/2018
#app.py

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from application import db
from application.models import Data
from create_scaffold import *

application = Flask(__name__)
#application.secret_key = '...'

@application.route("/")
def initial():
    return render_template("index.html", original_text="")

@application.route("/", methods = ['POST'])
def process_input():
    

    text_ = request.form['article']
    
    try:     
        db.session.add(text_)
        db.session.commit()        
        db.session.close()
    except:
        db.session.rollback()
    
    
    scaffold = create_scaffold(text_)
    
    p = scaffold.get_persons()
    l = scaffold.get_locations()
    s = scaffold.get_named_entities()
    d = scaffold.get_datetimes()
    q = scaffold.get_quotes()
    n = scaffold.get_num_data()
    a = scaffold.get_article()
    
    return render_template("results.html", people = p, locations = l, subj = s, dt = d, quotes = q, num = n, article = a, original_text = text_)

@application.route("/tutorial")
def tutorial_page():    
    return render_template("tutorial.html")

@application.route("/gh")
def github_page():
    return redirect("http://christina-hammer.github.io/Scaffold")

if __name__ == "__main__":
    application.run()

