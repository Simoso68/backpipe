from pathlib import Path
from shutil import rmtree

def rmdir(name):
    try:
        rmtree(name)
    except FileNotFoundError:
        print(f"Directory '{name}' not found, skipping ...")

rmdir("build")
rmdir("backpipe.egg-info")
rmdir("dist")

for file in Path(".").rglob("__pycache__"):
    rmtree(file.__str__())