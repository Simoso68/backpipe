def check(obj, types, name):
    if not isinstance(obj, types):
        type_msg = ""
        if not isinstance(types, tuple):
            type_msg = f"'{types.__name__}'"
        else:
            for t in types:
                type_msg += f"or '{t.__name__}'"
            type_msg = type_msg.replace("or ", "", 1)
        raise TypeError(f"{name} must be {type_msg}, not '{type(obj).__name__}'")