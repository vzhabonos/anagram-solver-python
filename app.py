from flask import Flask
from flask import request


app = Flask(__name__)


@app.route("/")
def hello():
    if request.args.get('test'):
        return 'test'
    else:
        return "NOT test"
