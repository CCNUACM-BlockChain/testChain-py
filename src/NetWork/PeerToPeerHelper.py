from twisted.internet.protocol import Factory, connectionDone
from twisted.internet import reactor, protocol


class QuoteProtocol(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):  # 建立连接后的回调函数
        self.factory.numConnections += 1

    def dataReceived(self, data):  # 接收到数据后的回调函数
        print("Number of active connections: %d"
              % self.factory.numConnections)
        print("Received:%s\n Sending: %s" % (data, self.getQuote()))

        self.transport.write(self.getQuote())
        self.updateQuote(data)

    def connectionLost(self, reason=connectionDone):  # 断开连接后的反应
        self.factory.numConnections -= 1

    def getQuote(self):
        return self.factory.quote

    def updateQuote(self, quote):
        self.factory.quote = quote


class QuoteFactory(Factory):
    numConnections = 0

    def __init__(self, quote=None):  # 数据接收后放在在quote中
        self.quote = quote or str("Test").encode("utf8")

    def buildProtocol(self, addr):
        return QuoteProtocol(self)


reactor.listenTCP(8000, QuoteFactory())
reactor.stop()
reactor.run()