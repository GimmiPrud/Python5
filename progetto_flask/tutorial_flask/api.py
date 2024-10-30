# Concetti base per creare un applicazione con flask 

from flask import Flask, url_for, render_template, request
from markupsafe import escape
# La libreria MarkupSafe di Python è utilizzata per rendere sicuro l'uso di stringhe in contesti HTML e XML 
# la funzione escape di MarkupSafe converte i caratteri speciali in entità HTML sicure

api = Flask(__name__) # crezione di un oggetto flask 
api.config['SECRET_KEY'] = 'sto_cazzo' # api.config si utilizza per gestire le impostazioni dell'applicazione 
# si scrive come un dizionario chiave-valore


@api.route("/")  # si definisce la route(percorso) con il decorator(@) associata alla sua funzione specifica 
def salve():
    return "ciao a tutti"

@api.route("/C")
def come_stai():
    return "come state stronzi ?"

@api.route('/user/<username>')  # sulla route possiamo richiamare la variabile della funzione (username) per richiamarla 
def show_user_profile(username): # nell'URL possiamo digitare il nome della variabile che verrà chiamato direttamente sulla pagina web 
    # show the user profile for that user
    return f'profilo di {escape(username)}'

# url_for si utilizza per costruire e generare url per le funzioni definite o aggiornarle quando le modifichi 
with api.test_request_context(): 
    print(url_for('salve'))  # ritornerà l'url della funzione salve --> "/"
    print(url_for('come_stai')) # ritornerà l'url della funzione come_stai --> "/C"
    print(url_for('show_user_profile', username = "Lupo Lucio")) # ritornerà l'url della funzione show_user_profile --> "/user/<username>"
    
# METODI HTTP:
# Sono il modo in cui i CLIENT comunicano con i SERVER 
# esistono diverse http request(richieste):
#- GET --> richiede dati ed informazioni ad un server 
#- POST --> invia dati al server ed informazioni che modificano il server stesso(come un nuovo utente registrato)
#- PUT --> aggiorna o crea una risorsa sul server 
#- DELETE --> elimina una risorsa dal server 
#- HEAD --> Simile a GET, ma richiede solo l'header della risposta, senza il corpo.
#- OPTIONS --> Richiede le opzioni di comunicazione disponibili per una risorsa.

# Questi metodi vengono specificati nell'url della route(percorso):
@api.route('/login', methods=['GET', 'POST']) # methods=['nome metodo/i']
def login():
    pass

# ora creiamo il collegamento e quindi la route del nostro file html con l'app flask:
@api.route('/index', methods=['GET'])
def index():
    welcome = "Ciao a tutti"
    return render_template('index.html', message = welcome) # render_template() permette di richiamare il file html sulla pagina web 
# sul render template possiamo anche aggiungere variabili(come message in questo caso)(ovviamente dobbiamo aggiungere la variabile anche sul file html)
# i file html che creiamo devono essere messi all'interno della cartella che deve chiamarsi templates


# creiamo la URL che comunica con l'http del file html registrazione(sulla directory templates):
@api.route('/registrazione', methods = ['get'])
def gestisci_registrazione():
    nome = request.args.get("nome") # request.args si utilizza per recuperare gli argomenti dalla pagina html  
    password = request.args.get("password") 
    # facendo cosi le informazioni vengono passati e salvati dall'html al backend 
    # gli argomenti all'interno delle variabili devono essere scritte sullo stesso modo sulla pagina html 

    return render_template('registrazione.html', nome=nome, password=password)

#--------------------------------------------------------------------------------------------------------------------#

# possiamo decidere dove sarà visibile la nostra applicazione web:
api.run(host="0.0.0.0", port=5000, debug=False) 

#-------------------------------------------#

# esecuzione applicazione:
# flask --[nome del modulo] run  

# attivazione dell'applicazione con il dedbug:
# flask --[nome del modulo] run --debug 