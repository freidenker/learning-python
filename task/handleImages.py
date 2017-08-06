import os
import json

def getNamesWithTag(jsonfile):
    """get images name with tag from json to list"""
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

# docker pull images
for image in getNamesWithTag("images.json"):
    print("#####docker pull "+ image)
   #os.system("docker pull SHC-ITSMAX-DOCKER-REG.hpeswlab.net:5000/itsma/" + image)
    print("#####docker save -o /tmp/xservice-images/"+image.replace(":","-"))


def getnames(jsonfile):
    """get only images name from jsonfile"""
    images_list=[]
    with open(jsonfile) as json_data:
         data = json.load(json_data)
         for image in data["images"]:
             name=image["image"].split(":")[0] 
             print("get only image name: " + name)
             images_list.append(name)
    return images_list



def getImagesdict(jsonfile):
    """get images name and tag as a python dictionary"""
    images_dict={}
    with open(jsonfile) as json_data:
         data = json.load(json_data)
         for image in data["images"]:
             name=image["image"].split(":")[0]
             tag=image["image"].split(":")[1]
             print("get image name as key and tag as value:--- "+ name +" : "+tag)
             images_dict[name]=tag 
    return images_dict

#print(len(getImagesdict("images.json")))


def handleImages(twoImagesJsons):
    """docker tag images"""
    images_name = [] 
    images_dict_org = {}
    images_dict_org = {}
    json_org = twoImagesJsons[0]
    json_des = twoImagesJsons[1]
    
    images_names_org = getnames(json_org)
    images_names_des = getnames(json_des)
    images_dict_org = getImagesdict(json_org)
    images_dict_des = getImagesdict(json_des)
    if len(images_dict_org) == len(images_dict_des) and images_names_org == images_names_des  :
       count=0;
       for name in images_names_org:
           count+=1
           orgtag = images_dict_org[name]
           destag = images_dict_des[name]
           print(count)
        #   print(" docker pull SHC-ITSMAX-DOCKER-REG.hpeswlab.net:5000/itsma/" + name + ":" + orgtag)
        #   print(" docker save -o /tmp/xservice-images/" + name + "-" + orgtag + ".tar" + " SHC-ITSMAX-DOCKER-REG.hpeswlab.net:5000/itsma/"+ name + ":" + orgtag)
           print(" docker load --input /tmp/xservice-images/"+ name + "-" + orgtag + ".tar")
        ##   os.system(" docker load --input /tmp/xservice-images/"+ name + "-" + orgtag + ".tar")
           print(" docker tag SHC-ITSMAX-DOCKER-REG.hpeswlab.net:5000/itsma/" + name + ":" + orgtag + " localhost:5000/hpeswitomsandbox/" + name + ":" + destag)
        ##   os.system(" docker tag SHC-ITSMAX-DOCKER-REG.hpeswlab.net:5000/itsma/" + name + ":" + orgtag + " localhost:5000/hpeswitomsandbox/" + name + ":" + destag)
           print(" docker push localhost:5000/hpeswitomsandbox/" + name + ":" + destag)
        ##   os.system(" docker push localhost:5000/hpeswitomsandbox/" + name + ":" + destag)
          
                


twoImagesJsons=["org.json","des.json"]

handleImages(twoImagesJsons)

## docker pull and save image, then uploads to aws s3
print("aws s3 cp /tmp/xservice-images/ s3://suite-images-one/itsma-xservices/ --exclude \"*\" --include \"*.tar\" --recursive")

## download images.tar to ec2 instance,then  docker load, tag and push image
print("aws s3 sync s3://suite-images-one/itsma-xservices /tmp/xservice-images")



           
       
        
    

