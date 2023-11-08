from .builder import BackPipeBuilder
from colorama import Fore, Back, init

init()

class BackPipe():
    def __init__(self, address: str = "", port: int = 3000) -> None:
        self.__builder__ = BackPipeBuilder(address, port)
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
        def wrapper():
            self.__builder__.set_get(function)
        return wrapper()
    def post(self, function):
        def wrapper():
            self.__builder__.set_post(function)
        return wrapper()
    def put(self, function):
        def wrapper():
            self.__builder__.set_put(function)
        return wrapper()
    def patch(self, function):
        def wrapper():
            self.__builder__.set_patch(function)
        return wrapper()
    def delete(self, function):
        def wrapper():
            self.__builder__.set_delete(function)
        return wrapper()
    def unknown(self, function):
        def wrapper():
            self.__builder__.set_unknown(function)
        return wrapper()
    def run(self):
        try:
            print(f"\r{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Starting server ...")
            print(f"\r{Back.YELLOW}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Press {Fore.LIGHTRED_EX}Ctrl + C{Fore.RESET} to quit.\n")
            self.__builder__.run()
        except KeyboardInterrupt:
            print(f"\r{Back.LIGHTRED_EX}{Fore.BLACK} EXIT {Back.RESET}{Fore.RESET} Received Keyboard interrupt.")
            exit(0)