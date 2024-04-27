from subprocess import run
from platform import system

if system() == "Windows":
    PY = "python"
else:
    PY = "python3"

try:
    run([PY, "setup.py", "sdist", "bdist_wheel"])
except FileNotFoundError:
    print("ERROR: Exception when trying to build package, is Python installed correctly?")