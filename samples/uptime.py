import backpipe

server = backpipe.BackPipe()

@server.get
def respond(r: backpipe.BackPipe):
    return (200, str(server.uptime()))

server.run()