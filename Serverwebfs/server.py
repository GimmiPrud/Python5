from flask import Flask, render_template, request

api = Flask(__name__)

utenti = [['lucio','password1','0'],['gianni','passwoe','0'],['alessia','delaie','1']]

@api.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@api.route('/reg_ok', methods = ['GET'])
def regok():
    return render_template('reg_ok.html')


@api.route('/reg_ko', methods = ['GET'])
def regko():
    return render_template('reg_ko.html')


@api.route('/registrati', methods = ['GET'])
def registrati():
    nome = request.args.get('nome')
    password = request.args.get('password')

    utente = []
    utente.append(nome)
    utente.append(password)
    utente.append('0')

    for u in utenti:
        if u[0] == nome and u[1] == password and u[2] == '0':
            return render_template('reg_ok.html')
        else:
            return render_template('reg_ko.html')


    
api.run(host="0.0.0.0",port=8085)  



