from backpipe.tools.check_type import check
from os import path

def write(filename: str, content: str | bytes):
    check(filename, str, "file name")
    check(content, (str, bytes), "file contents")
    if not path.exists(filename):
        raise FileNotFoundError(f"file '{filename}' does not exist")
    if isinstance(content, str):
        FILE = open(filename, "w")
    else:
        FILE = open(filename, "wb")
    
    FILE.write(content)
    FILE.close()