from .builder import BackPipeBuilder
from .config import config

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
        return f"BackPipe(address='{self.__builder__.addr}', port={self.__builder__.port})"
    def __repr__(self) -> str:
        return self.__str__()
    def set_ratelimit(self, limit: int):
        """
        Set a rate limit for how many requests from one IP address are allowed per minute.
        Set it to a number below 0 to disable rate limiting.
        Default rate limit is -1 (No limit.).
        """
        if not isinstance(limit, int):
            raise TypeError(f"given rate limit must be 'int' not '{type(limit).__name__}'")
        self.__builder__.ratelimit = limit
    def ratelimit(self, function):
        """
        Set a message, that gets responded, when a client is rate limited.
        Default is 'Too many requests from the same client.'
        """
        def wrapper():
            self.__builder__.ratelimit_message = function
        return wrapper()
    def get(self, function):
        """
        Set the GET request handler.
        """
        def wrapper():
            self.__builder__.set_get(function)
        return wrapper()
    def post(self, function):
        """
        Set the POST request handler.
        """
        def wrapper():
            self.__builder__.set_post(function)
        return wrapper()
    def put(self, function):
        """
        Set the PUT request handler.
        """
        def wrapper():
            self.__builder__.set_put(function)
        return wrapper()
    def patch(self, function):
        """
        Set the PATCH request handler.
        """
        def wrapper():
            self.__builder__.set_patch(function)
        return wrapper()
    def delete(self, function):
        """
        Set the DELETE request handler.
        """
        def wrapper():
            self.__builder__.set_delete(function)
        return wrapper()
    def unknown(self, function):
        """
        If an unknown method is used, the set function will handle it.
        """
        def wrapper():
            self.__builder__.set_unknown(function)
        return wrapper()
    def any(self, function):
        """
        Set the handler for GET, POST, PUT, PATCH, DELETE.
        Can be overwritten using the normal way:

        @{server_instance_name}.{method}

        def foo(r):
            return (200, "Blah.")

        """
        def wrapper():
            self.__builder__.set_all(function)
        return wrapper()
    def run(self):
        self.__builder__.run()