
# esempio di come creare un database:

import sqlite3 as sq # modulo python che integra SQLite per lavorare con i database 

connessione_database = sq.connect('data.db') # db = estensione per i database
# connect() permette di creare un database( e connettersi)

cursore = connessione_database.cursor()
# cursor() ci permette di creare un cursore che esegue i comandi

cursore.execute('CREATE TABLE IF NOT EXSISTS [nome tabella](nome, indirizzo, numero, ip)')
# exectute() ci permette di creare la tabella del database con un nome e i dati che vogliamo creare 

connessione_database.commit()
# si utilizza per salvare i dati che abbiamo creato 

connessione_database.close()
# close() si utilizza per evitare problemi come perdite di risorse e potenziali problemi di integrità dei dati

