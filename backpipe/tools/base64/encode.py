from base64 import encodebytes
from backpipe.tools.check_type import check

def encode(string: bytes) -> bytes:
    check(string, bytes, "string")
    return encodebytes(string)