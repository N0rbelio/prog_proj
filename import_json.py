from cgi import print_form
import json
with open('file.json') as f:
    file = json.load(f)

with open('file_AND.json') as f:
    file_AND = json.load(f)

with open('file_NOT.json') as f:
    file_NOT = json.load(f)

 #if file.opt1()file.opt2 == file_AND.opt1, file_AND.opt2) 
print(file)
print(file["dados"])

for plogica in file["dados"]: #faz o ciclo da porta_logica que se encontra no dicionario dados do ficheiro file.json 
   # print(plogica)

######################################################
#################        AND         #################
######################################################
    if plogica["op"] == "AND": #se a porta_logica "op" for igual a AND 
        for pAND in file_AND["AND"]: # entao vamos fazer o ciclo da porta_AND que se encontra no dicionario AND do ficheiro file_AND.json 
            if (plogica['opt1'] == pAND["opt1"]) and (plogica['opt2'] == pAND["opt2"]):
                res1=pAND["resul"]
                print(res1)
                plogica["resultado"]=res1
            with open('file.json', 'w') as f:
                json.dump(file, f)

######################################################
#################        OR         ##################
######################################################



######################################################
#################        NOT         #################
######################################################

    elif plogica["op"] == "NOT":
        for pNOT in file_NOT["NOT"]:
                if plogica['opt1'] == pNOT["opt1"]:
                    res3int=pNOT["res"]
                    
                    print(res3)

                    plogica["resultado"]=res3
                with open('file.json', 'w') as f:
                    json.dump(file, f)

quit()
#for plogica in file["dados"]: #faz o ciclo da porta_logica que se encontra no dicionario dados do ficheiro file.json 
   # print(plogica)
if plogica["op"] == "AND": #se a porta_logica "op" for igual a AND 
    for pAND in file_AND["AND"]: # entao vamos fazer o ciclo da porta_AND que se encontra no dicionario AND do ficheiro file_AND.json 
        if (plogica['opt1'] == pAND["opt1"]) and (plogica['opt2'] == pAND["opt2"]):
            res=pAND["resultado"]




            #plogica['opt1']= plogica['opt2'] and plogica['resultado0'].replace('',pAND['resultado'])
quit()





with open('file.json', 'w') as f:
    json.dump(file, f)
                             
                             #dados[0]["resultado"] = res



for plogica in file["dados"]: #faz o ciclo da porta_logica que se encontra no dicionario dados do ficheiro file.json 
   # print(plogica)

    if plogica["op"] == "AND": #se a porta_logica "op" for igual a AND 
        for pAND in file_AND["AND"]: # entao vamos fazer o ciclo da porta_AND que se encontra no dicionario AND do ficheiro file_AND.json 
                print(pAND)
                if (plogica['opt1'] and pAND["opt1"]) == (plogica['opt2'] and pAND["opt2"]):
                #if (plogica['opt1'] and plogica["opt2"]) == (pAND['opt1'] and pAND["opt2"]):
                    plogica["resultado0"].replace("" ,pAND["resultado"])

                    with open('file.json', 'w') as f:
                            json.dump(file, f)
                    





print()
print()
print()
print(plogica['opt1'])
print(plogica['opt2'])
print(pAND['opt1'])
print(pAND['opt2'])
print()
print(plogica['resultado0'])
print(pAND['resultado'])






for i in range(1,5):
    for test in file['op']: 
        if file["op"] == ["AND"]:
            for i in range(1,4):
                for file_AND in file_AND['AND']: 

                    if (file['opt1'] and file["opt2"]) == (file_AND['opt1'] and file_AND["opt2"]):
                        file["resultado0"].replace("", file_AND["resultado"])
                        

            
with open('file.json', 'w') as f:
    json.dump(file, f)



# elif file["op"] == file_OR["OR"]:
#     # load do json OR
#         o = open ('file_OR.json')
#         file_OR=json.load(o)
#         for i in file ['file_OR']:
#             print (i)
#         o.close()

# else: 
#     file["op"] == file_NOT["NOT"]
#     # load do json NOT
#     n = open ('file_NOT.json')
#     file_NOT=json.load(n)
#     for i in file ['file_NOT']:
#         print (i)
#     n.close()