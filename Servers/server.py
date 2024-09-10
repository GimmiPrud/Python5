from flask import Flask, render_template

api = Flask(__name__)

@api.route('/', methods = ['GET'])
def index():
    return render_template('index.html')


@api.route('/', methods = ['GET'])
def indexx():
    return render_template('index2.html')

api.run(host="127.0.0.1",port=8085)

