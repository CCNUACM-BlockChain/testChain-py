from twisted.internet import reactor
from dataModels import Host
import struct
import json

class Temp():
    pass

class Message:
    def __init__(self,dataType='',data=Temp()):
        self.data = str(data.__dict__)
        self.host = Host.host_ip
        self.port = Host.host_port
        self.type = dataType

    def safeSend(self,connectionObj):
        header = struct.pack("!1I", self.data.__len__())
        reactor.callInThread(connectionObj.transport.write, header + str(json.dumps(self.__dict__)).encode())

    def reset(self,data,dataType):
        self.data = str(data.__dict__)
        self.dataType = dataType
