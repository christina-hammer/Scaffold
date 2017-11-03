#Christina Hammer
#Last Edit: 11/03/2017
#app.py

from flask import Flask
from flask import render_template
from flask import request
import sample_backend

app = Flask(__name__)

@app.route("/")
def initial():
    return render_template("index.html", result=None)

@app.route("/", methods = ['POST'])
def process_input():
    text_ = request.form['article']
    result_ = text_.upper()
    return render_template("index.html", result=result_)

if __name__ == "__main__":
    app.run()

