def redirect_hoster(addr, port):
    import backpipe

    print("Set which path redirects to what website")
    print("Format: {path}={url};{path}={url}")
    print("Example: /google=https://google.com;/youtube=https://youtube.com")
    REDIRECTS = input("redirects: ")
    pages = {}
    for re in REDIRECTS.split(";"):
        page_and_url = re.split("=", 1)
        pages[page_and_url[0]] = page_and_url[1]
    
    server = backpipe.BackPipe(addr, port)

    def respond(r: backpipe.Request):
        try:
            return backpipe.redirect(pages[r.path], f"Redirects to {pages[r.path]}")
        except KeyError:
            return (404, "page not found")

    @server.any()
    def any_respond(r: backpipe.Request):
        return respond(r)
        
    @server.unknown()
    def unknown_respond(r: backpipe.Request):
        return respond(r)

    server.run()