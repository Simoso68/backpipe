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
        self.__title__ = "<title>Response</title>"
    def text(self) -> str:
        return f"{self.__data__}<html><head>{self.__head__}</head><body>{self.__body__}</body></html>"
    def add_tag(self, tag: str, inner: str, params: dict = {}):
        self.__body__ += _addTag(tag, inner, params)
    def add_head_tag(self, tag: str, inner: str, params: dict = {}):
        self.__head__ += _addTag(tag, inner, params)
    def add_meta_tag(self, name, content):
        self.__head__ += _addMeta(name, content)