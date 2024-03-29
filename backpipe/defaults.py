from .rq import Request

def undefined(r: Request):
    return (200, "Undefined")

def unknown_method(r: Request):
    return (405, f"Method {r.method.__repr__()} is not supported.")

def ratelimited_default(r: Request):
    return (429, "Too many requests from the same client.")

def blocked_default(r: Request):
    return (403, "Your client has been blocked.")