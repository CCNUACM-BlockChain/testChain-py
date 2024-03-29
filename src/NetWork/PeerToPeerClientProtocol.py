import struct
from twisted.internet import reactor
from twisted.application import internet, service
from twisted.internet.task import LoopingCall
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory, Protocol, ClientFactory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from Message import Message
import sys

message = Message()
headerSize = 4

class PeerToPeerClientProtocol(Protocol):
    def __init__(self,factory):
       self.factory = factory
    
    def connectionMade(self):
        print('connected',self.transport.getPeer())
        self.factory.numPorts += 1
        message.reset('ping')
        message.safeSend(self)
        self.stopProtocol()


    def connectionLost(self, reason):
        print('disconnected')

    def dataReceived(self,data):
        self.factory.dataBuffer += data
        while True:
            if len(self.factory.dataBuffer) < headerSize:
                break
            bodySize = struct.unpack('!1I', self.factory.dataBuffer[:headerSize])[0]
            if len(self.factory.dataBuffer) < headerSize + bodySize:
                break
            data = self.factory.dataBuffer[headerSize:headerSize + bodySize]
            self.factory.dataBuffer = self.factory.dataBuffer[headerSize + bodySize:]
        

        
class PeerToPeerClientProtocolFactory(ClientFactory):
    def __init__(self):
        self.numProtocol = 0
        self.dataBuffer = bytes()

    def startedConnecting(self, connecter):
        print('start Connecting')

    def buildProtocol(self,addr):
        return PeerToPeerClientProtocol(self)
    
    def clientConnectionFailed(self, connector, reason):
        print('connected failed')
    
    def clientConnectionLost(self, connector, reason):
        print("Connection failed. Reason:", reason)