from cgi import print_form
import json
with open('file_feed.json') as f:
    file = json.load(f)  

with open('file_AND.json') as f: 
    file_AND = json.load(f) 

with open('file_NOT.json') as f: 
    file_NOT = json.load(f)

with open('file_OR.json') as f: 
    file_OR = json.load(f) 

for plogica in file["dados"]:

######################################################
#################        AND         #################
######################################################
    if plogica["op"] == "AND": 
        for pAND in file_AND["AND"]: 
            if (plogica['opt1'] == pAND["opt1"]) and (plogica['opt2'] == pAND["opt2"]):
                res1=pAND["resul"]  #vai guardar o resultado nesta variavel temporaria 
                print(res1) 
                plogica["resultado"]=res1 #envia o resultado da variavel temporaria para a variavel resultado do ficheiro file_feed
            with open('file_feed.json', 'w') as f: 
                json.dump(file, f) 

######################################################
#################        OR         ##################
######################################################
    if plogica["op"] == "OR": 
        for pOR in file_OR["OR"]: 
            if (plogica['opt1'] == pOR["opt1"]) and (plogica['opt2'] == pOR["opt2"]): 
                res2=pOR["result"] 
                print(res2) 
                plogica["resultado"]=res2  #envia o resultado da variavel temporaria para a variavel resultado do ficheiro file_feed
            with open('file_feed.json', 'w') as f:
                json.dump(file, f) 


######################################################
#################        NOT         #################
######################################################

    if plogica["op"] == "NOT":
        for pNOT in file_NOT["NOT"]:
                if plogica['opt1'] == pNOT["opt1"]:
                    res3=pNOT["res"] 
                    print(res3)
                    plogica["resultado"]=res3 
                    with open('file_feed.json', 'w') as f:
                        json.dump(file, f) 
                else:
                    plogica["resultado"]="false"
                    with open('file_feed.json', 'w') as f:
                        json.dump(file, f)
