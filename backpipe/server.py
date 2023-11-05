from http.server import SimpleHTTPRequestHandler
from http import HTTPStatus
from socketserver import *
from colorama import Back, Fore ,init
from typing import Any
from .rq import Request
from .host import Server as BackPipeHoster

init()

def undefined(r: Request):
    return (200, "Undefined")

def unknown_method(r: Request):
    return (405, f"Method {r.method} is not supported.")

class BackPipeServer(SimpleHTTPRequestHandler):
    def __init__(self, request, client_address, server: BackPipeHoster, *, directory: str | None = None) -> None:
        super().__init__(request, client_address, server=server, directory=directory)
    def log_message(self, format: str, *args: Any) -> None:
        additional_info = ""
        if not self.command in ("GET", "POST", "PUT", "PATCH", "DELETE"):
            additional_info = f"{Fore.RED} (Unsupported Method){Fore.RESET}"
        print(f"{Back.LIGHTGREEN_EX}{Fore.BLACK} {self.command} {Back.RESET}{Fore.RESET}{additional_info} Request from {self.client_address[0]}")
    def handle_one_request(self) -> None:
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if len(self.raw_requestline) > 65536:
                self.requestline = ''
                self.request_version = ''
                self.command = ''
                self.send_error(HTTPStatus.REQUEST_URI_TOO_LONG)
                return
            if not self.raw_requestline:
                self.close_connection = True
                return
            if not self.parse_request():
                return
            mname = 'do_' + self.command
            if not hasattr(self, mname):
                answer = self.server.unknown(Request(self.client_address, self.path, self.headers, self.command))
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
    def do_GET(self) -> None:
        answer = self.server.get(Request(self.client_address, self.path, self.headers, self.command))
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
    def do_POST(self) -> None:
        answer = self.server.post(Request(self.client_address, self.path, self.headers, self.command))
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
    def do_PUT(self) -> None:
        answer = self.server.put(Request(self.client_address, self.path, self.headers, self.command))
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
    def do_PATCH(self) -> None:
        answer = self.server.patch(Request(self.client_address, self.path, self.headers, self.command))
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
    def do_DELETE(self) -> None:
        answer = self.server.delete(Request(self.client_address, self.path, self.headers, self.command))
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