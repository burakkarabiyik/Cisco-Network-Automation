import json
import sys


class device:

    def __init__(self, hostname, username, password, ip):
        self.__hostname = hostname
        self.__username = username
        self.__password = password
        self.__ip = ip

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getHostname(self):
        return self.__hostname

    def getIp(self):
        return self.__ip


def getConfig():
    try:
        with open("credentials.txt", 'r') as f:
            config = f.read()
    except FileNotFoundError:
        print(f"Credentials File is not found")
        sys.exit()

    data = json.loads(config)
    return data


def getCredentialsfromDevices():
    data = getConfig()
    devices = {}
    for key in data['Routers']:
        devices[key] = device(key, data['Routers'][key]["username"],
                              data['Routers'][key]["password"], data['Routers'][key]["ip"])
    return devices
