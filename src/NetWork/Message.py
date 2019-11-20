
import struct
import json

class Message:
    def __init__(self,msgType,data):
        self.msgType = msgType
        self.data = data

    def send(self,connectionObj):
        header = struct.pack("!1I", self.data.__len__())
        connectionObj.transport.write(header + str(json.dumps(self)).encode())
