import backpipe.server as server
from .host import Server

class BackPipeBuilder():
    def __init__(self, addr, port) -> None:
        self.addr = addr
        self.port = port
        self.get = server.undefined
        self.post = server.undefined
        self.put = server.undefined
        self.patch = server.undefined
        self.delete = server.undefined
        self.unknown = server.unknown_method
        self.ratelimit = -1
        self.ratelimit_message = server.ratelimited_default
    def set_get(self, f):
        self.get = f
    def set_post(self, f):
        self.post = f
    def set_put(self, f):
        self.put = f
    def set_patch(self, f):
        self.patch = f
    def set_delete(self, f):
        self.delete = f
    def set_unknown(self, f):
        self.unknown = f
    def run(self):
        Server(self.get, self.post, self.put, self.patch, self.delete, self.unknown, ratelimit=(self.ratelimit, self.ratelimit_message),server_address=(self.addr, self.port), RequestHandlerClass=server.BackPipeServer).serve_forever()