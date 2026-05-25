import os

def walk_files(root):
    for base, _, files in os.walk(root):
        for f in files:
            full = os.path.join(base, f)
            rel = os.path.relpath(full, root).replace("\\", "/")
            yield rel, full
