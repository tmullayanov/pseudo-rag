import sys

def read_from_file(path: str) -> str:
    with open(path) as f:
        contents = f.read()

    if not contents:
        print(f"Couldn't read file at {path=}, exit", file=sys.stderr)
        sys.exit(-1)
    
    return contents
