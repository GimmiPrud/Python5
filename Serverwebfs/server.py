from flask import Flask, render_template

api = Flask(__name__)

@api.route('/', methods = ['GET'])
def index():
    return render_template('index.html')


@api.route('/v', methods = ['GET'])
def indexx():
    return render_template('index2.html')


@api.route('/n', methods = ['GET'])
def reg_ok():
    return render_template('reg_ok')


@api.route('/r', methods = ['GET'])
def reg_ko():
    return render_template('reg_ko')

api.run(host="0.0.0.0",port=8085) 



