from backpipe.tools.html.addTag import addTag as _addTag
from backpipe.tools.html.addMeta import addMeta as _addMeta
from backpipe.tools.html.addStyle import addStyle as _addStyle

class HTML():
    """
    Simple HTML builder.
    """
    def __init__(self):
        self.__data__ = "<!DOCTYPE html>"
        self.__head__ = ""
        self.__body__ = ""
    def text(self) -> str:
        return f"{self.__data__}<html><head>{self.__head__}</head><body>{self.__body__}</body></html>"
    def add_tag(self, tag: str, inner: str, params: dict = {}):
        self.__body__ += _addTag(tag, inner, params)
    def add_head_tag(self, tag: str, inner: str, params: dict = {}):
        self.__head__ += _addTag(tag, inner, params)
    def add_tag_self_closing(self, tag: str, params: dict = {}):
        self.__body__ += _addTag(tag, "", params).replace(f"</{tag}>", "")
    def add_head_tag_self_closing(self, tag: str, params: dict = {}):
        self.__head__ += _addTag(tag, "", params).replace(f"</{tag}>", "")
    def add_meta_tag(self, name, content):
        self.__head__ += _addMeta(name, content)
    def add_style(self, css: str):
        self.__head__ += _addStyle(css)