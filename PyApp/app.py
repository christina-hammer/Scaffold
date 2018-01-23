#Christina Hammer
#Last Edit: 1/18/2018
#app.py

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from create_scaffold import *

app = Flask(__name__)

@app.route("/")
def initial():
    return render_template("index.html", original_text="")

@app.route("/", methods = ['POST'])
def process_input():
    
    text_ = request.form['article']
           
    scaffold = create_scaffold(text_)
    p = scaffold.get_persons()
    l = scaffold.get_locations()
    s = scaffold.get_named_entities()
    d = scaffold.get_datetimes()
    q = scaffold.get_quotes()
    n = scaffold.get_num_data()
    a = scaffold.get_article()
    
    return render_template("results.html", people = p, locations = l, subj = s, dt = d, quotes = q, num = n, article = a, original_text = text_)

@app.route("/tutorial")
def tutorial_page():    
    return render_template("tutorial.html")

@app.route("/gh")
def github_page():
    return redirect("http://christina-hammer.github.io/Scaffold")

if __name__ == "__main__":
    app.run()

