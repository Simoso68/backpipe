import backpipe

server = backpipe.BackPipe()

@server.get
def get(r: backpipe.Request):
    return (200, r.method)

@server.post
def post(r: backpipe.Request):
    return (200, r.method)

@server.put
def put(r: backpipe.Request):
    return (200, r.method)

@server.patch
def patch(r: backpipe.Request):
    return (200, r.method)

@server.delete
def delete(r: backpipe.Request):
    return (200, r.method)

@server.unknown
def delete(r: backpipe.Request):
    return (200, r.method)

server.run()