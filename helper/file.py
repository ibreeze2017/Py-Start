import os


def write(path: str, content: str):
    fp = open(path, "w+")
    fp.write(content)
    fp.flush()
    fp.close()


def read(path: str):
    fp = open(path, "r")
    res = fp.read()
    fp.close()
    return res


def exist(path: str):
    return os.path.exists(path)


def file_exists(path: str):
    return os.path.isfile(path)


def dir_exists(path: str):
    return os.path.isdir(path)


def create_dir(path: str, parent=True):
    if parent:
        os.makedirs(path)
    else:
        os.mkdir(path)
