import glob
from pathlib import Path

def find_files(directory, extension='.webp'):
    my_glob = directory + f'/**/*{extension}'
    return glob.iglob(my_glob, recursive=True)

def create_folder(path: str, is_file=False):
    directory = Path(path).parent if is_file else Path(path)
    directory.mkdir(parents=True, exist_ok=True)
