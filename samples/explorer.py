# Give Root/Admin Permissions for full access
# This script uses newer F-String features provided by Python 3.12

import backpipe
import os
import platform
import urllib

server = backpipe.BackPipe()

@server.get
def respond(r: backpipe.Request):
    try:
        if platform.system() == "Windows":
            PATH = urllib.parse.unquote(f"C:{r.path}")
        else:
            PATH = urllib.parse.unquote(r.path)

        if not os.path.exists(PATH):
            return (404, "File not found.")
    
        if os.path.isdir(PATH):
            HTML = "<!DOCTYPE html>\n"

            if r.path == "/":
                CURRENT_DIR = r.path[:-1]
            else:
                CURRENT_DIR = r.path

            for o in os.listdir(PATH):
                HTML += f"<a href='{CURRENT_DIR + f"/{o}"}'>{o}</a><br>"
            return (200, HTML)
        else:
            return (200, open(PATH, "rb").read())
    except PermissionError:
        return(403, "Can not access object")
    
server.run()