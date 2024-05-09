import backpipe
from random import choice

server = backpipe.BackPipe()

@server.get()
def coinflip(r: backpipe.Request):
    return (200, choice(["Heads", "Tails"]))

server.run()