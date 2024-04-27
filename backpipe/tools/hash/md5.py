from hashlib import md5 as _hash
from backpipe.tools.check_type import check

def md5(input: str | bytes):
    check(input, (str, bytes), "input")
    if isinstance(input, str):
        input = input.encode()
    HASHER = _hash()
    HASHER.update(input)
    return HASHER.hexdigest()