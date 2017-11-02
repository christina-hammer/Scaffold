#Christina Hammer
#Last Edit: 10/31/2017
#app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

