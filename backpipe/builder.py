from .server import BackPipeServer
from .host import Server
from colorama import Fore, Back
from platform import system
from os import kill, getpid
from signal import SIGTERM
from .defaults import *

class BackPipeBuilder():
    def __init__(self, addr, port) -> None:
        self.addr = addr
        self.port = port
        self.https = None
        self.get = undefined
        self.post = undefined
        self.put = undefined
        self.patch = undefined
        self.delete = undefined
        self.unknown = unknown_method
        self.uri_limit = 65536
        self.uri_limit_message = "URI-Limit exceeded."
        self.blocked_msg = blocked_default
        self.block_addrs = []
        self.ratelimit = -1
        self.ratelimit_message = ratelimited_default
        self.ratelimit_reset = 60
        self.ratelimit_exc_addrs = []
        self.ratelimit_exc_paths = []

        self.started_at = 0
    def __str__(self):
        return f"BackPipeBuilder(addr={self.addr.__repr__()}, port={self.port})"
    def __repr__(self):
        return self.__str__()
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
    def uri_limit_msg(self, message):
        self.uri_limit_message = message
    def run(self):
        try:
            if self.addr == "":
                ADDR = "127.0.0.1"
            else:
                ADDR = self.addr
            if system() == "Windows":
                print(f"\r{Back.YELLOW}{Fore.BLACK} COMPATIBILITY {Back.RESET}{Fore.RESET} Running Backpipe servers on Windows might lead to issues")
            print(f"\r{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Starting server ...")
            print(f"\r{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Running on {Fore.LIGHTBLUE_EX}{ADDR}{Fore.RESET}:{Fore.LIGHTGREEN_EX}{self.port}{Fore.RESET}")
            print(f"\r{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Press {Fore.LIGHTRED_EX}Ctrl + C{Fore.RESET} to quit.\n")
            backpipe_server = Server(self, self.https, self.get, self.post, self.put, self.patch, self.delete, self.unknown, self.uri_limit, self.uri_limit_message, self.blocked_msg, self.block_addrs, ratelimit=(self.ratelimit, self.ratelimit_message, self.ratelimit_reset, self.ratelimit_exc_addrs, self.ratelimit_exc_paths), server_address=(self.addr, self.port), RequestHandlerClass=BackPipeServer)
            backpipe_server.serve_forever()
        except KeyboardInterrupt:
            print(f"\r{Back.LIGHTRED_EX}{Fore.BLACK} EXIT {Back.RESET}{Fore.RESET} Received Keyboard interrupt, shutting down server.")
            kill(getpid(), SIGTERM)
        except Exception as x:
            print(f"\r{Back.LIGHTRED_EX}{Fore.BLACK} CRASH {Back.RESET}{Fore.RESET} {Fore.BLUE}{type(x).__name__}{Fore.RESET}: {Fore.LIGHTBLUE_EX}{x}{Fore.RESET}")
            try:
                backpipe_server.shutdown()
            except Exception:
                pass
            try:
                kill(getpid(), SIGTERM)
            except Exception:
                pass