import backpipe

server = backpipe.BackPipe()

@server.any()
def respond(r: backpipe.Request):
    return backpipe.redirect("https://google.com", "If you see this message, then redirects are not enabled by your client")

@server.unknown()
def u_respond(r: backpipe.Request):
    return backpipe.redirect("https://google.com", "If you see this message, then redirects are not enabled by your client")

server.run()