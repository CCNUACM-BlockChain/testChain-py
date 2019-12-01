import json
from twisted.internet import reactor, threads, defer
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.internet.protocol import Protocol, ClientCreator
from PeerToPeerClientProtocol import PeerToPeerClientProtocolFactory
from dataModels.IpAddress import IpAddress
from Message import Message
from tcp_latency import measure_latency
from handler.BoardCastHandler import handleBoardCast

ccnu = 'ccnuacm-bocai.com'
hport = 996

def tryConnected(host,port):
    latencyList = measure_latency(host=host, port=port, runs=3, timeout=2.5)
    for latency in latencyList:
        if latency != None:
            return True
    return False

def verify(data):
    return tryConnected(data.host,data.port)

def handleEvent(data,connection):
    data = json.loads(data.decode())
    print(data['dataType'])
    message = Message(dataType=data['dataType'],host=data['host'],port=data['port'],data=data['data'])
    return 
    if message.dataType == 'boardcast':
        pass   
    if message.dataType == 'verifyserver':
        connection.transport.abortConnection()


tryConnected(ccnu,hport)
reactor.run()