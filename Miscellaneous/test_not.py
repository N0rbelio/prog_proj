from ast import And
import json
with open('test_file.json') as f:
    data = json.load(f)

for item in data["dados"]:
    if item["resultado2"] == item["resultado2"].replace("", "False"):
        with open("test_file.json", "w") as f:
            json.dump(data, f)

for i in range(1, 5):
    if file:"op"== "AND" 
    for j in range(1, 4):
        if item.dados["opt1"]==  item.AND["opt1"] and item.dados["opt2"] == item.AND["opt2"]:
            item.dados["resultado2"].replace("", item.AND["resultado"])


