from flask import Flask, render_template, request

api = Flask(__name__)

utenti = [['lucio','password1','M','0'],['gianni','passwoe','M','0'],['alessia','delaie','D','0']]

@api.route('/', methods = ['GET'])
def index():
    return render_template('index.html')


@api.route('/a', methods = ['GET'])
def indexx():
    return render_template('index2.html')


@api.route('/ok', methods = ['GET'])
def regok():
    return render_template('reg_ok.html')


@api.route('/ko', methods = ['GET'])
def regko():
    return render_template('reg_ko.html')


@api.route('/registrati', methods = ['GET'])
def registra():
    nome = request.args.get('nome')
    print('Nome inserito', nome)
    password = request.args.get('cognome')
    # devo prendere tutti i dati e verificare se la terna c'è nel vettore degli utenti 
    return render_template('reg_ko.html')


api.run(host="0.0.0.0",port=8085)   


