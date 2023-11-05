import backpipe

server = backpipe.BackPipe()

@server.unknown
def unsupported_method(r: backpipe.Request):
    return f"the method {r.method} is not supported."

server.run()