from urllib import parse

class Request():
    """
    Request object for functions, that are called on request.

    address: client's IP address
    port: port used by client to connect
    method: HTTP method used by the client
    body: Request body sent by the client
    raw_path: Raw, unprocessed path (includes path and query)
    path: processed path (excludes query)
    params: processed path (excludes path)
    headers: Request headers sent by the client
    """
    def __init__(self, c_addr, path: str, headers, method, body) -> None:
        self.address: str = c_addr[0]
        self.port: int = c_addr[1]
        self.method = method
        self.body = body
        self.raw_path = path
        self.path = parse.urlparse(path).path
        self.params = parse.parse_qs(parse.urlparse(path).query)
        raw_headers = {}
        if headers != {}:
            for h in str(headers).splitlines():
                if h.strip() == "":
                    break
                raw_headers[h.split(":")[0]] = h.split(":", 1)[1][1:]
        self.headers: dict = raw_headers
    def __str__(self) -> str:
        return f"Request({self.address}:{self.port})"
    def __repr__(self) -> str:
        return self.__str__()