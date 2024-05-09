import backpipe

server = backpipe.BackPipe()

@server.get()
def info(r: backpipe.Request):
    return (200, f"""Connection Info:
Path: {r.path}
Params (JSON): {r.params}
Address: {r.address}
Port: {r.port}
Headers (JSON): {r.headers}""")

server.run()