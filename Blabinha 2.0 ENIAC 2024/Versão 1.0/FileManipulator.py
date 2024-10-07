import json
import os
import time
from datetime import datetime
import urllib.request


tempo = time.localtime()
momentoMacro = str(tempo.tm_mday) + "_" + str(tempo.tm_mon) + "_" + str(tempo.tm_year)

#Lê os jsons dos logs
def readJson(caminho):
    lista = []
    for filename in os.listdir(caminho):
        with open(os.path.join(caminho, filename), 'r',encoding="UTF-8") as f: # open in readonly mode
           lista.append(json.load(f))
    return lista

#Retorna somente os jsons referentes a parte 02
def returnParte2(file_path):
    lista = readJson(file_path)
    parte2 = []
    for l in lista:
        if ( 205 < l['secao'] <= 300):
            parte2.append(l)
    return parte2

#Retorna as falas que tem questões
def returnQuests(file_path):
    
    def retornaMenorTime(valores):
        inicial = valores[0]['TimeStamp']
        final = valores[0]
        for v in valores:
            timeStamp = v['TimeStamp']   
            if(timeStamp <= inicial):
                inicial = timeStamp
                final = v
        return final
    
    lista = readJson(file_path)
    listaCompleta = []
    quests = [213,215,217,219]
    lista1,lista2,lista3,lista4 = ([] for i in range(4))
    for l in lista:
        if ( l['secao'] == quests[0]):
            lista1.append(l)
        if ( l['secao'] == quests[1]):
            lista2.append(l)    
        if ( l['secao'] == quests[2]):
            lista3.append(l)
        if ( l['secao'] == quests[3]):
            lista4.append(l)
    if(len(lista1) != 0 ):
        listaCompleta.append(retornaMenorTime(lista1))
    if(len(lista2) != 0 ):
        listaCompleta.append(retornaMenorTime(lista2))
    if(len(lista3) != 0 ):
        listaCompleta.append(retornaMenorTime(lista3))
    if(len(lista4) != 0 ):
        listaCompleta.append(retornaMenorTime(lista4))


    return listaCompleta

#Retorna o bonus
def returnBonus(file_path):

    def retornaMenorTime(valores):
        inicial = valores[0]['TimeStamp']
        final = valores[0]
        for v in valores:
            timeStamp = v['TimeStamp']   
            if(timeStamp <= inicial):
                inicial = timeStamp
                final = v
        return final
    
    lista = readJson(file_path)
    listaCompleta = []
    for l in lista:
        if ( 250 > l['secao'] > 240):
            print("caiu aqui")
            listaCompleta.append(l)
    if(len(listaCompleta) == 0):
        return False
    return retornaMenorTime(listaCompleta)

#Recebe as variaveis para gerar o log
def completaLog(secao,falaGPT,falaUser,tokens,nome,subpasta,modeloGPT):
    log = {
        "Nome": nome,
        "secao": secao,
        "falaUser": falaUser,
        "falaGPT": falaGPT,
        "Tokens": tokens,
        "TimeStamp": datetime.now().strftime('%Y_%m_%d_%H_%M_%S'),
        "Model": modeloGPT

    }
    print("teste")
    print(log)
    gera_dialog(log,secao,nome,subpasta)

def saveImages(nome,subpasta,imgURL):
    gera_dialog_folder(nome ,subpasta)
    urllib.request.urlretrieve(imgURL, "./DiaLOGS/"+ nome + "/" + str(subpasta) + "/" + datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + ".png")
#Gera a pasta que vai conter os logs
def gera_dialog_folder(nome,subpasta):
    newpath = r".//DiaLOGS//" + nome + r"//" + subpasta 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def return_dialog_folder(nome,subpasta):
    return ".//DiaLOGS//" + nome + r"//" + subpasta 
    
def gera_dialog(log,secao,nome,subpasta,):

    gera_dialog_folder(nome ,subpasta)

    with open("./DiaLOGS/"+ nome + "/" + str(subpasta) + "/" + datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + "sec_" + str(secao) +"_" + ".json", "w",encoding="utf8") as outfile:
        json.dump(log, outfile,ensure_ascii=False)

