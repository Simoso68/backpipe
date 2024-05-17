from base64 import decodebytes
from backpipe.tools.check_type import check

def decode(string: bytes) -> bytes:
    check(string, (bytes, str), "string")
    if isinstance(string, str):
        string = string.encode()
    return decodebytes(string)