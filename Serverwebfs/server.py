from flask import Flask, render_template

api = Flask(__name__)

@api.route('/', methods = ['GET'])
def index():
    return render_template('index.html')


@api.route('/', methods = ['GET'])
def indexx():
    return render_template('index2.html')


@api.route('/', methods = ['GET'])
def regok():
    return render_template('reg_ok.html')


@api.route('/', methods = ['GET'])
def regko():
    return render_template('reg_ko.html')

api.run(host="0.0.0.0",port=8085) 



