import backpipe

server = backpipe.BackPipe()

@server.post()
def respond(r: backpipe.Request):
    return (200, r.body)

server.run()