import json
with open("test_file.json", "r") as jsonFile:
    data = json.load(jsonFile)

data["location"] = "NewPath"

with open("test_file.json", "r+") as jsonFile:
    data = json.load(jsonFile)

    data["location"] = "NewPath"

    jsonFile.seek(0)  # rewind
    json.dump(data, jsonFile)
    jsonFile.truncate()