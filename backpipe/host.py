from socketserver import TCPServer
from multiprocessing import Process
from time import sleep
from colorama import Fore, Back

class Server(TCPServer):
    def __init__(self, get, post, put, patch, delete, unknown, blocked_msg, blocked_addrs, server_address, ratelimit: tuple, RequestHandlerClass, bind_and_activate: bool = True) -> None:
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)
        self.get = get
        self.post = post
        self.put = put
        self.patch = patch
        self.delete = delete
        self.unknown = unknown

        self.blocked_msg = blocked_msg
        self.blocked_addresses = blocked_addrs

        self.ratelimit = ratelimit[0]
        self.ratelimit_msg = ratelimit[1]

        self.client_rq_minute = {}

        self.clearing_thread = Process(target=self.clearing_crqm)
        self.clearing_thread.start()
    def clearing_crqm(self):
        while True:
            sleep(60)
            self.client_rq_minute = {}
            print(f"{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Ratelimits were reset, next reset in 60 seconds.")