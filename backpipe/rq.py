from urllib import parse

class Request():
    """
    Request Object for function, that are called on request.
    """
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
    def __str__(self) -> str:
        return f"Request({self.address}:{self.port})"
    def __repr__(self) -> str:
        return self.__str__()