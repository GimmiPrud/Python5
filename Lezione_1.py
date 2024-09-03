# Giammarco Prudenzi
import os
import PyPDF2

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

def CercaStringaInTextfile(sFile,sStringa):
    iRet = -1
    with open(sFile,"r") as file1:
        sRiga = file1.readline()
        while (len(sRiga)>0):
            iRet = sRiga.lower().find(sStringa.lower())
            if (iRet >=0):
                return True
            sRiga = file1.readline()
    return False

def CercaStringaInPdffile(sFile,sStringa):
    object = PyPDF2.PdfReader(sFile)
    numPages = len(object.pages)
    for i in range(0, numPages):
        pageObj = object.pages[i]
        text = pageObj.extract_text()
        text = text.lower()
        if(text.find(sStringa)!=-1):
            return True
    return False

def CercaStringaInContenutofile(sPathfile,sStringa):
    sOutFileName,sOutFileExt = os.path.splitext(sPathfile)
    if sOutFileExt.lower() == ".txt":
        bRet = CercaStringaInTextfile(sPathfile,sStringa)
    
    if sOutFileExt.lower()==".pdf":
        bRet = CercaStringaInPdffile(sPathfile,sStringa)

    return bRet


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
            sFilepathcompleto = os.path.join(root,file)
            bRet = CercaStringaInContenutofile(sFilepathcompleto,sParola)
            if (bRet == True):
                inumfiletrovati += 1
        if bRet == True:
            print("Trovata parola in file" + file)

print(f" Ho trovato {inumfiletrovati} Files")

