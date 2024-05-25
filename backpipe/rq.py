from urllib import parse
from .uri import URI

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
    def __init__(self, c_addr, path: str, headers, method, body, uri: bytes) -> None:
        self.address: str = c_addr[0]
        self.port: int = c_addr[1]
        self.method: str = method
        self.body: bytes = body
        self.raw_path: str = path
        self.path: str = parse.urlparse(path).path
        self.params: dict[str, list[str]] = parse.parse_qs(parse.urlparse(path).query)
        self.uri: URI = URI(uri)
        raw_headers = {}
        if headers != {}:
            for h in str(headers).splitlines():
                if h.strip() == "":
                    break
                raw_headers[h.split(":")[0]] = h.split(":", 1)[1][1:]
        self.headers: dict[str, str] = raw_headers
    def __str__(self) -> str:
        return f"Request({self.address}:{self.port})"
    def __repr__(self) -> str:
        return self.__str__()