from getCredentials import getCredentialsfromDevices
from getConfig import getConfigfromDevices
import threading
from sendMyCommands import sendMyCommand

credentials = getCredentialsfromDevices()
configs = getConfigfromDevices()

threads = []

for key in configs:
    if credentials.get(key) is None:
        print(f"Warning : {key} has no credentials")


for key, credential in credentials.items():
    try:
        th = threading.Thread(target=sendMyCommand, args=(credential.getIp(), credential.getUsername(
        ), credential.getPassword(), configs[key].getCommands(), configs[key].getHostname(),))
        th.start()
        threads.append(th)
    except KeyError:
        print(f"Warning : {key} has no command")
for th in threads:
    th.join()
