def file_hoster(addr, port):
    import backpipe
    import os
    import platform
    import urllib

    server = backpipe.BackPipe(addr, port)

    server.set_ratelimit(60)

    @server.any()
    def wrong_method(r: backpipe.Request):
        return (405, f"unsupported method: {r.method}, use GET")
    
    @server.unknown()
    def unknown_method(r: backpipe.Request):
        return (405, f"unsupported method: {r.method}, use GET")

    @server.get()
    def respond(r: backpipe.Request):
        try: 
            if platform.system() == "Windows":
                PATH = urllib.parse.unquote(f"C:{r.path}")
            else:
                PATH = urllib.parse.unquote(r.path)

            if not os.path.exists(PATH):
                return (404, "file not found.")
    
            if os.path.isdir(PATH):
                HTML = backpipe.tools.html.HTML()

                if r.path == "/":
                    CURRENT_DIR = r.path[:-1]
                else:
                    CURRENT_DIR = r.path

                for o in os.listdir(PATH):
                    HTML.add_tag("a", o, {"href":f"{CURRENT_DIR}/{o}"})
                    HTML.add_tag_self_closing("br")
                return (200, HTML.text())
            else:
                return (200, open(PATH, "rb").read())
        except PermissionError:
            return (403, "can not access object")
        
    @server.ratelimit()
    def ratelimit_respond(r: backpipe.Request):
        return (429, "you sent too many requests")
    
    server.run()