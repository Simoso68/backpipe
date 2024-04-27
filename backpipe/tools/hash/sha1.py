from hashlib import sha1 as _hash
from backpipe.tools.check_type import check

def sha1(input: str | bytes):
    check(input, (str, bytes), "input")
    if isinstance(input, str):
        input = input.encode()
    HASHER = _hash()
    HASHER.update(input)
    return HASHER.hexdigest()