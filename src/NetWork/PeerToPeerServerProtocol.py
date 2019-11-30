from twisted.internet import reactor
from twisted.application import internet, service
from twisted.internet.task import LoopingCall
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from Message import Message

class PeerToPeerServerProtocol(LineReceiver):
    def __init__(self,factory):
       self.factory = factory
    
    def connectionMade(self):
        print('connected')

    def connectionLost(self, reason):
        print('disconnected')

    def dataReceived(self,data):
        print('received ', data)
        message = Message('test','ok')
        message.safeSend(self)

        
class PeerToPeerServerProtocolFactory(Factory):
    def __init__(self):
        self.numProtocol = 0

    def buildProtocol(self,addr):
        return PeerToPeerServerProtocol(self)

endpoint = TCP4ServerEndpoint(reactor, 996)
endpoint.listen(PeerToPeerServerProtocolFactory())
reactor.run()
