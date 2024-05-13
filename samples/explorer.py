# Give Root/Admin Permissions for full access
# This script uses newer F-String features provided by Python 3.12

import backpipe
import os
import platform
import urllib

server = backpipe.BackPipe()

@server.get()
def respond(r: backpipe.Request):
    try:
        if platform.system() == "Windows":
            PATH = urllib.parse.unquote(f"C:{r.path}")
        else:
            PATH = urllib.parse.unquote(r.path)

        if not os.path.exists(PATH):
            return (404, "File not found.")
    
        if os.path.isdir(PATH):
            HTML = backpipe.tools.html.HTML()

            if r.path == "/":
                CURRENT_DIR = r.path[:-1]
            else:
                CURRENT_DIR = r.path

            for o in os.listdir(PATH):
                HTML.add_tag("a", o, {"href":f"{CURRENT_DIR}/{o}"})
                HTML.add_tag_self_closing("br")
            return (200, HTML.text())
        else:
            return (200, open(PATH, "rb").read())
    except PermissionError:
        return(403, "Can not access object")
    
server.run()