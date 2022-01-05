from netmiko import ConnectHandler

def sendMyCommand(ip,username,password,commands,hostname):
    Network_Device = {
    "host": ip,
    "username": username,
    "password": password,
    'device_type': 'cisco_ios',
    'port': 22,
    }
    try:
        net_connect = ConnectHandler(**Network_Device)
        print(f"Connected to {hostname} ")
        net_connect.send_config_set(commands)
        print(f"{hostname} has been completed")
        net_connect.disconnect()
            
    except Exception:
        print(f"Connection error from {hostname} ")
                
    
        
    
    
    