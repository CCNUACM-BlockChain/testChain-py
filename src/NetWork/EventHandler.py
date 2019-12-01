from twisted.internet import reactor, threads, defer
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.internet.protocol import Protocol, ClientCreator
from PeerToPeerClientProtocol import PeerToPeerClientProtocolFactory
from dataModels.IpAddress import IpAddress

"""
def tryConnected(info):
    clientFactory = PeerToPeerClientProtocolFactory()
    reactor.connectTCP(info[1].host, info[1].port, clientFactory).addCallback()

def verify(data,connection):
    verifyDeffer = defer.Deferred()
    verifyDeffer.addCallback(tryConnected,connectedErrorHandler).addCallback(handleEvent,handleEventErroeHandler)
    verifyDeffer.callback((data,Ip))

"""

def handleEvent(data,connection):
    if data.type == 'boardcast':
        pass   
    if data.type == 'verifyserver':
        connection.transport.abortConnection()
