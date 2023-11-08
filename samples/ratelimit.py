import backpipe

server = backpipe.BackPipe(port=8000)

server.set_ratelimit(10)

@server.get
def get(r):
    return (200, "Got it!")

@server.ratelimit
def limited(r: backpipe.Request):
    return (429, f"You ({r.address}) were rate limited for spamming.")

server.run()