from twisted.internet import reactor
import struct
import json

class Temp():
    pass

class Message:
    def __init__(self,data=Temp()):
        self.data = str(data.__dict__)

    def safeSend(self,connectionObj):
        header = struct.pack("!1I", self.data.__len__())
        reactor.callInThread(connectionObj.transport.write, header + str(json.dumps(self.__dict__)).encode())

    def reset(self,data):
        self.data = str(data.__dict__)
