# Cisco Network Automation

#### How it works?
###### Step 1 : Get credentials from credentials.txt as JSON
###### Step 2 : Get config commands from config.txt as JSON
###### Step 3 : Send commands via netmiko to all device same time by threading

- pip install -r requirements.txt
- run main.py
 

### My Topology Start Config
	R0 
		F0/0 IP - 1.1.1.2
		SSH username = cisco password = cisco
	R1 
		F0/0 IP - 2.2.2.2
		SSH username = cisco password = cisco
	R2 
		F0/0 IP - 3.3.3.2
		SSH username = cisco password = cisco

### My Goal
	R0
		Giving IP address for e1/0 
		Adding dinamic routing protocol (EIGRP AS 40)
	R1
		Giving IP address for e1/0  and e1/1
		Adding dinamic routing protocol (EIGRP AS 40)
		Adding dinamic routing protocol (BGP AS 1)
	R2
		Giving IP address for e1/0 
		Adding dinamic routing protocol (BGP AS 40)
		



### My Topology

![](https://raw.githubusercontent.com/burakkarabiyik/cisco-network-automation/main/ss.png)
