class Config():
    def __init__(self) -> None:
        self.default_address = ""
        self.default_port = 3000
        self.use_html_header = False
    def address(self, val: str):
        """
        Set the default address.
        BackPipe's default: ''
        """
        if not isinstance(val, str):
            raise TypeError(f"value must be of type 'str' not '{type(val).__name__}'")
        self.use_html_header = val
    def port(self, val: int):
        """
        Set the default port.
        BackPipe's default: 3000
        """
        if not isinstance(val, int):
            raise TypeError(f"value must be of type 'int' not '{type(val).__name__}'")
        self.default_port = val
    def html(self, val: bool):
        """
        Set the default value if the 'text/html' header should be used.
        BackPipe's default: False
        """
        if not isinstance(val, bool):
            raise TypeError(f"value must be of type 'bool' not '{type(val).__name__}'")
        self.use_html_header = val
    def __str__(self):
        return f"Config(address={self.default_address.__repr__()}, port={self.default_port}, html={self.use_html_header})"
    def __repr__(self) -> str:
        return self.__str__()
    
config = Config()
