from twisted.internet import reactor
import struct
import json

class Message:
    def __init__(self,msgType,data):
        self.msgType = msgType
        self.data = data

    def safeSend(self,connectionObj):
        header = struct.pack("!1I", self.data.__len__())
        reactor.callInThread(connectionObj.transport.write, header + str(json.dumps(self.__dict__)).encode())
