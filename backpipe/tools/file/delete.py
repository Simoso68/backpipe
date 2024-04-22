from os import path, remove

def delete(filename):
    if not path.exists(filename):
        raise FileNotFoundError(f"file '{filename}' does not exist")
    if path.isdir(filename):
        raise IsADirectoryError(f"'{filename}' is a directory")
    try:
        remove(filename)
    except PermissionError:
        raise PermissionError(f"not enough permissions to delete '{filename}'")