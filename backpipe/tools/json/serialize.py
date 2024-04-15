from json import dumps

def serialize(dict, on_exception=None) -> str:
    """
    Serializes JSON, returns the value defined in the 'on_exception' parameter if failed.
    """
    try:
        return dumps(dict)
    except Exception:
        return on_exception