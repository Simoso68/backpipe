import backpipe.server as server
from .host import Server
from colorama import Fore, Back, init

init()

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
    def set_all(self, f):
        self.get = f
        self.post = f
        self.put = f
        self.patch = f
        self.delete = f
    def run(self):
        try:
            print(f"\r{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Starting server ...")
            print(f"\r{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Press {Fore.LIGHTRED_EX}Ctrl + C{Fore.RESET} to quit.\n")
            backpipe_server = Server(self.get, self.post, self.put, self.patch, self.delete, self.unknown, ratelimit=(self.ratelimit, self.ratelimit_message),server_address=(self.addr, self.port), RequestHandlerClass=server.BackPipeServer)
            backpipe_server.serve_forever()
        except KeyboardInterrupt:
            print(f"\r{Back.LIGHTRED_EX}{Fore.BLACK} EXIT {Back.RESET}{Fore.RESET} Received Keyboard interrupt, shutting down server.")
            server.clearing_thread.kill()