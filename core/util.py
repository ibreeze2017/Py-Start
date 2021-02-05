import hashlib
from helper import file


def get_hash(url: str):
    md5 = hashlib.md5()
    md5.update(url.encode("utf-8"))
    return md5.hexdigest()


def check_dirs(dirs: tuple, path=None):
    for _dir in dirs:
        if not file.exist(_dir):
            file.create_dir(_dir if path is None else _dir + path)
