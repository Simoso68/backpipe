from backpipe.tools.check_type import check

def addTag(tag, inner, params):
    check(tag, str, "tag")
    check(inner, str, "inner HTML")
    check(params, dict, "element parameters")

    param_text = " "

    for p in params.keys():
        param_text += f"{p}='{params[p]}'"

    param_text += " "

    return f"<{tag}{param_text}>{inner}</{tag}>"