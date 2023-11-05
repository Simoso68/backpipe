class Request():
    def __init__(self, c_addr, path: str, headers, method) -> None:
        self.address: str = c_addr[0]
        self.port: int = c_addr[1]
        self.params = {}
        self.method = method
        if not "?" in path:
            self.path = path
        else:
            self.path = path.split("?")[0]
            for p in path.split("?", 1)[1].split("&"):
                self.params[p.split("=")[0]] = p.split("=", 1)[1]
        raw_headers = {}
        for h in str(headers).splitlines():
            if h.strip() == "":
                break
            raw_headers[h.split(":")[0]] = h.split(":", 1)[1][1:]
        self.headers: dict = raw_headers