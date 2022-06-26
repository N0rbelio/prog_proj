import json
with open('test_file.json') as f:
    data = json.load(f)

for data in data['dados']:

    data['resultado2'] = data['resultado2'].replace("", data['resultado1'])

with open('new_data.json', 'w') as f:
    json.dump(data, f)