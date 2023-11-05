from .builder import BackPipeBuilder
from colorama import Fore, Back, init

init()

class BackPipe():
    def __init__(self, address: str = "", port: int = 3000) -> None:
        self.__builder__ = BackPipeBuilder(address, port)
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
            print(f"\r{Back.LIGHTGREEN_EX}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Starting server ...")
            print(f"\r{Back.LIGHTGREEN_EX}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} Press {Fore.LIGHTRED_EX}Ctrl + C{Fore.RESET} to quit.\n")
            self.__builder__.run()
        except KeyboardInterrupt:
            print(f"\r{Back.LIGHTRED_EX}{Fore.BLACK} EXIT {Back.RESET}{Fore.RESET} Received Keyboard interrupt.")
            exit(0)