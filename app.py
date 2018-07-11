# coding:utf=8
from flask import Flask
from config import *
from flask import render_template

app = Flask(__name__)


@app.route('/version')
def hello_world():
    return 'hello pandadex!'


@app.route('/test')
def test():
    return 'test version'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == "__main__":

    app.run(host=HOST, port=PORT, debug=DEBUG)
