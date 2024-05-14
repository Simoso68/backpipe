from .builder import BackPipeBuilder
from .config import config
from .uptime import _uptime
from backpipe.tools.check_type import check

class BackPipe():
    """
    The class, that is the instance of your API server.
    """
    def __init__(self, address = None, port = None) -> None:
        if address == None:
            set_address = config.default_address
        else:
            set_address = address
        if port == None:
            set_port = config.default_port
        else:
            set_port = port
            
        self.__builder__ = BackPipeBuilder(set_address, set_port)
    def __str__(self) -> str:
        return f"BackPipe(address={self.__builder__.addr.__repr__()}, port={self.__builder__.port})"
    def __repr__(self) -> str:
        return self.__str__()
    # HTTPS support still in Development, uncomment it, if you want to test it.
    #def enable_https(self, certfile, keyfile):
    #    """
    #    Offers integrated SSL support.
    #    Certfiles and Keyfiles can be generated using OpenSSL.
    #    Tools such as CURL or your web browser will raise warnings, that the connection is unsafe if you self-sign your certificate.
    #    """
    #    self.__builder__.https = {"certfile":certfile, "keyfile":keyfile}
    def set_ratelimit(self, limit: int):
        """
        Set a rate limit for how many requests from one IP address are allowed per minute.
        Set it to a number below 0 to disable rate limiting.
        Default rate limit is -1 (No limit.).
        """
        if not isinstance(limit, int):
            raise TypeError(f"given rate limit must be 'int' not '{type(limit).__name__}'")
        self.__builder__.ratelimit = limit
    def ratelimit(self):
        """
        Set a message, that gets responded, when a client is rate limited.
        Default is 'Too many requests from the same client.'
        """
        def wrapper(function):
            self.__builder__.ratelimit_message = function
        return wrapper
    def set_ratelimit_reset_interval(self, time):
        """
        Set a time, that determines how long it takes until the ratelimits are reset.
        Default is 60.
        """
        check(time, (int, float), "time")
            
        self.__builder__.ratelimit_reset = time
    def ratelimit_exception_ipaddr(self, *addresses):
        """
        Set an exception for ratelimiting based on the clients IP address.
        """
        for a in addresses:
            check(a, str, "all addresses")

        self.__builder__.ratelimit_exc_addrs.extend(addresses)
    def ratelimit_exception_paths(self, *paths):
        """
        Set an exception for ratelimiting based on the requested path.
        """
        for p in paths:
            check(p, str, "all paths")

        self.__builder__.ratelimit_exc_paths.extend(paths)
    def uptime(self):
        """
        Uptime counter starts when the server is started.
        """
        return _uptime(self.__builder__)
    def set_uri_limit(self, amount):
        """
        Set the URI limit, which can't be exceeded by the client.
        If the URI limit was exceeded the client gets a special message.
        Default is 65536.
        """
        check(amount, int, "amount")
        
        self.__builder__.uri_limit = amount
    def uri_limit_message(self, message):
        """
        Set the returned message when the client exceeded the URI limit.
        """
        if isinstance(message, str):
            message = message.encode()
        elif isinstance(message, bytes):
            pass
        else:
            raise TypeError(f"message parameter must be 'str' not '{type(message).__name__}'")
        self.__builder__.uri_limit_msg(message)
    def get(self):
        """
        Set the GET request handler.
        """
        def wrapper(function):
            self.__builder__.set_get(function)
        return wrapper
    def post(self):
        """
        Set the POST request handler.
        """
        def wrapper(function):
            self.__builder__.set_post(function)
        return wrapper
    def put(self):
        """
        Set the PUT request handler.
        """
        def wrapper(function):
            self.__builder__.set_put(function)
        return wrapper
    def patch(self):
        """
        Set the PATCH request handler.
        """
        def wrapper(function):
            self.__builder__.set_patch(function)
        return wrapper
    def delete(self):
        """
        Set the DELETE request handler.
        """
        def wrapper(function):
            self.__builder__.set_delete(function)
        return wrapper
    def unknown(self):
        """
        If an unknown method is used, the set function will handle it.
        """
        def wrapper(function):
            self.__builder__.set_unknown(function)
        return wrapper
    def any(self):
        """
        Set the handler for GET, POST, PUT, PATCH, DELETE.
        Can be overwritten using the normal way:

        @{server_instance_name}.{method}

        def foo(r):
            return (200, "Blah.")

        """
        def wrapper(function):
            self.__builder__.set_all(function)
        return wrapper
    def block(self):
        """
        Set the request handler for client's with blocked IP addresses.
        Block an IP address by using {server_instance_name}.block_address("addr1", "addr2") ...
        """
        def wrapper(function):
            self.__builder__.blocked_msg = function
        return wrapper
    def block_address(self, *addresses):
        self.__builder__.block_address(addresses)
    def run(self):
        self.__builder__.run()