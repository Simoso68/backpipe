from urllib import parse

class Request():
    def __init__(self, c_addr, path: str, headers, method) -> None:
        self.address: str = c_addr[0]
        self.port: int = c_addr[1]
        self.method = method
        self.path = parse.urlparse(path).path
        self.params = parse.parse_qs(parse.urlparse(path).query)
        raw_headers = {}
        for h in str(headers).splitlines():
            if h.strip() == "":
                break
            raw_headers[h.split(":")[0]] = h.split(":", 1)[1][1:]
        self.headers: dict = raw_headers