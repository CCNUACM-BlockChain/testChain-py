from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from PeerToPeerServerProtocol import PeerToPeerServerProtocolFactory
from PeerToPeerClientProtocol import PeerToPeerClientProtocolFactory
from DNSRouting import getClientEndPointFromPool
from dataModels import Host

IP_address = []

class PeerToPeerHelper:
    def __init__(self):
        self.serverEndPoint = TCP4ServerEndpoint(reactor, Host.host_port)
    
    def run(self):
        self.serverEndPoint.listen(PeerToPeerServerProtocolFactory())
        reactor.run()
        
h=PeerToPeerHelper()
h.run()