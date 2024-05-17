from base64 import encodebytes
from backpipe.tools.check_type import check

def encode(string: bytes | str) -> bytes:
    check(string, (bytes, str), "string")
    if isinstance(string, str):
        string = string.encode()
    return encodebytes(string)