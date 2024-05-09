import backpipe

server = backpipe.BackPipe()

@server.get()
def get(r: backpipe.Request):
    return (200, "Supported!")

@server.post()
def post(r: backpipe.Request):
    return (200, "Supported!")

@server.put()
def put(r: backpipe.Request):
    return (200, "Supported!")

@server.patch()
def patch(r: backpipe.Request):
    return (200, "Supported!")

@server.delete()
def delete(r: backpipe.Request):
    return (200, "Supported!")

server.run()