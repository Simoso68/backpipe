from backpipe.tools.check_type import check
from os import path

def create(filename: str | bytes):
    check(filename, str, "file name")
    if path.exists(filename):
        raise FileExistsError(f"file '{filename}' already exists")
    FILE = open(filename, "w")
    FILE.write("")
    FILE.close()