import json
with open('test_file.json') as f:
    data = json.load(f)

for item in data['dados']:

    item['resultado2'] = item['resultado2'].replace("", item['resultado1'])

with open('new_data.json', 'w') as f:
    json.dump(data, f)