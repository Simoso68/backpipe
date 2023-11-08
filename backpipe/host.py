from socketserver import TCPServer

class Server(TCPServer):
    def __init__(self, get, post, put, patch, delete, unknown, server_address, ratelimit: tuple, RequestHandlerClass, bind_and_activate: bool = True) -> None:
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)
        self.get = get
        self.post = post
        self.put = put
        self.patch = patch
        self.delete = delete
        self.unknown = unknown
        self.ratelimit = ratelimit[0]
        self.ratelimit_msg = ratelimit[1]