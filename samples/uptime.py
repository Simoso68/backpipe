from backpipe import *

server = BackPipe()

@server.get
def respond(r):
    return (200, str(server.uptime()))

server.run()