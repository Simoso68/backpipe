from backpipe.tools.check_type import check

class BackPipeRedirect():
    def __init__(self, location, message) -> None:
        self.location = location
        self.message = message
    def __str__(self) -> str:
        return f"Redirect(location={self.location})"
    def __repr__(self) -> str:
        return self.__str__()

def redirect(location: str, message: str) -> BackPipeRedirect:
    check(location, str, "location")
    check(message, (str, bytes), "message")
    return BackPipeRedirect(location, message)