import os
import json

def getNames(jsonfile):
    """get images name from json to list"""
    images_list=[]
    with open(jsonfile) as json_data:
         data = json.load(json_data)
         for image in data["images"]:
             print("get image name: " + image["image"])
             images_list.append(image["image"])
    return images_list

# print(getNames("images.json"))
#print(getNames("images.json"))
#print("type of imagesname is: " + type(getNames("images.json")))
for image in getNames("images.json"):
   # print(image)
   os.system("docker pull SHC-ITSMAX-DOCKER-REG.hpeswlab.net:5000/itsma/" + image)
