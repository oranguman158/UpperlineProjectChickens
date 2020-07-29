# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_amount_chicken


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/results', methods=['GET', 'POST'])
def results():
    weight = request.form['weight']
    chickens = get_amount_chicken(weight)
    return render_template("results.html", chickens=chickens, weight=weight)