# coding:utf=8
from flask import Flask
from config import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello pandadex!'


@app.route('/test')
def hello_world():
    return 'test version'




if __name__ == "__main__":

    app.run(host=HOST,port=PORT,debug=DEBUG)


