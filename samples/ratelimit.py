import backpipe

server = backpipe.BackPipe()

server.set_ratelimit(10)
server.set_ratelimit_reset_interval(10)

@server.get()
def get(r: backpipe.Request):
    return (200, "Got it!")

@server.ratelimit()
def limited(r: backpipe.Request):
    return (429, f"You ({r.address}) were rate limited for spamming.")

server.run()