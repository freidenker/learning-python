import json

with open('images.json') as json_data:
    d = json.load(json_data)
    print(len(d["images"]))
