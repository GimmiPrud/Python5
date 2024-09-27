import json, requests

base_url = "http://127.0.0.1:8080"

def Richiedi_dati_cittadino():
    nome = input("Inserisci nome cittadino: ")
    cognome = input("Inserisci cognome cittadino: ")
    data_nascita = input("inserisci data di nascita: ")
    codice_fiscale = input("inserisci codice fiscale: ")
    j_request = {"nome": nome, "cognome": cognome, "data nascita": data_nascita, "codice fiscale": codice_fiscale}
    return j_request


def CreaInterfaccia():
    print("Operazioni disponibili")
    print("1. Inserisci cittadino (es. atto di nascita)")
    print("2. Richiedi dati cittadino (es. cert. residenza)")
    print("3. Modifica dati cittadino")
    print("4. Elimina Cittadino")
    print("5. Exit")


CreaInterfaccia()
sOper = input("Seleziona operazione: ")
while (sOper != "5"):
    if sOper == "1":
        api_url = base_url + "/add_cittadino"
        json_data_request = Richiedi_dati_cittadino()
        try:
            response = requests.post(api_url, json= json_data_request)
            print(response.status_code)
            print(response.headers["Content-Type"])
            data1 = response.json()
            print(data1)
        except:
            print("Problemi di comunicazione con il server, riprovare")
    
    CreaInterfaccia()
    sOper = input("Seleziona operazione")


