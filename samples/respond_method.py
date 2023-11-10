import backpipe

server = backpipe.BackPipe()

@server.any
def respond(r: backpipe.Request):
    return (200, r.method)

@server.unknown
def delete(r: backpipe.Request):
    return (200, r.method)

server.run()