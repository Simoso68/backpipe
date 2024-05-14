def ipaddr_hoster(addr, port):
    import backpipe

    server = backpipe.BackPipe(addr, port)

    @server.any()
    def wrong_method(r: backpipe.Request):
        return (405, f"unsupported method: {r.method}, use GET")
    
    @server.unknown()
    def unknown_method(r: backpipe.Request):
        return (405, f"unsupported method: {r.method}, use GET")

    @server.get()
    def respond(r: backpipe.Request):
        return (200, r.address)

    server.run()