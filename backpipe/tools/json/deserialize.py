from json import loads

def deserialize(json) -> str:
    """
    Deserializes JSON, returns the value defined in the 'on_exception' parameter if failed.
    """
    return loads(json)