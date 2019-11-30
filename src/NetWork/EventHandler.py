from twisted.internet import reactor, threads, defer
def verify(data,connection):
    d = defer.Deferred()
    d.addCallback(tryConnected,connectedErrorHandler).addCallback(handleEvent,handleEventErroeHandler)
    d.callback(data)

def handleEvent(data,reactor,connection):
    verify(data,reactor,connection)
    if data.type == 'boardcast':
        