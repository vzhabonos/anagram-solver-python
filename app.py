from flask import Flask
from flask import request
from solver import Solver


app = Flask(__name__)


@app.route("/")
def hello():
    solver = Solver('33bob sandvagene')
    return 'TEST'
