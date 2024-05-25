class URI(bytes):
    def __init__(self) -> None:
        super().__init__()
    def __str__(self) -> str:
        return self.decode()
    def __repr__(self) -> str:
        return f"URI({self.__str__()})"