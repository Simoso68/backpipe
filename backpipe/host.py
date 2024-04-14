from socketserver import TCPServer
from threading import Thread
from time import sleep, time
from colorama import Fore, Back
import ssl

class Server(TCPServer):
    def __init__(self, context, https: dict | None, get, post, put, patch, delete, unknown, uri_limit, uri_limited_msg, blocked_msg, blocked_addrs, server_address, ratelimit: tuple, RequestHandlerClass, bind_and_activate: bool = True) -> None:
        super().__init__(server_address, RequestHandlerClass, bind_and_activate)

        if https != None:
            self.ssl = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
            self.ssl.load_cert_chain(https["certfile"], https["keyfile"])
            self.socket = self.ssl.wrap_socket(self.socket, server_side=True)

        self.https = https

        context.started_at = time()

        self.get = get
        self.post = post
        self.put = put
        self.patch = patch
        self.delete = delete
        self.unknown = unknown

        self.uri_limit = uri_limit
        self.uri_limited_msg = uri_limited_msg

        self.blocked_msg = blocked_msg
        self.blocked_addresses = blocked_addrs

        self.ratelimit = ratelimit[0]
        self.ratelimit_msg = ratelimit[1]
        self.ratelimit_reset = ratelimit[2]
        self.ratelimit_exc_addr = ratelimit[3]
        self.ratelimit_exc_path = ratelimit[4]

        self.client_rq_minute = {}

        self.clearing_thread = Thread(target=self.clearing_crqm)
        self.clearing_thread.start()
    def clearing_crqm(self):
        while True:
            sleep(self.ratelimit_reset)
            self.client_rq_minute = {}
            print(f"{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Ratelimits were reset, next reset in {self.ratelimit_reset} seconds.")
    def add_ip_ratelimiter(self, ip):
        try:
            self.client_rq_minute[ip] += 1
        except KeyError:
            self.client_rq_minute[ip] = 1