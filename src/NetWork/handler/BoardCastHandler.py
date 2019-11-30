import random
import sys
import os
sys.path.append('../')
from PeerToPeerHelper import IP_address
from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.internet import reactor, defer

def handleBoardCast(data,func):
    boardCastList = random.sample(IP_address, min(3,len(IP_address)))
    for ip in boardCastList: 
        clientEndPoint = TCP4ClientEndpoint(reactor,ip.host,ip.port)
    #self.clientController = connectProtocol(self.clientEndPoint)