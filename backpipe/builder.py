from .server import BackPipeServer
from .host import Server
from colorama import Fore, Back, init
from .defaults import *

init()

class BackPipeBuilder():
    def __init__(self, addr, port) -> None:
        self.addr = addr
        self.port = port
        self.get = undefined
        self.post = undefined
        self.put = undefined
        self.patch = undefined
        self.delete = undefined
        self.unknown = unknown_method
        self.blocked_msg = blocked_default
        self.block_addrs = []
        self.ratelimit = -1
        self.ratelimit_message = ratelimited_default
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
    def set_blocked(self, f):
        self.blocked_msg = f
    def block_address(self, addrs):
        self.block_addrs.extend(addrs)
    def run(self):
        try:
            print(f"\r{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Starting server ...")
            print(f"\r{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Press {Fore.LIGHTRED_EX}Ctrl + C{Fore.RESET} to quit.\n")
            backpipe_server = Server(self.get, self.post, self.put, self.patch, self.delete, self.unknown, self.blocked_msg, self.block_addrs, ratelimit=(self.ratelimit, self.ratelimit_message),server_address=(self.addr, self.port), RequestHandlerClass=BackPipeServer)
            backpipe_server.serve_forever()
        except KeyboardInterrupt:
            print(f"\r{Back.LIGHTRED_EX}{Fore.BLACK} EXIT {Back.RESET}{Fore.RESET} Received Keyboard interrupt, shutting down server.")
            backpipe_server.clearing_thread.kill()
        except Exception as x:
            print(f"\r{Back.LIGHTRED_EX}{Fore.BLACK} CRASH {Back.RESET}{Fore.RESET} {Fore.BLUE}{type(x).__name__}{Fore.RESET}: {Fore.LIGHTBLUE_EX}{x}{Fore.RESET}")
            try:
                backpipe_server.shutdown()
            except Exception:
                pass
            try:
                backpipe_server.clearing_thread.kill()
            except Exception:
                pass