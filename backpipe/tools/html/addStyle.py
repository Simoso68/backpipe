from backpipe.tools.check_type import check

def addStyle(css: str):
    check(css, str, "CSS")
    return f"<style>{css}</style>"