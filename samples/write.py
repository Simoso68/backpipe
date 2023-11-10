import backpipe

server = backpipe.BackPipe()

@server.any
def get(r: backpipe.Request):
    return (405, "Method not supported, please use POST.")

@server.post
def post(r: backpipe.Request):
    try:
        content = r.headers["txt"]
    except KeyError:
        return (400, "txt header is missing")
    with open(f"{r.address}.txt", "w") as f:
        f.write(content)
    return (200, "File written successfully.")

server.run()