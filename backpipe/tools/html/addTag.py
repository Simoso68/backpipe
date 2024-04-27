from backpipe.tools.check_type import check

def addTag(tag: str, inner: str, params: dict):
    check(tag, str, "tag")
    check(inner, str, "inner HTML")
    check(params, dict, "element parameters")

    param_text = " "

    for p in params.keys():
        param_text += f"{p}='{params[p]}' "

    return f"<{tag}{param_text}>{inner}</{tag}>"