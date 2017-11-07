#Christina Hammer
#Last Edit: 11/03/2017
#app.py

from flask import Flask
from flask import render_template
from flask import request
from create_scaffold import *

app = Flask(__name__)

@app.route("/")
def initial():
    return render_template("index.html", result=None)

@app.route("/", methods = ['POST'])
def process_input():
    text_ = request.form['article']
    
    result_ = create_scaffold(text_)
    return render_template("index.html", result=result_)

if __name__ == "__main__":
    app.run()

