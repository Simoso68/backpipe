import backpipe

server = backpipe.BackPipe()

@server.unknown
def unsupported_method(r: backpipe.Request):
    return (405, f"the method {r.method} is not supported.")

server.run()