import backpipe

server = backpipe.BackPipe()

def respond(r: backpipe.Request):
    return (200, r.uri)

@server.any()
def any_respond(r: backpipe.Request):
    return respond(r)

@server.unknown()
def unknown_respond(r: backpipe.Request):
    return respond(r)

server.run()