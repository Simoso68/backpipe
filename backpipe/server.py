from http.server import SimpleHTTPRequestHandler
from socketserver import *
from colorama import Back, Fore , init
from typing import Any

from .rq import Request
from .host import Server as BackPipeHoster
from .config import config
from .redirect import BackPipeRedirect

init()

class BackPipeServer(SimpleHTTPRequestHandler):
    def __init__(self, request, client_address, server: BackPipeHoster, *, directory: str | None = None) -> None:
        super().__init__(request, client_address, server=server, directory=directory)
    def log_message(self, format: str, *args: Any) -> None:
        additional_info = ""
        if not self.command in ("GET", "POST", "PUT", "PATCH", "DELETE"):
            additional_info = f"{Fore.RED} (Unsupported Method){Fore.RESET}"
        if self.command == None:
            if self.uri_too_long:
                additional_info = f"{Fore.RED} (URI too long){Fore.RESET}"
            print(f"{Back.YELLOW}{Fore.BLACK} EMPTY {Back.RESET}{Fore.RESET}{additional_info} Request from {self.client_address[0]}")
            return
        else:
            print(f"{Back.LIGHTGREEN_EX}{Fore.BLACK} {self.command} {Back.RESET}{Fore.RESET}{additional_info} Request from {self.client_address[0]}")
    def handle_one_request(self) -> None:
        # RQ HANDLING
        try:
            self.uri_too_long = False
            self.raw_requestline = self.rfile.readline(self.server.uri_limit + 1)
            if len(self.raw_requestline) > self.server.uri_limit:
                self.uri_too_long = True
                self.requestline = ""
            if not self.raw_requestline:
                self.close_connection = True
                return
            if not self.parse_request():
                return
            if self.uri_too_long:
                self.send_response(414)
                if config.use_html_header:
                    self.send_header("Content-Type", "text/html")
                self.end_headers()
                self.wfile.write(self.server.uri_limited_msg)
                return
            
            self.body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
            
            mname = f'do_{self.command}'
            # RATE LIMIT CHECKING
            ratelimit = self.server.ratelimit

            if self.client_address[0] in self.server.blocked_addresses:
                print(f"{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET} {Fore.LIGHTRED_EX}Latest request from {self.client_address[0]} was blocked (Address blocked).{Fore.RESET}")
                answer = self.server.blocked_msg(Request(self.client_address, self.path, self.headers, self.command, self.body))
                self.handlerq(answer)
                return

            try:
                if not ratelimit < 0:
                    if not self.client_address[0] in self.server.ratelimit_exc_addr and not self.path in self.server.ratelimit_exc_path:
                        if self.server.client_rq_minute[self.client_address[0]] >= ratelimit:
                            print(f"{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET} {Fore.LIGHTRED_EX}Latest request from {self.client_address[0]} was blocked (Rate-Limit).{Fore.RESET}")
                            answer = self.server.ratelimit_msg(Request(self.client_address, self.path, self.headers, self.command, self.body))
                            self.handlerq(answer)
                            return
            except KeyError:
                pass

            if not self.client_address[0] in self.server.ratelimit_exc_addr and not self.path in self.server.ratelimit_exc_path:
                self.server.add_ip_ratelimiter(self.client_address[0])

            if not hasattr(self, mname):
                answer = self.server.unknown(Request(self.client_address, self.path, self.headers, self.command, self.body))
                if isinstance(answer, BackPipeRedirect):
                    self.send_response(301)
                    self.send_header("Location", answer.location)
                    if config.use_html_header:
                        self.send_header("Content-Type", "text/html")
                    self.end_headers()
                    if isinstance(answer.message, str):
                        self.wfile.write(answer.message.encode())
                    else:
                        self.wfile.write(answer.message)
                    return
                if not isinstance(answer[0], int):
                    raise TypeError(f"HTTP status code must be 'int' not '{type(answer[0]).__name__}'")
                self.send_response(answer[0])
                self.end_headers()
                if isinstance(answer[1], str):
                    self.wfile.write(answer[1].encode())
                elif isinstance(answer[1], bytes):
                    self.wfile.write(answer[1])
                else:
                    raise TypeError(f"HTTP content must be 'str' or 'bytes' not '{type(answer[1]).__name__}'")
                return
            method = getattr(self, mname)
            method()
            self.wfile.flush()
        except TimeoutError as e:
            self.log_error("Request timed out: %r", e)
            self.close_connection = True
            return
    def handlerq(self, answer):
        if isinstance(answer, BackPipeRedirect):
            self.send_response(301)
            self.send_header("Location", answer.location)
            if config.use_html_header:
                self.send_header("Content-Type", "text/html")
            self.end_headers()
            if isinstance(answer.message, str):
                self.wfile.write(answer.message.encode())
            else:
                self.wfile.write(answer.message)
            return
        if not isinstance(answer[0], int):
            raise TypeError(f"HTTP status code must be 'int' not '{type(answer[0]).__name__}'")
        self.send_response(answer[0])
        if config.use_html_header:
            self.send_header("Content-Type", "text/html")
        self.end_headers()
        if isinstance(answer[1], str):
            self.wfile.write(answer[1].encode())
        elif isinstance(answer[1], bytes):
            self.wfile.write(answer[1])
        else:
            raise TypeError(f"HTTP content must be 'str' or 'bytes' not '{type(answer[1]).__name__}'")
    def do_GET(self) -> None:
        answer = self.server.get(Request(self.client_address, self.path, self.headers, self.command, self.body))
        self.handlerq(answer)
    def do_POST(self) -> None:
        answer = self.server.post(Request(self.client_address, self.path, self.headers, self.command, self.body))
        self.handlerq(answer)
    def do_PUT(self) -> None:
        answer = self.server.put(Request(self.client_address, self.path, self.headers, self.command, self.body))
        self.handlerq(answer)
    def do_PATCH(self) -> None:
        answer = self.server.patch(Request(self.client_address, self.path, self.headers, self.command, self.body))
        self.handlerq(answer)
    def do_DELETE(self) -> None:
        answer = self.server.delete(Request(self.client_address, self.path, self.headers, self.command, self.body))
        self.handlerq(answer)