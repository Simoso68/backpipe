from pathlib import Path
chars = 0

for file in Path(".").rglob("*.py"):
    chars += len(open(file.__str__(), "r").read())

print(chars)