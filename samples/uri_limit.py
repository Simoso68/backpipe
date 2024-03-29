import backpipe

server = backpipe.BackPipe()

@server.get
def coinflip(r: backpipe.Request):
    return (200, "Looks like you didn't exceed the URI limit!")

server.set_uri_limit(100)
server.uri_limit_message("Looks like you exceeded the URI limit!")

server.run()