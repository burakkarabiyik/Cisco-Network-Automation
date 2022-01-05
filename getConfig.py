import json
import sys


class ciscocommand:
    __commands=[]
    def __init__(self,hostname,command):
        self.__commands=[]
        self.__hostname=hostname
        for i in command:
            self.__commands.append(i)
        
     
    def getHostname(self):
        return self.__hostname

    def getCommands(self):
        return self.__commands
        

def getConfig():
    try:
        with open("config.txt",'r',encoding='utf-8') as f:
            config=f.read()
    except FileNotFoundError:
        print(f"Credentials File is not found")
        sys.exit()
    data = json.loads(config)
    return data

def getConfigfromDevices():
    data=getConfig()
    commands={}
    for key in data['Routers']:
        commands[key]=ciscocommand(key,data['Routers'][key]["config"])
    return commands