from subprocess import run
from platform import system
from os import path

if system() == "Windows":
    PY = "python"
else:
    PY = "python3"

SCRIPT = "scripts/" + input("Script: ") + ".py"

if not path.exists(SCRIPT):
    print("ERROR: Script does not exist")
    exit(1)

try:
    run([PY, SCRIPT])
except FileNotFoundError:
    print("ERROR: Exception when trying to execute script, is Python installed correctly?")