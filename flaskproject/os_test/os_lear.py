import os


def new_file():
    lists = os.listdir(os.getcwd())
    lists.sort(key=lambda fn: os.path.getatime(os.getcwd() + '\\' + fn))
    file_path = os.path.join(os.getcwd(), lists[-1])
    return file_path


s = lambda a, b: a + b
print(s(2, 1))
print(new_file())
