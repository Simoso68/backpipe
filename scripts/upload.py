from subprocess import run
from os import getenv

KEY = getenv("PYPI_API_KEY")

if KEY == None:
    print("ERROR: No PyPi API key specified in system's environment variables.")

try:
    run(["twine", "upload", "dist/*", "--username", "__token__", "--password", KEY])
except FileNotFoundError:
    print("ERROR: Exception when trying to build package, is Python installed correctly?")