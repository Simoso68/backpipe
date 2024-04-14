def check(obj, types, name):
    if not isinstance(obj, types):
        type_msg = ""
        if isinstance(types, str):
            type_msg = f"'{types}'"
        else:
            for t in types:
                type_msg += f"or '{t}'"
            type_msg = type_msg.replace("or ", "", 1)
        raise TypeError(f"{name} must be {type_msg}, not '{type(obj).__name__}'")