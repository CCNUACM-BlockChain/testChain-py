from twisted.internet import reactor
from twisted.internet.task import LoopingCall
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol


class PeerToPeerProtocol(LineReceiver):
    def __init__(self,factory):
       self.factory = factory
    
    def connectionMade(self):
        LineReceiver.connectionMade(self)

    def connectionLost(self, reason):
        LineReceiver.connectionLost(self)
