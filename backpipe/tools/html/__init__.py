from backpipe.tools.html.addTag import addTag as _addTag
from backpipe.tools.html.addMeta import addMeta as _addMeta

class HTML():
    """
    Simple HTML builder.
    """
    def __init__(self):
        self.__data__ = "<DOCTYPE html>"
        self.__head__ = ""
        self.__body__ = ""
    def text(self) -> str:
        return f"{self.__data__}<html><head>{self.__head__}</head><body>{self.__body__}</body></html>"
    def addTag(self, tag: str, inner: str, params: dict = {}):
        self.__body__ += _addTag(tag, inner, params)
    def addMeta(self, name, content):
        self.__head__ += _addMeta(name, content)