from flask import Flask, render_template, request

api = Flask(__name__)

utenti = [['lucio','password1','0'],['gianni','passwoe','0'],['alessia','delaie','0']]

@api.route('/', methods = ['GET'])
def index():
    return render_template('index.html')


@api.route('/reg_ok', methods = ['GET'])
def regok():
    return render_template('reg_ok.html')


@api.route('/reg_ko', methods = ['GET'])
def regko():
    return render_template('reg_ko.html')


@api.route('/reg_ko', methods = ['GET'])
def accesso():
    render_template('accedi.html')



@api.route('/registrati', methods = ['GET'])
def registra():
    nome = request.args.get('nome')
    password = request.args.get('password')

    utente = [nome,password,'0']

    if utente in utenti:
        return render_template('reg_ok.html')
    else:
        return render_template('reg_ko.html')
    

@api.route('/accedi', methods = ['GET'])
def accedi():
    nome = request.args.get('nome')
    password = request.args.get('password')

    for utente in utenti:
        if utente[0]==nome and utente[1]==password and utente[2]=='1':
            return render_template('reg_ok.html')
        else:
            return render_template('reg_ko.html')



if __name__ == '__main__':
    api.run(host="0.0.0.0",port=8085) 



