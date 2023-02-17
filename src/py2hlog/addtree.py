from pathlib import Path
from itertools import islice

COUNTER_ADDRESS = 0
ALL_ADDRESS = {}
space = '<span style="padding-left:1rem"></span>'
branch = '│   '
tee = '├─ '
last = ' └─ '
output = ""
pathname = ""

# Based on -->
# https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python


def tree(dir_path: Path, level: int = -1, limit_to_directories: bool = False,
         length_limit: int = 500, filename=""):
    """Given a directory Path object print a visual tree structure"""
    dir_path = Path(dir_path)
    files = 0
    directories = 0

    def inner(dir_path: Path, prefix: str = '', level=-1):
        nonlocal files, directories
        if not level:
            return
        if limit_to_directories:
            contents = [d for d in dir_path.iterdir() if d.is_dir()]
        else:
            contents = list(dir_path.iterdir())
        pointers = [tee] * (len(contents) - 1) + [last]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield prefix + pointer + path.name
                directories += 1
                extension = branch if pointer == tee else space
                yield from inner(path, prefix=prefix+extension, level=level-1)
            elif not limit_to_directories:
                global pathname
                if filename == path.name:
                    pathname = f'<b style="color: coral;">{path.name}</b>'
                    yield prefix + pointer + pathname
                else:
                    yield prefix + pointer + path.name
                files += 1
    global output
    output += f'<br><b>{dir_path.name}</b>'
    iterator = inner(dir_path, level=level)
    for line in islice(iterator, length_limit):
        output += f'<br>{line}'
    if next(iterator, None):
        output += f'... length_limit, {length_limit}, reached, counted:'
    return output
