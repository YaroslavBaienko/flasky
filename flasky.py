import flask
from flask import (
    Flask,
    request,
    make_response
)

app = flask.Flask(__name__)


@app.route('/')
def index():
    return "Hello world!"


@app.route()

if __name__ == '__main__':
    app.run()
