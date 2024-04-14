# BackPipe CLI tool.

from colorama import Fore, Back, init
from sys import argv, exit
from os import mkdir, path
from subprocess import run
from json import loads
from packaging.version import Version

from backpipe import __version__

init()

def info(msg):
    print(f"{Back.LIGHTGREEN_EX}{Fore.BLACK} INFO {Back.RESET}{Fore.RESET} {msg}")

def err(msg, t="ERROR"):
    print(f"{Back.LIGHTRED_EX}{Fore.BLACK} {t} {Back.RESET}{Fore.RESET} {msg}")

def warn(msg):
    print(f"{Back.LIGHTYELLOW_EX}{Fore.BLACK} WARN {Back.RESET}{Fore.RESET} {msg}")

def crash(exc):
    print(f"\r{Back.LIGHTRED_EX}{Fore.BLACK} CRASH {Back.RESET}{Fore.RESET} {Fore.BLUE}{type(exc).__name__}{Fore.RESET}: {Fore.LIGHTBLUE_EX}{exc}{Fore.RESET}")

def file_hoster(addr, port):
    # Give Root/Admin Permissions for full access
    # This script uses newer F-String features provided by Python 3.12

    import backpipe
    import os
    import platform
    import urllib

    server = backpipe.BackPipe(addr, port)

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
            return (403, "Can not access object")
    
    server.run()

def main():
    if "-v" in argv[1:] or "--version" in argv[1:]:
        print(f"BackPipe {__version__}")
        exit()

    elif "-h" in argv[1:] or "--help" in argv[1:]:
        print("""BackPipe Help
backpipe -h / --help        This message.
backpipe -v / --version     Display the current version of backpipe.
backpipe new                BackPipe project template.
backpipe exec               Executes your BackPipe project.
backpipe update             Update backpipe using pip.""")
        exit()
    
    elif "host" in argv[1:]:
        print("Available presets: ")
        for preset in ("file",): # More will be added soon
            print(f"- {preset}")
        TYPE = input("What server preset do you want to host?: ")
        if TYPE == "file":
            SERVER = file_hoster
        else:
            err("preset does not exist", "UNKNOWN")
            return
        
        ADDR = input("server address (leave empty for default): ")
        PORT = input("server port: ")

        try:
            int(PORT)
        except ValueError:
            err("port must be a number")

        try:
            SERVER(ADDR, int(PORT))
            return
        except Exception as server_exc:
            crash(server_exc)
            return

    elif "new" in argv[1:]:
        try:
            if not path.exists("src"):
                info("Creating 'src' directory ...")
                mkdir("src")
            if not path.exists("src/main.py"):
                info("Creating main executable 'src/main.py' ...")
                with open("src/main.py", "w") as n_main:
                    n_main.write("""# Importing backpipe's components
from backpipe import *
                             
# Creating a new server instance
server = BackPipe()

# Setting a response, that gets sent, when a GET, POST, PUT, PATCH or DELETE request comes in                                                                 
@server.any
def hello_world(r: Request):
    return (200, "Hello World!")
                             
# Setting a response, that gets sent, when a request with an unsupported method comes in
@server.unknown
def unknown_method(r: Request):
    return (405, f"The method '{r.method}' is not supported.")
                             
# Setting a response for a ratelimited client
@server.ratelimit
def ratelimited_response(r: Request):
    return (429, "Your client got ratelimited, please wait.")
                             
# Set a ratelimit
server.set_ratelimit(60)

# Run the server
server.run()""")
            if not path.exists("backpipe.json"):
                info("Creating backpipe.json ...")
                with open("backpipe.json", "w") as n_cfg:
                    n_cfg.write("""{
    "main":"src/main.py",
    "version":"VERSION"   
}""".replace("VERSION", __version__))
            if not path.exists(".gitignore"):
                info("Creating '.gitignore' file ...")
                with open(".gitignore", "w") as n_ignore:
                    n_ignore.write("__pycache__")
        except Exception as x:
            err(f"{Fore.BLUE}{type(x).__name__}{Fore.RESET}: {Fore.LIGHTBLUE_EX}{x}{Fore.RESET}")
            exit()
    elif "exec" in argv[1:]:
        try:
            raw = open("backpipe.json", "r").read()
            cfg = loads(raw)
            if not path.exists(cfg["main"]):
                err(f"set main executable '{cfg['main']}' does not exist.")
                exit()
            if Version(__version__) < Version(cfg["version"]):
                warn("your current version is lower than the in the config specified/recommended version, problems may occurr.")
            exec(open("src/main.py", "r").read())
        except FileNotFoundError:
            err("file 'backpipe.json' does not exist.")
            exit()
        except Exception:
            err(f"{Fore.BLUE}{type(x).__name__}{Fore.RESET}: {Fore.LIGHTBLUE_EX}{x}{Fore.RESET}", "CRASH")
            exit()
    elif "update" in argv[1:]:
        try:
            run(["pip", "install", "--upgrade", "backpipe"])
        except Exception as x:
            err(f"{Fore.BLUE}{type(x).__name__}{Fore.RESET}: {Fore.LIGHTBLUE_EX}{x}{Fore.RESET}")
            exit()
    else:
        err("unknown or not given arguments, use 'backpipe --help' for assistance.")
        exit()