from backpipe.tools.check_type import check

def addMeta(name: str, content: str):
    check(name, str, "meta name")
    check(content, str, "meta content")

    return f"<meta name='{name}' content='{content}'>"