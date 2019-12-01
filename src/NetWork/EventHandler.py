import json
from twisted.internet import reactor, threads, defer
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.internet.protocol import Protocol, ClientCreator
from PeerToPeerClientProtocol import PeerToPeerClientProtocolFactory
from dataModels.IpAddress import IpAddress
from Message import Message

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
    data = json.loads(data.decode())
    print(data['dataType'])
    message = Message(dataType=data['dataType'],host=data['host'],port=data['port'],data=data['data'])
    return 
    if message.dataType == 'boardcast':
        pass   
    if message.dataType == 'verifyserver':
        connection.transport.abortConnection()
