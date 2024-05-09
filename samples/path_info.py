import backpipe

server = backpipe.BackPipe()

@server.get()
def respond(r: backpipe.Request):
    return (200, f"Path: {r.path}\nParams (Query): {r.params}")

server.run()