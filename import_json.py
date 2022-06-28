from cgi import print_form
import json
with open('file_feed.json') as f: #abre o ficheiro OR
    file = json.load(f) #define a variavel file para chamar mais tarde o ficheiro 

with open('file_AND.json') as f: #abre o ficheiro OR
    file_AND = json.load(f) #define a variavel file_AND para chamar mais tarde o ficheiro 

with open('file_NOT.json') as f: #abre o ficheiro OR
    file_NOT = json.load(f) #define a variavel file_NOT para chamar mais tarde o ficheiro 

with open('file_OR.json') as f: #abre o ficheiro OR
    file_OR = json.load(f) #define a variavel file_OR para chamar mais tarde o ficheiro 

for plogica in file["dados"]: #faz o ciclo da porta_logica que se encontra no dicionario dados do ficheiro file.json 

######################################################
#################        AND         #################
######################################################
    if plogica["op"] == "AND": #se a porta_logica "op" for igual a AND 
        for pAND in file_AND["AND"]: # entao vamos fazer o ciclo da porta_AND que se encontra no dicionario AND do ficheiro file_AND.json 
            if (plogica['opt1'] == pAND["opt1"]) and (plogica['opt2'] == pAND["opt2"]): #verifica se o opt1 da porta logica é igual á opt1 do AND e verifica se o opt2 da porta logica é igual á opt2 do AND
                res1=pAND["resul"]  #vai guardar o resultado nesta variavel temporaria 
                print(res1) #printa na consola o valor guardado
                plogica["resultado"]=res1 #envia o resultado da variavel temporaria para a variavel resultado do ficheiro file_feed
            with open('file_feed.json', 'w') as f: #abre o ficheiro 
                json.dump(file, f) #faz upload das info para o ficheiro 

######################################################
#################        OR         ##################
######################################################
    if plogica["op"] == "OR": #se a porta_logica "op" for igual a OR 
        for pOR in file_OR["OR"]: # entao vamos fazer o ciclo da porta_AND que se encontra no dicionario AND do ficheiro file_OR.json 
            if (plogica['opt1'] == pOR["opt1"]) and (plogica['opt2'] == pOR["opt2"]): #verifica se o opt1 da porta logica é igual á opt1 do OR e verifica se o opt2 da porta logica é igual á opt2 do OR
                res2=pOR["result"] #vai guardar o resultado nesta variavel temporaria 
                print(res2) #printa na consola o valor guardado
                plogica["resultado"]=res2 #envia o resultado da variavel temporaria para a variavel resultado do ficheiro file_feed
            with open('file_feed.json', 'w') as f: #abre o ficheiro 
                json.dump(file, f) #faz upload das info para o ficheiro 


######################################################
#################        NOT         #################
######################################################

    if plogica["op"] == "NOT":#se a porta_logica "op" for igual a NOT 
        for pNOT in file_NOT["NOT"]:# entao vamos fazer o ciclo da porta_NOTque se encontra no dicionario AND do ficheiro file_NOT.json 
                if plogica['opt1'] == pNOT["opt1"]: #verifica se o opt1 da porta logica é igual á opt1 do not
                    res3=pNOT["res"] #vai guardar o resultado nesta variavel temporaria 
                    print(res3)#printa na consola o valor guardado
                    plogica["resultado"]=res3 #envia o resultado da variavel temporaria para a variavel resultado do ficheiro file_feed
                    with open('file_feed.json', 'w') as f: #abre o ficheiro 
                        json.dump(file, f) #faz upload das info para o ficheiro 
                else:
                    plogica["resultado"]="false" #envia o resultado para a variavel resultado do ficheiro file_feed
                    with open('file_feed.json', 'w') as f: #abre o ficheiro 
                        json.dump(file, f) #faz upload das info para o ficheiro 