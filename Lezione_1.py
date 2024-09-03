# Giammarco Prudenzi
import os

def CercaStringaInNomeFile(sFile,sStringa):
# mettiamo tutto minuscolo
    sFileLC = sFile.lower()
    sStringa = sStringa.lower()
# usiamo sFileLower.find() che torna -1 se la parola non c'è e la pos altrimenti
    if (sFileLC.find(sStringa.lower())>=0):
        return True
    else:
        return False  
# torniamo True o False  


sRoot = input("inserisci directory in cui cercare:")
sParola = input("inserisci parola da cercare:")
sOutDir = input ("inserisci directory di output")

inumfiletrovati = 0
for root,dirs,files in os.walk(sRoot):
    print(f"sto guardando {root} che contiene {len(dirs)} subdir e {len(files)} files")
    for file in files:
        print(f"Devo vedere se {file} contiene {sParola}")
        bRet = CercaStringaInNomeFile(file,sParola)
        if bRet ==True: 
            inumfiletrovati += 1
        else:
         #  bRet = CercaStringaInContenutofile()
            pass    

print(f" Ho trovato {inumfiletrovati} Files")
