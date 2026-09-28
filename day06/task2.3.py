import os

def list_all(path):
    names = []
    for name in sorted(os.listdir(path)):
        if not name.startswith("."):
            names.append(name)

    print(path + ":")
    print("  ".join(names))
    print()

    for name in names:
        full = os.path.join(path, name)
        if os.path.isdir(full):
            list_all(full)

list_all(".")
