from flask import Flask
from flask import request
from solver import Solver


app = Flask(__name__)


@app.route("/")
def hello():
    query = request.args.get('query')
    alphas = {}
    if query:
        solver = Solver(query)
        alphas = solver.generate_all_possible_alphas()
    return str(len(alphas)) + " alphas generated for query - " + str(query)
