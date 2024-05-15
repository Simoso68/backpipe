from json import loads
from typing import Any

def deserialize(json, on_exception=None) -> Any:
    """
    Deserializes JSON, returns the value defined in the 'on_exception' parameter if failed.
    """
    try:
        return loads(json)
    except Exception:
        return on_exception