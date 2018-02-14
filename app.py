from flask import Flask
from flask import request
from solver import Solver


app = Flask(__name__)


@app.route("/")
def hello():
    solver = Solver('33bob sandvagene')
    alphas = solver.generate_all_possible_alphas()
    print(alphas)
    return 'TEST'
