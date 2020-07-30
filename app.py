# ---- YOUR APP STARTS HERE ----
# -- Import section --
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request
from model import get_amount_chicken
from model import how_many_slaps



# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())


@app.route('/results', methods=['GET', 'POST'])
def results():
    weight = request.form['weight']
    chickens = get_amount_chicken(weight)
    return render_template("results.html", chickens=chickens, weight=weight, time=datetime.now())

@app.route('/cooking', methods = ['GET', 'POST'])
def cooking():
    c_weight = request.form['c_weight']
    speed = request.form['speed']
    if c_weight == "Rhode Island Wright":
        c_weight = 3.4
    elif c_weight == "Plymouth Rock chicken":
        c_weight = 3.2
    else:
        c_weight = c_weight
    slaps = how_many_slaps(float(c_weight), float(speed))
    return render_template("cook_results.html", slaps=slaps, c_weight=c_weight, speed=speed, time=datetime.now())
