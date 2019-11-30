import time
import dataModels.Host as Host

class Ping():
    def __init__(self):
        self.host = Host.host_ip
        self.port = Host.host_port
        self.timeStamp = time.time() 
        self.type = 'ping'